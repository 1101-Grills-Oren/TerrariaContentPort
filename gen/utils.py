
def findLinkedBracket(content,brackets={"[":"]","{":"}"},start=0):
	"""
		Finds the brackets linked to the one at the very start, and gives an index. If not found, returns -1
	"""
	depth=""
	i=start
	while((depth.__len__()!=0)|(i==start)):
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
def getVariable(classname,varnamewithtype):
	x=classname.split(".")
	f=open("C:/StuffAndThings/tmodloadercode/"+".".join(x[:-1])+"/"+x[-1]+".cs")
	c=f.read()
	f.close()
	c=c[c.index(varnamewithtype)+varnamewithtype.__len__():].strip()
	c=c[2:c.index(";")]
	return c;
def calcBoolConditionwhenvarisval(varname,value,cond):
	try:
		x=-1
		exec("x=("+cond.replace("&&","&").replace("||","|").replace(varname,str(value))+")")
		return x
	except KeyboardInterrupt as e:
		raise e
	except Exception:
		return None
def getItemInitLines(itemtype:int):
	x=getFunctionContents("Terraria.Item","void SetDefaults(int Type, ItemVariant variant = null)")
	print(keepOnlyContentsWhen(x,"this.type",itemtype)[0])
def keepOnlyContentsWhenSwitchStatement(block,varname,value,swc):
	if(("case "+swc+":") in block):
		startind=block.index("case "+swc+":")
	else:
		startind=-1
	if(startind==-1):
		return ["",False]
	newcontents=""
	block=block[startind:]
	c=0
	while(c<block.__len__()):
		#print(c)
		ind1=block.find(";",c)
		ind2=block.find("{",c)
		if(block[c:c+4]=="case"):
			c=block.index(":",c)+1
		elif((ind1>=0)&((ind1<ind2)|(ind2<0))):
			#; first, not a block
			if(block[c:ind1]=="break"):
				break
			if(block[c:ind1]=="return"):
				return [newcontents,True]
			newcontents+=block[c:ind1+2]
			
			c=ind1+2
		elif(ind1<0):
			break
		else:
			#a block!
			v=block[c:ind2].strip()
			if(v[0:9+varname.__len__()]=="switch ("+varname+")"):
				y=keepOnlyContentsWhenSwitchStatement(block[ind2+2:findLinkedBracket(block,start=ind2)],varname,value,str(value))
				c=findLinkedBracket(block,start=ind2)+2
				if(y[0].__len__()>0):
					newcontents+=y[0]+"\n"
				if(y[1]):
					return [newcontents,True]
			elif(v[0:3] in ["if ","if("]):
				n=calcBoolConditionwhenvarisval(varname,value,v[2:])
				if(n==None):
					newcontents+=v+"{\n\t"+keepOnlyContentsWhen(block[ind2+1:findLinkedBracket(block,start=ind2)],varname,value)[0].replace("\n","\n\t")+"}"
					c=findLinkedBracket(block,start=ind2)+2;
				elif(n==True):
					m=keepOnlyContentsWhen(block[ind2+1:findLinkedBracket(block,start=ind2)],varname,value)
					newcontents+=m[0]
					if(m[1]):
						return [newcontents,True]
					c=findLinkedBracket(block,start=ind2)+2;
				else:
					c=findLinkedBracket(block,start=ind2)+2;
			else:
				print("v",v)
				raise Exception()
	return [newcontents,False]
def keepOnlyContentsWhen(block,varname,value):
	block="\n".join([i.strip() for i in block.split("\n")])
	newcontents=""
	c=0
	while(c<block.__len__()):
		ind1=block.find(";",c)
		ind2=block.find("{",c)
		if((ind1>=0)&((ind1<ind2)|(ind2<0))):
			#; first, not a block
			newcontents+=block[c:ind1+2]
			c=ind1+2
		elif(ind1<0):
			break
		else:
			#a block!
			v=block[c:ind2].strip()
			if(v[0:9+varname.__len__()]=="switch ("+varname+")"):
				y=keepOnlyContentsWhenSwitchStatement(block[ind2+2:findLinkedBracket(block,start=ind2)],varname,value,str(value))
				c=findLinkedBracket(block,start=ind2)+2
				if(y[0].__len__()>0):
					newcontents+=y[0]+"\n"
				if(y[1]):
					return [newcontents,True]
			elif(v[0:3] in ["if ","if("]):
				n=calcBoolConditionwhenvarisval(varname,value,v[2:])
				if(n==None):
					newcontents+=v+"{\n\t"+keepOnlyContentsWhen(block[ind2+1:findLinkedBracket(block,start=ind2)],varname,value)[0].replace("\n","\n\t")[:-1]+"}\n"
					c=findLinkedBracket(block,start=ind2)+2;
					if(block[c:c+7]=="else if"):
						c=c+5
					elif(block[c:c+4]=="else"):
						ind1=block.find(";",c)
						ind2=block.find("{",c)
						newcontents+="else{\n\t"+keepOnlyContentsWhen(block[ind2+1:findLinkedBracket(block,start=ind2)],varname,value)[0].replace("\n","\n\t")[:-1]+"}\n"
						c=findLinkedBracket(block,start=ind2)+2;
				elif(n==True):
					m=keepOnlyContentsWhen(block[ind2+1:findLinkedBracket(block,start=ind2)],varname,value)
					newcontents+=m[0]
					if(m[1]):
						return [newcontents,True]
					c=findLinkedBracket(block,start=ind2)+2;
					while(block[c:c+4]=="else"):
						ind1=block.find(";",c)
						ind2=block.find("{",c)
						c=findLinkedBracket(block,start=ind2)+2;
				else:
					c=findLinkedBracket(block,start=ind2)+2;
					if(block[c:c+7]=="else if"):
						c=c+5
					elif(block[c:c+4]=="else"):
						newcontents+=keepOnlyContentsWhen(block[c+6:findLinkedBracket(block,start=c+5)],varname,value)[0]
						c=findLinkedBracket(block,start=c+5)+2
			else:
				print("line",[i for i in block[:c] if i=="\n"].__len__())
				print("v",v)
				raise Exception()
	return [newcontents,False]
def indexListFromBoolSetCreator(x):
	return [int(i.strip()) for i in x["Sets.Factory.CreateBoolSet(".__len__():-1].split(",")]
def BoolListFromBoolSetCreator(x):
	x=x["Sets.Factory.CreateBoolSet(".__len__():-1].split(",");
	return [int(i.strip()) for i in x["Sets.Factory.CreateBoolSet(".__len__():-1].split(",")]


class ItemID:
	class Sets:
		IsFood=indexListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] IsFood"))
	Count=6145



ItemIsFood=indexListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] IsFood"))
print(ItemIsFood)
#getItemInitLines(3005)
print("C:\\StuffAndThings\\itemportgen")
