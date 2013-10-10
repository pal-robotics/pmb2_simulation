cmake_minimum_required(VERSION 2.6.4)
include($ENV{ROS_ROOT}/core/rosbuild/rosbuild.cmake)

rosbuild_init()

rosbuild_find_ros_package(xacro)
rosbuild_find_ros_package(reem_description)

# Generate an up-to-date URDF robot description of REEM
set(INPUT_XACRO_FILE ${reem_description_PACKAGE_PATH}/robots/reem_full.urdf.xacro)
set(OUTPUT_URDF_FILE ${CMAKE_CURRENT_SOURCE_DIR}/models/reem_full/model.urdf)

add_custom_command(OUTPUT ${OUTPUT_URDF_FILE}
                   COMMAND ${xacro_PACKAGE_PATH}/xacro.py ${INPUT_XACRO_FILE} -o ${OUTPUT_URDF_FILE})

add_custom_target(generate_reem_urdf ALL DEPENDS ${OUTPUT_URDF_FILE})


# Generate an up-to-date URDF robot description of REEM with a head-mounted RGBD sensor
set(INPUT_RGBD_XACRO_FILE ${reem_description_PACKAGE_PATH}/robots/reem_rgbd.urdf.xacro)
set(OUTPUT_RGBD_URDF_FILE ${CMAKE_CURRENT_SOURCE_DIR}/models/reem_rgbd/model.urdf)

add_custom_command(OUTPUT ${OUTPUT_RGBD_URDF_FILE}
                   COMMAND ${xacro_PACKAGE_PATH}/xacro.py ${INPUT_RGBD_XACRO_FILE} -o ${OUTPUT_RGBD_URDF_FILE})

add_custom_target(generate_reem_rgbd_urdf ALL DEPENDS ${OUTPUT_RGBD_URDF_FILE})

# Generate an up-to-date URDF robot description of REEM with an AR marker on its right hand
set(INPUT_RIGHT_HAND_MARKER_XACRO_FILE ${reem_description_PACKAGE_PATH}/robots/reem_right_hand_marker.urdf.xacro)
set(OUTPUT_RIGHT_HAND_MARKER_URDF_FILE ${CMAKE_CURRENT_SOURCE_DIR}/models/reem_right_hand_marker/model.urdf)

add_custom_command(OUTPUT ${OUTPUT_RIGHT_HAND_MARKER_URDF_FILE}
                   COMMAND ${xacro_PACKAGE_PATH}/xacro.py ${INPUT_RIGHT_HAND_MARKER_XACRO_FILE} -o ${OUTPUT_RIGHT_HAND_MARKER_URDF_FILE})

add_custom_target(generate_reem_right_hand_marker_urdf ALL DEPENDS ${OUTPUT_RIGHT_HAND_MARKER_URDF_FILE})


# Generate an up-to-date URDF robot description of the REEM head
set(INPUT_HEAD_XACRO_FILE ${reem_description_PACKAGE_PATH}/robots/reem_head.urdf.xacro)
set(OUTPUT_HEAD_URDF_FILE ${CMAKE_CURRENT_SOURCE_DIR}/models/reem_head/model.urdf)

add_custom_command(OUTPUT ${OUTPUT_HEAD_URDF_FILE}
                   COMMAND ${xacro_PACKAGE_PATH}/xacro.py ${INPUT_HEAD_XACRO_FILE} -o ${OUTPUT_HEAD_URDF_FILE})

add_custom_target(generate_reem_head_urdf ALL DEPENDS ${OUTPUT_HEAD_URDF_FILE})

# Generate an up-to-date URDF robot description of the REEM arm
set(INPUT_ARM_XACRO_FILE ${reem_description_PACKAGE_PATH}/robots/reem_arm.urdf.xacro)
set(OUTPUT_ARM_URDF_FILE ${CMAKE_CURRENT_SOURCE_DIR}/models/reem_arm/model.urdf)

add_custom_command(OUTPUT ${OUTPUT_ARM_URDF_FILE}
                   COMMAND ${xacro_PACKAGE_PATH}/xacro.py ${INPUT_ARM_XACRO_FILE} -o ${OUTPUT_ARM_URDF_FILE})

add_custom_target(generate_reem_arm_urdf ALL DEPENDS ${OUTPUT_ARM_URDF_FILE})


# Generate an up-to-date URDF robot description of the REEM upper body
set(INPUT_UPPER_BODY_XACRO_FILE ${reem_description_PACKAGE_PATH}/robots/reem_upper_body.urdf.xacro)
set(OUTPUT_UPPER_BODY_URDF_FILE ${CMAKE_CURRENT_SOURCE_DIR}/models/reem_upper_body/model.urdf)

add_custom_command(OUTPUT ${OUTPUT_UPPER_BODY_URDF_FILE}
                   COMMAND ${xacro_PACKAGE_PATH}/xacro.py ${INPUT_UPPER_BODY_XACRO_FILE} -o ${OUTPUT_UPPER_BODY_URDF_FILE})

add_custom_target(generate_reem_upper_body_urdf ALL DEPENDS ${OUTPUT_UPPER_BODY_URDF_FILE})


# Create symlink to robot model resources (meshes, images)
#Never use absolute paths, as they are broken when the stacks are copied to another computer
#Better solution is in the way, see https://redmine/issues/5827
set(INPUT_MESHES_DIR ../../../../reem_common/reem_description/meshes)
set(OUTPUT_MESHES_SYMLINK ${CMAKE_CURRENT_SOURCE_DIR}/models/reem_description/meshes)

# NOTE: Because of a cmake bug [1], we cannot add a custom command/target pair here, otherwise calling 'make clean'
# deletes the pointed-to folder contents!. This is fixed in CMake 2.8.11
# [1] http://public.kitware.com/Bug/view.php?id=10538
execute_process(COMMAND ${CMAKE_COMMAND} -E create_symlink ${INPUT_MESHES_DIR} ${OUTPUT_MESHES_SYMLINK})

# add_custom_command(OUTPUT ${OUTPUT_MESHES_SYMLINK}
#                    COMMAND ${CMAKE_COMMAND} -E create_symlink ${INPUT_MESHES_DIR} ${OUTPUT_MESHES_SYMLINK})
# 
# add_custom_target(generate_meshes_link ALL DEPENDS ${OUTPUT_MESHES_SYMLINK})
