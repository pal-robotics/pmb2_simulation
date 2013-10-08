///////////////////////////////////////////////////////////////////////////////
// Copyright (C) 2013, PAL Robotics S.L.
//
// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions are met:
//   * Redistributions of source code must retain the above copyright notice,
//     this list of conditions and the following disclaimer.
//   * Redistributions in binary form must reproduce the above copyright
//     notice, this list of conditions and the following disclaimer in the
//     documentation and/or other materials provided with the distribution.
//   * Neither the name of PAL Robotics S.L. nor the names of its
//     contributors may be used to endorse or promote products derived from
//     this software without specific prior written permission.
//
// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
// AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
// IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
// ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
// LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
// CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
// SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
// INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
// CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
// ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
// POSSIBILITY OF SUCH DAMAGE.
//////////////////////////////////////////////////////////////////////////////

#ifndef REEM_HARDWARE_GAZEBO_REEM_HARDWARE_GAZEBO_H
#define REEM_HARDWARE_GAZEBO_REEM_HARDWARE_GAZEBO_H

#include <vector>
#include <string>

#include <control_toolbox/pid.h>

#include <hardware_interface/robot_hw.h>
#include <hardware_interface/joint_state_interface.h>
#include <hardware_interface/joint_command_interface.h>

#include <pluginlib/class_list_macros.h>

#include <ros_control_gazebo/robot_sim.h>

#include <angles/angles.h>

#include <gazebo/gazebo.hh>
#include <gazebo/physics/physics.hh>
#include <gazebo/common/common.hh>

namespace reem_hardware_gazebo
{

class ReemHardwareGazebo : public ros_control_gazebo::RobotSim
{
public:

  ReemHardwareGazebo();

  // Simulation-specific
  bool initSim(ros::NodeHandle nh, gazebo::physics::ModelPtr model);
  void readSim(ros::Time time, ros::Duration period);
  void writeSim(ros::Time time, ros::Duration period);


private:
  // Raw data
  unsigned int pos_n_dof_;
  unsigned int vel_n_dof_;
  unsigned int n_dof_;

  std::vector<std::string> transmission_names_;

  std::vector<double> jnt_pos_;
  std::vector<double> jnt_vel_;
  std::vector<double> jnt_eff_;

  std::vector<double> jnt_pos_cmd_;
  std::vector<double> jnt_pos_cmd_curr_; // NOTE: This is the same as jnt_pos_ but only with the joints in pos_sim_joints_. Needs cleaner implementation

  std::vector<double> jnt_vel_cmd_;

  // Simulation-specific
  std::vector<gazebo::physics::JointPtr> sim_joints_;
  std::vector<gazebo::physics::JointPtr> pos_sim_joints_;
  std::vector<gazebo::physics::JointPtr> vel_sim_joints_;

  // Hardware interface: joints
  hardware_interface::JointStateInterface    jnt_state_interface_;
  hardware_interface::PositionJointInterface jnt_pos_cmd_interface_;
  hardware_interface::VelocityJointInterface jnt_vel_cmd_interface_;

  // PID controllers
  std::vector<control_toolbox::Pid> pids_;

};

}

#endif // REEM_HARDWARE_GAZEBO_REEM_HARDWARE_GAZEBO_H
