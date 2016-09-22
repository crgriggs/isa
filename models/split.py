import os


for file in os.listdir("."):
	isModel = True
	isModule = False
	fileName = file.split(".")
	model = open(fileName[0] + "_model", "w")
	module = open(fileName[0] + "_module", "w")
	control = open(fileName[0] + "_control", "w")
	for line in open(file, "r"):
		if(isModel):
			if line.startswith("MODULE"):
				isModel = False
				isModule = True
			else:
				model.write(line)
		elif (isModule):
			if line.startswith("CONTROL"):
				isModule = False
			else:
				module.write(line)
		else:
			control.write(line)
	




