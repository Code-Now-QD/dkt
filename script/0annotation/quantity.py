import os


def labels():
    """
    labels用于检索数据集label总量，及每个class占比，以便统计文本；
    :file_list: json文件夹的子目录列表；
    :file: 拼接起来的完整路径；
    :file_str: read读取到的str类型；
    :label_: 是统计单文件标签数量的系列变量；
    :count_: 是统计整个数据集的系列变量；
    """

    json_in: str = '/home/dkt/ultralytics/data/1204-1220_new_2d/json备份/json'  # 要统计的数据集      ***
    file_list: list[str] = os.listdir(json_in)  # 获取文件所有子目录，list类型；
    # label计数器
    count_label = 0
    count_person = 0
    count_bicycle = 0
    count_car = 0
    count_truck = 0
    count_excavator = 0
    count_bulldozer = 0
    count_pothole = 0
    count_road = 0

    # 遍历文件查找标签
    for i in file_list:
        # 仅操作目标文件；
        if i.endswith('.json'):
            file: str = os.path.join(os.path.abspath(json_in), i)  # 构造绝对路径
            file_str: str = open(file).read()  # 读取json文件的全部内容；

            # 统计label在单文件中的数量，以及每种class对应的数量
            label_count: int = file_str.count("label")
            label_person = file_str.count("person")
            label_bicycle: int = file_str.count("bicycle")
            label_car: int = file_str.count("car")
            label_truck = file_str.count("truck")
            label_excavator = file_str.count("excavator")
            label_bulldozer = file_str.count("bulldozer")
            label_pothole: int = file_str.count("pothole")
            label_road = file_str.count("road")

            # 统计label在此数据集中的总量，以及每种class对应的总量
            label_sum = file_str.count("label")
            count_label += label_sum  # 将当前文件的标签数量加到总数s对应的总量

            person_sum = file_str.count("person")
            count_person += person_sum

            bicycle_sum = file_str.count("bicycle")
            count_bicycle += bicycle_sum

            car_sum = file_str.count("car")
            count_car += car_sum

            truck_sum = file_str.count("truck")
            count_truck += truck_sum

            excavator_sum = file_str.count("excavator")
            count_excavator += excavator_sum

            bulldozer_sum = file_str.count("bulldozer")
            count_bulldozer += bulldozer_sum

            pothole_sum = file_str.count("pothole")
            count_pothole += pothole_sum

            road_sum = file_str.count("road")
            count_road += road_sum

            print(
                f"{i}标签数量分布如下:\n标签：{label_count}   人：{label_person}    两轮车：{label_bicycle}   桥车：{label_car}   "
                f"卡车：{label_truck}    挖掘机：{label_excavator}    推土机:{label_bulldozer}   "
                f" 坑洞：{label_pothole}    路面：{label_road} \n")

    print(f"总标签数量：{count_label}     人：{count_person}    两轮车：{count_bicycle}   桥车：{count_car}   "
          f"卡车：{count_truck}    挖掘机：{count_excavator}    推土机:{count_bulldozer}   "
          f" 坑洞：{count_pothole}    路面：{count_road} \n")
    return (count_label, count_person, count_bicycle, count_car, count_truck,
            count_excavator, count_bulldozer, count_pothole, count_road)


if __name__ == "__main__":
    labels()
