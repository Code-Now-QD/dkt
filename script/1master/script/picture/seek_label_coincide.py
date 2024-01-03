import os
import json

folder_path = "925_type3/925_type3_coco/labels"  # 指定文件夹路径
size = 5


# 遍历文件夹中的所有文件
for file_name in os.listdir(folder_path):
    if file_name.endswith('.json'):  # 确保文件是JSON文件
        json_file_path = os.path.join(folder_path, file_name)

        #读取json文件
        with open(json_file_path, 'r') as file:
            label_data = json.load(file)
        u=0
        mus=len(label_data['shapes'])
        for i in range(mus): #判断"shapes"字段的长度,然后用下标引出各个"label"字段
            for j in range (i+1,mus):
                k_0=label_data["shapes"][i]["points"][0][0]-label_data["shapes"][j]["points"][0][0]
                k_1=label_data["shapes"][i]["points"][0][1]-label_data["shapes"][j]["points"][0][1]
                k_2=label_data["shapes"][i]["points"][1][0]-label_data["shapes"][j]["points"][1][0]
                k_3=label_data["shapes"][i]["points"][1][1]-label_data["shapes"][j]["points"][1][1]
                zhi=(abs(k_0)+abs(k_1)+abs(k_2)+abs(k_3))/4
                if(zhi> size-(2*size) and zhi<size):
                    u=1
                    print("",file_name)


#更改一个文件夹内所有json文件的标签值/////////////
