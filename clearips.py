
number = 8

i =  1

while i <= number:
	for t in ["P", "M"]:
		mfile = open("./ip/" + t + str(i) + "ip.txt", "w")
		mfile.write("")
		mfile.close()
	i += 1
