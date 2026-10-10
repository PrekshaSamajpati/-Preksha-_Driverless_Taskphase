#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, String

rclpy.init()
node = Node('node3')
pub = node.create_publisher(String, '/answer', 10)


def on_value(msg):
    reply = String()
    reply.data = 'Yes' if msg.data == 1 else 'No'
    pub.publish(reply)


node.create_subscription(Int32, '/is_palindrome', on_value, 10)

try:
    rclpy.spin(node)
except KeyboardInterrupt:
    pass