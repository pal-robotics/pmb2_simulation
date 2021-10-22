// Copyright 2021 PAL Robotics SL.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include <rclcpp/rclcpp.hpp>
#include <gtest/gtest.h>
#include <std_msgs/msg/string.hpp>


TEST(TestGazeboPMB2, test_topics)
{

  std::shared_ptr<rclcpp::Executor> executor =
    std::make_shared<rclcpp::executors::SingleThreadedExecutor>();

  auto test_node = std::make_shared<rclcpp::Node>("test_pmb2_gazebo");

  std_msgs::msg::String::SharedPtr robot_description;

  std::string topic_name = "robot_description";
  auto robot_description_sub = test_node->create_subscription<std_msgs::msg::String>(
    topic_name, 1, [&robot_description](const std_msgs::msg::String::SharedPtr msg)
    {
      robot_description = msg;
    });

  rclcpp::WaitSet wait_set;
  wait_set.add_subscription(robot_description_sub);
  auto ret = wait_set.wait(std::chrono::seconds(10));
  EXPECT_EQ(ret.kind(), rclcpp::WaitResultKind::Ready) << "Did not receive any message on " << topic_name;
  if (ret.kind() == rclcpp::WaitResultKind::Ready)
  {
    std_msgs::msg::String msg;
    rclcpp::MessageInfo info;
    auto ret_take = robot_description_sub->take(msg, info);
    EXPECT_TRUE(ret_take) << "Error retrieving message";
  }
  else
  {
    RCLCPP_INFO_STREAM(test_node->get_logger(), "Got " << topic_name);
  }
}

int main(int argc, char ** argv)
{
  rclcpp::init(argc, argv);
  ::testing::InitGoogleTest(&argc, argv);
  auto res = RUN_ALL_TESTS();
  rclcpp::shutdown();
  return res;
}

