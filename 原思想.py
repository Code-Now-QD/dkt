def calculate_overlap(rect1, rect2):
    # 获取两个矩形的顶点坐标
    p1, q1, p2, q2 = rect1  # 这里假设每个点有x和y两个坐标值
    r1, s1, r2, s2 = rect2  # 这里假设每个点有x和y两个坐标值

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


data = {
  "version": "1.0.0",
  "flags": {},
  "shapes": [
    {
      "label": "car",
      "text": "",
      "points": [
        [
          877.0,
          677.0
        ],
        [
          918.0,
          716.0
        ]
      ],
      "group_id": None,
      "shape_type": "rectangle",
      "flags": None
    },
    {
      "label": "car",
      "text": "",
      "points": [
        [
          1387.0,
          613.0
        ],
        [
          1806.0,
          933.0
        ]
      ],
      "group_id": None,
      "shape_type": "rectangle",
      "flags": None
    }
  ],
  "imagePath": "../images/1204_images_254.jpg",
  "imageData": None,
  "imageHeight": 1080,
  "imageWidth": 1920
}

shapes = data["shapes"]  # 获取所有形状的列表
total_overlap = 0  # 用于累计重叠面积的总和

# 遍历每个形状，与其他形状进行重叠面积计算
for i in range(len(shapes)):
    shape1 = shapes[i]
    for j in range(i + 1, len(shapes)):  # 避免重复计算同一个形状对之间的重叠面积
        shape2 = shapes[j]
        overlap_area = calculate_overlap(shape1["points"], shape2["points"])
        total_overlap += overlap_area  # 累加重叠面积的总和
        print(f"Shape {i + 1} and Shape {j + 1} overlap area: {overlap_area}")
        if overlap_area > 0.5:  # 判断重叠程度，例如大于0.5则认为重合
            print("Shape", i + 1, "and Shape", j + 1, "are overlapping!")