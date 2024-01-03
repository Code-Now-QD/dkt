import os
import shutil


def walk_path(path, ext=['jpg']):
    L = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.split('.')[-1] in ext:
                file_path = os.path.join(root, file)
                L.append(file_path)
    return L


#pcd_path = '/home/gy/Documents/maps/pcd2/'
#pcd_new_path = '/home/gy/Documents/pcdnew/'
image_path = '/home/heizi/pedestrian/camera/right14/'
image_new_path = '/home/heizi/pedestrian/camera/right'
#pcds = walk_path(pcd_path, ext=['pcd'])
#pcds = sorted(pcds, key=lambda k: float('.'.join(os.path.split(k)[-1].split('.')[:-1])))
images = walk_path(image_path, ext=['jpg'])
images = sorted(images, key=lambda k: float('.'.join(os.path.split(k)[-1].split('.')[:-1])))
#for i, pcd in enumerate(pcds):
#    shutil.copy(pcd, os.path.join(pcd_new_path, str(i).rjust(8,'0') + '.pcd'))

for j, image in enumerate(images):
    shutil.copy(image, os.path.join(image_new_path, str(j).rjust(4,'0') + '.jpg'))
