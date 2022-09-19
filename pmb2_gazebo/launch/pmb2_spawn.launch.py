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

from launch_pal.include_utils import include_launch_py_description
from launch_ros.actions import Node


def generate_launch_description():
    #    This format doesn't work because because we have to expand gzpose into
    #    different args for spawn_entity.py
    #    declare_gz_pose = DeclareLaunchArgument(
    #        'gzpose', default_value='-x 0 -y 0 -z 0.0 -R 0.0 -P 0.0 -Y 0.0 ',
    #        description='Spawn gazebo position as provided to spawn_entity.py'
    #    )
    declare_model_name = DeclareLaunchArgument(
        'model_name', default_value='pmb2',
        description='Gazebo model name'
    )

    pmb2_state_publisher = include_launch_py_description('pmb2_description',
                                                         ['launch',
                                                          'robot_state_publisher.launch.py'])
    spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py',
                        arguments=['-topic', 'robot_description',
                                   '-entity', LaunchConfiguration(
                                       'model_name'),
                                   # LaunchConfiguration('gzpose'),
                                   ],
                        output='screen')

    # Create the launch description and populate
    ld = LaunchDescription()

    # ld.add_action(declare_gz_pose)
    ld.add_action(declare_model_name)
    ld.add_action(pmb2_state_publisher)
    ld.add_action(spawn_entity)

    return ld
