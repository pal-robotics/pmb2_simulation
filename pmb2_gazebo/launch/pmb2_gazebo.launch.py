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
from os import environ, pathsep

from ament_index_python.packages import get_package_prefix, get_package_share_directory
from launch import LaunchDescription
from launch.actions import (
    DeclareLaunchArgument,
    SetEnvironmentVariable,
    SetLaunchConfiguration,
    GroupAction,
)
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import (
    LaunchConfiguration,
    PathJoinSubstitution,
    PythonExpression,
    AndSubstitution,
    NotSubstitution,
)
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch_pal.actions import CheckPublicSim
from launch_pal.conditions import UnlessNodeRunning
from launch_pal.substitutions import RobotInfoFile
from launch_pal.robot_arguments import CommonArgs
from launch_pal.arg_utils import LaunchArgumentsBase
from launch_pal.include_utils import include_scoped_launch_py_description
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
    namespace: DeclareLaunchArgument = CommonArgs.namespace


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
    packages = ['pmb2_description', 'pal_urdf_utils']

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
        },
        condition=UnlessNodeRunning("gazebo"),
    )

    launch_description.add_action(gazebo)

    robot_spawn = include_scoped_launch_py_description(
        pkg_name='pmb2_gazebo',
        paths=['launch', 'robot_spawn.launch.py'],
        launch_arguments={
            'namespace': launch_args.namespace,
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
            'namespace': launch_args.namespace,
            'wheel_model': launch_args.wheel_model,
            'laser_model': launch_args.laser_model,
            'add_on_module': launch_args.add_on_module,
            'camera_model': launch_args.camera_model,
            'use_sim_time': LaunchConfiguration('use_sim_time'),
            'is_public_sim': launch_args.is_public_sim,
        }
    )

    launch_description.add_action(pmb2_bringup)

    # Robot Info Publisher
    robot_info_ns = PythonExpression([
        "'/", LaunchConfiguration('namespace'),
        "' if '", LaunchConfiguration('namespace'), "' else ''"
    ])
    robot_info_file = RobotInfoFile(
        content={
            'robot_type': robot_name,
            'base_type': robot_name,
            'wheel_model': launch_args.wheel_model,
            'camera_model': launch_args.camera_model,
            'add_on_module': launch_args.add_on_module,
            'laser_model': launch_args.laser_model,
            'has_dock': launch_args.docking,
            'advanced_navigation': launch_args.advanced_navigation,
            'namespace': robot_info_ns,
            'use_sim_time': LaunchConfiguration('use_sim_time'),
        },
    )
    robot_info_env = SetEnvironmentVariable(
        name='ROBOT_INFO_PATH',
        value=robot_info_file
    )
    launch_description.add_action(robot_info_env)

    robot_info_publisher = Node(
        namespace=LaunchConfiguration('namespace'),
        package='robot_info_publisher',
        executable='robot_info_publisher',
        name='robot_info_publisher',
        output='screen',
        condition=UnlessCondition(LaunchConfiguration('is_public_sim')),
    )
    launch_description.add_action(robot_info_publisher)

    public_nav_params = os.path.join(
        get_package_share_directory('pmb2_2dnav'), 'config', 'nav_public_sim.yaml'
    )
    public_navigation_launch = GroupAction(
        condition=IfCondition(AndSubstitution(
            LaunchConfiguration('is_public_sim'), LaunchConfiguration('navigation'))
        ),
        actions=[
            # Navigation
            include_scoped_launch_py_description(
                pkg_name='nav2_bringup',
                paths=['launch', 'navigation_launch.py'],
                launch_arguments={
                    'params_file': public_nav_params,
                    'use_sim_time': LaunchConfiguration('use_sim_time'),
                },
            ),

            # Localization
            include_scoped_launch_py_description(
                pkg_name='nav2_bringup',
                paths=['launch', 'localization_launch.py'],
                launch_arguments={
                    'params_file': public_nav_params,
                    'map': PathJoinSubstitution([
                        get_package_share_directory('pal_maps'),
                        'maps',
                        LaunchConfiguration('world_name'),
                        'map.yaml'
                    ]),
                    'use_sim_time': LaunchConfiguration('use_sim_time'),
                },
                condition=UnlessCondition(LaunchConfiguration('slam')),
            ),

            # SLAM
            include_scoped_launch_py_description(
                pkg_name='nav2_bringup',
                paths=['launch', 'slam_launch.py'],
                launch_arguments={
                    'params_file': public_nav_params,
                    'use_sim_time': LaunchConfiguration('use_sim_time'),
                },
                condition=IfCondition(LaunchConfiguration('slam')),
            ),

            # RViz
            include_scoped_launch_py_description(
                pkg_name='nav2_bringup',
                paths=['launch', 'rviz_launch.py'],
            ),
        ]
    )
    launch_description.add_action(public_navigation_launch)

    rviz_cfg_pkg = PythonExpression([
        "'pmb2_advanced_2dnav' if '",
        LaunchConfiguration('advanced_navigation'),
        "'=='True' else 'pmb2_2dnav'",
    ]),
    private_navigation_launch = GroupAction(
        condition=IfCondition(AndSubstitution(
            NotSubstitution(LaunchConfiguration('is_public_sim')),
            LaunchConfiguration('navigation'))
        ),
        actions=[
            # Laser Sensors
            include_scoped_launch_py_description(
                pkg_name='pmb2_laser_sensors',
                paths=['launch', 'laser_sim.launch.py'],
                launch_arguments={
                    'namespace': launch_args.namespace,
                    'wheel_model': launch_args.wheel_model,
                    'camera_model': launch_args.camera_model,
                    'add_on_module': launch_args.add_on_module,
                    'laser_model': launch_args.laser_model,
                    'docking': launch_args.docking,
                    'advanced_navigation': launch_args.advanced_navigation,
                    'use_sim_time': LaunchConfiguration('use_sim_time'),
                },
                env_vars=[robot_info_env],
            ),

            # Navigation
            include_scoped_launch_py_description(
                pkg_name='pmb2_2dnav',
                paths=['launch', 'navigation.launch.py'],
                launch_arguments={
                    'namespace': launch_args.namespace,
                    'wheel_model': launch_args.wheel_model,
                    'camera_model': launch_args.camera_model,
                    'add_on_module': launch_args.add_on_module,
                    'laser_model': launch_args.laser_model,
                    'docking': launch_args.docking,
                    'advanced_navigation': launch_args.advanced_navigation,
                    'use_sim_time': LaunchConfiguration('use_sim_time'),
                },
                env_vars=[robot_info_env],
            ),

            # Localization
            include_scoped_launch_py_description(
                pkg_name='pmb2_2dnav',
                paths=['launch', 'localization.launch.py'],
                launch_arguments={
                    'namespace': launch_args.namespace,
                    'wheel_model': launch_args.wheel_model,
                    'camera_model': launch_args.camera_model,
                    'add_on_module': launch_args.add_on_module,
                    'laser_model': launch_args.laser_model,
                    'docking': launch_args.docking,
                    'advanced_navigation': launch_args.advanced_navigation,
                    'use_sim_time': LaunchConfiguration('use_sim_time'),
                },
                env_vars=[robot_info_env],
                condition=UnlessCondition(LaunchConfiguration('slam')),
            ),

            # SLAM
            include_scoped_launch_py_description(
                pkg_name='pmb2_2dnav',
                paths=['launch', 'slam.launch.py'],
                launch_arguments={
                    'namespace': launch_args.namespace,
                    'wheel_model': launch_args.wheel_model,
                    'camera_model': launch_args.camera_model,
                    'add_on_module': launch_args.add_on_module,
                    'laser_model': launch_args.laser_model,
                    'docking': launch_args.docking,
                    'advanced_navigation': launch_args.advanced_navigation,
                    'use_sim_time': LaunchConfiguration('use_sim_time'),
                },
                env_vars=[robot_info_env],
                condition=IfCondition(LaunchConfiguration('slam')),
            ),

            # Docking
            include_scoped_launch_py_description(
                pkg_name='pmb2_docking',
                paths=['launch', 'docking_sim.launch.py'],
                launch_arguments={
                    'namespace': launch_args.namespace,
                    'wheel_model': launch_args.wheel_model,
                    'camera_model': launch_args.camera_model,
                    'add_on_module': launch_args.add_on_module,
                    'laser_model': launch_args.laser_model,
                    'docking': launch_args.docking,
                    'has_dock': launch_args.docking,
                    'advanced_navigation': launch_args.advanced_navigation,
                    'use_sim_time': LaunchConfiguration('use_sim_time'),
                },
                env_vars=[robot_info_env],
                condition=IfCondition(LaunchConfiguration('docking'))
            ),

            # Stores Server
            Node(
                namespace=LaunchConfiguration('namespace'),
                package='pal_stores_server',
                executable='pal_stores_server',
                arguments=[PathJoinSubstitution([
                    os.environ['HOME'], '.pal',
                    PythonExpression(["'", LaunchConfiguration('namespace'), "stores.db'"]),
                ])],
                condition=IfCondition(LaunchConfiguration('advanced_navigation'))
            ),

            # Advanced Navigation
            include_scoped_launch_py_description(
                pkg_name='pmb2_advanced_2dnav',
                paths=['launch', 'advanced_navigation.launch.py'],
                launch_arguments={
                    'namespace': launch_args.namespace,
                    'wheel_model': launch_args.wheel_model,
                    'camera_model': launch_args.camera_model,
                    'add_on_module': launch_args.add_on_module,
                    'laser_model': launch_args.laser_model,
                    'has_dock': launch_args.docking,
                    'docking': launch_args.docking,
                    'advanced_navigation': launch_args.advanced_navigation,
                    'use_sim_time': LaunchConfiguration('use_sim_time'),
                },
                env_vars=[robot_info_env],
                condition=IfCondition(LaunchConfiguration('advanced_navigation'))
            ),

            # RViz
            Node(
                namespace=LaunchConfiguration('namespace'),
                package='rviz2',
                executable='rviz2',
                arguments=['-d', PathJoinSubstitution([
                    FindPackageShare(rviz_cfg_pkg),
                    'config',
                    'rviz',
                    'navigation.rviz',
                ])],
                parameters=[{'use_sim_time': LaunchConfiguration('use_sim_time')}],
                output='screen',
                remappings=[
                    ('/tf', 'tf'),
                    ('/tf_static', 'tf_static'),
                ],
            ),
        ]
    )
    launch_description.add_action(private_navigation_launch)


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
