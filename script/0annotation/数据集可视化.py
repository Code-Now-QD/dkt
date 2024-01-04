import os
"""
可优化项：把统计数量的字典也改成列表类型，让表和统计共用一个数据源；  -- 下面pie预期的类型有些特殊
"""
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
    "roadblocks": 0,        # 路障
    "tricycle": 0,          # 三轮车
    "motorcycle": 0,        # 电/摩（仅车）
    "bus": 0,               # 巴士
    "signs": 0              # 告示牌
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
    f"总标签数量：{data_key['label']}\n\t人：{data_key['person']}\n\t骑行的人:{data_key['bicyclerider']}\n\t"
    f"电/摩(仅车):{data_key['motorcycle']}\n\t三轮车:{data_key['tricycle']}\n\t巴士:{data_key['bus']}\n\t"
    f"自行车(仅车)：{data_key['bicycle']}\n\t轿车：{data_key['car']}\n\t交通告示灯:{data_key['trafficlight']}\n\t"
    f"卡车：{data_key['truck']}\n\t挖掘机：{data_key['excavator']}\n\t推土机：{data_key['bulldozer']}\n\t"
    f"坑洞：{data_key['pothole']}\n\t路面：{data_key['road']}\n\t路障:{data_key['roadblocks']}\n\t告示牌:{data_key['signs']}\n")

# 因为下面的pie方法预期类型是list，不接收字典，所以用不了上面的字典数据；
data = [
    ["人", data_key['person']],
    ["自行车(仅车)", data_key['bicycle']],
    ["轿车", data_key['car']],
    ["卡车", data_key['truck']],
    ["挖掘机", data_key['excavator']],
    ["推土机", data_key['bulldozer']],
    ["坑洞", data_key['pothole']],
    ["路面", data_key['road']],
    ["骑行的人", data_key['bicyclerider']],
    ["电/摩(仅车)", data_key['motorcycle']],
    ["交通告示灯", data_key['trafficlight']],
    ["大巴", data_key['bus']],
    ["告示牌", data_key['signs']],
    ["三轮车", data_key['tricycle']],
    ["路障", data_key['roadblocks']]
]

user_input = int(input("1生成饼状图，2生成柱状图\n"))

if user_input == 1:
    # 饼状图
    pie = Pie()
    pie.add("", data)
    # noinspection PyTypeChecker
    pie.set_global_opts(title_opts=opts.TitleOpts(title=data_key["label"]))
    pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    pie.render("/home/dkt/饼状图.html")
elif user_input == 2:
    # 柱状图
    data = list(data_key.values())  # 获取数据

    bar = Bar()
    bar.add_xaxis(["总标签", "人", "两轮车", "轿车", "卡车", "挖掘机", "推土机", "坑洞", "路面", "电/摩(仅车)", "自行车(仅车)",
                   "大巴", "告示牌", "三轮车", "交通告示灯", "路障"])
    bar.add_yaxis("labels", data)
    bar.set_global_opts(
        title_opts=TitleOpts(title="11月16日数据集类别分布情况", pos_left='center', pos_bottom='1%')
    )
    bar.render("/home/dkt/柱状图.html")
else:
    print("无效的输入，请输入1或2")
