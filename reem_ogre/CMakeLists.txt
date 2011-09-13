# NOTE: This script borrows its contents from the original script found in the pr2_ogre package, version 1.0.0

cmake_minimum_required(VERSION 2.4.6)
include($ENV{ROS_ROOT}/core/rosbuild/rosbuild.cmake)
rosbuild_init()

# find needed paths
rosbuild_find_ros_package(reem_description)
rosbuild_find_ros_package(reem_ogre)
rosbuild_find_ros_package(ogre)

set(reem_gen_files "")

# build the ogre mesh files from *.stl (and *.stlb from convex decomposition)
file(GLOB_RECURSE reem_description_stl_files RELATIVE ${reem_description_PACKAGE_PATH}/meshes
                                                      ${reem_description_PACKAGE_PATH}/meshes/*/*.stl
                                                      ${reem_description_PACKAGE_PATH}/meshes/*/convex/*.stlb)

set(reem_description_out_path ${CMAKE_CURRENT_SOURCE_DIR}/Media/models)

MAKE_DIRECTORY(${reem_description_out_path})

foreach(it ${reem_description_stl_files})
  get_filename_component(relative_path ${it} PATH)
  get_filename_component(basename ${it} NAME_WE)

  # create subdirectory
  add_custom_command(
    OUTPUT ${reem_description_out_path}/${relative_path}
    #COMMAND ${CMAKE_COMMAND} -E make_directory
    COMMAND mkdir -p
    ARGS ${reem_description_out_path}/${relative_path})

  # convert to ogre files
  add_custom_command(
    OUTPUT ${reem_description_out_path}/${relative_path}/${basename}.mesh
    COMMAND rosrun
    ARGS ogre_tools stl_to_mesh ${reem_description_PACKAGE_PATH}/meshes/${it} ${reem_description_out_path}/${relative_path}/${basename}.mesh
    DEPENDS ${reem_description_out_path}/${relative_path} ${reem_description_PACKAGE_PATH}/meshes/${it})

  set(reem_gen_files ${reem_gen_files} ${reem_description_out_path}/${relative_path}/${basename}.mesh)
endforeach(it)

add_custom_target(media_files ALL DEPENDS ${reem_gen_files})
