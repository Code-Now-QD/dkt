# -*- coding: utf-8 -*-
import os

path1 = '/home/dkt/test/train_images'
path2 = '/home/dkt/test/train_json'


def keep_one(image_dir, json_dir):
    """
    keep_one:用于比较两个目录中的文件，并删除那些在其中一个目录存在，但在另一个目录不存在的文件；
    一般应用场景：  同步images和json目录中的文件数量
    :diff: 用来
    """
    jpg_list = os.listdir(image_dir)
    json_list = os.listdir(json_dir)
    print("images的数量", len(jpg_list))
    print("json的数量", len(json_list))
    for i in range(len(jpg_list)):
        jpg_list[i] = jpg_list[i].split(".")[0]  # 只保留文件名，split分隔开，0：第一个索引，去掉扩展名；
    for i in range(len(json_list)):
        json_list[i] = json_list[i].split(".")[0]
    diff = set(json_list).difference(set(jpg_list))  # 差集，在a(json)中但不在b(jpg)中的元素
    print("差集数量-在json不在jpg:", len(diff))
    for name in diff:
        print("no json", name + ".json")
        name = name + ".json"
        json_file = os.path.join(path2, name)
        os.remove(json_file)
        print(f"Deleted json file: {json_file}")
    diff2 = set(jpg_list).difference(set(json_list))  # 差集，在b中但不在a中的元素
    print("差集数量-在json不在jpg:", len(diff2))
    for name in diff2:
        picture_list = [".jpg", ".jpeg", ".png", ".gif"]
        a = 0
        while a < 4:
            name = name + picture_list[a]
            jpg_file = os.path.join(path1, name)
            if os.path.exists(jpg_file):
                os.remove(jpg_file)
                print("no json", name + picture_list[a])
                print(f"Deleted jpg file: {jpg_file}")
            a = a + 1
            name = name.split(".")[0]


if __name__ == '__main__':
    keep_one(path1, path2)
