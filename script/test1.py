class Restaurant:
    # 构造函数
    def __init__(self, name, type):
        self.res1_name = name
        self.cuisine_type = type

    def describe_res1(self):
        print("The name of the res1 is "
              + self.res1_name.title() + ".")
        print("The cuisine type of the res1 is "
              + self.cuisine_type.title() + ".")

    def open_res1(self):
        print(self.res1_name.title()
              + " is open now.")
