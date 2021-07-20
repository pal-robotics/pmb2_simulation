# Copyright (c) 2021 PAL Robotics S.L.
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

from ament_index_python.packages import get_package_share_directory, get_package_prefix

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration

from launch_pal.include_utils import include_launch_py_description


def generate_launch_description():
    # This should be removed, it should be retrieved automatically from pal_gazebo.launch.py
    # See https://github.com/ros2/launch/issues/313
    declare_world_name = DeclareLaunchArgument(
        'world_name', default_value='',
        description='Specify world name, we\'ll convert to full path'
    )

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('pal_gazebo_worlds'), 'launch'), '/pal_gazebo.launch.py']),
        launch_arguments={
            'world_name': LaunchConfiguration('world_name')}.items(),
    )

    pmb2_spawn = include_launch_py_description(
        'pmb2_gazebo', ['launch', 'pmb2_spawn.launch.py'])
    pmb2_bringup = include_launch_py_description(
        'pmb2_bringup', ['launch', 'pmb2_bringup.launch.py'])

    pkg_path = get_package_prefix('pmb2_description')
    model_path = os.path.join(pkg_path, "share")
    resource_path = pkg_path

    if 'GAZEBO_MODEL_PATH' in environ:
        model_path += pathsep + environ['GAZEBO_MODEL_PATH']
    if 'GAZEBO_RESOURCE_PATH' in environ:
        resource_path += pathsep + environ['GAZEBO_RESOURCE_PATH']
    return LaunchDescription([
        SetEnvironmentVariable("GAZEBO_MODEL_PATH", model_path),
        # Using this prevents shared library from being found
        # SetEnvironmentVariable("GAZEBO_RESOURCE_PATH", resource_path),
        declare_world_name,
        gazebo,
        pmb2_spawn,
        pmb2_bringup
    ])
