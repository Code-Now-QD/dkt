import json
import os


def area(x1, x2, y1, y2):
    """
    calculate_overlap计算两个矩形框的重叠面积
    :param x1: 当前矩形框的左边界x坐标
    :param x2: 当前矩形框的右边界x坐标
    :param y1: 当前矩形框的上边界y坐标
    :param y2: 当前矩形框的下边界y坐标
    :return: 返回矩形框宽和高
    """
    # 计算矩形框宽度和高度
    cx1 = (x1 + x2) / 2
    cy1 = (y1 + y2) / 2
    width1 = x2 - x1
    height1 = y2 - y1
    return width1, height1


# 需要检测的文件
# json_in = input("需要检测的文件：")
json_in = "/home/dkt/ultralytics/data/1204-1220_new_2d/labels"
# 获取形状列表
for item in sorted(os.listdir(json_in)):
    json_file: str = os.path.join(json_in, item)  # 文件的绝对路径
    with open(json_file, "r") as f:
        json_dict = json.load(f)  # 转字典
        shapes = json_dict["shapes"]  # 获取所有形状的列表
        total_overlap = 0  # 用于累计重叠面积的总和

    # 遍历每个形状，与其他形状进行重叠面积计算
    for i in range(len(shapes)):  # 遍历有几个形状
        points1x = shapes[i]["points"][0][0]  # shapes[i]为当前的形状
        points2x = shapes[i]["points"][1][0]  # [x][y]为形状左右两点的xy坐标
        points1y = shapes[i]["points"][0][1]
        points2y = shapes[i]["points"][1][1]
        for j in range(i + 1, len(shapes)):  # +1就是始终为当前形状的下一个 避免重复计算同一个形状对之间的重叠面积
            two_points1x = shapes[j]["points"][0][0]  # shapes[j]为下一个形状
            two_points2x = shapes[j]["points"][1][0]  # [x][y]为形状左右两点的xy坐标
            two_points1y = shapes[j]["points"][0][1]
            two_points2y = shapes[j]["points"][1][1]

            # 传入当前形状和下个形状的坐标点，并返回给width
            width, height = area(points1x, points2x, points1y, points2y)
            box = width * height
            print(item, box)
