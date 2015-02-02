#!/bin/sh
#
# Starts the sensor given by argument.
# If no argument is given, no sensor is started.
#
# Supported sensors are all pmb2_laser_sensors pkg launch files.
# This allows to run sensor filters or sensors not supported or
# running inside gazebo.

if [ $# -gt 2 ]; then
    SENSOR=$1
    roslaunch pmb2_laser_sensors ${SENSOR}.launch
fi

