import json
import os
import cv2
from cv2 import FONT_HERSHEY_SIMPLEX

img_folder_path = '/home/dkt/test/images'  # 图片存放文件夹
folder_path = '/home/dkt/test/fg2'  # 存放标注数据的文件地址
txt_folder_path = "/home/dkt/test/txt2/"  # 转换后的txt标签文件存放的文件夹

 
# 相对坐标格式
def show_label_from_txt(img_path, txt_path):
    window_name = ('src')
    cv2.namedWindow(window_name, cv2.WINDOW_FREERATIO)
    src_img = cv2.imread(img_path)
    h, w = src_img.shape[:2]
    font = cv2.FONT_HERSHEY_SIMPLEX
    with open(txt_path, "r", encoding='UTF-8') as f:
        line = f.readline()
        # 该函数返回的是字符串
        newline = line[1: ]
        data = newline.split('  ')
        # 返回值是字符串列表
        label = data[0]
        cx = float(data[1])
        cy = float(data[2])
        ww = float(data[3])
        hh = float(data[4])
        x1 = int(cx * w - 0.5 * ww * w)
        x2 = int(cx * w + 0.5 * ww * w)
        y1 = int(cy * h - 0.5 * hh * h)
        y2 = int(cy * h + 0.5 * hh * h)
        p1 = (x1, y1)
        p2 = (x2, y2)
        cv2.rectangle(src_img, p1, p2, (0, 255, 0), 5)
        # 图片，顶点1，顶点2，矩形颜色，组成矩形的线粗细若为负值如-1表示绘制一个填充矩形
        cv2.putText(src_img, label, p1, FONT_HERSHEY_SIMPLEX, 200, (255, 0, 0), 5)
        # 图片，要绘制的文本字符串，文本字符串左下角的坐标，字体类型，字体大小，文本颜色，线宽
        x00 = float(data[5])*w
        y00 = float(data[6])*h
        x01 = float(data[7])*w
        y01 = float(data[8])*h
        x11 = float(data[9])*w
        y11 = float(data[10])*h
        x10 = float(data[11])*w
        y10 = float(data[12])*h
        coordinates = [[x00,y00],[x01,y01],[x11,y11],[x10,y10]]
        for coo in coordinates:
            cv2.circle(src_img,(int(coo[0]),int(coo[1])),25,(0,255,0),-5)
        #图像，圆心坐标，半径，圆边框颜色，正值表示线宽负值表示填充一个圆形
        cv2.imshow(window_name, src_img)
        cv2.waitKey(0)
    cv2.destroyAllWindows()
    return

 
i = 0
for txtfile in os.listdir(txt_folder_path):
    txt_path = os.path.join(txt_folder_path, txtfile)
    # 一直报错utf-8，原因是我txt文件没有放对位置，地址没有写对，导致
    # for循环第一次循环没找到txt文件解码失败。
    i += 1
    if i > 15:
        break
    # 如果是一个子目录就继续
    if os.path.isdir(txt_path):
        continue
    print("txt_path:\t", txt_path)
    img_name = txtfile.split("\\")[-1].split(".")[0] + ".jpg"
    img_path = os.path.join(img_folder_path, img_name)
    show_label_from_txt(img_path, txt_path)

