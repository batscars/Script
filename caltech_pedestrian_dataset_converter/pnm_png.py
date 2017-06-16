from PIL import Image
import os
import sys

in_path = sys.argv[1]
out_path = sys.argv[2]
if not os.path.exists(out_path):
    os.makedirs(out_path)

for parent, dirs, files in os.walk(in_path):
    if len(files) > 0:
        temp = parent.split('\\')
        dir = temp[len(temp) - 2] + '\\' + temp[len(temp) - 1]
        dir = os.path.join(out_path, dir)
        if not os.path.exists(dir):
            os.makedirs(dir)
        for file_ in files:
            if '.pnm' in file_:
                read_path = os.path.join(parent, file_)
                image_name = file_.split('.')[0] + '.png'
                write_path = os.path.join(dir, image_name)
                print(read_path)
                img = Image.open(read_path).save(write_path)

