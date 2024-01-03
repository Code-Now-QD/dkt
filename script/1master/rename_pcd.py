# -*- coding: utf-8 -*-

import os
import shutil


def walk_path(path, ext=['pcd']):
    L = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.split('.')[-1] in ext:
                file_path = os.path.join(root, file)
                L.append(file_path)
    return L


pcd_path = '/home/heizi/car/lidar14/'
pcd_new_path = '/home/heizi/car/lidar'

pcds = walk_path(pcd_path, ext=['pcd'])
pcds = sorted(pcds, key=lambda k: float('.'.join(os.path.split(k)[-1].split('.')[:-1])))

for i, pcd in enumerate(pcds):
    shutil.copy(pcd, os.path.join(pcd_new_path, str(i).rjust(4,'0') + '.pcd'))
    
