pmb2_simulation
==================

This repository contains the launch files to simulate the pmb2/TIAGo Base robot.

## Setup

> **Disclaimer**: In our testing environment, we've found out that the simulation is more reliable if we switch to Cyclone DDS. You can do this by setting the `RMW_IMPLEMENTATION` environment variable: `export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp`. More information on working with different DDS implementations [here](https://docs.ros.org/en/humble/How-To-Guides/Working-with-multiple-RMW-implementations.html).
>
> We are still looking on the issues when working with Fast RTPS.


1. Create a workspace for pmb2 simulation:

    `mkdir -p ~/pmb2_public_ws/src`

2. Download the [rosinstall](https://github.com/pal-robotics/pmb2_tutorials/blob/humble-devel/pmb2_public.rosinstall) file and move it to the src directory.

3. Move to the src directory and use rosinstall to clone the packages:

    `cd ~/pmb2_public_ws/src && rosinstall . pmb2_public.rosinstall`

    To install rosinstall tool you can use `sudo apt install python3-rosinstall`.

4. Build the workspace:

    `cd .. && colcon build`

5. Source the workspace:

    `source install/setup.bash`


## Simulate pmb2 robot

1. Launch gazebo simulation:

    `ros2 launch pmb2_gazebo pmb2_gazebo.launch.py`

2. To move the robot you can use the following command:

    ros2 topic pub /mobile_base_controller/cmd_vel_unstamped geometry_msgs/msg/Twist '{linear: {x: 1}, angular: {z: 0}}' -r10

The velocities can be modified by changing the values of x and z.


## Simulate pmb2 robot with navigation

1. Launch gazebo simulation with navigation

    `ros2 launch pmb2_2dnav_gazebo pmb2_navigation_gazebo.launch.py`

2. Set the initial pose in rviz2 and send a goal

You can also start the simulation and navigation separately by following the steps of the [Simulate pmb2 robot](#simulate-pmb2-robot) section to launch the simulation and then launch navigation in other terminal with the following command:
    `ros2 launch pmb2_2dnav pmb2_nav_bringup.launch.py`

Then, rviz can be used in the same way.
