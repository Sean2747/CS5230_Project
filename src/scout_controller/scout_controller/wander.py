import math
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class WanderNode(Node):                                                         
    def __init__(self):
        super().__init__("wander_node")
        self.turning = False
        self.cmd_vel_pub_=self.create_publisher(Twist, "/cmd_vel", 10)
        self.scan_sub_ = self.create_subscription(LaserScan, "/scan", self.lidar_callback, 10)
        self.timer_=self.create_timer(0.5, self.send_velocity_command)
        self.get_logger().info("Wander node has started.")

    def send_velocity_command(self):
        msg = Twist()
        if self.turning == True:
            msg.linear.x = 0.0
            msg.angular.z = 0.5
        else:
            msg.linear.x = 1.5
            msg.angular.z = 0.0
        self.cmd_vel_pub_.publish(msg)

    def lidar_callback(self, msg: LaserScan):
        i = 319
        window = msg.ranges[max(0, i-15):min(len(msg.ranges), i+16)]

        vals = [r for r in window if math.isfinite(r) and r > msg.range_min]
        front_distance = min(vals) if vals else msg.range_max
        #front_distance = min(min(msg.ranges[0:20] + msg.ranges[-20:]), 10.0)

        if front_distance < 4.0:
            self.turning = True
        else:
            self.turning = False


def main(args=None):
    rclpy.init(args=args)
    node = WanderNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=='__main__':
    main()