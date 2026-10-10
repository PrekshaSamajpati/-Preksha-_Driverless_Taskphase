cmake_minimum_required(VERSION 3.8)
project(rt2_task)

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/RT2String.msg"
)

install(PROGRAMS
  scripts/node1.py
  scripts/node2.py
  scripts/node3.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()