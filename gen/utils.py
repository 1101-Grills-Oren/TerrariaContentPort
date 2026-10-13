short=int
sbyte=int
ubyte=int
byte=int
global calcBoolConditionwhenvarisval
global callUsingThis
class ItemHolder:
	def __init__(this,typ):
		this.type=typ
		this.knockBack:float=0#default value
		this.scale:float=1
		this.useSoundPitch:float=0#default value
		this.shootSpeed:float=0#default value
		this.width:int=0#default value
		this.height:int=0#default value
		this.tileWand:int=-1
		this.tooltipContext:int=-1
		this.tooltipSlot:int=-1
		this.fishingPole:int=1
		this.bait:int=0#default value
		this.type:int=0#default value
		this.holdStyle:int=0#default value
		this.useStyle:int=0#default value
		this.useAnimation:int=0#default value
		this.useTime:int=0#default value
		this.stack:int=0#default value
		this.maxStack:int=0#default value
		this.pick:int=0#default value
		this.axe:int=0#default value
		this.hammer:int=0#default value
		this.tileBoost:int=0#default value
		this.createTile:int=-1
		this.createWall:int=-1
		this.placeStyle:int=0#default value
		this.damage:int=0#default value
		this.healLife:int=0#default value
		this.healMana:int=0#default value
		this.alpha:int=0#default value
		this.defense:int=0#default value
		this.headSlot:int=-1
		this.bodySlot:int=-1
		this.legSlot:int=-1
		this.stringColor:int=0#default value
		this.rare:int=0#default value
		this.shoot:int=0#default value
		this.ammo:int=0#AmmoID.None
		this.useAmmo:int=0#AmmoID.None
		this.lifeRegen:int=0#default value
		this.manaIncrease:int=0#default value
		this.mana:int=0#default value
		this.value:int=0#default value
		this.buffType:int=0#default value
		this.buffTime:int=0#default value
		this.mountType:int=-1
		this.shopSpecialCurrency:int=-1
		this.shopCustomPrice:int|None=None
		this.crit:int=0#default value
		this.armorPenetration:int=0#default value
		this.bonusTagDamage:int=0#default value
		this.reuseDelay:int=0#default value
		this.makeNPC:short=0#default value
		this.hairDye:short=-1
		this.glowMask:short=0#default value
		this.handOnSlot:sbyte=-1
		this.handOffSlot:sbyte=-1
		this.backSlot:sbyte=-1
		this.frontSlot:sbyte=-1
		this.shoeSlot:sbyte=-1
		this.waistSlot:sbyte=-1
		this.wingSlot:sbyte=-1
		this.shieldSlot:sbyte=-1
		this.neckSlot:sbyte=-1
		this.faceSlot:sbyte=-1
		this.balloonSlot:sbyte=-1
		this.beardSlot:sbyte=-1
		this.voiceSlot:sbyte=0#default value
		this.dye:byte=0#default value
		this.paint:byte=0#default value
		this.paintCoating:byte=0#default value
		this.prefix:byte=0#default value
		this.questItem:bool=False#default value
		this.flame:bool=False#default value
		this.mech:bool=False#default value
		this.wornArmor:bool=False#default value
		this.expertOnly:bool=False#default value
		this.expert:bool=False#default value
		this.isAShopItem:bool=False#default value
		this.favorited:bool=False#default value
		this.channel:bool=False#default value
		this.accessory:bool=False#default value
		this.potion:bool=False#default value
		this.consumable:bool=False#default value
		this.autoReuse:bool=False#default value
		this.useTurn:bool=False#default value
		this.notAmmo:bool=False#default value
		this.buyOnce:bool=False#default value
		this.noUseGraphic:bool=False#default value
		this.noMelee:bool=False#default value
		this.buy:bool=False#default value
		this.social:bool=False#default value
		this.vanity:bool=False#default value
		this.material:bool=False#default value
		this.noWet:bool=False#default value
		this.cartTrack:bool=False#default value
		this.uniqueStack:bool=False#default value
		this.shootsEveryUse:bool=False#default value
		this.chlorophyteExtractinatorConsumable:bool=False#default value
		this.DD2Summon:bool=False#default value
		this.melee:bool=False#default value
		this.magic:bool=False#default value
		this.ranged:bool=False#default value
		this.summon:bool=False#default value
		this.sentry:bool=False#default value
		this.newAndShiny:bool=False#default value
		this.hasVanityEffects:bool=False#default value
		this.color:any=None#default value
		this.UseSound:any=None#default value
	def SetDefaults1(self,typ):
		x=getFunctionContents("Terraria.Item","void SetDefaults1(int type)")
		return keepOnlyContentsWhen(x,"type",typ)[0]
	def SetDefaults2(self,typ):
		x=getFunctionContents("Terraria.Item","void SetDefaults2(int type)")
		return keepOnlyContentsWhen(x,"type",typ)[0]
	def SetDefaults3(self,typ):
		x=getFunctionContents("Terraria.Item","void SetDefaults3(int type)")
		return keepOnlyContentsWhen(x,"type",typ)[0]
	def SetDefaults4(self,typ):
		x=getFunctionContents("Terraria.Item","void SetDefaults4(int type)")
		return keepOnlyContentsWhen(x,"type",typ)[0]
	def SetDefaults5(self,typ):
		print("z",typ)
		x=getFunctionContents("Terraria.Item","void SetDefaults5(int type)")
		y=keepOnlyContentsWhen(x,"type",typ)[0]
		print(y)
		return y
		
	def fromTypeInd(typ):
		tmpval=ItemHolder(typ)
		global calcBoolConditionwhenvarisval
		def calcBoolConditionwhenvarisvalLocal(varname,value,cond):
			this=[tmpval][0]
			try:
				x=-1
				exec("x=("+cond.replace("&&","&").replace("||","|").replace(varname,str(value))+")")
				return x
			except KeyboardInterrupt as e:
				raise e
			except Exception:
				return None
		calcBoolConditionwhenvarisval=calcBoolConditionwhenvarisvalLocal
		global callUsingThis
		def callUsingThisLocal(what):
			this=[tmpval][0]
			
			try:
				x=None
				exec("x="+what.strip())
				if("SetDefaults" in what):
					print("detdefasdafef",what,x)
					return x
			except KeyboardInterrupt as e:
				raise e
			except Exception:
				print("x="+what.strip())
				return None
			
			return None;
			
		callUsingThis=callUsingThisLocal
		x=getFunctionContents("Terraria.Item","void SetDefaults(int Type, ItemVariant variant = null)")
		print(keepOnlyContentsWhen(x,"this.type",typ)[0])

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
	if(varnamewithtype+";" in c):
		return ""
	c=c[c.index(varnamewithtype+" ")+varnamewithtype.__len__():].strip()
	c=c[2:c.index(";")]
	return c;
def getVariablesOfType(classname,vartype):
	x=classname.split(".")
	f=open("C:/StuffAndThings/tmodloadercode/"+".".join(x[:-1])+"/"+x[-1]+".cs")
	c=f.read()
	f.close()
	d=[]
	while(vartype in c):
		c=c[c.index(vartype)+vartype.__len__():].strip()
		e=c[:c.index(";")].strip()
		if(False==("=>" in e)):
			if(False==("{" in e)):
				if("=" in e):
					e=e[:e.index("=")].strip()
				d.append(e)
	return d;
def calcBoolConditionwhenvarisvalNormal(varname,value,cond):
	try:
		x=-1
		exec("x=("+cond.replace("&&","&").replace("||","|").replace(varname,str(value))+")")
		return x
	except KeyboardInterrupt as e:
		raise e
	except Exception:
		return None
calcBoolConditionwhenvarisval=calcBoolConditionwhenvarisvalNormal
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
			y=callUsingThis(block[c:ind1])
			if(y!=None):
				newcontents+=y
			else:
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
			y=callUsingThis(block[c:ind1])
			if(y!=None):
				newcontents+=y
			else:
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
	if("Sets.Factory.CreateBoolSet" in x):
		x=[i.strip() for  i in x["Sets.Factory.CreateBoolSet(".__len__():-1].split(",")];
		if(x.__len__()>0):
			if(x[0]==""):
				x=[]
			if(x.__len__()>0):
				if(x[0]=="true"):
					x=[int(i) for i in x[1:]]
					return [True==(i in x) for i in range(ItemID.Count)]
				elif(x[0]=="false"):
					x=[int(i) for i in x[1:]]
					return [False==(i in x) for i in range(ItemID.Count)]
				else:
					x=[int(i) for i in x]
					return [True==(i in x) for i in range(ItemID.Count)]
		return [False for i in range(ItemID.Count)]


class ItemID:
	Count=6145
	NumItemsInPrevVersion=5456
class ItemID:
	Count=6145
	NumItemsInPrevVersion=5456
	class Sets:
		DualEquipArmor=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] DualEquipArmor"))
		ReceivesDiagonalCorrectionAsFakeFish=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] ReceivesDiagonalCorrectionAsFakeFish"))
		ShootsOnUseRelease=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] ShootsOnUseRelease"))
		NoMeleeSpeedBonus=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] NoMeleeSpeedBonus"))
		IsLavaImmuneRegardlessOfRarity=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] IsLavaImmuneRegardlessOfRarity"))
		ItemsThatAllowRepeatedRightClick=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] ItemsThatAllowRepeatedRightClick"))
		ItemsThatCountAsBombsForDemolitionistToSpawn=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] ItemsThatCountAsBombsForDemolitionistToSpawn"))
		RapidAttackBonusDamage=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] RapidAttackBonusDamage"))
		ItemsThatShouldNotBeInInventory=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] ItemsThatShouldNotBeInInventory"))
		DrawUnsafeIndicator=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] DrawUnsafeIndicator"))
		CanBeExtractinated=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] CanBeExtractinated"))
		UsesBetterMeleeItemLocation=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] UsesBetterMeleeItemLocation"))
		WorksInVoidBag=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] WorksInVoidBag"))
		GrassSeeds=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] GrassSeeds"))
		Moss=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] Moss"))
		ShimmerPostMoonlord=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] ShimmerPostMoonlord"))
		SkipsInitialUseSound=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] SkipsInitialUseSound"))
		UsesCursedByPlanteraTooltip=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] UsesCursedByPlanteraTooltip"))
		IsAKite=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] IsAKite"))
		PlaceTileOnAltUse=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] PlaceTileOnAltUse"))
		HasAProjectileThatHasAUsabilityCheck=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] HasAProjectileThatHasAUsabilityCheck"))
		CanGetPrefixes=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] CanGetPrefixes"))
		ColorfulDyeValues=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] ColorfulDyeValues"))
		IsAMaterial=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] IsAMaterial"))
		IgnoresEncumberingStone=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] IgnoresEncumberingStone"))
		IsAPickup=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] IsAPickup"))
		IsDrill=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] IsDrill"))
		IsChainsaw=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] IsChainsaw"))
		IsPaintScraper=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] IsPaintScraper"))
		SummonerWeaponThatScalesWithAttackSpeed=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] SummonerWeaponThatScalesWithAttackSpeed"))
		IsFood=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] IsFood"))
		CanFishInLava=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] CanFishInLava"))
		IsLavaBait=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] IsLavaBait"))
		FakeFishInanimate=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] FakeFishInanimate"))
		IsBasicFish=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] IsBasicFish"))
		IsFishingCrate=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] IsFishingCrate"))
		IsFishingCrateHardmode=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] IsFishingCrateHardmode"))
		IsAVoiceChangeItem=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] IsAVoiceChangeItem"))
		CanBePlacedOnWeaponRacks=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] CanBePlacedOnWeaponRacks"))
		IsQuestFish=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] IsQuestFish"))
		TrapSigned=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] TrapSigned"))
		Deprecated=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] Deprecated"))
		NeverAppearsAsNewInInventory=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] NeverAppearsAsNewInInventory"))
		CommonCoin=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] CommonCoin"))
		ItemIconPulse=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] ItemIconPulse"))
		ItemNoGravity=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] ItemNoGravity"))
		ExoticPlantsForDyeTrade=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] ExoticPlantsForDyeTrade"))
		NebulaPickup=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] NebulaPickup"))
		AnimatesAsSoul=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] AnimatesAsSoul"))
		ErrorWorldChestSwapImmunity=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] ErrorWorldChestSwapImmunity"))
		gunProj=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] gunProj"))
		GamepadWholeScreenUseRange=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] GamepadWholeScreenUseRange"))
		GamepadSmartQuickReach=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] GamepadSmartQuickReach"))
		Yoyo=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] Yoyo"))
		AlsoABuildingItem=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] AlsoABuildingItem"))
		NeverLocksOn=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] NeverLocksOn"))
		LockOnIgnoresCollision=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] LockOnIgnoresCollision"))
		SingleUseInGamepad=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] SingleUseInGamepad"))
		Torches=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] Torches"))
		WaterTorches=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] WaterTorches"))
		Campfires=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] Campfires"))
		Glowsticks=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] Glowsticks"))
		BossBag=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] BossBag"))
		OpenableBag=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] OpenableBag"))
		HasItemSwap=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] HasItemSwap"))
		RecoverableImportantItem=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] RecoverableImportantItem"))
		HasRightFire=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] HasRightFire"))
		IsRangedSpecialistWeapon=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] IsRangedSpecialistWeapon"))
		IsWireableStatue=BoolListFromBoolSetCreator(getVariable("Terraria.ID.ItemID","public static bool[] IsWireableStatue"))

"""tmp=""
vartypes={"float":("float",0),
		 "int":("int",0),
		 "short":("short",0),
		 "sbyte":("sbyte",0),
		 "byte":("byte",0),
		 "bool":("bool",False),
		 "Color":("any",None),
		 "LegacySoundStyle":("any",None)}

for vt in vartypes:
	for i in getVariablesOfType("Terraria.Item","public "+vt):
		if(i[0]=="?"):
			y=getVariable("Terraria.Item","public "+vt+i)
			if(y.__len__()==0):
				tmp+=i[2:]+":"+vartypes[vt][0]+"|None=None\n"
			else:
				tmp+=i[2:]+":"+vartypes[vt][0]+"|None="+y+"\n"
		else:
			y=getVariable("Terraria.Item","public "+vt+" "+i)
			if(y.__len__()==0):
				tmp+=i+":"+vartypes[vt][0]+"="+str(vartypes[vt][1])+"#default value\n"
			else:
				tmp+=i+":"+vartypes[vt][0]+"="+y+"\n"
print(tmp.replace("\n","\nthis."))
#getItemInitLines(3005)
"""
ItemHolder.fromTypeInd(3005)
print("C:\\StuffAndThings\\itemportgen")
