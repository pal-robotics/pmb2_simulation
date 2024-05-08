^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package pmb2_gazebo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

4.0.10 (2024-05-08)
-------------------
* added pose configuration in spawn entity
* added pose conifiguration in spawn_entity args
* Contributors: martinaannicelli

4.0.9 (2024-04-11)
------------------
* Merge branch 'feat/ros2-pipelines' into 'humble-devel'
  navigation pipeline integration for private sim
  See merge request robots/pmb2_simulation!68
* cosmetic
* update readme and cosmetic
* removed slam arg
* linters
* navigation pipeline integration for private sim
* Contributors: andreacapodacqua, antoniobrandi

4.0.8 (2024-02-05)
------------------

4.0.7 (2024-02-02)
------------------
* Merge branch 'feat/register-components' into 'humble-devel'
  use single entry point for navigation
  See merge request robots/pmb2_simulation!66
* use single entry point for navigation
* Merge branch 'abr/fix/world-name' into 'humble-devel'
  moving world_name to pal_gazebo_worlds
  See merge request robots/pmb2_simulation!65
* moving world_name to pal_gazebo_worlds
* Contributors: Noel Jimenez, antoniobrandi

4.0.6 (2023-11-14)
------------------
* Add website tag
* Contributors: Noel Jimenez

4.0.5 (2023-11-13)
------------------
* Set use_sim_time true
* Remove pal flags dependency
* Contributors: Noel Jimenez

4.0.4 (2023-06-16)
------------------
* Merge branch 'fix/set-is-robot' into 'humble-devel'
  Use a different navigation launcher for simulation
  See merge request robots/pmb2_simulation!60
* use pmb2_sim_navigation
* setting is_robot argument for simulation
* Contributors: antoniobrandi

4.0.3 (2023-04-28)
------------------
* add missing gazebo_plugins dependencies
* Contributors: Noel Jimenez

4.0.2 (2023-02-08)
------------------
* Merge branch 'fix/2dnav' into 'humble-devel'
  using pmb2_2dnav
  See merge request robots/pmb2_simulation!55
* using pmb2_2dnav
* Merge branch 'robot_state_publisher' into 'humble-devel'
  remove robot_state_publisher from pmb2_spawn
  See merge request robots/pmb2_simulation!53
* remove robot_state_publisher from pmb2_spawn
* Contributors: Jordan Palacios, Noel Jimenez, antoniobrandi

4.0.1 (2022-11-30)
------------------

4.0.0 (2022-11-08)
------------------
* Merge branch 'refactor_simulation_launchers' into 'humble-devel'
  Refactor simulation launchers
  See merge request robots/pmb2_simulation!50
* move navigation to simulation launcher
* Contributors: Jordan Palacios, Noel Jimenez

3.0.3 (2022-10-21)
------------------
* Merge branch 'add_missing_dep' into 'humble-devel'
  add missing dependency
  See merge request robots/pmb2_simulation!47
* add missing dependency
* Merge branch 'cleanup' into 'humble-devel'
  Update package.xml deps
  See merge request robots/pmb2_simulation!46
* update package.xml deps
* Merge branch 'refactor_launch_files' into 'humble-devel'
  Refactor ld population
  See merge request robots/pmb2_simulation!42
* refactor LaunchDescription population
* Merge branch 'update_copyright' into 'humble-devel'
  Update copyright and license
  See merge request robots/pmb2_simulation!41
* update copyright and license
* Merge branch 'update_maintainers' into 'humble-devel'
  update maintainers
  See merge request robots/pmb2_simulation!40
* update maintainers
* Merge branch 'run_tests' into 'humble-devel'
  fix linter errors
  See merge request robots/pmb2_simulation!39
* linters
* Contributors: Jordan Palacios, Noel Jimenez

3.0.2 (2021-10-19)
------------------
* Add gazebo_ros2_control dependency
* Contributors: Victor Lopez

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
* Cleanup old launch files
* Correct python launch file
* Add ament and apply corrections
* Cleanup
* Cleanup pmb2_gazebo spawn
* Path fixes for gazebo
* First gazebo launch with ROS2
* Contributors: Victor Lopez

2.0.24 (2021-01-13)
-------------------

2.0.23 (2020-07-30)
-------------------
* Merge branch 'rename_tf_prefix' into 'erbium-devel'
  Rename tf_prefix to robot_namespace
  See merge request robots/pmb2_simulation!30
* Rename tf_prefix to robot_namespace
* Contributors: davidfernandez, victor

2.0.22 (2020-04-14)
-------------------
* Merge branch 'add-more-gz-args' into 'erbium-devel'
  Add more gz args to use other worlds or models
  See merge request robots/pmb2_simulation!29
* Add more gz args to use other worlds or models
* Contributors: Victor Lopez, victor

2.0.21 (2020-04-03)
-------------------

2.0.20 (2020-03-19)
-------------------

2.0.19 (2019-10-22)
-------------------

2.0.18 (2019-10-14)
-------------------
* Merge branch 'refactoring' into 'erbium-devel'
  removed public launches in favor of using public_sim flag
  See merge request robots/pmb2_simulation!23
* removed joystick teleop
* Contributors: Procópio Stein, Victor Lopez

2.0.17 (2019-10-10)
-------------------
* Merge branch 'remove-sonar-cloud' into 'erbium-devel'
  remove sonar cloud
  See merge request robots/pmb2_simulation!21
* remove sonar cloud
* Contributors: Procópio Stein, Victor Lopez

2.0.16 (2019-10-10)
-------------------

2.0.15 (2019-10-10)
-------------------

2.0.14 (2019-09-25)
-------------------
* Merge branch 'remove-speed-limit' into 'erbium-devel'
  removed speed limit
  See merge request robots/pmb2_simulation!20
* removed remap of twist_mux topic
* removed speed limit
* Contributors: Procópio Stein, Victor Lopez

2.0.13 (2019-09-23)
-------------------

2.0.12 (2019-08-14)
-------------------

2.0.11 (2019-08-01)
-------------------
* Merge branch 'multi_pmb2' into 'erbium-devel'
  Changes for multi pmb2 simulation
  See merge request robots/pmb2_simulation!17
* Fix parameters in multi pmb2 simulation
* Changes for multi pmb2 simulation
* Contributors: Adria Roig, Victor Lopez

2.0.10 (2019-07-02)
-------------------
* Merge branch 'simple_sim' into 'erbium-devel'
  Add simple pmb2 model in launch files
  See merge request robots/pmb2_simulation!16
* Missing simple_models_gazebo depend
* Add simple pmb2 model in launch files
* Contributors: Adria Roig, Victor Lopez

2.0.9 (2019-06-17)
------------------

2.0.8 (2019-05-20)
------------------

2.0.7 (2019-02-01)
------------------

2.0.6 (2019-01-25)
------------------

2.0.5 (2019-01-23)
------------------
* Merge branch 'args_fix' into 'erbium-devel'
  fix for unused arg exception with pass_all_args
  See merge request robots/pmb2_simulation!11
* fix for unused arg exception with pass_all_args
* Contributors: Sai Kishor Kothakota, Victor Lopez

2.0.4 (2019-01-17)
------------------

2.0.3 (2018-12-19)
------------------
* Merge branch 'specifics-refactor' into 'erbium-devel'
  Change robot for laser_model
  See merge request robots/pmb2_simulation!9
* Add and pass all arguments
* Remove unused argument
* Change robot for laser_model
* Contributors: Victor Lopez

2.0.2 (2018-07-25)
------------------

2.0.1 (2018-07-17)
------------------
* Add recording arguments
* Merge branch 'prevent-upload-warning' into 'erbium-devel'
  prevent calling deprecated launch file
  See merge request robots/pmb2_simulation!7
* prevent calling deprecated launch file
* Contributors: Hilario Tome, Jordi Pages, Victor Lopez

2.0.0 (2018-02-05)
------------------
* Use pal_gazebo_worlds
* tmp addition of 'pal_robot_info' in spawn launch
* Contributors: Jeremie Deray, Victor Lopez

1.0.1 (2017-02-28)
------------------
* refs #14797. Add public_sim argument
* add tiago_support as maintainer
* Contributors: Jordi Pages

1.0.0 (2016-04-20)
------------------
* Add missing gazebo_plugins dependency
* Contributors: Victor Lopez

0.9.7 (2016-04-15)
------------------
* Update simulation hardware abstraction dependence
* rm ususless launch
* rm sim dock launch as it doesn,t exist yet
* Contributors: Jeremie Deray, Sam Pfeiffer

0.9.6 (2016-02-09)
------------------
* use robot default
* removed worlds that should be there!
* Contributors: Jeremie Deray

0.9.5 (2015-10-27)
------------------
* Don't install deleted file
* Remove dependency of removed package
* Remove scripts
* Update maintainer
* Remove sensors script reference
* Contributors: Bence Magyar

0.9.4 (2015-02-18)
------------------
* Make rgbd camera fixed
* Use full robot by default
* Contributors: Enrique Fernandez

0.9.3 (2015-02-03)
------------------

0.9.2 (2015-02-02)
------------------
* Replace ant -> pmb2
* Rename files
* Contributors: Enrique Fernandez
