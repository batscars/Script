# coding=utf-8
'''
write confirmed profile info into a list file
'''
import sys
import os

first = open(sys.argv[1])
second = open(sys.argv[2])
content = second.read().split('\n')
merge = open(sys.argv[3], 'w')

while 1:
	line = first.readline()
	if not line:
		break
	image_name = line.split('.')[0]
	merge.write(line)
	line = second.readline()
	num1 = first.readline().strip('\n')
	for i, items in enumerate(content):
		if image_name in items:
			print(image_name, items)
			num2 = content[i+1]
			begin = i+2
			break
	num = int(num1) + int(num2)
	merge.write(str(num) + '\n')
	for i in range(int(num1)):
		line = first.readline()
		merge.write(line)
	for i in range(begin, begin + int(num2)):
		merge.write(content[i] + '\n')
first.close()
second.close()
merge.close()


