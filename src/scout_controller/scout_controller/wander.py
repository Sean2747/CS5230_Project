import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

#at this point, this node only tells the car to run in a circle

class WanderNode(Node):                                                         
    def __init__(self):
        super().__init__("wander_node")
        self.cmd_vel_pub_=self.create_publisher(Twist, "/cmd_vel", 10)
        self.timer_=self.create_timer(0.5, self.send_velocity_command)
        self.get_logger().info("Wander node has started.")

    def send_velocity_command(self):
        msg = Twist()
        msg.linear.x = 1.5
        msg.angular.z = 1.0
        self.cmd_vel_pub_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = WanderNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=='__main__':
    main()