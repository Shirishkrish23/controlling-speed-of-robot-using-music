cmake_minimum_required(VERSION 3.5)
project(articubot_one)

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)

# Generate message files
rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/RobotSpeed.msg"
)

# Add executable for audio_processing_node.py
ament_python_install_package(${PROJECT_NAME})

install(PROGRAMS
  DESTINATION lib/${PROJECT_NAME}
)

# Add launch file if needed
install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
