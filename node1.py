#!/usr/bin/env python3
import threading
import rclpy
from rclpy.node import Node
from rt2_task.msg import RT2String

rclpy.init()
node = Node('node1')
pub = node.create_publisher(RT2String, '/rt2_string', 10)
current = RT2String()


def publish_current():
    if current.data != '':
        pub.publish(current)


node.create_timer(1.0, publish_current)


def get_input():
    while True:
        current.data = input('Enter a string: ')


threading.Thread(target=get_input, daemon=True).start()

try:
    rclpy.spin(node)
except KeyboardInterrupt:
    pass