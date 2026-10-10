#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from wheel_speed.msg import TaskOne

rclpy.init()
node = Node('subscriber')

def callback(msg):
    speed = msg.ang_vel * msg.radius
    print(f'Longitudinal speed: {speed:.3f} m/s')

node.create_subscription(TaskOne, '/taskone', callback, 10)
rclpy.spin(node)