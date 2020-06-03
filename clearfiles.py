
number = 8

i =  1

while i <= number:
	for type in ["P", "M"]:
		mfile = open("./results/" + type + str(i) + ".txt", "w")
		mfile.write("")
		mfile.close()
	i += 1
