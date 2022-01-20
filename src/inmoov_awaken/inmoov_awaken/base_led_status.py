#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class BaseLedStatus(Node):
    def __init__(self):
        super().__init__("base_led_status")
        self.twist_subscriber = self.create_subscription(Twist,"base/cmd_vel",self.send_cmd_vel,10)
        self.get_logger().info("base_led_status has started")

    def send_cmd_vel(self,msg):
        self.get_logger().info("LED1 Status is: %f LED2 Status velocity: %f" % (msg.linear.x, msg.angular.z))

def main(args=None):
    rclpy.init(args=args)
    node = BaseLedStatus() #MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()