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

import os
from os import environ, pathsep

from ament_index_python.packages import get_package_prefix

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, SetEnvironmentVariable, SetLaunchConfiguration
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch_pal.arg_utils import LaunchArgumentsBase, CommonArgs
from launch_pal.robot_arguments import PMB2Args
from launch_pal.include_utils import include_scoped_launch_py_description
from dataclasses import dataclass


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):
    wheel_model: DeclareLaunchArgument = PMB2Args.wheel_model
    laser_model: DeclareLaunchArgument = PMB2Args.laser_model
    has_courier_rgbd_sensors: DeclareLaunchArgument = PMB2Args.has_courier_rgbd_sensors
    use_sim_time: DeclareLaunchArgument = CommonArgs.use_sim_time
    world_name: DeclareLaunchArgument = CommonArgs.world_name
    navigation: DeclareLaunchArgument = CommonArgs.navigation
    x: DeclareLaunchArgument = CommonArgs.x
    y: DeclareLaunchArgument = CommonArgs.y
    yaw: DeclareLaunchArgument = CommonArgs.yaw


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
    set_sim_time = SetLaunchConfiguration("use_sim_time", "True")
    launch_description.add_action(set_sim_time)

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
            "world_name":  launch_args.world_name,
            "model_paths": packages,
            "resource_paths": packages,
        })

    launch_description.add_action(gazebo)

    navigation = include_scoped_launch_py_description(
        pkg_name='pmb2_2dnav',
        paths=['launch', 'pmb2_nav_bringup.launch.py'],
        launch_arguments={
            "robot_name":  robot_name,
            "laser":  launch_args.laser_model,
        },
        condition=IfCondition(LaunchConfiguration('navigation')))

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
            "wheel_model": launch_args.wheel_model,
            "laser_model": launch_args.laser_model,
            "has_courier_rgbd_sensors": launch_args.has_courier_rgbd_sensors,
            "use_sim_time": launch_args.use_sim_time,
        }
    )

    launch_description.add_action(pmb2_bringup)


def get_model_paths(packages_names):
    model_paths = ""
    for package_name in packages_names:
        if model_paths != "":
            model_paths += pathsep

        package_path = get_package_prefix(package_name)
        model_path = os.path.join(package_path, "share")

        model_paths += model_path

    if 'GAZEBO_MODEL_PATH' in environ:
        model_paths += pathsep + environ['GAZEBO_MODEL_PATH']

    return model_paths
