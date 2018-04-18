inp=str(input("Enter source:"))
des=str(input("Enter dest:"))
with open(inp,"r") as file1:
	with open(des,"w") as file2:
		for x in file1.readlines():
			li=x.split(",")
			z=li[0]+','+li[1]
			file2.write(z)
