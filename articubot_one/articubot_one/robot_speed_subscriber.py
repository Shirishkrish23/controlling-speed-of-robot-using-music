import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class RobotSpeedSubscriber(Node):
    def __init__(self):
        super().__init__('robot_speed_subscriber')
        # Create a subscription to the 'robot_speed' topic with a callback function
        self.subscription = self.create_subscription(
            Float32,            # Message type
            'robot_speed',      # Topic name
            self.speed_callback,# Callback function
            10                  # QoS profile, here 10 is the depth of the subscription queue
        )
        self.subscription  # prevent unused variable warning

    def speed_callback(self, msg):
        # Callback function to handle received messages
        # Print the received robot speed
        self.get_logger().info('Received Robot Speed: %.2f' % msg.data)


def main(args=None):
    rclpy.init(args=args)
    robot_speed_subscriber = RobotSpeedSubscriber()
    try:
        rclpy.spin(robot_speed_subscriber)  # Start spinning the node
    except KeyboardInterrupt:
        pass

    robot_speed_subscriber.destroy_node()  # Clean up the node
    rclpy.shutdown()  # Shutdown the ROS 2 communication


if __name__ == '__main__':
    main()
