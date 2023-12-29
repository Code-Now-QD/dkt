import json
import os


def calculate_overlap(rect1, rect2):
    """
    calculate_overlap计算形状的重叠
    :param rect1: 当前形状的顶点坐标
    :param rect2: 对比形状的顶点坐标
    :return: 返回重叠面积
    """
    print(rect1)
    print(rect2)
    # 计算重叠部分的坐标
    x1 = max(p1[0], r1[0])
    y1 = max(p1[1], r1[1])
    x2 = min(p2[0], r2[0])
    y2 = min(p2[1], r2[1])

    # 计算重叠面积
    overlap_width = x2 - x1
    overlap_height = y2 - y1
    overlap_area = max(overlap_width, 0) * max(overlap_height, 0)

    return overlap_area


# 需要检测的文件
json_in = "/home/dkt/ultralytics/data/1204-1220_new_2d/重合框"

# 获取形状列表
for item in sorted(os.listdir(json_in)):
    json_file: str = os.path.join(json_in, item)     # 文件的绝对路径
    with open(json_file, "r") as f:
        json_dict = json.load(f)    # 转字典
        shapes = json_dict["shapes"]  # 获取所有形状的列表
        total_overlap = 0  # 用于累计重叠面积的总和

    # 遍历每个形状，与其他形状进行重叠面积计算
    for i in range(len(shapes)):    # 遍历有几个形状
        points1x = shapes[i]["points"][0][0]    # shapes[i]为当前的形状
        points2x = shapes[i]["points"][1][0]    # [x][y]为形状左右两点的xy坐标
        points1y = shapes[i]["points"][0][1]
        points2y = shapes[i]["points"][1][1]

        for j in range(i + 1, len(shapes)):  # +1就是始终为当前形状的下一个 避免重复计算同一个形状对之间的重叠面积
            two_points1x = shapes[j]["points"][0][0]  # shapes[j]为下一个形状
            two_points2x = shapes[j]["points"][1][0]  # [x][y]为形状左右两点的xy坐标
            two_points1y = shapes[j]["points"][0][1]
            two_points2y = shapes[j]["points"][1][1]

            # 传入当前形状和下个形状的坐标点，并返回给overlap_area
            overlap_area: float = calculate_overlap(points1x, two_points1x)

            total_overlap += overlap_area  # 累加重叠面积的总和

            print(f"Shape {i + 1} and Shape {j + 1} overlap area: {overlap_area}")
            if overlap_area > 0.5:  # 判断重叠程度，例如大于0.5则认为重合
                print("Shape", i + 1, "and Shape", j + 1, "are overlapping!")
