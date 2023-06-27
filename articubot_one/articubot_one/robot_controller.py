import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Vector3
from std_msgs.msg import Float32

class RobotController(Node):
    def __init__(self):
        super().__init__('robot_controller')
        self.subscription = self.create_subscription(
            Float32,
            'robot_speed',
            self.speed_callback,
            10
        )
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.speed = 0.0

    def speed_callback(self, msg):
        self.speed = msg.data

    def control_robot(self):
        cmd_vel = Twist()
        cmd_vel.linear.x = self.speed
        cmd_vel.linear.y = 0.0
        cmd_vel.linear.z = 0.0
        cmd_vel.angular.x = 0.0
        cmd_vel.angular.y = 0.0
        cmd_vel.angular.z = 0.0
        self.publisher_.publish(cmd_vel)


def main(args=None):
    rclpy.init(args=args)
    robot_controller = RobotController()
    try:
        while rclpy.ok():
            robot_controller.control_robot()
            rclpy.spin_once(robot_controller)
    except KeyboardInterrupt:
        pass
    finally:
        robot_controller.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
