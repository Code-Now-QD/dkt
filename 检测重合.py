import json
import os


def calculate_overlap(x1, x2, y1, y2, two_x1, two_x2, two_y1, two_y2):
    """
    calculate_overlap计算两个矩形框的重叠面积
    :param x1: 当前矩形框的左边界x坐标
    :param x2: 当前矩形框的右边界x坐标
    :param y1: 当前矩形框的上边界y坐标
    :param y2: 当前矩形框的下边界y坐标
    :param two_x1: 对比矩形框的左边界x坐标
    :param two_x2: 对比矩形框的右边界x坐标
    :param two_y1: 对比矩形框的上边界y坐标
    :param two_y2: 对比矩形框的下边界y坐标
    :return: 返回重叠面积，以百分比形式展示
    """
    # 计算当前矩形框的中心点、宽度和高度
    cx1 = (x1 + x2) / 2
    cy1 = (y1 + y2) / 2
    width1 = x2 - x1
    height1 = y2 - y1

    # 计算对比矩形框的中心点、宽度和高度
    cx2 = (two_x1 + two_x2) / 2
    cy2 = (two_y1 + two_y2) / 2
    width2 = two_x2 - two_x1
    height2 = two_y2 - two_y1

    # 计算中心点之间的距离
    distance = ((cx1 - cx2) ** 2 + (cy1 - cy2) ** 2) ** 0.5

    # 判断是否重叠
    if distance <= (width1 / 2 + width2 / 2) and distance <= (height1 / 2 + height2 / 2):
        # 计算重叠部分的面积
        overlap_width = min(cx1, cx2) - max(cx1 - width1, cx2 - width2)
        overlap_height = min(cy1, cy2) - max(cy1 - height1, cy2 - height2)
        overlap_area = overlap_width * overlap_height

        # 以百分比形式展示重叠面积
        overlap_percentage = overlap_area / (width1 * height1) * 100 if width1 * height1 != 0 else 0
        return overlap_percentage
    else:
        return 0  # 如果不重叠，返回0


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

            # 传入当前形状和下个形状的坐标点，并返回给overlap_area
            overlap_area: float = calculate_overlap(points1x, points2x, points1y, points2y, two_points1x, two_points2x, two_points1y, two_points2y)

            total_overlap += overlap_area  # 累加重叠面积的总和
            if overlap_area > 0.5:  # 判断重叠程度，例如大于0.5则认为重合
                print(f'{item}：  形状 {i + 1} 和 {j + 1} 的重叠程度为: {overlap_area:.0f}%')
