import random
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Temp_publisher():
    def __init__(self):
         super().__init__("temperature_publisher")
         self.publisher = self.create_publisher(String, "temperature", 10)
         self.timer_period = 1.0 
         self.timer = self.create_timer(self.timer_period, self.timer_callback)
        
    
    def time_callback(self):
         temperature = random.uniform(0,50)
         msg = String()
         msg.data =temperature
         self.publisher.publish(msg)
         self.get_logger().info(f"Publisher msg:{temperature:.2f} degrees")

def main(args=None):
        rclpy.init(args=args)

        temperature_publisher_node = Temp_publisher()

        rclpy.spin(temperature_publisher_node)

        rclpy.shutdown()      

if __name__ == "__main__":
    main()