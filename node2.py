#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, String
from rt2_task.msg import RT2String

rclpy.init()
node = Node('node2')
pub = node.create_publisher(Int32, '/is_palindrome', 10)
last = {'text': ''}


def on_string(msg):
    last['text'] = msg.data
    result = Int32()
    result.data = 1 if msg.data == msg.data[::-1] else 0
    pub.publish(result)


def on_answer(msg):
    print(f"{last['text']} -> {msg.data}")


node.create_subscription(RT2String, '/rt2_string', on_string, 10)
node.create_subscription(String, '/answer', on_answer, 10)

try:
    rclpy.spin(node)
except KeyboardInterrupt:
    pass