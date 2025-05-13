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

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch_pal.robot_arguments import CommonArgs
from launch_pal.arg_utils import LaunchArgumentsBase
from launch_ros.actions import Node


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):
    robot_name: DeclareLaunchArgument = DeclareLaunchArgument(
        name='robot_name', description='Gazebo model name'
    )

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
    robot_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        namespace=LaunchConfiguration('namespace'),
        arguments=[
            '-topic',
            'robot_description',
            '-entity',
            # 'namespace' if $arg('namespace') is not empty else 'robot_name'
            PythonExpression(
                [
                    "'",
                    LaunchConfiguration('namespace'),
                    "' if '",
                    LaunchConfiguration('namespace'),
                    "' else '",
                    LaunchConfiguration('robot_name'),
                    "'"
                ]
            ),
            '-robot_namespace',
            LaunchConfiguration('namespace'),
            '-x', LaunchConfiguration('x'),
            '-y', LaunchConfiguration('y'),
            '-Y', LaunchConfiguration('yaw'),
        ],

        output='screen',
    )
    launch_description.add_action(robot_entity)

    return
