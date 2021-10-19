^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package pmb2_2dnav_gazebo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

3.0.2 (2021-10-19)
------------------

3.0.1 (2021-08-13)
------------------
* Resolve missing dependency
* Merge branch 'foxy_obstacle_avoidance' into 'foxy-devel'
  default world
  See merge request robots/pmb2_simulation!33
* default world
* Contributors: Noel Jimenez Garcia, Victor Lopez, victor

3.0.0 (2021-07-20)
------------------
* Add ament and apply corrections
* Migrate pmb2_2dnav_gazebo to ROS2
* First gazebo launch with ROS2
* Contributors: Victor Lopez

2.0.24 (2021-01-13)
-------------------
* Merge branch 'mapping-rgbd' into 'erbium-devel'
  feat: Add rgbd_sensors argument to pmb2 mapping
  See merge request robots/pmb2_simulation!31
* feat: Add rgbd_sensors argument to pmb2 mapping
* Contributors: victor, yueerro

2.0.23 (2020-07-30)
-------------------
* Merge branch 'rename_tf_prefix' into 'erbium-devel'
  Rename tf_prefix to robot_namespace
  See merge request robots/pmb2_simulation!30
* Rename tf_prefix to robot_namespace
* Contributors: davidfernandez, victor

2.0.22 (2020-04-14)
-------------------
* Merge branch 'fix-public-stvl' into 'erbium-devel'
  fix public sim condition for pal_pcl
  See merge request robots/pmb2_simulation!28
* fix public sim condition for pal_pcl
* Contributors: Procópio Stein, federiconardi

2.0.21 (2020-04-03)
-------------------
* Merge branch 'pmb2-stvl' into 'erbium-devel'
  Pmb2 stvl
  See merge request robots/pmb2_simulation!27
* updated config filenames
* launching pcl filters for rgbd cameras
* adding rgbd_sensors param
* Contributors: federiconardi, procopiostein

2.0.20 (2020-03-19)
-------------------

2.0.19 (2019-10-22)
-------------------
* Merge branch 'disable-laser-footprint' into 'erbium-devel'
  disabled laser filter for multi
  See merge request robots/pmb2_simulation!25
* disabled laser filter for multi
* Merge branch 'removed-relay' into 'erbium-devel'
  removed map relay
  See merge request robots/pmb2_simulation!24
* removed map relay
* Contributors: Jordan Palacios, Procópio Stein, Victor Lopez

2.0.18 (2019-10-14)
-------------------
* Merge branch 'refactoring' into 'erbium-devel'
  removed public launches in favor of using public_sim flag
  See merge request robots/pmb2_simulation!23
* removed public launches in favor of using public_sim flag
* Contributors: Procópio Stein, Victor Lopez

2.0.17 (2019-10-10)
-------------------

2.0.16 (2019-10-10)
-------------------

2.0.15 (2019-10-10)
-------------------
* Merge branch 'add-relay' into 'erbium-devel'
  added relay from map to vo_map
  See merge request robots/pmb2_simulation!22
* added relay from map to vo_map
* Contributors: Procópio Stein, Victor Lopez

2.0.14 (2019-09-25)
-------------------

2.0.13 (2019-09-23)
-------------------
* Merge branch 'stockbot-carrot-migration' into 'erbium-devel'
  added laser filter for simulations
  See merge request robots/pmb2_simulation!19
* use  vo filling
* added laser filter for simulations
* Contributors: Procópio Stein, Victor Lopez

2.0.12 (2019-08-14)
-------------------
* Merge branch 'add-robot-pose' into 'erbium-devel'
  Add robot pose to navigation.launch
  See merge request robots/pmb2_simulation!18
* Add robot pose to navigation.launch
* Contributors: Victor Lopez

2.0.11 (2019-08-01)
-------------------
* Merge branch 'multi_pmb2' into 'erbium-devel'
  Changes for multi pmb2 simulation
  See merge request robots/pmb2_simulation!17
* Changes for multi pmb2 simulation
* Contributors: Adria Roig, Victor Lopez

2.0.10 (2019-07-02)
-------------------
* Merge branch 'simple_sim' into 'erbium-devel'
  Add simple pmb2 model in launch files
  See merge request robots/pmb2_simulation!16
* Add simple pmb2 model in launch files
* Contributors: Adria Roig, Victor Lopez

2.0.9 (2019-06-17)
------------------
* Merge branch 'new_nav_cfg' into 'erbium-devel'
  moved simulation launches from pmb2_2dnav
  See merge request robots/pmb2_simulation!15
* moved simulation launches from pmb2_2dnav
* Contributors: Hilario Tome, Sai Kishor Kothakota

2.0.8 (2019-05-20)
------------------
* Merge branch 'update_adv_nav' into 'erbium-devel'
  Adv param for AdvNav
  See merge request robots/pmb2_simulation!14
* Adv param for AdvNav
* Contributors: Victor Lopez, davidfernandez

2.0.7 (2019-02-01)
------------------
* Merge branch 'gazebo_args' into 'erbium-devel'
  added extra_gazebo_args argument in launch files
  See merge request robots/pmb2_simulation!13
* added extra_gazebo_args argument in launch files
* Contributors: Sai Kishor Kothakota, Victor Lopez

2.0.6 (2019-01-25)
------------------
* Merge branch 'public_eband_conf' into 'erbium-devel'
  changing default planner in public_sim launch
  See merge request robots/pmb2_simulation!12
* changing default planner in public_sim launch
* Contributors: Sai Kishor Kothakota, Victor Lopez

2.0.5 (2019-01-23)
------------------

2.0.4 (2019-01-17)
------------------
* Merge branch 'public_sim_kinetic' into 'erbium-devel'
  add kinetic public simulation changes
  See merge request robots/pmb2_simulation!10
* add kinetic public simulation changes
* Contributors: Sai Kishor Kothakota, Victor Lopez

2.0.3 (2018-12-19)
------------------
* Merge branch 'specifics-refactor' into 'erbium-devel'
  Change robot for laser_model
  See merge request robots/pmb2_simulation!9
* Change robot for laser_model
* Contributors: Victor Lopez

2.0.2 (2018-07-25)
------------------
* Add recording argument
* Contributors: Victor Lopez

2.0.1 (2018-07-17)
------------------

2.0.0 (2018-02-05)
------------------

1.0.1 (2017-02-28)
------------------
* add tiago_support as maintainer
* Contributors: Jordi Pages

1.0.0 (2016-04-20)
------------------

0.9.7 (2016-04-15)
------------------

0.9.6 (2016-02-09)
------------------
* use robot default
* Contributors: Jeremie Deray

0.9.5 (2015-10-27)
------------------
* Update maintainer
* Contributors: Bence Magyar

0.9.4 (2015-02-18)
------------------

0.9.3 (2015-02-03)
------------------

0.9.2 (2015-02-02)
------------------
* Set 'full' as default robot
* Replace ant -> pmb2
* Rename files
* Contributors: Enrique Fernandez
