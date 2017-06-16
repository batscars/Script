import sys
import os
import json

annotations = json.load(open('D:\\Alg\\PedestrainRecog\\Data\\Caltech\\annotations\\annotations.json'))
root = sys.argv[1]
res = open(sys.argv[2], 'w')

for parent, dirs, files in os.walk(root):
    if len(files) > 0:
        for f in files:
            if '.png' in f:
                img_path = os.path.join(parent, f)
                print(img_path)
                tmp = f.split('.')[0].split('_')
                set_name = tmp[0]
                video_name = tmp[1]
                frame_num = tmp[2]
                if str(frame_num) in annotations[set_name][video_name]['frames']:
                    data = annotations[set_name][video_name]['frames'][str(frame_num)]
                    for datum in data:
                        x, y, w, h = [int(v) for v in datum['pos']]
                        res.write(img_path + ' ' + str(x) + ' ' + str(y) + ' ' + str(w) + ' ' + str(h) + '\n')
