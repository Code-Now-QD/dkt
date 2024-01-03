from PIL import Image
import os
import json
import cv2

image_path = "/home/dkt/test/images"  # 存放图片文件夹
json_path = "/home/dkt/test/train_json"  # 存放json的文件夹
label_class = "/home/dkt/test/test_json/"  # 用于存放标签分类

# 提取两文件夹内容至列表,使用特殊方式使两列表顺序相同
list1 = os.listdir(image_path)
for json_name in os.listdir(json_path):
    new_name = json_name.split(".")[0]
    os.rename(os.path.join(json_path, json_name), os.path.join(json_path, new_name + '.jpg'))

list2 = os.listdir(json_path)

for json_name in os.listdir(json_path):
    new_name = json_name.split(".")[0]
    os.rename(os.path.join(json_path, json_name), os.path.join(json_path, new_name + '.json'))

u = 0

'''
  //循环变量简介
  im : 原始图像信息
  im1 : 截取后图像信息
  json_data : json文件信息
  o : 控制先创建x[],y[],然后依次写入值
  x[] : 存放多边形的所有x轴坐标
  y[] : 存放多边形的所有y轴坐标
  r : 控制在执行crop操作时才能进行保存
'''
for image_name, json_name in zip(list1, list2):  # 同时便利对应图片与json
    new_name = json_name.split(".")[0]
    json_name = new_name + '.json'
    im = Image.open(os.path.join(image_path, image_name))
    with open(os.path.join(json_path, json_name), 'r') as file:
        json_data = json.load(file)
    mus = len(json_data["shapes"])  # 判断"shapes"字段的长度(多少个标签框)
    u = u + mus
    for i in range(mus):  # 遍历每一个标签框
        o = 0
        label = json_data["shapes"][i]["label"]  # 拷贝标签类并进行分类
        enl = len(json_data["shapes"][i]["points"])  # 判断多少个坐标点
        for p in range(enl):
            if o == 0:
                x = [json_data["shapes"][i]["points"][p][0]] * mus * enl
                y = [json_data["shapes"][i]["points"][p][1]] * mus * enl
            x[o] = json_data["shapes"][i]["points"][p][0]
            y[o] = json_data["shapes"][i]["points"][p][1]
            o = o + 1
        # 设置截取box框的面积范围
        if (max(x) - min(x)) * (max(y) - min(y)) <= 9999999:
            im1 = im.crop((min(x), min(y), max(x), max(y)))
            r = 0
        else:
            r = 1

        if r == 0:
            # 分类保存
            if os.path.exists(label_class + label) == 0:
                os.mkdir(label_class + label)
            im1.save(label_class + label + '/' + str(i + 1) + '_' + image_name)
            print(1)

print(u)  # 输出所有标签总数

'''
  //全局变量简介
  list1[] : 存放图片文件
  list2[] : 存放json文件
  u : 计算总标签数;
'''
