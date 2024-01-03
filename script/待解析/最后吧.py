import json
import os
from PIL import Image

images_in = "/home/dkt/test/images"  # 输入图片位置
json_in = "/home/dkt/test/jx1_json"  # 输入json位置
label_out = "/home/dkt/test/test_json"  # 输出标签位置

# 提取两文件夹内容至列表,将json后缀改为jpg，使两列表顺序相同，避免方法使两列表的文件不对应
images_list = os.listdir(images_in)
for json_name in os.listdir(json_in):       # 遍历目录下文件
    new_name = json_name.split(".")[0]          # 去除文件后缀名
    os.rename(os.path.join(json_in, json_name), os.path.join(json_in, new_name + '.jpg'))   # 重命名方法直接操作本地文件，拼接绝对路径时加上.jpg的后缀；

json_list = os.listdir(json_in)     # 获取json目录下的文件，文件已经被重命名为jpg格式了。因为下面格式会被改回，所以现在用一个变量获取jpg格式的json；

# 再将该目录下的文件重命名回去，此时会有一些jpg后缀的残留(暂不明原因)；
for i in os.listdir(json_in):
    new_name = i.split(".")[0]
    os.rename(os.path.join(json_in, i), os.path.join(json_in, new_name + '.json'))

u = 0       # 用来统计标签数量

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
# 上面更改json文件的后缀名就是为了让他们两的顺序能够对应上，否则不同后缀的文件listdir转为list时会有json和jpg顺序不对应的情况；
for image_name, json_name in zip(images_list, json_list):  # 同时遍历对应图片与json，两个list都是jpg的后缀，顺序对应的上；
    new_name = json_name.split(".")[0]  # 去除文件后缀
    i = new_name + '.json'  # 加上json后缀的文件名
    im = Image.open(os.path.join(images_in, image_name))    # 拼接构造图片的完整路径
    # 获取文件，转为字典，获取文件有多少个标签框，遍历这个标签框：在这里进行相应操作
    with open(os.path.join(json_in, i), 'r') as file:   # 打开完整路径的json文件，读模式，别名 file；
        json_data = json.load(file)     # json文件转字典
    mus = len(json_data["shapes"])  # 判断"shapes"字段的长度(多少个标签框)
    u += mus    # 每次加上单个文件的标签框数量
    for i in range(mus):  # 遍历每一个标签框
        o = 0       # 用于限制重复执行坐标点部分的if代码
        label = json_data["shapes"][i]["label"]  # 拷贝标签类并进行分类
        enl = len(json_data["shapes"][i]["points"])  # 获取坐标点数量
        for p in range(enl):    # 遍历坐标点，每个文件执行一遍坐标计算即可，所以下面if来限制多次计算
            if o == 0:
                x = [json_data["shapes"][i]["points"][p][0]] * mus * enl    # 标签框的数量 * 坐标点数量
                y = [json_data["shapes"][i]["points"][p][1]] * mus * enl    # fuck, 数值并没有乘积起来，只是变成了mus*enl份的坐标点
                print("json_x", json_data["shapes"][i]["points"][p][0])
                print("json_y", json_data["shapes"][i]["points"][p][1])
                print("x", x)
                print("y", y)
                print("标签框mus", mus)
                print("坐标点enl", enl)
                print("原图", im)
            x[o] = json_data["shapes"][i]["points"][p][0]
            y[o] = json_data["shapes"][i]["points"][p][1]
            print("坐标累加次数ooo", o)
            o = o + 1
            print("最终o", o)
        # 设置截取box框的面积范围
        if (max(x) - min(x)) * (max(y) - min(y)) <= 9999999:
            im1 = im.crop((min(x), min(y), max(x), max(y)))
            r = 0
        else:
            r = 1

        if r == 0:
            # 分类保存
            if os.path.exists(label_out + label) == 0:
                os.mkdir(label_out + label)
            im1.save(label_out + label + '/' + str(i + 1) + '_' + image_name)

print(u)  # 输出所有标签总数

'''

  //全局变量简介
  images_list[] : 存放图片文件
  json_list[] : 存放json文件
  u : 计算总标签数;
'''
