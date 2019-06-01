#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
import os

def convert_text_for_servo(command_action,time):
	text=[]
	if command_action == 'A1':
		text = 'print(\''+ command_action + "," + str(time) + '\')'
		#print(text)
	elif command_action == 'A2':
		text = 'print(\''+ command_action + "," + str(time) + '\')'
		#print(text)
	elif command_action == 'A3':
		text = 'print(\''+ command_action + "," + str(time) + '\')'
		#print(text)
	elif command_action == 'B1':
		text = 'print(\''+ command_action + "," + str(time) + '\')'
		#print(text)
	elif command_action == 'B2':
		text = 'print(\''+ command_action + "," + str(time) + '\')'
		#print(text)
	elif command_action == 'B3':
		text = 'print(\''+ command_action + "," + str(time) + '\')'
		#print(text)
	elif command_action == 'C1':
		text = 'print(\''+ command_action + "," + str(time) + '\')'
		#print(text)
	elif command_action == 'C2':
		text = 'print(\''+ command_action + "," + str(time) + '\')'
		#print(text)
	elif command_action == 'C3':
		text = 'print(\''+ command_action + "," + str(time) + '\')'
		#print(text)
	else:
		test =''
	return text

fp = open(sys.argv[1], 'r')
command =[]
for line in fp.readlines():
	l = line.strip().strip("\n")
	l = l.split(',')
	l[1] = float(l[1])

	out = convert_text_for_servo(l[0],l[1])
	command.append(out)
fp.close()

#print(command)
file_name = sys.argv[1].replace("csv", "py")
file = open(file_name, 'w')
file.write("#!/usr/bin/env python\n")
file.write("# -*- coding: UTF-8 -*-\n\n")
for w_c in command:
	file.write(w_c+"\n")

file.close()

os.chmod(file_name, 0o777)
