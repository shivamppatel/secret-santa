import csv
import random
import copy
contacts = {}
names = []
with open('numbers.txt') as fi:
	for line in fi:
		arr = line.split(",")
		names.append(arr[0])
		print(arr[1].replace(" ", ""))

valid_shuffle = False
while not valid_shuffle:
	valid_shuffle = True
	shuffled = copy.deepcopy(names)
	random.shuffle(shuffled)
	for i in range(0, len(names)):
		if names[i] == shuffled[i]:
			valid_shuffle = False
for i in range(0, len(names)):
	print(names[i], shuffled[i])



