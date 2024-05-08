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


from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

from launch_ros.actions import Node


def generate_launch_description():
    #    This format doesn't work because because we have to expand gzpose into
    #    different args for spawn_entity.py

    pose = {
        'x': LaunchConfiguration('x', default='0.0'),
        'y': LaunchConfiguration('y', default='0.0'),
        'z': LaunchConfiguration('z', default='0.0'),
        'R': LaunchConfiguration('R', default='0.0'),
        'P': LaunchConfiguration('P', default='0.0'),
        'Y': LaunchConfiguration('Y', default='0.0'),
    }

    declare_model_name = DeclareLaunchArgument(
        'model_name', default_value='pmb2',
        description='Gazebo model name'
    )

    spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py',
                        arguments=['-topic', 'robot_description',
                                   '-entity', LaunchConfiguration(
                                       'model_name'),
                                   '-x',
                                   pose['x'],
                                   '-y',
                                   pose['y'],
                                   '-z',
                                   pose['z'],
                                   '-R',
                                   pose['R'],
                                   '-P',
                                   pose['P'],
                                   '-Y',
                                   pose['Y'],
                                   ],
                        output='screen')

    # Create the launch description and populate
    ld = LaunchDescription()

    # ld.add_action(declare_gz_pose)
    ld.add_action(declare_model_name)
    ld.add_action(spawn_entity)

    return ld
