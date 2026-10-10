#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from wheel_speed.msg import TaskOne

rclpy.init()
node = Node('publisher')
pub = node.create_publisher(TaskOne, '/taskone', 10)

while rclpy.ok():
    msg = TaskOne()
    msg.ang_vel = float(input('Angular velocity (rad/s): '))
    msg.radius = float(input('Radius (m): '))
    pub.publish(msg)
    print('Published')