import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Vector3
from std_msgs.msg import Float32

class RobotController(Node):
    def __init__(self):
        super().__init__('robot_controller')

        # Create a subscription to receive the robot speed
        self.subscription = self.create_subscription(
            Float32,
            'robot_speed',
            self.speed_callback,
            10
        )

        # Create a publisher to send velocity commands to the robot
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)

        # Initialize the robot speed
        self.speed = 0.0

    def speed_callback(self, msg):
        # Callback function to update the robot speed when a new message is received
        self.speed = msg.data

    def control_robot(self):
        # Create a Twist message for velocity commands
        cmd_vel = Twist()

        # Set the linear velocity along the x-axis using the robot speed
        cmd_vel.linear.x = self.speed

        # Set the remaining components of the Twist message to zero
        cmd_vel.linear.y = 0.0
        cmd_vel.linear.z = 0.0
        cmd_vel.angular.x = 0.0
        cmd_vel.angular.y = 0.0
        cmd_vel.angular.z = 0.0

        # Publish the Twist message to control the robot
        self.publisher_.publish(cmd_vel)


def main(args=None):
    # Initialize the ROS 2 system
    rclpy.init(args=args)

    # Create an instance of the RobotController class
    robot_controller = RobotController()

    try:
        # Main control loop
        while rclpy.ok():
            # Control the robot based on the received speed
            robot_controller.control_robot()

            # Process any pending messages
            rclpy.spin_once(robot_controller)
    except KeyboardInterrupt:
        pass
    finally:
        # Clean up the node
        robot_controller.destroy_node()

        # Shutdown the ROS 2 communication
        rclpy.shutdown()

if __name__ == '__main__':
    main()
