^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package pmb2_gazebo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.9.1 (2014-11-18)
------------------
* fixes install rule for pmb2_sensors.sh
* removes not needed output="screen"
* fixes pmb2_sensors
* adds sensors (or filters)
* adds Adler Erfurt shop worlds
* adds large_corridor world
  it's been created to validate an issue with karto not considering the
  covariance of the scan matching; see this video for instance:
  /mnt/Data/common/personal/Enrique/videos/mapping/karto_large_corridor_no_check_scan_matching_covariance.ogv
* Add pids for a xtion revolute joint
  A revolute joint with 0 limits needs to be defined for the Xtion pose wrt /base_link in order to get the point cloud properly generated in simulation. Using fixed joints is not supported by Gazebo and this is the typical workaround, i.e. defining a revolute joint with 0 limits and
  fake PID parameters.
* uses full v2.0 robot by default
* sets furniture as non-static (needed by openni-kinect plugin)
  see http://answers.gazebosim.org/question/6914/gazebo-191-openni_kinect-plugin-does-not-refresh/
* sets model name as 'pmb2' (is always the same)
* uses final dock model
* updates small_office world (with reemc one)
* adds dock prototype
* fixes doc_peaks stl and sdf
* inverts faces orientation
* updates dock_square
* updates dock_peak_out
* updates dock_circular
* refs #8415 : adds dock forms
* loads only mobile_base_controller multipliers
* adds tray trolley
  NOTE this one is of Ave Maria project
* refs #8415 : sets initial dock pose
* refs #8415 : adds dock spawner
* uses pose, with angle as yaw inside
* fixes code names
* refs #8415 : ir emitters as an array
* refs #8415 : adds dock (IR emitter) params and launch
* removes deprecated vcg files
* fixes #8221 : adds dock station to the simple office world
* refs #8221 : sets the back side to y=0
* refs #8221 : sets model bottom at z=0
* refs #8221 : removes models' database (not really needed/used)
* refs #8221 : adds dock_station model
* refs #8173 : pmb2_gazebo done (missed rm/add = mv)
* refs #8173 : pmb2_gazebo done
* Contributors: Enrique Fernandez, Jordi Pages
