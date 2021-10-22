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

import launch_testing
import unittest
import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import PathJoinSubstitution, LaunchConfiguration
from launch_ros.actions import Node
from launch_pal.include_utils import include_launch_py_description


def generate_test_description():
    # This is necessary to get unbuffered output from the process under test
    proc_env = os.environ.copy()
    proc_env['PYTHONUNBUFFERED'] = '1'

    test_dir = DeclareLaunchArgument('test_dir')

    # dut = device under test, aka the actual test
    dut_process = launch_testing.actions.GTest(
        path=PathJoinSubstitution(
            [LaunchConfiguration('test_dir'), 'test_pmb2_gazebo']),
        output="both")

    pmb2_gazebo_launch = include_launch_py_description('pmb2_gazebo',
                                                       ['launch', 'pmb2_gazebo.launch.py'])

    return LaunchDescription([
        test_dir,
        pmb2_gazebo_launch,
        dut_process,

        launch_testing.actions.ReadyToTest(),
    ]), {'dut_process': dut_process}


class TestDescriptionPublished(unittest.TestCase):

    def test_wait_for_end(self, proc_output, proc_info, dut_process):
        # Wait until process ends
        proc_info.assertWaitForShutdown(process=dut_process, timeout=10)


@ launch_testing.post_shutdown_test()
class TestSuccessfulExit(unittest.TestCase):

    def test_exit_code(self, proc_info, dut_process):
        # Check that dut_process finishes with code 0
        launch_testing.asserts.assertExitCodes(proc_info, process=dut_process)
