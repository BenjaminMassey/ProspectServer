
number = 8

i =  1

while i <= number:
	for t in ["P", "M"]:
		mfile = open("./results/" + t + str(i) + ".txt", "w")
		mfile.write("")
		mfile.close()
	i += 1
