import os, argparse

#  创建一个解析器对象
parser = argparse.ArgumentParser()
# 添加参数
parser.add_argument("-p", "--path", help="dir path of imamges")
# 解析参数
args = parser.parse_args()
# 获取数据
json_names = list(filter(lambda x: '.json' in x, os.listdir(args.path)))
os.chdir(args.path)
if not os.path.exists('../labels'):
    os.mkdir('../labels')

for n in json_names:
    os.system('labelme_json_to_dataset {} -o ../labels/{}'.format(n, os.path.splitext(n)[0]))
