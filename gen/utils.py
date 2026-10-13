def findLinkedBracket(content,brackets={"[":"]","{":"}"}):
	"""
		Finds the brackets linked to the one at the very start, and gives an index. If not found, returns -1
	"""
	depth=""
	i=0
	while((depth.__len__()!=0)|(i==0)):
		if(i>=content.__len__()):
			return -1
		if(content[i] in brackets):
			depth+=content[i]
		elif(content[i]==brackets[depth[-1]]):
			depth=depth[:-1]
		i=i+1
	return i-1;
def getFunctionContents(classname,methodname):
	x=classname.split(".")
	f=open("C:/StuffAndThings/tmodloadercode/"+".".join(x[:-1])+"/"+x[-1]+".cs")
	c=f.read()
	f.close()
	c=c[c.index(methodname)+methodname.__len__():].strip()
	return c[1:findLinkedBracket(c)]
def getItemInitLines(itemtype:int):
	pass
def keepOnlyContentsWhen(varname,value):
	pass
getFunctionContents("Terraria.Item","void SetDefaults4(int type)")
print("C:\\StuffAndThings\\itemportgen")
