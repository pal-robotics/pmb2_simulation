cmake_minimum_required(VERSION 3.4.0)
project(pmb2_gazebo)

find_package(ament_cmake_auto REQUIRED)
ament_auto_find_build_dependencies()

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

# Media commented out
ament_auto_package(INSTALL_TO_SHARE launch models worlds)
