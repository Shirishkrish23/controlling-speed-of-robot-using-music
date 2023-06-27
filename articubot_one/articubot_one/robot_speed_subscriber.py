import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class RobotSpeedSubscriber(Node):
    def __init__(self):
        super().__init__('robot_speed_subscriber')
        self.subscription = self.create_subscription(
            Float32,
            'robot_speed',
            self.speed_callback,
            10
        )
        self.subscription  # prevent unused variable warning

    def speed_callback(self, msg):
        self.get_logger().info('Received Robot Speed: %.2f' % msg.data)


def main(args=None):
    rclpy.init(args=args)
    robot_speed_subscriber = RobotSpeedSubscriber()
    try:
        rclpy.spin(robot_speed_subscriber)
    except KeyboardInterrupt:
        pass

    robot_speed_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
