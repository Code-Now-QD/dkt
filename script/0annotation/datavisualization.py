import os

from pyecharts.charts import Bar
from pyecharts.options import TitleOpts

# label计数器
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


class Datavisualization:
    """
    此类用于数据集可视化
    """

    def __int__(self):
        print()

    @staticmethod
    def labels():  # 给类提供一个行为
        """
        labels用于检索数据集label总量，及每个class占比，以便统计文本；
        :file_list: json文件夹的子目录列表；
        :file: 拼接起来的完整路径；
        :file_str: read读取到的str类型；
        :label_: 是统计单文件标签数量的系列变量；
        """

        global label_dict   # 声明全局变量，便于修改值(因为这个地方要给全局变量赋值，并不是单纯访问)；

        json_in: str = '/home/dkt/data/11_02/labels'  # 要统计的数据集      ***
        file_list: list[str] = os.listdir(json_in)  # 获取文件所有子目录，list类型；

        # 遍历文件列表查找标签
        for i in file_list:
            # 仅操作目标文件；
            if i.endswith('.json'):
                file: str = os.path.join(os.path.abspath(json_in), i)  # 构造绝对路径
                file_str: str = open(file).read()  # 打开完整路径的json文件并读取文件内全部字符；

                # 统计label在此数据集中的总量，以及每种class对应的总量,
                for item in label_dict.keys():
                    label_dict[item] += file_str.count(item)    # 将当前文件的标签数量加到总数label_key对应的总量

        print(
            f"总标签数量：{label_dict['label']}    人：{label_dict['person']}    两轮车：{label_dict['bicycle']}  "
            f"轿车：{label_dict['car']}   卡车：{label_dict['truck']}    挖掘机：{label_dict['excavator']} "
            f"   推土机:{label_dict['bulldozer']}  坑洞：{label_dict['pothole']}    路面：{label_dict['road']} \n")

    @staticmethod
    def visualization():
        """
        visualization用于将labels方法统计到的数据进行可视化；
        """
        # 数据集   字典的取值方法，再使用list强转类型就符合bar的预期类型了
        data: list[int] = list(label_dict.values())
        # 构建柱状图对象
        bar = Bar()
        # 添加x轴和y轴数据
        bar.add_xaxis(["总标签", "人", "两轮车", "轿车", "卡车", "挖掘机", "推土机", "坑洞", "路面", ])
        bar.add_yaxis("labels", data)
        # 全局配置项
        bar.set_global_opts(
            # 标题设置
            title_opts=TitleOpts(title="11月16日数据集分布情况", pos_left='center', pos_bottom='1%')
        )
        # 渲染成html文件
        bar.render("data.html")


if __name__ == "__main__":
    # 执行类中的两个行为
    Datavisualization.labels()
    Datavisualization.visualization()
