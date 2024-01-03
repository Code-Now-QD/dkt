# -*- coding: utf-8 -*-

import os
import shutil


def walk_path(path, ext=['json']):
    L = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.split('.')[-1] in ext:
                file_path = os.path.join(root, file)
                L.append(file_path)
    return L


label_path = '/home/heizi/1000z/car/label1/'
label_new_path = '/home/heizi/1000z/car/label'

labels = walk_path(label_path, ext=['json'])
labels = sorted(labels, key=lambda k: float('.'.join(os.path.split(k)[-1].split('.')[:-1])))

for j, label in enumerate(labels):
    shutil.copy(label, os.path.join(label_new_path, str(j).rjust(4,'0') + '.json'))
