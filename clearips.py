
number = 8

i =  1

while i <= number:
	mfile = open("./ip/" + str(i) + "ip.txt", "w")
	mfile.write("")
	mfile.close()
	i += 1
