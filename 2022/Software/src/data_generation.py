#!/usr/bin/env python

import rospy
import cv2 as cv
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

bridge = CvBridge()
count = 0

def imgCallback(data):
    global count
    cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
    cv.imshow("Raw image", cv_image)
    
    if count % 30 == 0:
        quotient = count//30
        cv.imwrite("images/frame" + str(quotient) + ".jpg", cv_image)
        print("frame no. " + str(quotient) + " stored")
    count += 1
    
    # Display the annotated frame
    cv.imshow("Camera feed", cv_image)
    cv.waitKey(3)


def main():
    print("Hey Universe!")
    rospy.init_node('my_planner_node')
    img_sub = rospy.Subscriber("/mobrob/camera/image_raw", Image, imgCallback)
    rospy.spin()

if __name__ == "__main__":
    main()
