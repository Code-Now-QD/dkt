# 导入 os 模块，该模块提供了与操作系统交互的功能  
import os  
  
# 提示用户输入文件路径，并将用户输入的路径存储在变量 path 中  
path = input("请输入包含需要重命名文件的完整路径: ")  
  
# 使用 os.path.exists 函数检查用户输入的路径是否存在，如果存在则执行花括号中的代码块  
# os.path.exists(path) 函数返回 True 或 False，表示路径是否存在  
if os.path.exists(path):  
    # 获取指定路径下的所有文件名，并将它们存储在变量 files 中  
    # os.listdir(path) 函数返回指定路径下的所有文件名列表  
    files = os.listdir(path)  
      
    # 使用 enumerate 函数遍历 files 中的每个文件，为每个文件提供一个索引，并将文件的名称存储在变量 file 中  
    # enumerate(files) 函数返回一个枚举对象，它生成一个索引和值的元组，用于遍历列表中的每个元素  
    for index, file in enumerate(files):  
        # 将文件名和后缀名分开，并分别存储在变量 filename 和 ext 中  
        # os.path.splitext(file) 函数将文件名和后缀名分开，并返回一个包含文件名和后缀名的元组  
        filename, ext = os.path.splitext(file)  
          
        # 构建新的文件名，由当前索引加上原始文件名和原始后缀名组成  
        # 使用 f-string 格式化字符串，将索引、原始文件名和原始后缀名组合成新的文件名  
        new_name = f"{index + 1}{ext}"  
          
        # 将旧文件的完整路径和新文件的完整路径分别存储在变量 old_file_path 和 new_file_path 中  
        # os.path.join(path, file) 函数将路径和文件名组合成一个完整的文件路径  
        old_file_path = os.path.join(path, file)  
        new_file_path = os.path.join(path, new_name)  
          
        # 将旧文件重命名为新文件名  
        # os.rename(old_file_path, new_file_path) 函数将旧文件重命名为新文件名  
else:  
    # 如果用户输入的路径不存在，则输出“路径不存在”  
    print("路径不存在。")
