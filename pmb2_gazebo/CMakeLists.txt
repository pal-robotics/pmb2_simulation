cmake_minimum_required(VERSION 3.4.0)
project(pmb2_gazebo)

find_package(ament_cmake_auto REQUIRED)

# PAL Robotics stricter build flags, other developers should not worry about this
find_package(ament_cmake_pal QUIET)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)

  ament_lint_auto_find_test_dependencies()

  ament_add_gtest_executable(test_pmb2_gazebo
      test/test_pmb2_gazebo.cpp)

  ament_target_dependencies(test_pmb2_gazebo
    control_msgs
    rclcpp
  )
add_launch_test(
  test/test_gazebo.launch.py
  TARGET "test_pmb2_gazebo"
  ARGS "test_dir:=${CMAKE_CURRENT_BINARY_DIR}"
)

endif()

ament_auto_package(INSTALL_TO_SHARE launch models worlds)
