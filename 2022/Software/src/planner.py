#!/usr/bin/env python3


from ultralytics import YOLO
import rospy
import cv2 as cv
from math import atan2, cos, sin, sqrt, pi
from sensor_msgs.msg import Image
from std_msgs.msg import Float32MultiArray
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

bridge = CvBridge()
count = 0

# Load a model
model = YOLO('/home/ritesh/mobrob_ws/src/mobrob/src/images/best_06_07_2023.pt')  # load a custom model

def pipe_detection(data,pub):
    cv_image = bridge.imgmsg_to_cv2(data, "bgr8")

    # Predict with the model
    results = model.track(cv_image, persist=True)  # predict on an image

    boxes = results[0].boxes.xyxy.cpu().numpy().astype(int)
    ids = results[0].boxes.id.cpu().numpy().astype(int)
    for box, id in zip(boxes, ids):
        cv.rectangle(cv_image, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 2)
        cv.putText(
            cv_image,
            f"Id {id}",
            (box[0], box[1]),
            cv.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2,
        )

    annotated_image = bridge.cv2_to_imgmsg(cv_image, "bgr8")
    pub.publish(annotated_image)

def main():
    print("Hey Universe!")
    rospy.init_node('my_planner_node')
    annotated_img_pub = rospy.Publisher("/arrow/image", Image, queue_size=10)
    img_sub = rospy.Subscriber("/mobrob/camera/image_raw", Image, pipe_detection, annotated_img_pub)

    rospy.spin()

if __name__ == "__main__":
    main()