^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package pmb2_gazebo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

2.0.32 (2023-04-04)
-------------------
* Merge branch 'fix_world' into 'erbium-devel'
  Move world to pal_gazebo_world + rm duplicated models
  See merge request robots/pmb2_simulation!57
* Remove Media, models and worlds from the install rules
* Move models to pal_gazebo_worlds
* Move models dependent of the worlds
* Move world to pal_gazebo_world + rm duplicated models
* Contributors: saikishor, thomaspeyrucain

2.0.31 (2023-02-23)
-------------------

2.0.30 (2023-01-27)
-------------------

2.0.29 (2022-08-18)
-------------------

2.0.28 (2022-02-23)
-------------------

2.0.27 (2021-11-29)
-------------------

2.0.26 (2021-09-17)
-------------------
* Merge branch 'gallium_fixes' into 'erbium-devel'
  Gallium fixes
  See merge request robots/pmb2_simulation!35
* Use robot_state_publisher instead of state_publisher
* Contributors: Jordan Palacios

2.0.25 (2021-09-17)
-------------------
* Merge branch 'pass-laser-info' into 'erbium-devel'
  Pass laser info to navigation.sh
  See merge request robots/pmb2_simulation!34
* Add missing dependency on pal_gazebo_plugins
* Contributors: Victor Lopez, victor

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
