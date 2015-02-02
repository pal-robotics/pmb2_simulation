^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package ant_2dnav_gazebo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.9.1 (2014-11-18)
------------------
* takes map from $HOME/.pal/ant_maps
* uses full v2.0 robot by default
* sets PAL local planner as default also for simulation
* changes to trajectory local planner as default
  instead of PAL
  NOTE that PAL was working correctly, but the robot moves backwards
  specially when it starts to follow a new path
* sets small_office as default one
  NOTE with simple_office the laser range (5.6m) is very short and karto fails to create a map
* syncs with reem_2dnav_gazebo/launch
* refs #8317 : uses single rviz layout
* refs #8173 : ant_2dnav_gazebo done
* Contributors: Enrique Fernandez
