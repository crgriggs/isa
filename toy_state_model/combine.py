#!/usr/bin/env python
import sys, os

if len(sys.argv) == 2:
	propType = sys.argv[1]
else:
	print "Enter folder that handles current property"
	quit()
if not os.path.isdir("./" + str(propType)):
	print str(propType) + "is not a folder in the current directory" 
with open("state.ucl", 'w+') as f:
	with open("header.txt") as h:
		for line in h:
			f.write(line)
		h.close()
	f.write('\n')
	for filename in os.listdir("./" + str(propType)):
		with open("./" + str(propType)+"/"+filename) as h:
			for line in h:
				f.write(line)
			h.close()
		f.write('\n')
	with open("state.txt") as h:
		for line in h:
			f.write(line)
		h.close()
	f.write('\n')
	with open("control.txt") as h:
		for line in h:
			f.write(line)
		h.close()


