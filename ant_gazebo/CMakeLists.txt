cmake_minimum_required(VERSION 2.8.3)
project(ant_gazebo)

find_package(catkin REQUIRED)

catkin_package()

install(PROGRAMS scripts/sensors.sh
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

foreach(dir launch Media models worlds)
    install(DIRECTORY ${dir}/
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)
