# Copyright (c) 2022 PAL Robotics S.L. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from dataclasses import dataclass
import os
import yaml
import tempfile
from os import environ, pathsep

from ament_index_python.packages import get_package_prefix, get_package_share_directory
from launch import LaunchDescription
from launch.actions import (
    DeclareLaunchArgument,
    SetEnvironmentVariable,
    SetLaunchConfiguration,
    GroupAction,
    OpaqueFunction,
)
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_pal.actions import CheckPublicSim
from launch_pal.robot_arguments import CommonArgs
from launch_pal.arg_utils import LaunchArgumentsBase, read_launch_argument
from launch_pal.include_utils import (
    include_scoped_launch_py_description,
    include_launch_py_description,
)
from pmb2_description.launch_arguments import PMB2Args


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):
    wheel_model: DeclareLaunchArgument = PMB2Args.wheel_model
    laser_model: DeclareLaunchArgument = PMB2Args.laser_model
    add_on_module: DeclareLaunchArgument = PMB2Args.add_on_module
    camera_model: DeclareLaunchArgument = PMB2Args.camera_model
    is_public_sim: DeclareLaunchArgument = CommonArgs.is_public_sim
    world_name: DeclareLaunchArgument = CommonArgs.world_name
    navigation: DeclareLaunchArgument = CommonArgs.navigation
    slam: DeclareLaunchArgument = CommonArgs.slam
    advanced_navigation: DeclareLaunchArgument = CommonArgs.advanced_navigation
    docking: DeclareLaunchArgument = CommonArgs.docking
    x: DeclareLaunchArgument = CommonArgs.x
    y: DeclareLaunchArgument = CommonArgs.y
    yaw: DeclareLaunchArgument = CommonArgs.yaw


def private_navigation(context, *args, **kwargs):
    actions = []
    camera_model = read_launch_argument('camera_model', context)
    add_on_module = read_launch_argument('add_on_module', context)
    docking = read_launch_argument('docking', context)
    advanced_navigation = read_launch_argument('advanced_navigation', context)
    use_sim_time = read_launch_argument('use_sim_time', context)
    rviz_cfg_pkg = 'pmb2_2dnav'
    if advanced_navigation == 'True':
        rviz_cfg_pkg = 'pmb2_advanced_2dnav'

    robot_info = {
        "robot_info_publisher": {
            "ros__parameters": {
                "robot_type": "pmb2",
                "base_type": "pmb2",
                "add_on_module": add_on_module,
                "laser_model": "sick-571",
                "camera_model": camera_model,
                "advanced_navigation": (advanced_navigation == 'True'),
                "has_dock": (docking == 'True'),
                "use_sim_time": (use_sim_time == 'True'),
            }
        }
    }

    temp_yaml = tempfile.mkdtemp()
    temp_robot_info = os.path.join(temp_yaml, '99_robot_info.yaml')
    with open(temp_robot_info, 'w') as temp_robot_info_file:
        yaml.safe_dump(robot_info, temp_robot_info_file)

    # Robot Info Publisher
    robot_info_env = SetEnvironmentVariable(
        name='ROBOT_INFO_PATH',
        value=temp_yaml,
    )
    actions.append(robot_info_env)

    robot_info_publisher = Node(
        package='robot_info_publisher',
        executable='robot_info_publisher',
        name='robot_info_publisher',
        output='screen',
    )
    actions.append(robot_info_publisher)

    # Laser Sensors
    laser_bringup_launch = include_launch_py_description(
        pkg_name='pmb2_laser_sensors',
        paths=['launch', 'laser_sim.launch.py'],
    )
    actions.append(laser_bringup_launch)

    # Navigation
    nav_bringup_launch = include_launch_py_description(
        pkg_name='pmb2_2dnav',
        paths=['launch', 'navigation.launch.py'],
    )
    actions.append(nav_bringup_launch)

    # Localization
    loc_bringup_launch = include_launch_py_description(
        pkg_name='pmb2_2dnav',
        paths=['launch', 'localization.launch.py'],
        condition=UnlessCondition(LaunchConfiguration('slam'))
    )
    actions.append(loc_bringup_launch)

    # SLAM
    slam_bringup_launch = include_launch_py_description(
        pkg_name='pmb2_2dnav',
        paths=['launch', 'slam.launch.py'],
        condition=IfCondition(LaunchConfiguration('slam'))
    )
    actions.append(slam_bringup_launch)

    # Docking
    docking_bringup_launch = include_launch_py_description(
        pkg_name='pmb2_docking',
        paths=['launch', 'docking_sim.launch.py'],
        condition=IfCondition(LaunchConfiguration('docking'))
    )
    actions.append(docking_bringup_launch)

    # Stores Server
    db_bringup_launch = Node(
        package='pal_stores_server',
        executable='pal_stores_server',
        arguments=[os.path.join(
            os.environ['HOME'], '.pal', 'stores.db'
        )],
        output='screen',
        condition=IfCondition(LaunchConfiguration('advanced_navigation'))
    )
    actions.append(db_bringup_launch)

    # Advanced Navigation
    advanced_nav_bringup_launch = include_launch_py_description(
        pkg_name='pmb2_advanced_2dnav',
        paths=['launch', 'advanced_navigation.launch.py'],
        condition=IfCondition(LaunchConfiguration('advanced_navigation'))
    )
    actions.append(advanced_nav_bringup_launch)

    # RViz
    rviz_bringup_launch = Node(
        package='rviz2',
        executable='rviz2',
        arguments=['-d', os.path.join(
            get_package_share_directory(rviz_cfg_pkg),
            'config',
            'rviz',
            'navigation.rviz',
        )],
        parameters=[{'use_sim_time': LaunchConfiguration('use_sim_time')}],
        output='screen',
    )
    actions.append(rviz_bringup_launch)
    return actions


def public_navigation(context, *args, **kwargs):
    actions = []
    pmb2_2dnav = get_package_share_directory('pmb2_2dnav')
    pal_maps = get_package_share_directory('pal_maps')
    world_name = read_launch_argument('world_name', context)
    param_file = os.path.join(pmb2_2dnav, 'config', 'nav_public_sim.yaml')
    map_path = os.path.join(pal_maps, 'maps', world_name, 'map.yaml')

    # Navigation
    nav2_bringup_launch = include_scoped_launch_py_description(
        pkg_name='nav2_bringup',
        paths=['launch', 'navigation_launch.py'],
        launch_arguments={
            'params_file': param_file,
            'use_sim_time': LaunchConfiguration('use_sim_time'),
        }
    )
    actions.append(nav2_bringup_launch)

    # Localization
    loc_bringup_launch = include_scoped_launch_py_description(
        pkg_name='nav2_bringup',
        paths=['launch', 'localization_launch.py'],
        launch_arguments={
            'params_file': param_file,
            'map': map_path,
            'use_sim_time': LaunchConfiguration('use_sim_time'),
        },
        condition=UnlessCondition(LaunchConfiguration('slam')),
    )
    actions.append(loc_bringup_launch)

    # SLAM
    slam_bringup_launch = include_scoped_launch_py_description(
        pkg_name='nav2_bringup',
        paths=['launch', 'slam_launch.py'],
        launch_arguments={
            'params_file': param_file,
            'use_sim_time': LaunchConfiguration('use_sim_time'),
        },
        condition=IfCondition(LaunchConfiguration('slam')),
    )
    actions.append(slam_bringup_launch)

    # RViz
    rviz_bringup_launch = include_scoped_launch_py_description(
        pkg_name='nav2_bringup',
        paths=['launch', 'rviz_launch.py'],
    )
    actions.append(rviz_bringup_launch)
    return actions


def generate_launch_description():

    # Create the launch description and populate
    ld = LaunchDescription()
    launch_arguments = LaunchArguments()

    launch_arguments.add_to_launch_description(ld)

    declare_actions(ld, launch_arguments)

    return ld


def declare_actions(
    launch_description: LaunchDescription, launch_args: LaunchArguments
):
    # Set use_sim_time to True
    set_sim_time = SetLaunchConfiguration('use_sim_time', 'True')
    launch_description.add_action(set_sim_time)

    # Shows error if is_public_sim is not set to True when using public simulation
    public_sim_check = CheckPublicSim()
    launch_description.add_action(public_sim_check)

    robot_name = 'pmb2'
    packages = ['pmb2_description']

    model_path = get_model_paths(packages)

    gazebo_model_path_env_var = SetEnvironmentVariable(
        'GAZEBO_MODEL_PATH', model_path)

    gazebo = include_scoped_launch_py_description(
        pkg_name='pal_gazebo_worlds',
        paths=['launch', 'pal_gazebo.launch.py'],
        env_vars=[gazebo_model_path_env_var],
        launch_arguments={
            'world_name':  launch_args.world_name,
            'model_paths': packages,
            'resource_paths': packages,
        })

    launch_description.add_action(gazebo)

    navigation = GroupAction(
        condition=IfCondition(LaunchConfiguration('navigation')),
        actions=[
            # Private Navigation
            OpaqueFunction(
                function=private_navigation,
                condition=UnlessCondition(LaunchConfiguration('is_public_sim'))
            ),
            # Public Navigation
            OpaqueFunction(
                function=public_navigation,
                condition=IfCondition(LaunchConfiguration('is_public_sim'))
            ),
        ]
    )
    launch_description.add_action(navigation)

    robot_spawn = include_scoped_launch_py_description(
        pkg_name='pmb2_gazebo',
        paths=['launch', 'robot_spawn.launch.py'],
        launch_arguments={
            'robot_name': robot_name,
            'x': launch_args.x,
            'y': launch_args.y,
            'yaw': launch_args.yaw,
        }
    )

    launch_description.add_action(robot_spawn)

    pmb2_bringup = include_scoped_launch_py_description(
        pkg_name='pmb2_bringup', paths=['launch', 'pmb2_bringup.launch.py'],
        launch_arguments={
            'wheel_model': launch_args.wheel_model,
            'laser_model': launch_args.laser_model,
            'add_on_module': launch_args.add_on_module,
            'camera_model': launch_args.camera_model,
            'use_sim_time': LaunchConfiguration('use_sim_time'),
            'is_public_sim': launch_args.is_public_sim,
        }
    )

    launch_description.add_action(pmb2_bringup)


def get_model_paths(packages_names):
    model_paths = ''
    for package_name in packages_names:
        if model_paths != '':
            model_paths += pathsep

        package_path = get_package_prefix(package_name)
        model_path = os.path.join(package_path, 'share')

        model_paths += model_path

    if 'GAZEBO_MODEL_PATH' in environ:
        model_paths += pathsep + environ['GAZEBO_MODEL_PATH']

    return model_paths
