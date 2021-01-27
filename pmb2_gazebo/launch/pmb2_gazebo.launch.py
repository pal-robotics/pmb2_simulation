# Copyright (c) 2020 PAL Robotics S.L. All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met:
#
#  1. Redistributions of source code must retain the above copyright notice,
#  this list of conditions and the following disclaimer.
#  2. Redistributions in binary form must reproduce the above copyright notice,
#  this list of conditions and the following disclaimer in the documentation
#  and/or other materials provided with the distribution.
#  3. Neither the name of the copyright holder nor the names of its
#  contributors may be used to endorse or promote products derived from this
#  software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
#  IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
#  TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
#  PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
#  HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#  SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
#  LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#  DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import os
from os import environ, pathsep

from ament_index_python.packages import get_package_share_directory, get_package_prefix

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node

import xacro


def generate_launch_description():
    gazebo = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('pal_gazebo_worlds'), 'launch'), '/pal_gazebo.launch.py']),
             )

    pmb2_state_publisher  = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('pmb2_description'), 'launch'), '/robot_state_publisher.launch.py']),
             )

    spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py',
                        arguments=['-topic', 'robot_description',
                                   '-entity', 'pmb2'],
                        output='screen')

    pkg_path = get_package_prefix('pmb2_description')
    model_path = os.path.join(pkg_path, "share")
    resource_path = pkg_path

    if 'GAZEBO_MODEL_PATH' in environ:
        model_path += pathsep+environ['GAZEBO_MODEL_PATH']
    if 'GAZEBO_RESOURCE_PATH' in environ:
        resource_path += pathsep+environ['GAZEBO_RESOURCE_PATH']
    return LaunchDescription([
        SetEnvironmentVariable("GAZEBO_MODEL_PATH", model_path),
        # Using this prevents shared library from being found
        # SetEnvironmentVariable("GAZEBO_RESOURCE_PATH", resource_path), 
        gazebo,
        pmb2_state_publisher,
        spawn_entity,
    ])
