^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package ant_controller_configuration_gazebo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.9.1 (2014-11-18)
------------------
* updates the joint name
* Add pids for a xtion revolute joint
  A revolute joint with 0 limits needs to be defined for the Xtion pose wrt /base_link in order to get the point cloud properly generated in simulation. Using fixed joints is not supported by Gazebo and this is the typical workaround, i.e. defining a revolute joint with 0 limits and
  fake PID parameters.
* only multipliers could be different in simulation
  NOTE they should be always 1.0 (the default), so we
  could even remove this file
* adds base_frame_id
* refs #8173 : ant_controller_configuration_gazebo done
* Contributors: Enrique Fernandez, Jordi Pages
