# Python libs
import rclpy
from rclpy.node import Node

# ROS Messages 
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class MoveCar(Node):
    def __init__(self):
        super().__init__('move_car')
        # Create publisher to control the robot
        self.publisher = self.create_publisher(Twist, "/cmd_vel", 10)
        # Create a subscriber to Laserscan topic to listen laser scans
        self.subscriber = self.create_subscription(LaserScan, "/scan", self.laserscan_callback, 10)
    
    def laserscan_callback(self, data):
        # Callback called any time a new laser scan become available
        # Setup obstacle detection ranges
        ranges = data.ranges
        middle_index = int(len(ranges) / 2)
        min_dist = min(ranges[middle_index - 30: middle_index + 30])
        
        if min_dist < 0.5:          # Obstacle detection range
            angular_z = -0.5       # Obstacle avoidance turning angle  
            linear_x = 0
        else:
            angular_z = 0
            linear_x = 0.3
        
        twist_msg = Twist()
        twist_msg.angular.z = angular_z
        twist_msg.linear.x = linear_x
        self.publisher.publish(twist_msg)


def main(args=None):
    rclpy.init(args=args)
    move_car = MoveCar()
    rclpy.spin(move_car)
    move_car.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

