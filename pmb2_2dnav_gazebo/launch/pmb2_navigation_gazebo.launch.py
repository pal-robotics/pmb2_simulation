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

from launch import LaunchDescription
from launch_pal.include_utils import include_launch_py_description


def generate_launch_description():
    # Create the launch description and populate
    ld = LaunchDescription([
        include_launch_py_description(
            'pmb2_gazebo', ['launch', 'pmb2_gazebo.launch.py']
        ),
        include_launch_py_description(
            'pmb2_2dnav', ['launch', 'pmb2_nav_bringup.launch.py'],
            launch_arguments={
                'slam': 'False'
                }.items()),
    ])

    return ld
