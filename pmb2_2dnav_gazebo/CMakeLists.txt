cmake_minimum_required(VERSION 3.4.0)
project(pmb2_2dnav_gazebo)

find_package(ament_cmake_auto REQUIRED)

# PAL Robotics stricter build flags, other developers should not worry about this
find_package(ament_cmake_pal QUIET)

# Media commented out
ament_auto_package(INSTALL_TO_SHARE launch)
