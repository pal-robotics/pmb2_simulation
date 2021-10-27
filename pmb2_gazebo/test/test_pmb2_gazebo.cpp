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
#include <sensor_msgs/msg/joint_state.hpp>

template<typename MsgType>
void waitForMessage(
  const rclcpp::Node::SharedPtr & node, const std::string & topic_name,
  const std::chrono::milliseconds & timeout)
{
  typename MsgType::SharedPtr msg;

  auto sub = node->create_subscription<std_msgs::msg::String>(
    topic_name, 1, [&msg](const typename MsgType::SharedPtr recv_msg)
    {});

  rclcpp::WaitSet wait_set;
  wait_set.add_subscription(sub);
  auto ret = wait_set.wait(timeout);
  EXPECT_EQ(
    ret.kind(),
    rclcpp::WaitResultKind::Ready) << "Did not receive any message on " << topic_name;
  if (ret.kind() == rclcpp::WaitResultKind::Ready) {
    MsgType msg;
    rclcpp::MessageInfo info;
    auto ret_take = sub->take(msg, info);
    EXPECT_TRUE(ret_take) << "Error retrieving message";
  } else {
    RCLCPP_INFO_STREAM(node->get_logger(), "Got " << topic_name);
  }
}

TEST(TestGazeboPMB2, test_topics)
{
  std::shared_ptr<rclcpp::Executor> executor =
    std::make_shared<rclcpp::executors::SingleThreadedExecutor>();

  auto test_node = std::make_shared<rclcpp::Node>("test_pmb2_gazebo");

  waitForMessage<std_msgs::msg::String>(test_node, "robot_description", std::chrono::seconds(10));
//  test_node->get_clock()->
    rclcpp::sleep_for(std::chrono::seconds(20));
}

int main(int argc, char ** argv)
{
  rclcpp::init(argc, argv);
  ::testing::InitGoogleTest(&argc, argv);
  auto res = RUN_ALL_TESTS();
  rclcpp::shutdown();
  return res;
}
