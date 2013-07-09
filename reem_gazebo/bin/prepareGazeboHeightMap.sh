#!/bin/bash

if [ $# != 2 ];
then
	echo "Usage: $0 map_file map_side_size_in_meters"
	exit -1
fi

MAP_FILE=$1
MAP_SIZE=$2



MODEL_SDF_FILE=`rospack find reem_gazebo`/environments/reem_heightmap_1/model.sdf
GAZEBO_MAP_FILE=`rospack find reem_gazebo`/environments/reem_heightmap_1/materials/textures/map.png

NEW_SIZE="<size> $MAP_SIZE $MAP_SIZE 1.5 <\/size>"

#REALLY DIRTY WAY OF MODIFYING model.sdf Replace all the occurences of <size>A B C</size> with the new size, this could potentially modify size tags we don't want to modify
sed -i "s/<size>.* .* .*<\/size>/$NEW_SIZE/" $MODEL_SDF_FILE


cp $MAP_FILE $GAZEBO_MAP_FILE

