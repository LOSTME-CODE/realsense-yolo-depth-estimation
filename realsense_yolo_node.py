import rclpy
from rclpy.node import Node
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from ultralytics import YOLO

class RealSenseYOLO(Node):
    def __init__(self):
        super().__init__('realsense_yolo')
        self.bridge = CvBridge()
        self.model = YOLO("yolov8n.pt")  # Load YOLOv8 model

        # Subscribe to RealSense topics
        self.color_sub = self.create_subscription(
            Image, '/camera/color/image_raw', self.color_callback, 10)
        self.depth_sub = self.create_subscription(
            Image, '/camera/depth/image_rect_raw', self.depth_callback, 10)
        
        self.depth_image = None  # Store latest depth frame

    def color_callback(self, msg):
        frame = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        results = self.model(frame)  # Run YOLO object detection

        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])  # Extract bounding box
                
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                # Depth estimation (if depth frame is available)
                if self.depth_image is not None:
                    depth_value = self.get_depth(int((x1 + x2) / 2), int((y1 + y2) / 2))
                    cv2.putText(frame, f"Depth: {depth_value:.2f}m", 
                                (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 
                                0.5, (0, 255, 255), 2)

                    self.get_logger().info(f"Detected object at ({x1}, {y1}), Depth: {depth_value:.2f}m")

        cv2.imshow("YOLO Detection", frame)
        cv2.waitKey(1)

    def depth_callback(self, msg):
        self.depth_image = self.bridge.imgmsg_to_cv2(msg, "16UC1")

    def get_depth(self, x, y):
        if self.depth_image is not None:
            if 0 <= x < self.depth_image.shape[1] and 0 <= y < self.depth_image.shape[0]:
                return self.depth_image[y, x] / 1000.0  # Convert mm to meters
        return 0.0

def main():
    rclpy.init()
    node = RealSenseYOLO()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
