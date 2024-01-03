import numpy as np  
import cv2  
from sklearn.model_selection import train_test_split  
from sklearn.image import RandomRotation, RandomCrop, RandomTranslation
  
# 加载图像数据  
images = []  
labels = []  
for image_path in image_paths:  
    image = cv2.imread(image_path)  
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  
    images.append(image)  
    labels.append(image_label)
  
# 将图像数据转换为numpy数组  
X = np.array(images)  
y = np.array(labels)  
  
# 划分训练集和测试集  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  
  
# 定义数据增强器  
enhancer = RandomRotation(rotation_range=15, interpolation=cv2.INTER_CUBIC)  
enhancer.fit(X_train)  
  
# 对训练集进行数据增强  
X_train_enhanced = enhancer.transform(X_train)  
  
# 对测试集进行数据增强  
X_test_enhanced = enhancer.transform(X_test)
