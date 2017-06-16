import os
import sys


def open_save(seq_file, save_root):
    f = open(seq_file, 'rb')
    string = str(f.read())
    split_string = "\xFF\xD8\xFF\xE0\x00\x10\x4A\x46\x49\x46"
    str_lst = string.split(split_string)
    f.close()
    count = 0
    if not os.path.exists(save_root):
        os.makedirs(save_root)
    for img in str_lst:
        filename = str(count) + '.png'
        save_path = os.path.join(save_root, filename)
        if count > 0:
            i = open(save_path, 'wb+')
            i.write(split_string)
            i.write(img)
            i.close()
        count += 1

in_dir = sys.argv[1]
out_dir = sys.argv[2]
if not os.path.exists(out_dir):
    os.makedirs(out_dir)
seqs = []
for root, dirs, files in os.walk(in_dir):
    if len(files) > 0:
        for f in files:
            if '.seq' in f:
                seqs.append(os.path.join(root, f))
seqs = sorted(seqs)

for seq in seqs:
    print(seq)
    temp = seq.split('\\')
    dir = temp[len(temp) - 2]
    save_root = os.path.join(out_dir, dir)
    open_save(seq, save_root)
