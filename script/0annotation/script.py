import os
import re
import cv2
import json
import glob
import shutil
import os.path as osp
from PIL import Image
from tqdm import tqdm
from pyecharts.charts import Bar, Pie
from pyecharts.options import TitleOpts
from pyecharts import options as opts


class Script:
    def __int__(self):
        return

    @staticmethod
    def labelme_yolov():
        """
        此函数用来将labelme软件标注好的数据集转换为yolov5_7.0s ege中使用的数据集
        json_file_path: labelme标注好的*.json文件所在文件夹
        param result_dir_path: 转换好后的*.txt保存文件夹
        param class_list: 数据集中的类别标签
        :return:
        """
        json_file_path = input("要转换的json文件所在目录:")  # 要转换的json文件所在目录
        result_dir_path = input("要生成的txt文件夹:")  # 要生成的txt文件夹
        class_list = ["person", "bicycle", "car", "truck", "excavator", "bulldozer", "pothole", "road"]

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

    @staticmethod
    def delete_json_files_between():
        """
        delete_json_files_between函数用于删除指定序号内的文件
        """
        # 指定要删除文件的文件夹路径、起始序号和结束序号
        folder_path = input("要删除文件的绝对路径：")
        json_extensions = list(input("需要操作的文件类型:"))  # 创建一个需要操作类型的列表
        start_index = int(input("请输入要删除的开始序号int："))
        end_index = int(input("请输入要删除的结束序号int："))

        for root, dirs, files in os.walk(folder_path):  # walk方法固定返回三个元组
            for file in files:
                # 检查文件是否为JSON文件  any函数接收一个迭代器   -- 过滤条件
                # ext从列表中取出后缀名，lower方法将文件转为小写，endswith检查文件是不是指定后缀，
                # 最后所有的方法调用结果组成一个生成器(提供了一个迭代器)，作为any函数的输入，并输出bool型
                if any(file.lower().endswith(ext) for ext in json_extensions):  # 禁止套娃
                    # 使用正则表达式从文件名中提取序号，扫描整个字符串，并返回第一个符合的字符串
                    match = re.search(r'\d+', file)  # '\d+' 扫描整个file(目录下文件)
                    if match:
                        index = int(match.group())
                        # 检查序号是否在指定范围内
                        if start_index <= index <= end_index:
                            # 构建JSON文件路径
                            json_file = os.path.join(root, file)
                            # 删除JSON文件
                            os.remove(json_file)
                            print(f"Deleted JSON file: {json_file}")  # 提示删除了那些

    @staticmethod
    def extract_picture():
        """
        extract_picture函数用于随机抽帧
        """
        # 设置输入和输出文件夹路径
        input_dir = input("要抽帧的文件夹：")
        output_dir = input("希望抽帧的输出路径：")
        n = int(input("请输入抽帧的规则(每隔N帧抽取一帧)int："))

        # 创建输出文件夹
        os.makedirs(output_dir, exist_ok=True)

        # 获取所有输入文件夹中的图像文件名
        input_files = os.listdir(input_dir)
        input_files.sort()  # 按名称顺序排序

        # 设置进度条
        pbar = tqdm(total=len(input_files), desc='Processing images')

        # 遍历每个输入文件，每隔N张抽取一张并保存到输出文件夹
        for i, file in enumerate(input_files):
            if (i + 1) % n == 0:  # 每隔N张抽取一张
                input_path = os.path.join(input_dir, file)
                output_path = os.path.join(output_dir, file)
                shutil.copy(input_path, output_path)
                pbar.update(1)  # 更新进度条

        # 关闭进度条
        pbar.close()

    @staticmethod
    def fixed_zoom():
        # 设置输入和输出文件夹路径
        img_dir = input("输入图片路径:")
        output_dir = input("输出图片路径:")

        # 创建输出文件夹
        os.makedirs(output_dir, exist_ok=True)

        # 获取所有输入文件夹中的图像文件名
        input_files = os.listdir(img_dir)

        # 设置进度条
        pbar = tqdm(total=len(input_files), desc='Resizing images')

        def resize_by_width(image, new_width=50):
            """
            按照宽度缩放图像，并保持宽高比不变
            """
            h, w, _ = image.shape
            scale = new_width / w
            new_h = int(h * scale)
            image_resized = cv2.resize(image, (new_width, new_h))
            return image_resized

        # 缩放并保存结果
        for file in input_files:
            # 读取图像
            img_path = os.path.join(img_dir, file)
            img = cv2.imread(img_path)

            # 缩放并保存结果
            img_resized = resize_by_width(img)
            # 设置输出文件路径和文件名
            output_path = os.path.join(output_dir, file)
            # 保存图像并更新进度条
            cv2.imwrite(output_path, img_resized)
            pbar.update(1)

        # 关闭进度条
        pbar.close()
        print(f"缩放后的图片已放入:{output_dir}")

    @staticmethod
    def imagedata():
        """
        imageData函数用于去除图片信息,便于数据增强，转换yolov格式；
        """
        json_in = input("需要去除图片信息的json文件路径:")  # 获取原始文件
        json_out = input("去除信息后的路径(可放原目录，会覆盖)：")  # 保险起见，输出到新目录

        file_list = os.listdir(json_in)  # 转为列表
        # 遍历文件查找标签
        for i in file_list:
            # 仅操作目标文件；
            if i.endswith('.json'):
                file = os.path.join(os.path.abspath(json_in), i)  # 需要绝对路径才能知道文件内容，单文件名不够
                # 获取键  -- 需要先读取到文件的内容，既然是键 值类型，那就要转成字典；
                file_str = open(file).read()  # 读取到的是字符串
                file_dict = json.loads(file_str)
                # 将图片信息设置为null
                file_dict['imageData'] = None
                # 下面这条会将被更改的地方会变成"str"类型加"";
                # file_dict['不在字典嵌套'] = "更改"
                # 保存更新至新变量(变量内容是新地址)；
                out = os.path.join(json_out, i)

                # 保存上述更新至设定好的文件夹
                with open(out, 'w') as f:
                    json.dump(file_dict, f, indent=2)
                    print(out)

    @staticmethod
    def keep_one():
        image_dir = input("images目录：")
        json_dir = input("json目录：")
        jpg_list = os.listdir(image_dir)
        json_list = os.listdir(json_dir)
        print("images的数量", len(jpg_list))
        print("json的数量", len(json_list))
        for i in range(len(jpg_list)):
            jpg_list[i] = jpg_list[i].split(".")[0]  # 只保留文件名，split去掉扩展名
        for i in range(len(json_list)):
            json_list[i] = json_list[i].split(".")[0]
        diff = set(json_list).difference(set(jpg_list))  # 差集，在a中但不在b中的元素
        print("差集数量-在json不在jpg:", len(diff))
        for name in diff:
            print("no json", name + ".json")
            name = name + ".json"
            json_file = os.path.join(json_dir, name)
            os.remove(json_file)
            print(f"Deleted json file: {json_file}")
        diff2 = set(jpg_list).difference(set(json_list))  # 差集，在b中但不在a中的元素
        print("差集数量-在json不在jpg:", len(diff2), "\n")
        for name in diff2:
            picture_list = [".jpg", ".jpeg", ".png", ".gif"]
            a = 0
            while a < 4:
                name = name + picture_list[a]
                jpg_file = os.path.join(image_dir, name)
                if os.path.exists(jpg_file):
                    os.remove(jpg_file)
                    print("no json", name + picture_list[a])
                    print(f"Deleted jpg file: {jpg_file}")
                a = a + 1
                name = name.split(".")[0]

    @staticmethod
    def label_update():  # 函数接收两个位置形参
        """
        label_update: 此函数用于更新label标签的值；
        :filelist: 是json的子目录列表；
        :src: 子目录的完整路径；
        :j,jj: j为单个目录的完整字符串内容，jj为单个目录全部的字典内容；
        """
        json_in = input("输入json路径：")
        label = input("将标签更改为：")
        json_out = input("更改后输出json路径(可原目录，会覆盖):")
        filelist = os.listdir(json_in)  # 获取文件路径,转化为一个列表
        for item in filelist:  # 遍历转为列表的文件；
            if item.endswith('.json'):  # 检查文件的后缀（选择自己需要的操作的后缀）
                # 把里面两个路径拼接成一个赋值给src
                src = os.path.join(os.path.abspath(json_in), item)
                print(type('src'))
                j = open(src).read()  # json文件的内容读入成字符串格式
                jj = json.loads(j)  # 载入字符串，json格式转python格式
                # len用来返回键shapes对应值的数量，然后循环更新
                for i in range(len(jj['shapes'])):
                    # 将json文件中键shapes的第i个shape_type的值更新为''
                    jj["shapes"][i]["label"] = label  # 把所有label的值都改成‘xxx’  *****

                    print(jj["shapes"][i]["label"])  # 测试是否符合条件执行到这里，输出一下结果；

                # 这里实现的是把上面改动的结果保存到自定义目录中；
                # 构造绝对路径
                out = os.path.join(os.path.abspath(json_out), item)
                # 文件管理器，写入模式，文件已存在则覆盖；
                with open(out, 'w') as f:
                    json.dump(jj, f, indent=2)  # 缩进保存json文件

    @staticmethod
    def prefix_name():
        # 设置图片目录路径和新命名的起始数字
        img_folder: str = input("需要修改的图片路径：")
        name: str = input("输入想要的前缀:")   # 文件前缀名
        start_num: int = int(input("图片起始序号"))

        # 遍历图片目录中的所有文件，加入进度条
        file_list = sorted(os.listdir(img_folder))

        # 第一步：检查并转换S_RGB图像为RGB，并删除S_RGB图像
        for img_file in tqdm(file_list):
            img_path = os.path.join(img_folder, img_file)

            try:
                img = Image.open(img_path)
                if img.mode == "RGB":
                    continue
                elif img.mode == "RGBA":
                    img = img.convert("RGB")
                else:
                    print(f"Converting S_RGB image {img_file} to RGB.")
                    img = img.convert("RGB")
                    os.remove(img_path)  # 删除原始的S_RGB图像文件
            except (OSError, IOError):
                print(f"Unable to open {img_file}. Skipping...")
                continue

        # 第二步：检查并转换图像格式为JPEG，并删除其他格式的图像
        for img_file in tqdm(file_list):
            img_path = os.path.join(img_folder, img_file)

            try:
                img = Image.open(img_path)
                if img.format == "JPEG":
                    continue
                else:
                    print(f"Converting {img_file} to JPEG.")
                    new_file_name = os.path.splitext(img_file)[0] + ".jpg"
                    new_path = os.path.join(img_folder, new_file_name)
                    img.save(new_path, "JPEG")  # 转换图像格式为JPEG
                    os.remove(img_path)  # 删除原始的非JPEG图像文件
            except (OSError, IOError):
                print(f"Unable to process {img_file}. Skipping...")
                continue

        # 第三步：顺序重命名图像文件
        for i, img_file in tqdm(enumerate(sorted(os.listdir(img_folder)))):
            img_path = os.path.join(img_folder, img_file)
            new_file_name = "{:05d}.jpg".format(i + start_num)
            new_path = os.path.join(img_folder, new_file_name)
            os.rename(img_path, new_path)

        # 第四步：在重命名后的文件名中添加关键字add_
        for img_file in tqdm(os.listdir(img_folder)):
            img_path = os.path.join(img_folder, img_file)
            new_file_name = f"{name}{img_file}"
            new_path = os.path.join(img_folder, new_file_name)
            os.rename(img_path, new_path)

            # 输出已重命名的图像文件名和新文件名
            print(f"Renamed {img_file} to {new_file_name}")

    @staticmethod
    def visualization():
        """
         visualization用于将labels方法统计到的数据进行可视化；
        :file_list: json文件夹的子目录列表；
        :file: 拼接起来的完整路径；
        :file_str: read读取到的str类型；
        :label_: 是统计单文件标签数量的系列变量；
        """

        # label计数器，统计数量
        label_dict: dict[str, int] = {
            "label": 0,
            "person": 0,
            "bicycle": 0,
            "car": 0,
            "truck": 0,
            "excavator": 0,
            "bulldozer": 0,
            "pothole": 0,
            "road": 0
        }

        json_in: str = input("要进行可视化的数据集(json)：")  # 要统计的数据集      ***
        file_list: list[str] = os.listdir(json_in)  # 获取文件所有子目录，list类型；

        # 遍历文件列表查找标签
        for i in file_list:
            # 仅操作目标文件；
            if i.endswith('.json'):
                file: str = os.path.join(os.path.abspath(json_in), i)  # 构造绝对路径
                file_str: str = open(file).read()  # 打开完整路径的json文件并读取文件内全部字符；

                # 统计label在此数据集中的总量，以及每种class对应的总量,
                for item in label_dict.keys():
                    label_dict[item] += file_str.count(item)  # 将当前文件的标签数量加到总数label_key对应的总量

        print(
            f"总标签数量：{label_dict['label']}    人：{label_dict['person']}    两轮车：{label_dict['bicycle']}  "
            f"轿车：{label_dict['car']}   卡车：{label_dict['truck']}    挖掘机：{label_dict['excavator']} "
            f"   推土机:{label_dict['bulldozer']}  坑洞：{label_dict['pothole']}    路面：{label_dict['road']} \n")

        # 数据集   字典的取值方法，再使用list强转类型就符合bar的预期类型了
        user_in = int(input("1生成饼状图，2生成柱状图\n"))
        data = [
            ["人", label_dict['person']],
            ["两轮车", label_dict['bicycle']],
            ["轿车", label_dict['car']],
            ["卡车", label_dict['truck']],
            ["挖掘机", label_dict['excavator']],
            ["推土机", label_dict['bulldozer']],
            ["坑洞", label_dict['pothole']],
            ["路面", label_dict['road']]
        ]
        if user_in == 1:
            # 饼状图
            pie = Pie()
            pie.add("label", data)
            pie.set_global_opts(title_opts=opts.TitleOpts(title=str(label_dict["label"])))
            pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
            html = input("起名(绝对路径+name，直接name则生成在脚本同目录):")
            pie.render(html)    # 生成html文件
        elif user_in == 2:
            # 柱状图
            data = list(label_dict.values())  # 获取数据

            bar = Bar()
            bar.add_xaxis(["总标签", "人", "两轮车", "轿车", "卡车", "挖掘机", "推土机", "坑洞", "路面"])
            bar.add_yaxis("labels", data)
            bar.set_global_opts(
                title_opts=TitleOpts(title="X月X日数据集类别分布情况", pos_left='center', pos_bottom='1%')
            )
            html = input("起名(绝对路径+name，直接name则生成在脚本同目录):")
            # render只能生成文件，并不能操作文件夹(即要么生成文件，要么with给w在文件夹下生成文件)
            bar.render(html)   # 用户输入的绝对路径加上拼接的str构成文件的绝对路径
        else:
            print("无效的输入，请输入1或2")

    @staticmethod
    def image_path():
        folder_path = input("需要修改的图片路径的json文件")   # 需要修改的图片路径的json文件
        print("图片位置默认是上级的\"../images\" 有需要可源码修改")
        image_folder = "../images"  # 图片文件夹路径

        # 遍历文件夹中的所有文件
        for file_name in os.listdir(folder_path):
            if file_name.endswith('.json'):  # 确保文件是JSON文件
                json_file_path = os.path.join(folder_path, file_name)  # 构造json文件绝对路径
                image_name = os.path.splitext(file_name)[0] + '.jpg'  # 根据JSON文件名生成对应的图片路径,索引上第一个参数文件名，并且加上手动加上后缀，这样好处是无论什么格式的文件最终都是jpg。方法自动的是原后缀
                image_path: str = os.path.join(image_folder, image_name)  # 构建图片路径的完整路径

                with open(json_file_path, 'r') as file:  # 读模式访问文件
                    label_data: object = json.load(file)  # 获取内容转字典

                # 修改 "imagePath" 字段的值
                label_data['imagePath'] = image_path

                with open(json_file_path, 'w') as file:
                    json.dump(label_data, file, indent=4)

    @staticmethod
    def new_name():
        file_in = input("文件传入地址：")  # 需要重命名的文件
        prefix = input("需要的前缀（可空）：")  # 想要重命名的前缀
        start_num = int(input("开始序号:"))  # 文件起始序号
        file_list = sorted(os.listdir(file_in))  # 用于对列表进行排序
        print("检查后缀，可源码改文件类型（json）")
        for i in tqdm(file_list):
            if i.endswith(".json"):
                a, file_ext = os.path.splitext(i)  # 取文件扩展名
                newname: str = f"{prefix}{start_num}"
                start_num += 1
                old_filepath = os.path.join(file_in, i)
                new_filepath = os.path.join(file_in, newname + file_ext)
                os.rename(old_filepath, new_filepath)
                print(f"Renamed {old_filepath} to {new_filepath}")


if __name__ == '__main__':
    # 命令选项字典
    my_dict = {
        1: Script.imagedata,
        2: Script.visualization,
        3: Script.extract_picture,
        4: Script.fixed_zoom,
        5: Script.labelme_yolov,
        6: Script.keep_one,
        7: Script.label_update,
        8: Script.prefix_name,
        9: Script.delete_json_files_between,
        10: Script.image_path,
        11: Script.new_name
    }

    while True:
        user_input = input("请输入需要的功能（输入exit退出）：\n\n"
                           "[1]  去除json文件中labelme保存的图片信息\n\n"
                           "[2]  数据集可视化\n\n"
                           "[3]  随机抽帧\n\n"
                           "[4]  数据增强(按照宽度缩放图像，并保持宽高比不变)\n\n"
                           "[5]  json格式转txt格式\n\n"
                           "[6]  同步images和json目录中的文件数量\n\n"
                           "[7]  更新label标签值\n\n"
                           "[8]  指定前缀并按顺序重命名图片文件\n\n"
                           "[9]  删除文件指定的起始序号和结束序号内的范围\n\n"
                           "[10] 更改图片路径 (根据json文件名)，以便json正确访问图片的位置\n\n"
                           "[11] 可选前缀按顺序重命名文件\n\n")

        if user_input.lower() == 'exit':  # 用户输入'exit'时，转换为小写后比较
            print('程序已退出。')
            break
        elif user_input.isdigit():  # 检查输入是否为数字
            function = my_dict.get(int(user_input))  # 如果是数字，则将其转换为整数并从my_dict中获取对应的函数
            if function:
                function()
            else:
                print('无效的输入，请重新输入。\n')
        else:
            print('无效的输入，请重新输入。\n')  # 既不是exit也不是数字的情况
