cmake_minimum_required(VERSION 3.8)
project(wheel_speed)

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/TaskOne.msg"
)

install(PROGRAMS
  scripts/publisher.py
  scripts/subscriber.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()