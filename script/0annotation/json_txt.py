import json
import os
import glob
import os.path as osp


def labelme_yolov(json_file_path="", result_dir_path="", class_list=["dusty", "defect", "damaged"]):
    """
    此函数用来将labelme软件标注好的数据集转换为yolov格式
    :param json_file_path: labelme标注好的*.json文件所在文件夹
    :param result_dir_path: 转换好后的*.txt保存文件夹
    :param class_list: 数据集中的类别标签
    :return:
    """
    # 0.创建保存转换结果的文件夹
    if not os.path.exists(result_dir_path):
        os.mkdir(result_dir_path)

    # 1.获取目录下所有的labelme标注好的Json文件，存入列表中
    jsonfile_list = glob.glob(osp.join(json_file_path, "*.json"))
    print(jsonfile_list)  # 打印文件夹下的文件名称

    # 2.遍历json文件，进行转换
    for jsonfile in jsonfile_list:
        # 3. 打开json文件
        with open(jsonfile, "r") as f:
            file_in = json.load(f)  # 将每个json文件转成字典；

            # 4. 读取文件中记录的所有标注目标
            shapes = file_in["shapes"]

            # 5. 使用图像名称创建一个txt文件，用来保存数据;    文件夹路径拼接一个/来构建绝对路径，用split "/"减去一位进行分隔（后缀），replace替换字符串（替换的是后缀名）
            with open(result_dir_path + "/" + jsonfile.split("/")[-1].replace(".json", ".txt"), "w") as file_handle:
                # 6. 遍历shapes中的每个目标的轮廓
                for shape in shapes:
                    # 7.根据json中目标的类别标签，从class_list中寻找类别的ID，然后写入txt文件中
                    # 查找shape["label"]的索引位置再转为字符串并在末尾加上一个空格区分不同元素，最后再写入file_handle(单个txt文件)
                    file_handle.writelines(str(class_list.index(shape["label"])) + " ")
                    # 8. 遍历shape轮廓中的每个点，每个点要进行图像尺寸的缩放，即x/width, y/height
                    for point in shape["points"]:
                        x = point[0] / file_in["imageWidth"]  # mask轮廓中一点的X坐标
                        y = point[1] / file_in["imageHeight"]  # mask轮廓中一点的Y坐标
                        file_handle.writelines(str(x) + " " + str(y) + " ")  # 写入mask轮廓点

                    # 9.每个物体一行数据，一个物体遍历完成后需要换行
                    file_handle.writelines("\n")
            # 10.所有物体都遍历完，需要关闭文件
            file_handle.close()
        # 10.所有物体都遍历完，需要关闭文件
        f.close()


if __name__ == "__main__":
    json_file_in = "/home/dkt/test/jx2_json"  # 要转换的json文件所在目录
    result_dir_in = "/home/dkt/test/00"  # 要生成的txt文件夹
    labelme_yolov(json_file_path=json_file_in, result_dir_path=result_dir_in,
                  class_list=["person", "bicycle", "car", "truck", "excavator", "bulldozer", "pothole", "road"])
