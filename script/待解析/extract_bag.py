#coding:utf-8
 
import roslib;
import rosbag
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from cv_bridge import CvBridgeError
 
path='/media/dakuaitou/My Book/ROS_data/picture_0712/19-10-41/' 

class ImageCreator():
    def __init__(self):
        self.bridge = CvBridge()
        with rosbag.Bag('/media/dakuaitou/My Book/ROS_data/0712/2023-07-10-19-10-41.bag', 'r') as bag:   
            for topic,msg,t in bag.read_messages():
                if topic == "/tztek/camera0_throttle":  #图像的topic；
                        try:
                            cv_image = self.bridge.imgmsg_to_cv2(msg,"bgr8")
                        except CvBridgeError as e:
                            print("success!")
                        timestr = "%.6f" %  msg.header.stamp.to_sec()
                        image_name = timestr+ ".jpg" #图像命名：时间戳.jpg
                        cv2.imwrite(path+image_name, cv_image)  #保存；
	

if __name__ == '__main__':
 
    #rospy.init_node(PKG)
    try:
        image_creator = ImageCreator()
    except rospy.ROSInterruptException:
        pass
