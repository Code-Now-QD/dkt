import os
from typing import List
from pyecharts import options as opts
from pyecharts.charts import Bar, Pie
from pyecharts.options import TitleOpts

# 用于累计
data_key: dict[str, int] = {
    "label": 0,
    "person": 0,
    "bicycle": 0,
    "car": 0,
    "truck": 0,
    "excavator": 0,         # 挖掘机
    "bulldozer": 0,         # 推土机
    "pothole": 0,           # 坑洞
    "road": 0,              # 路面
    "bicyclerider": 0,      # 骑行的人
    "trafficlight": 0,      # 交通告示灯
    }

json_in: str = "/home/dkt/ultralytics/data/1204-1220_new_2d/labels"  # 要统计的数据集      ***
file_list: list[str] = os.listdir(json_in)
for i in file_list:
    if i.endswith('.json'):
        file: str = os.path.join(os.path.abspath(json_in), i)
        file_str: str = open(file).read()

        for keyword in data_key.keys():
            data_key[keyword] += file_str.count(keyword)

print(
    f"总标签数量：{data_key['label']}     人：{data_key['person']}  骑行的人:{data_key['bicyclerider']}    "
    f"两轮自行车：{data_key['bicycle']}   轿车：{data_key['car']}   交通告示灯:{data_key['trafficlight']}"
    f"卡车：{data_key['truck']}    挖掘机：{data_key['excavator']}    推土机：{data_key['bulldozer']}   "
    f" 坑洞：{data_key['pothole']}    路面：{data_key['road']} \n")

# 因为下面的pie方法预期类型是list，不接收字典，所以用不了上面的字典数据；
data = [
    ["人", data_key['person']],
    ["两轮车", data_key['bicycle']],
    ["轿车", data_key['car']],
    ["卡车", data_key['truck']],
    ["挖掘机", data_key['excavator']],
    ["推土机", data_key['bulldozer']],
    ["坑洞", data_key['pothole']],
    ["路面", data_key['road']],
    ["骑行的人", data_key['bicyclerider']],
    ["交通告示灯", data_key['trafficlight']]
]

user_input = int(input("1生成饼状图，2生成柱状图\n"))

if user_input == 1:
    # 饼状图
    pie = Pie()
    pie.add("", data)
    # noinspection PyTypeChecker
    pie.set_global_opts(title_opts=opts.TitleOpts(title=data_key["label"]))
    print(type(data_key["label"]))
    print(data_key["label"])
    pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    pie.render("/home/dkt/饼状图.html")
elif user_input == 2:
    # 柱状图
    data = list(data_key.values())  # 获取数据

    bar = Bar()
    bar.add_xaxis(["总标签", "人", "两轮车", "轿车", "卡车", "挖掘机", "推土机", "坑洞", "路面"])
    bar.add_yaxis("labels", data)
    bar.set_global_opts(
        title_opts=TitleOpts(title="11月16日数据集类别分布情况", pos_left='center', pos_bottom='1%')
    )
    bar.render("/home/dkt/柱状图.html")
else:
    print("无效的输入，请输入1或2")
