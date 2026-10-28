true=True
false=False
short=int
sbyte=int
ubyte=int
byte=int
global calcBoolConditionwhenvarisval
global callUsingThis
global currentvars
import threading
import colorama
colorama.init()
function=type(lambda x:0)
drawlock=threading.Lock()
def drawbar(progress,vind,text,fprogress=None):
    if(fprogress==None):
        vind=vind+1
        from shutil import get_terminal_size
        width=get_terminal_size()[0]
        width=100
        formattedtext=text+f"[{int(1000*progress)/10}%]"
        if(text=="-"):
            formattedtext="-"
        formattedtext="▏"+" "*(int(width/2-formattedtext.__len__()/2)-1)+formattedtext+" "*(width-formattedtext.__len__()-(int(width/2-formattedtext.__len__()/2))-2)+"▕"
        sp=width*progress-int(width*progress)
        if(sp<0.5):
            sp=int(sp*255)
            formattedtext="\033[38;2;0;0;0;48;2;255;255;255m\033[53;4m"+formattedtext[0:int(width*progress)]+f"\033[38;2;255;255;255;48;2;{sp};{sp};{sp}m\033[53;4m"+formattedtext[int(width*progress):int(width*progress+1)]+"\033[38;2;255;255;255;48;2;0;0;0m\033[53;4m"+formattedtext[int(width*progress+1):]
        else:
            sp=int(sp*255)
            formattedtext="\033[38;2;0;0;0;48;2;255;255;255m\033[53;4m"+formattedtext[0:int(width*progress)]+f"\033[48;2;{sp};{sp};{sp}m\033[53;4m"+formattedtext[int(width*progress):int(width*progress+1)]+"\033[38;2;255;255;255;48;2;0;0;0m\033[53;4m"+formattedtext[int(width*progress+1):]
        with drawlock:
            if(vind==0):
                print(f"\033[s\033[{width}D"+formattedtext+"\033[0m")
                print(f"\033[1B",end="")
            else:
                print(f"\033[s\033[{width}D\033[{vind}A"+formattedtext+"\033[0m")
                print(f"\033[{vind-1}B",end="")
    else:
        vind=vind+1
        from shutil import get_terminal_size
        width=100#get_terminal_size()[0]
        formattedtext=text+f"[{int(100*progress)}%]"
        formattedtext="▏"+" "*(int(width/2-formattedtext.__len__()/2)-1)+formattedtext+" "*(width-formattedtext.__len__()-(int(width/2-formattedtext.__len__()/2))-2)+"▕"
        formattedtext="\033[7m\033[53;4m"+formattedtext[0:int(width*progress)]+"\033[0m\033[48;5;240;53;4m"+formattedtext[int(width*progress):int(width*fprogress)]+"\033[0m\033[53;4m"+formattedtext[int(width*fprogress):]
        with drawlock:
            if(vind==0):
                print(f"\033[s\033[{width}D"+formattedtext+"\033[0m")
                print(f"\033[1B",end="")
            else:
                print(f"\033[s\033[{width}D\033[{vind}A"+formattedtext+"\033[0m")
                print(f"\033[{vind-1}B",end="")
def drawbarwithLosses(progress,vind,text,lossprogress):
	vind=vind+1
	from shutil import get_terminal_size
	width=100#get_terminal_size()[0]
	formattedtext=text+f"[{int(1000*progress)/10}%-{int(1000*lossprogress)/10}%]"
	if(text=="-"):
		formattedtext="-"
	formattedtext="▏"+" "*(int(width/2-formattedtext.__len__()/2)-1)+formattedtext+" "*(width-formattedtext.__len__()-(int(width/2-formattedtext.__len__()/2))-2)+"▕"
	w2=formattedtext.__len__()
	sp=w2*progress-int(w2*progress)
	sf=w2*lossprogress-int(w2*lossprogress)
	colorsp=[255 if i<int(w2*progress) else int(sp*255) if i==int(w2*progress) else 0 for i in range(w2)]
	colorsf=[255 if i<int(w2*lossprogress) else int(sf*255) if i==int(w2*lossprogress) else 0 for i in range(w2-1,-1,-1)]
	colors=[(colorsp[i]+colorsf[i],colorsp[i],colorsp[i]) for i in range(w2)]
	newformattedtext=""
	for i in range(w2):
		b=False
		if(i!=0):
			if(colors[i]!=colors[i-1]):
				b=True
		else:
			b=True
		if(b):
			bgc=255 if (colors[i][0]+colors[i][1]+colors[i][2])<382 else 0
			newformattedtext+=f"\033[38;2;{bgc};{bgc};{bgc};48;2;{colors[i][0]};{colors[i][1]};{colors[i][2]}m\033[53;4m"
		newformattedtext+=formattedtext[i]
	formattedtext=newformattedtext
	with drawlock:
		if(vind==0):
			print(f"\033[s\033[{width}D"+formattedtext+"\033[0m")
			print(f"\033[1B",end="")
		else:
			print(f"\033[s\033[{width}D\033[{vind}A"+formattedtext+"\033[0m")
			print(f"\033[{vind-1}B",end="")

class Vector2:
	@classmethod
	@property
	def One(cls):
		return Vector2(1)
	def __init__(*args):
		if(args.__len__()==1):
			this.X=args[0]
			this.Y=args[0]
		elif(args.__len__()==2):
			this.X=args[0]
			this.Y=args[1]
class Vector3:
	@classmethod
	@property
	def One(cls):
		return Vector3(1)
	def __init__(*args):
		if(args.__len__()==1):
			this.X=args[0]
			this.Y=args[0]
			this.Z=args[0]
		elif(args.__len__()==2):
			this.X=args[0].X
			this.Y=args[0].Y
			this.Z=args[1]
		elif(args.__len__()==3):
			this.X=args[0]
			this.Y=args[1]
			this.Z=args[2]
class Texture2D:
	pass
from typing import Generic, TypeVar
class Asset(Generic[TypeVar('T')]):
	def __init__(this,name,mode):
		this._name=name
		this._mode=mode
	Empty=None
	def Width(this):
		return 15
	def Height(this):
		return 15
	def __repr__(this):
		return "<Asset _name="+this._name.__repr__()+">"
class ItemMethods:
	def sellPrice(platinum=0,gold=0,silver=0,copper=0):
		return platinum*1000000+gold*10000+silver*100+copper
class ItemHolder:
	default=None
	def __init__(this,typ):
		this.type:int=typ
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
		this.dye:byte=-1#default value
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
		this.Variant:any=-1#private set, public get
	def SetDefaults1(self,typ):
		x=getFunctionContents("Terraria.Item","void SetDefaults1(int type)")
		return keepOnlyContentsWhen(x,"type",typ)[0]
	def SetDefaults2(self,typ):
		x=getFunctionContents("Terraria.Item","void SetDefaults2(int type)")
		return keepOnlyContentsWhen(x,"type",typ)[0]
	def SetDefaults3(self,typ):
		x=getFunctionContents("Terraria.Item","void SetDefaults3(int type)")
		try:
			result=keepOnlyContentsWhen(x,"type",typ,["type"])
		except Exception as e:
			raise KeyboardInterrupt(e)
		return result[0]
	def SetDefaults4(self,typ):
		x=getFunctionContents("Terraria.Item","void SetDefaults4(int type)")
		return keepOnlyContentsWhen(x,"type",typ)[0]
	def SetDefaults5(self,typ):
		x=getFunctionContents("Terraria.Item","void SetDefaults5(int type)")
		result=keepOnlyContentsWhen(x,"type",typ,["type"])
		#print(result[0])
		return result[0]
	def SetFoodDefaults(self,typ):
		x=getFunctionContents("Terraria.Item","void SetFoodDefaults(int type)")
		global currentvars
		currentvars['type']=typ
		result=keepOnlyContentsWhen(x,"type",typ,["type"])
		#print(result[0])
		return result[0]
	def DefaultToRangedWeapon(self,baseProjType,ammoID,singleShotTime,shotVelocity,hasAutoReuse=False):
		x=getFunctionContents("Terraria.Item","public void DefaultToRangedWeapon(int baseProjType, int ammoID, int singleShotTime, float shotVelocity, bool hasAutoReuse = false)")
		currentvars["baseProjType"]=baseProjType
		currentvars["ammoID"]=ammoID
		currentvars["singleShotTime"]=singleShotTime
		currentvars["shotVelocity"]=shotVelocity
		currentvars["hasAutoReuse"]=hasAutoReuse
		result=keepOnlyContentsWhen(x,"sidjfoaiehd",None,[])
		#print(result[0])
		return
		#return result[0]
	def DefaultToThrownWeapon(self,baseProjType,singleShotTime,shotVelocity,hasAutoReuse=False):
		x=getFunctionContents("Terraria.Item","public void DefaultToThrownWeapon(int baseProjType, int singleShotTime, float shotVelocity, bool hasAutoReuse = false)")
		currentvars["baseProjType"]=baseProjType
		currentvars["singleShotTime"]=singleShotTime
		currentvars["shotVelocity"]=shotVelocity
		currentvars["hasAutoReuse"]=hasAutoReuse
		result=keepOnlyContentsWhen(x,"sidjfoaiehd",None,[])
		#print(result[0])
		return
	def DefaultToMagicWeapon(self,projType,singleShotTime,shotVelocity,hasAutoReuse=False):
		x=getFunctionContents("Terraria.Item","public void DefaultToMagicWeapon(int projType, int singleShotTime, float shotVelocity, bool hasAutoReuse = false)")
		currentvars["projType"]=projType
		currentvars["singleShotTime"]=singleShotTime
		currentvars["shotVelocity"]=shotVelocity
		currentvars["hasAutoReuse"]=hasAutoReuse
		result=keepOnlyContentsWhen(x,"sidjfoaiehd",None,[])
		#print(result[0])
		return
	def DefaultToWhip(self,projectileId,dmg,kb,shootspeed,animationTotalTime=30):
		x=getFunctionContents("Terraria.Item","public void DefaultToWhip(int projectileId, int dmg, float kb, float shootspeed, int animationTotalTime = 30)")
		currentvars["projectileId"]=projectileId
		currentvars["dmg"]=dmg
		currentvars["kb"]=kb
		currentvars["shootspeed"]=shootspeed
		currentvars["animationTotalTime"]=animationTotalTime
		result=keepOnlyContentsWhen(x,"sidjfoaiehd",None,[])
		#print(result[0])
		return
		
	def fromTypeInd(typ):
		global tmpval
		tmpval=ItemHolder(typ)
		global calcBoolConditionwhenvarisval
		global currentvars
		currentvars={"x":None,"this":[tmpval][0],"true":True,"false":False,"Item":ItemMethods,"ItemID":ItemID,"null":None,"variant":None,"GameShaders":GameShadersMethods,"Main":Main}
		def calcBoolConditionwhenvarisvalLocal(varname,value,cond):
			global tmpval
			global currentvars
			try:
				if(findWhilstRespectingBrackets(cond,"&&")!=-1):
					s=splitWhilstRespectingBrackets(cond,"&&")
					a=calcBoolConditionwhenvarisvalLocal(varname,value,s[0])
					b=calcBoolConditionwhenvarisvalLocal(varname,value,"&&".join(s[1:]))
					if(a==False):
						return False
					if(b==False):
						return False
					if(a==True):
						if(b==True):
							return True
						else:
							return a
					else:
						if(b==True):
							return b
						else:
							return a+"&&"+b
				if(findWhilstRespectingBrackets(cond,"||")!=-1):
					s=splitWhilstRespectingBrackets(cond,"||")
					a=calcBoolConditionwhenvarisvalLocal(varname,value,s[0])
					b=calcBoolConditionwhenvarisvalLocal(varname,value,"||".join(s[1:]))
					if(a==True):
						return True
					if(b==True):
						return True
					if(a==False):
						if(b==False):
							return False
						else:
							return b
					else:
						if(b==True):
							return a
						else:
							return a+"||"+b
						
				exec("x=((("+cond.replace("&&",")&(").replace("||",")|(").replace(varname,str(value))+")))",{},currentvars)
				return currentvars['x']
			except KeyboardInterrupt as e:
				print(cond)
				raise e
			except Exception:
				return cond
		calcBoolConditionwhenvarisval=calcBoolConditionwhenvarisvalLocal
		global callUsingThis
		def callUsingThisLocal(what):
			global tmpval
			global currentvars
			this=[tmpval][0]
			what=what.strip()
			what=what.replace(":","=")
			what2=""
			for i in what:
				if((i=="f")&(what2[-1:] in [i for i in "0123456789"])):
					pass
				else:
					what2+=i
			what=what2
			if(what[0:3]=="int"):
				what=what[4:]
			try:
				if("this.type =" in what.strip()):
					return None

				exec("x="+what.strip(),{},currentvars)
				tmpval=currentvars["this"]
				if("SetDefaults" in what)|("SetFoodDefaults" in what):
					return currentvars['x']
			except KeyboardInterrupt as e:
				raise e
			except Exception:
				return None
			
			return None;
			
		callUsingThis=callUsingThisLocal
		x=getFunctionContents("Terraria.Item","void SetDefaults(int Type, ItemVariant variant = null)")
	
		y=keepOnlyContentsWhen(x,"Type",typ)[0]
		#print(y)
		#print(typ)
		y=y[y.index("this.material = "):]
		y=y[y.index(";")+2:]
		y=y[:y.index("this.RebuildTooltip()")]
		return [tmpval,y]
class ProjectileHolder:
	default=None
	def __init__(this,typ):
		this.type:int=typ
		this.StartAngle:float=0#default value
		this.AnglePerBullet:float=0#default value
		this.BulletsProgressInStormStartNormalized:float=0#default value
		this.BulletsProgressInStormBonusByIndexNormalized:float=0#default value
		this.StormTotalRange:float=0#default value
		this.ownerHitCheckDistance:float=1000#f
		this.scale:float=1#f
		this.rotation:float=0#default value
		#this.ai:list[float]=new float[Projectile.maxAI]
		#this.localAI:list[float]=new float[Projectile.maxAI]
		this.gfxOffY:float=0#default value
		this.stepSpeed:float=1#f
		this.knockBack:float=0#default value
		this.light:float=0#default value
		#this.oldRot:list[float]=#new float[10]
		this.minionSlots:float=0#default value
		this.BulletsInStorm:int=0#default value
		this.numHits:int=0#default value
		#this.alpha:int=0#default value
		this.owner:int=255
		this.aiStyle:int=0#default value
		this.timeLeft:int=0#default value
		this.soundDelay:int=0#default value
		this.damage:int=0#default value
		this.originalDamage:int=0#default value
		this.spriteDirection:int=1
		this.penetrate:int=1
		#this.localNPCImmunity:list[int]=[];#new int[Main.maxNPCs]
		this.maxPenetrate:int=1
		this.identity:int=0#default value
		this.netSpam:int=0#default value
		#this.oldSpriteDirection:list[int]=new int[10]
		this.minionPos:int=0#default value
		this.restrikeDelay:int=0#default value
		this.extraUpdates:int=0#default value
		this.numUpdates:int=0#default value
		this.drawLayer:int=0#default value
		#this.playerImmune:list[int]=new int[255]
		this.frameCounter:int=0#default value
		this.frame:int=0#default value
		this.projUUID:int=-1
		this.localNPCHitCooldown:int=-2
		this.idStaticNPCHitCooldown:int=-1
		this.bannerIdToRespondTo:int=0#default value
		this.tagEffectType:int=0#default value
		this.bonusTagDamage:int=0#default value
		this.armorPenetration:int=0#default value
		this.bonusCritChance:int=0#default value
		this.glowMask:short=0#default value
		this.active:bool=False#default value
		this.arrow:bool=False#default value
		this.bobber:bool=False#default value
		this.netImportant:bool=False#default value
		this.noDropItem:bool=False#default value
		this.counterweight:bool=False#default value
		this.sentry:bool=False#default value
		this.hostile:bool=False#default value
		this.reflected:bool=False#default value
		this.friendly:bool=False#default value
		this.usesLocalNPCImmunity:bool=False#default value
		this.usesIDStaticNPCImmunity:bool=False#default value
		this.appliesImmunityTimeOnSingleHits:bool=False#default value
		this.netUpdate:bool=False#default value
		this.netUpdate2:bool=False#default value
		this.minion:bool=False#default value
		this.tileCollide:bool=False#default value
		this.stopsDealingDamageAfterPenetrateHits:bool=False#default value
		this.ignoreWater:bool=False#default value
		this.isAPreviewDummy:bool=False#default value
		this.isAPreviewDisplayDoll:bool=False#default value
		this.usesOwnerLight:bool=False#default value
		this.hide:bool=False#default value
		this.ownerHitCheck:bool=False#default value
		this.usesOwnerMeleeHitCD:bool=False#default value
		this.melee:bool=False#default value
		this.ranged:bool=False#default value
		this.magic:bool=False#default value
		this.coldDamage:bool=False#default value
		this.noEnchantments:bool=False#default value
		this.noEnchantmentVisuals:bool=False#default value
		this.trap:bool=False#default value
		this.npcProj:bool=False#default value
		this.originatedFromActivableTile:bool=False#default value
		this.manualDirectionChange:bool=False#default value
		this.correctSlopeCollision:bool=False#default value
		this.decidesManualFallThrough:bool=False#default value
		this.shouldFallThrough:bool=False#default value
		this.AImethod:string=""
		this.SetDefaultsMethod:string=""
	
	def AI_149_GolfBall(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_149_GolfBall()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_151_SuperStar(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_151_SuperStar()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_152_SuperStarSlash(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_152_SuperStarSlash()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_DisplayDoll_Reset(this, doll):
		x=getFunctionContents("Terraria.Projectile","private void AI_DisplayDoll_Reset(Player doll)")
		return keepOnlyContentsWhen(keepOnlyContentsWhen(x,"this.type",this.type)[0],"doll",doll)[0]
	def AI_205_RemoteControlCar(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_205_RemoteControlCar()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_204_Digtoise(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_204_Digtoise()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_003_Boomerang(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_003_Boomerang()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_203_StormLightning(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_203_StormLightning()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_202_TorchGodHelper(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_202_TorchGodHelper()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_201_ThrownMelee(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_201_ThrownMelee()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_200_BirdDroppings(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_200_BirdDroppings()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_199_MeteorOre(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_199_MeteorOre()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_105_SporeSac(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_105_SporeSac()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_197_HandleTileCollision(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_197_HandleTileCollision()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_197_CeilingAndHoverTurret(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_197_CeilingAndHoverTurret()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_196_Petal(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_196_Petal()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_113_TargetSticker(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_113_TargetSticker()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_113_UpdateDrawLayer(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_113_UpdateDrawLayer()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_195_JimsDrone(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_195_JimsDrone()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_111_DryadsWard(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_111_DryadsWard()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_194_HorsemanPumpkin(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_194_HorsemanPumpkin()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_193_Flamethrower(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_193_Flamethrower()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_047_MagnetSphere(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_047_MagnetSphere()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_047_MagnetSphere_TryAttacking(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_047_MagnetSphere_TryAttacking()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_192_JuminoAnimation(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_192_JuminoAnimation()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_191_TrueNightsEdge(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_191_TrueNightsEdge()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_190_NightsEdge(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_190_NightsEdge()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_188_LightsBane(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_188_LightsBane()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_189_Volcano(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_189_Volcano()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_066_TryInterceptingTarget(this, targetDir, targetVelocity, speed):
		x=getFunctionContents("Terraria.Projectile","private void AI_066_TryInterceptingTarget(Vector2 targetDir, Vector2 targetVelocity, float speed)")
		return keepOnlyContentsWhen(keepOnlyContentsWhen(keepOnlyContentsWhen(keepOnlyContentsWhen(x,"this.type",this.type)[0],"targetDir",targetDir)[0],"targetVelocity",targetVelocity)[0],"speed",speed)[0]
	def AI_187_ShadowHand(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_187_ShadowHand()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_187_ShadowHand_GetVariation(this, variation, fakeCounter, counterMax):
		x=getFunctionContents("Terraria.Projectile","private void AI_187_ShadowHand_GetVariation(out int variation, out float fakeCounter, out float counterMax)")
		return keepOnlyContentsWhen(keepOnlyContentsWhen(keepOnlyContentsWhen(keepOnlyContentsWhen(x,"this.type",this.type)[0],"variation",variation)[0],"fakeCounter",fakeCounter)[0],"counterMax",counterMax)[0]
	def AI_185_LifeDrain(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_185_LifeDrain()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_186_PrincessWeapon(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_186_PrincessWeapon()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_184_BadTorchLuck(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_184_BadTorchLuck()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_121_StardustDragon(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_121_StardustDragon()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_183_ZoologistStrike(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_183_ZoologistStrike()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_182_FinalFractal(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_182_FinalFractal()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_181_FairyQueenRangedItemShot(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_181_FairyQueenRangedItemShot()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_009_MagicMissiles(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_009_MagicMissiles()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_009_MagicMissiles_Old(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_009_MagicMissiles_Old()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_015_HandleMovementCollision(this, wetVelocity, lastVelocity):
		x=getFunctionContents("Terraria.Projectile","private void AI_015_HandleMovementCollision(ref Vector2 wetVelocity, ref Vector2 lastVelocity)")
		return keepOnlyContentsWhen(keepOnlyContentsWhen(keepOnlyContentsWhen(x,"this.type",this.type)[0],"wetVelocity",wetVelocity)[0],"lastVelocity",lastVelocity)[0]
	def AI_015_Flails(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_015_Flails()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_015_HandleMovementCollision_Old(this, wetVelocity, lastVelocity):
		x=getFunctionContents("Terraria.Projectile","private void AI_015_HandleMovementCollision_Old(ref Vector2 wetVelocity, ref Vector2 lastVelocity)")
		return keepOnlyContentsWhen(keepOnlyContentsWhen(keepOnlyContentsWhen(x,"this.type",this.type)[0],"wetVelocity",wetVelocity)[0],"lastVelocity",lastVelocity)[0]
	def AI_015_Flails_Old(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_015_Flails_Old()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_015_Flails_Dust(this, doFastThrowDust):
		x=getFunctionContents("Terraria.Projectile","private void AI_015_Flails_Dust(bool doFastThrowDust)")
		return keepOnlyContentsWhen(keepOnlyContentsWhen(x,"this.type",this.type)[0],"doFastThrowDust",doFastThrowDust)[0]
	def AI_100_Medusa(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_100_Medusa()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_120_StardustGuardian(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_120_StardustGuardian()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_120_StardustGuardian_FindTarget(this, lookupRange, targetNPCIndex, distanceToClosestTarget):
		x=getFunctionContents("Terraria.Projectile","private void AI_120_StardustGuardian_FindTarget(float lookupRange, ref int targetNPCIndex, ref float distanceToClosestTarget)")
		return keepOnlyContentsWhen(keepOnlyContentsWhen(keepOnlyContentsWhen(keepOnlyContentsWhen(x,"this.type",this.type)[0],"lookupRange",lookupRange)[0],"targetNPCIndex",targetNPCIndex)[0],"distanceToClosestTarget",distanceToClosestTarget)[0]
	def AI_180_FairyQueenSunDance(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_180_FairyQueenSunDance()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_179_FairyQueenLance(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_179_FairyQueenLance()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_176_EdgyLightning(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_176_EdgyLightning()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_177_IceWhipSlicer(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_177_IceWhipSlicer()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_178_FireExplosion(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_178_FireExplosion()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_175_TitaniumStormShards(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_175_TitaniumStormShards()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_174_MultisegmentPet(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_174_MultisegmentPet()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_173_HallowBossRainbowTrail(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_173_HallowBossRainbowTrail()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_171_HallowBossRainbowStreak(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_171_HallowBossRainbowStreak()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_172_HallowBossRainbowPelletStorm(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_172_HallowBossRainbowPelletStorm()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_170_FairyGlowstick(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_170_FairyGlowstick()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_169_Smolstars(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_169_Smolstars()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_019_Spears(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_019_Spears()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_019_Spears_Old(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_019_Spears_Old()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_168_FirstFractal(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_168_FirstFractal()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_167_SparkleGuitar(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_167_SparkleGuitar()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_164_StormTigerGem(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_164_StormTigerGem()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_162_TigerPounce(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_162_TigerPounce()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_016_Bombs(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_016_Bombs()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_166_Dove(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_166_Dove()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_161_RapierStabs(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_161_RapierStabs()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_165_Whip(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_165_Whip()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_160_Kites(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_160_Kites()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_159_PaperAirplanes(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_159_PaperAirplanes()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_158_BabyBird(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_158_BabyBird()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_067_FreakingPirates(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_067_FreakingPirates()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_067_FreakingPirates_TryJumpingToTarget(this, targetVelocity, toTarget, targetCenter):
		x=getFunctionContents("Terraria.Projectile","private void AI_067_FreakingPirates_TryJumpingToTarget(Vector2 targetVelocity, Vector2 toTarget, Vector2 targetCenter)")
		return keepOnlyContentsWhen(keepOnlyContentsWhen(keepOnlyContentsWhen(keepOnlyContentsWhen(x,"this.type",this.type)[0],"targetVelocity",targetVelocity)[0],"toTarget",toTarget)[0],"targetCenter",targetCenter)[0]
	def AI_067_FreakingPirates_HitIntention(this, idealPosition):
		x=getFunctionContents("Terraria.Projectile","private void AI_067_FreakingPirates_HitIntention(Vector2 idealPosition)")
		return keepOnlyContentsWhen(keepOnlyContentsWhen(x,"this.type",this.type)[0],"idealPosition",idealPosition)[0]
	def AI_067_FreakingPirates_TryAssigningHelp(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_067_FreakingPirates_TryAssigningHelp()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_157_SharpTears(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_157_SharpTears()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_156_BatOfLight(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_156_BatOfLight()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_156_Think(this, blacklist):
		x=getFunctionContents("Terraria.Projectile","private void AI_156_Think(List<int> blacklist)")
		return keepOnlyContentsWhen(keepOnlyContentsWhen(x,"this.type",this.type)[0],"blacklist",blacklist)[0]
	def AI_156_StartAttack(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_156_StartAttack()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_GetMyGroupIndexAndFillBlackList(this, blackListedTargets, index, totalIndexesInGroup):
		x=getFunctionContents("Terraria.Projectile","private void AI_GetMyGroupIndexAndFillBlackList(List<int> blackListedTargets, out int index, out int totalIndexesInGroup)")
		return keepOnlyContentsWhen(keepOnlyContentsWhen(keepOnlyContentsWhen(keepOnlyContentsWhen(x,"this.type",this.type)[0],"blackListedTargets",blackListedTargets)[0],"index",index)[0],"totalIndexesInGroup",totalIndexesInGroup)[0]
	def AI_156_GetIdlePosition(this, stackedIndex, totalIndexes, idleSpot, idleRotation):
		x=getFunctionContents("Terraria.Projectile","private void AI_156_GetIdlePosition(int stackedIndex, int totalIndexes, out Vector2 idleSpot, out float idleRotation)")
		return keepOnlyContentsWhen(keepOnlyContentsWhen(keepOnlyContentsWhen(keepOnlyContentsWhen(keepOnlyContentsWhen(x,"this.type",this.type)[0],"stackedIndex",stackedIndex)[0],"totalIndexes",totalIndexes)[0],"idleSpot",idleSpot)[0],"idleRotation",idleRotation)[0]
	def AI_155_MysticSnakeCoil(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_155_MysticSnakeCoil()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_155_RemoveRope(this, start, end):
		x=getFunctionContents("Terraria.Projectile","private void AI_155_RemoveRope(Point start, Point end)")
		return keepOnlyContentsWhen(keepOnlyContentsWhen(keepOnlyContentsWhen(x,"this.type",this.type)[0],"start",start)[0],"end",end)[0]
	def AI_155_SpawnRopeIn(this, x, y):
		x=getFunctionContents("Terraria.Projectile","private void AI_155_SpawnRopeIn(int x, int y)")
		return keepOnlyContentsWhen(keepOnlyContentsWhen(keepOnlyContentsWhen(x,"this.type",this.type)[0],"x",x)[0],"y",y)[0]
	def AI_154_VoidLens(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_154_VoidLens()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_153_ToiletPop(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_153_ToiletPop()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_198_Flint(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_198_Flint()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_198_Flint_EmitSpikes(this, startPosition, direction):
		x=getFunctionContents("Terraria.Projectile","private void AI_198_Flint_EmitSpikes(Vector2 startPosition, int direction)")
		return keepOnlyContentsWhen(keepOnlyContentsWhen(keepOnlyContentsWhen(x,"this.type",this.type)[0],"startPosition",startPosition)[0],"direction",direction)[0]
	def AI_150_GolfClubHelper(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_150_GolfClubHelper()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_007_GrapplingHooks(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_007_GrapplingHooks()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_147_Celeb2Rocket(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_147_Celeb2Rocket()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_148_StarSpawner(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_148_StarSpawner()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_147_Explosion(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_147_Explosion()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_163_Chum(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_163_Chum()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_061_FishingBobber(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_061_FishingBobber()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_061_FishingBobber_DoASplash(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_061_FishingBobber_DoASplash()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_061_FishingBobber_GiveItemToPlayer(this, thePlayer, itemType):
		x=getFunctionContents("Terraria.Projectile","private void AI_061_FishingBobber_GiveItemToPlayer(Player thePlayer, int itemType)")
		return keepOnlyContentsWhen(keepOnlyContentsWhen(keepOnlyContentsWhen(x,"this.type",this.type)[0],"thePlayer",thePlayer)[0],"itemType",itemType)[0]
	def AI_146_DD2Victory(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_146_DD2Victory()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_001(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_001()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_010(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_010()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_026(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_026()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_062(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_062()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_075(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_075()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_099_1_Counterweights(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_099_1_Counterweights()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_099_2_Yoyos(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_099_2_Yoyos()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_130_FlameBurstTower(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_130_FlameBurstTower()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_131_FlameBurstShot(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_131_FlameBurstShot()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_134_Ballista(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_134_Ballista()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_135_OgreStomp(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_135_OgreStomp()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_136_BetsyBreath(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_136_BetsyBreath()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_137_LightningAura(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_137_LightningAura()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_138_ExplosiveTrap(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_138_ExplosiveTrap()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_139_ExplosiveTrapExplosion(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_139_ExplosiveTrapExplosion()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_140_MonkStaffT1(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_140_MonkStaffT1()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_141_MonkStaffT1Explosion(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_141_MonkStaffT1Explosion()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_142_MonkStaffT2And3(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_142_MonkStaffT2And3()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_143_MonkStaffT2Ghast(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_143_MonkStaffT2Ghast()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_144_DD2Pet(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_144_DD2Pet()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	def AI_145_BookStaffStorm(this):
		x=getFunctionContents("Terraria.Projectile","private void AI_145_BookStaffStorm()")
		return keepOnlyContentsWhen(x,"this.type",this.type)[0]
	
	def fromTypeInd(typ):
		global tmpval
		tmpval=ProjectileHolder(typ)
		global calcBoolConditionwhenvarisval
		global currentvars
		currentvars={"x":None,"this":[tmpval][0],"true":True,"false":False,"Item":ItemMethods,"ItemID":ItemID,"null":None,"variant":None,"GameShaders":GameShadersMethods,"Main":Main,"SoundID":SoundID}
		def calcBoolConditionwhenvarisvalLocal(varname,value,cond):
			cond=cond.strip()
			global tmpval
			global currentvars
			try:
				if(findWhilstRespectingBrackets(cond,"&&")!=-1):
					s=splitWhilstRespectingBrackets(cond,"&&")
					a=calcBoolConditionwhenvarisvalLocal(varname,value,s[0])
					b=calcBoolConditionwhenvarisvalLocal(varname,value,"&&".join(s[1:]))
					if(a==False):
						return False
					if(b==False):
						return False
					if(a==True):
						if(b==True):
							return True
						else:
							return b
					else:
						if(b==True):
							return a
						else:
							return a+"&&"+b
				if(findWhilstRespectingBrackets(cond,"||")!=-1):
					s=splitWhilstRespectingBrackets(cond,"||")
					a=calcBoolConditionwhenvarisvalLocal(varname,value,s[0])
					b=calcBoolConditionwhenvarisvalLocal(varname,value,"||".join(s[1:]))
					if(a==True):
						return True
					if(b==True):
						return True
					if(a==False):
						if(b==False):
							return False
						else:
							return b
					else:
						if(b==False):
							return a
						else:
							return a+"||"+b
				if((cond[0]=="(")&(cond[-1]==")")):
					return calcBoolConditionwhenvarisvalLocal(varname,value,cond[1:-1])
				exec("x=((("+cond.replace("&&",")&(").replace("||",")|(").replace(varname,str(value))+")))",{},currentvars)
				return currentvars['x']
			except KeyboardInterrupt as e:
				print(cond)
				raise e
			except Exception:
				return cond
		calcBoolConditionwhenvarisval=calcBoolConditionwhenvarisvalLocal
		global callUsingThis
		def callUsingThisLocal(what):
			global tmpval
			global currentvars
			currentvars['this']=tmpval
			what=what.strip()
			what2=""
			for i in what:
				if((i=="f")&(what2[-1] in "0123456789")):
					pass
				else:
					what2+=i
			what=what2
			if(what[0:3]=="int"):
				what=what[4:]
			try:
				if("this.type =" in what.strip()):
					return None

				exec("x="+what.strip(),{},currentvars)
				tmpval=currentvars["this"]
			except KeyboardInterrupt as e:
				raise e
			except Exception:
				return None
			
			return None;
			
		callUsingThis=callUsingThisLocal
		x=getFunctionContents("Terraria.Projectile","void SetDefaults(int Type)")
		x=x[x.index("frameCounter"):]
		x=x[x.index(";")+2:]
		y=keepOnlyContentsWhen(x,"Type",typ,["Type",'this.type'])[0]
		tmpval.SetDefaultsMethod=y
		x=getFunctionContents("Terraria.Projectile","void AI()")
		y2=keepOnlyContentsWhen(x,"this.type",typ)[0]
		tmpval.AImethod=y2
		return [tmpval,y]
#Port C:/StuffAndThings/tmodloadercode/Terraria/Mount.cs
#public void SetMount(int m, Player mountedPlayer)
# to SetMount (Player player, ref bool skipDust)
#class PlayerMount:
#	
class MountDelegatesData:
	def __init__(this):
		this.MinecartDust=None;
		this.MinecartJumpingSound=None
		this.MinecartLandingSound=None
		this.MinecartBumperSound=None
		this.MouthPosition=None
		this.HandPosition=None
		this.PlayerSize=None
		this.DashDust=None
		#this.MinecartDust = DelegateMethods.Minecart.Sparks;
		#this.MinecartJumpingSound = DelegateMethods.Minecart.JumpingSound;
		#this.MinecartLandingSound = DelegateMethods.Minecart.LandingSound;
		#this.MinecartBumperSound = DelegateMethods.Minecart.BumperSound;
	
class MountData:
	def __init__(this):
		this.backTexture:Asset[Texture2D]=Asset[Texture2D].Empty
		this.backTextureGlow:Asset[Texture2D]=Asset[Texture2D].Empty
		this.backTextureExtra:Asset[Texture2D]=Asset[Texture2D].Empty
		this.backTextureExtraGlow:Asset[Texture2D]=Asset[Texture2D].Empty
		this.frontTexture:Asset[Texture2D]=Asset[Texture2D].Empty
		this.frontTextureGlow:Asset[Texture2D]=Asset[Texture2D].Empty
		this.frontTextureExtra:Asset[Texture2D]=Asset[Texture2D].Empty
		this.frontTextureExtraGlow:Asset[Texture2D]=Asset[Texture2D].Empty
		this.textureWidth:int=0# default value
		this.textureHeight:int=0# default value
		this.xOffset:int=0# default value
		this.yOffset:int=0# default value
		this.playerYOffsets:list[int]=None# default value
		this.bodyFrame:int=0# default value
		this.playerHeadOffset:int=0# default value
		this.heightBoost:int=0# default value
		this.buff:int=0# default value
		this.flightTimeMax:int=0# default value
		this.usesHover:bool=False# default value
		this.runSpeed:float=0# default value
		this.dashSpeed:float=0# default value
		this.swimSpeed:float=0# default value
		this.acceleration:float=0# default value
		this.jumpSpeed:float=0# default value
		this.jumpHeight:int=0# default value
		this.fallDamage:float=0# default value
		this.extraFall:int=0# default value
		this.fatigueMax:int=0# default value
		this.constantJump:bool=False# default value
		this.blockExtraJumps:bool=False# default value
		this.abilityChargeMax:int=0# default value
		this.abilityDuration:int=0# default value
		this.abilityCooldown:int=0# default value
		this.walkingGraceTimeMax:int=0# default value
		this.dismountsOnItemUse:bool=False# default value
		this.spawnDust:int=0# default value
		this.spawnDustNoGravity:bool=False# default value
		this.totalFrames:int=0# default value
		this.standingFrameStart:int=0# default value
		this.standingFrameCount:int=0# default value
		this.standingFrameDelay:int=0# default value
		this.runningFrameStart:int=0# default value
		this.runningFrameCount:int=0# default value
		this.runningFrameDelay:int=0# default value
		this.flyingFrameStart:int=0# default value
		this.flyingFrameCount:int=0# default value
		this.flyingFrameDelay:int=0# default value
		this.inAirFrameStart:int=0# default value
		this.inAirFrameCount:int=0# default value
		this.inAirFrameDelay:int=0# default value
		this.idleFrameStart:int=0# default value
		this.idleFrameCount:int=0# default value
		this.idleFrameDelay:int=0# default value
		this.idleFrameLoop:bool=False# default value
		this.swimFrameStart:int=0# default value
		this.swimFrameCount:int=0# default value
		this.swimFrameDelay:int=0# default value
		this.dashingFrameStart:int=0# default value
		this.dashingFrameCount:int=0# default value
		this.dashingFrameDelay:int=0# default value
		this.Minecart:bool=False# default value
		this.CanRideMinecartTracks:bool=False# default value
		this.CanUseWings:bool=False# default value
		this.lightColor:Vector3=Vector3.One
		this.emitsLight:bool=False# default value
		this.delegations:MountDelegatesData=MountDelegatesData()
		this.playerXOffset:int=0# default value
		this.UpdateFrameMethod=None#don't exist in terraria
		this.SetMountMethod=None
		this.UpdateEffectsMethod=None
import math as Math
class MountHolder:
	currentShader:int=0
	FrameStanding:int=0
	FrameRunning:int=1
	FrameInAir:int=2
	FrameFlying:int=3
	FrameSwimming:int=4
	FrameDashing:int=5
	DrawBack:int=0
	DrawBackExtra:int=1
	DrawFront:int=2
	DrawFrontExtra:int=3
	mounts:list[MountData]=None# default value
	scutlixEyePositions:list[Vector2]=None# default value
	scutlixTextureSize:Vector2=None# default value
	scutlixBaseDamage:int=50
	drillDiodePoint1:Vector2=Vector2(36, -6)
	drillDiodePoint2:Vector2=Vector2(36, 8)
	drillTextureSize:Vector2=None# default value
	drillTextureWidth:int=80
	drillRotationChange:float=Math.pi / 60
	drillPickPower:int=210
	drillPickTime:int=1
	amountOfBeamsAtOnce:int=2
	maxDrillLength:float=48
	santankTextureSize:Vector2=None# default value
	SuperCartRunSpeed:float=20
	SuperCartDashSpeed:float=20
	SuperCartAcceleration:float=0.1
	SuperCartJumpHeight:int=15
	SuperCartJumpSpeed:float=5.15
	idleFrames_Rat:list[int]=[
					0, 1, 3, 2, 3, 2, 3, 2, 1, 0,
					0
	]
	default=None
	def __init__(this):
		this._data:MountData=None# default value
		this._type:int=0# default value
		this._flipDraw:bool=False# default value
		this._frame:int=0# default value
		this._frameCounter:float=0# default value
		this._frameExtra:int=0# default value
		this._frameExtraCounter:float=0# default value
		this._frameState:int=0# default value
		this._flyTime:int=0# default value
		this._idleTime:int=0# default value
		this._idleTimeNext:int=0# default value
		this._fatigue:float=0# default value
		this._fatigueMax:float=0# default value
		this._abilityCharging:bool=False# default value
		this._abilityCharge:int=0# default value
		this._abilityCooldown:int=0# default value
		this._abilityDuration:int=0# default value
		this._abilityActive:bool=False# default value
		this._aiming:bool=False# default value
		this._shouldSuperCart:bool=False# default value
		this._walkingGraceTimeLeft:int=0# default value
		this._mountSpecificData:any=None# default value
		this._active:bool=False# default value
		this._defaultDelegatesData:MountDelegatesData=MountDelegatesData()

	@property
	def Active(this)->bool:
		return this._active
	@property
	def Type(this)->int:
		return this._type
	@property
	def Frame(this)->int:
		return this._frame
	@property
	def FlyTime(this)->int:
		return this._flyTime
	@property
	def BuffType(this)->int:
		return this._data.buff
	@property
	def BodyFrame(this)->int:
		return this._data.bodyFrame
	@property
	def XOffset(this)->int:
		return this._data.xOffset
	@property
	def YOffset(this)->int:
		return this._data.yOffset
	@property
	def RunningGraceTime(this)->int:
		return this._walkingGraceTimeLeft
	@property
	def PlayerXOFfset(this)->int:
		return this._data.playerXOffset
	@property
	def HeightBoost(this)->int:
		return this._data.heightBoost
	@property
	def ExtraFall(this)->int:
		return this._data.extraFall
	@property
	def FallDamage(this)->float:
		return this._data.fallDamage
	@property
	def AutoJump(this)->bool:
		return this._data.constantJump
	@property
	def BlockExtraJumps(this)->bool:
		return this._data.blockExtraJumps
	@property
	def Origin(this)->Vector2:
		return Vector2(this._data.textureWidth / 2, this._data.textureHeight / (2 * this._data.totalFrames))
	@property
	def AbilityCharging(this)->bool:
		return this._abilityCharging
	@property
	def AbilityActive(this)->bool:
		return this._abilityActive
	@property
	def AbilityCharge(this)->float:
		return this._abilityCharge / this._data.abilityChargeMax
	def SetAsChillet(newMount:MountData,buff:int,texture:Asset[Texture2D]):
		global currentvars
		currentvars["newMount"]=newMount
		currentvars["texture"]=texture
		currentvars["buff"]=buff
		x=getFunctionContents("Terraria.Mount","public static void SetAsChillet(MountData newMount, int buff, Asset<Texture2D> texture)")
		x=x.split("new int[")[0]+"".join(["[0 for i in range("+i[0][:i[1]-1]+")]"+i[0][i[1]:] for i in [[i,findLinkedBracket("["+i)] for i in x.split("new int[")[1:]]])
		keepOnlyContentsWhen(x,"thisisntavar",None)[0]
		currentvars['mountData']=currentvars["newMount"]
	def SetAsRollerSkate(newMount:MountData,buff:int):
		global currentvars
		currentvars["newMount"]=newMount
		currentvars["buff"]=buff
		x=getFunctionContents("Terraria.Mount","public static void SetAsRollerSkate(MountData newMount, int buff)")
		x=x.split("new int[")[0]+"".join(["[0 for i in range("+i[0][:i[1]-1]+")]"+i[0][i[1]:] for i in [[i,findLinkedBracket("["+i)] for i in x.split("new int[")[1:]]])
		currentvars['mountData']=currentvars["newMount"]
	def SetAsMinecart(newMount:MountData, buff:int, texture:Asset[Texture2D], verticalOffset:int = 0, playerVerticalOffset:int = 0):
		global currentvars
		currentvars["newMount"]=newMount
		currentvars["buff"]=buff
		currentvars["texture"]=texture
		currentvars["verticalOffset"]=verticalOffset
		currentvars["playerVerticalOffset"]=playerVerticalOffset
		x=getFunctionContents("Terraria.Mount","public static void SetAsMinecart(MountData newMount, int buff, Asset<Texture2D> texture, int verticalOffset = 0, int playerVerticalOffset = 0)")
		x=x.split("new int[")[0]+"".join(["[0 for i in range("+i[0][:i[1]-1]+")]"+i[0][i[1]:] for i in [[i,findLinkedBracket("["+i)] for i in x.split("new int[")[1:]]])
		
		keepOnlyContentsWhen(x,"thisisntavar",None)[0]
		v=vars(currentvars["newMount"])
		for i in v:
			vars(currentvars['mountData'])[i]=v[i]
	def UpdateFrame_Velociraptor(this, mountedPlayer, state):
		#print("UpdateFrame_Velociraptor")
		global currentvars
		currentvars['callmethodoutput']=None
		currentvars["state"]=state
		currentvars["mountedPlayer"]=mountedPlayer
		x=getFunctionContents("Terraria.Mount","public void UpdateFrame_Velociraptor(Player mountedPlayer, ref int state)")
		#print("a")
		currentvars['callmethodoutput']=x#keepOnlyContentsWhen(x,"thisisntavar",None)[0]
		#print("b")
	def fromTypeInd(typ,text=None):
		global tmpval
		tmpval=MountHolder()
		global calcBoolConditionwhenvarisval
		global currentvars
		
		def toUInt(value):
			if(value<0):
				return value+2147483648
			return value
		currentvars={"x":None,"this":[tmpval][0],"true":True,"false":False,"Item":ItemMethods,"ItemID":ItemID,"null":None,"variant":None,"GameShaders":GameShadersMethods,"Main":Main,"Mount":MountHolder,"MountData":MountData,"MountID":MountID,"MountDelegatesData":MountDelegatesData,"TextureAssets":TextureAssets,"Vector2":Vector2,"Vector3":Vector3,"Asset":Asset,"Texture2D":Texture2D,"toUInt":toUInt}
		def calcBoolConditionwhenvarisvalLocal(varname,value,cond,shortened=False):
			if(shortened==False):
				what2=""
				for i in cond:
					if((i in ["f","u"])&(what2[-1:] in [i for i in "0123456789"])):
						pass
					else:
						what2+=i
				cond=what2
				cond=cond.replace("(uint)","toUInt")
			cond=cond.strip()
			global tmpval
			global currentvars
			try:
				if(findWhilstRespectingBrackets(cond,"&&")!=-1):
					s=splitWhilstRespectingBrackets(cond,"&&")
					a=calcBoolConditionwhenvarisvalLocal(varname,value,s[0],True)
					b=calcBoolConditionwhenvarisvalLocal(varname,value,"&&".join(s[1:]),True)
					if(a==False):
						return False
					if(b==False):
						return False
					if(a==True):
						if(b==True):
							return True
						else:
							return b
					else:
						if(b==True):
							return a
						else:
							return a+"&&"+b
				if(findWhilstRespectingBrackets(cond,"||")!=-1):
					s=splitWhilstRespectingBrackets(cond,"||")
					a=calcBoolConditionwhenvarisvalLocal(varname,value,s[0],True)
					b=calcBoolConditionwhenvarisvalLocal(varname,value,"||".join(s[1:]),True)
					if(a==True):
						return True
					if(b==True):
						return True
					if(a==False):
						if(b==False):
							return False
						else:
							return b
					else:
						if(b==False):
							return a
						else:
							return a+"||"+b
				if((cond[0]=="(")&(cond[-1]==")")):
					return calcBoolConditionwhenvarisvalLocal(varname,value,cond[1:-1],True)
				exec("x=((("+cond.replace("&&",")&(").replace("||",")|(").replace(varname,str(value))+")))",{},currentvars)
				return currentvars['x']
			except KeyboardInterrupt as e:
				#print(cond)
				raise e
			except Exception as e:
				return cond
		calcBoolConditionwhenvarisval=calcBoolConditionwhenvarisvalLocal
		global callUsingThis
		def callUsingThisLocal(what):
			global tmpval
			global currentvars
			currentvars['callmethodoutput']=None
			currentvars['this']=tmpval
			what=what.strip()
			#if("UpdateFrame_Velociraptor" in what):
			#	print(what)
			what2=""
			for i in what:
				if((i=="f")&(what2[-1:] in [i for i in "0123456789"])):
					pass
				else:
					what2+=i
			what=what2
			if(what[0:3]=="int"):
				what=what[4:]
			try:
				if("this.type =" in what.strip()):
					return None
				exec(what.strip(),{},currentvars)
				tmpval=currentvars["this"]
				return currentvars['callmethodoutput']
			except KeyboardInterrupt as e:
				raise e
			except Exception as e:
				#print(str(e)[0:50])
				return None
			
			return None;
			
		callUsingThis=callUsingThisLocal
		#x=getFunctionContents("Terraria.Projectile","void SetDefaults(int Type)")
		#x=x[x.index("frameCounter"):]
		#x=x[x.index(";")+2:]
		#y=keepOnlyContentsWhen(x,"Type",typ,["Type",'this._type'])[0]
		#tmpval.SetDefaultsMethod=y
		tmpval=currentvars['this']
		tmpval._type=typ
		tmpval._idleTime=NonCompareable()
		tmpval._data=MountHolder.mounts[typ]
		#print(tmpval._idleTime)
		currentvars['this']=tmpval
		currentvars['mountedPlayer']=None
		currentvars['state']=NonCompareable()
		x=getFunctionContents("Terraria.Mount","public void UpdateFrame(Player mountedPlayer, int state, Vector2 velocity)").replace(" ref "," ")
		y2=keepOnlyContentsWhen(x,"this._type",typ,text=[text,0,0.33,1])[0]
		MountHolder.mounts[typ].UpdateFrameMethod=y2
		tmpval._type=-1
		tmpval._idleTime=NonCompareable()
		currentvars['mountedPlayer']=None
		x=getFunctionContents("Terraria.Mount","public void SetMount(int m, Player mountedPlayer)")
		y2=keepOnlyContentsWhen(x,"m",typ,text=[text,0.33,0.67,1])[0]
		MountHolder.mounts[typ].SetMountMethod=y2
		currentvars['mountedPlayer']=None
		currentvars['this']._type=typ
		x=getFunctionContents("Terraria.Mount","public void UpdateEffects(Player mountedPlayer)")
		y2=keepOnlyContentsWhen(x,"djfoadjsf0oij",None,["this._type"],text=[text,0.67,1,1])[0]
		MountHolder.mounts[typ].UpdateEffectsMethod=y2
		callUsingThis=callUsingThisRegular
		drawbar(0,1,"-")
		return tmpval
#public void UpdateFrame(Player mountedPlayer, int state, Vector2 velocity)
class jsstr(str):
	def __add__(self,other):
		return super().__add__(str(other))
	def __radd__(self,other):
		return super().__radd__(str(other))
def tojsstr(value:str):
	return jsstr(value)
import ast
class StringLiteralWrapper(ast.NodeTransformer):
	def visit_Constant(self, node):
		if isinstance(node,ast.Constant):
			#print("*",node.value)
			if(type(node.value)==type("5")):
				v=ast.Call(func=ast.Name(id="tojsstr",ctx=ast.Load(),lineno=node.lineno,col_offset=node.col_offset,end_lineno=node.end_lineno,end_col_offset=node.end_col_offset),args=[node],lineno=node.lineno,col_offset=node.col_offset,end_lineno=node.end_lineno,end_col_offset=node.end_col_offset)
				#print(v)
				return v
		return node
def callUsingThisRegular(whattocall):
	global currentvars
	currentvars["tojsstr"]=tojsstr
	whattocall=whattocall.strip()
	whattocall=whattocall.replace("(AssetRequestMode)","")
	whattocall=whattocall.replace("(int)","int")
	whattocall=whattocall.replace("(float)","")
	what2=""
	for i in whattocall:
		if((i=="f")&(what2[-1:] in ['0','1','2','3','4','5','6','7','8','9'])):
			pass
		else:
			what2+=i
	whattocall=what2
	try:
		if("=" in whattocall):
			s=splitWhilstRespectingBrackets(whattocall,"=")
			if(findWhilstRespectingBrackets(s[0].strip()," ")!=-1):
				if(s[0][-1]==" "):
					whattocall=s[0].split(" ")[-2]+"="+"=".join(s[1:])
					#print("-",whattocall)
			s=splitWhilstRespectingBrackets(whattocall,"=")
			if(s[1].strip()[0:3]=="new"):
				whattocall=s[0]+"= "+"=".join([s[1].strip()[4:]]+s[2:])
			s=splitWhilstRespectingBrackets(whattocall,"=")
			whattocall=s[0]+"= ["+"=".join(s[1:])+"][0]"
		whattocall=ast.parse(whattocall)
		StringLiteralWrapper().visit(whattocall)
		exec(compile(whattocall, filename="<ast>", mode="exec"),{},currentvars)
		#print("+",currentvars[x])
	except KeyboardInterrupt as e:
		raise e
	except Exception as e:
		#if("mountData" in whattocall):
		#	print(currentvars["mountData"],currentvars["mountData"].fallDamage)
		print("!","x="+ast.unparse(whattocall),type(e),str(e)[0:150])
		return None
	
	return None;
def calcformula(what):
	global currentvars
	what=what.strip()
	if(what[-1]=="f"):
		if(what[-2] in "0123456789"):
			what=what[:-1]
	if(what[0:3]=="int"):
		what=what[4:]
	try:
		exec("x="+what.strip(),{},currentvars)
		return currentvars['x']
	except KeyboardInterrupt as e:
		raise e
	except Exception as e:
		return None
	
	return None
callUsingThis=callUsingThisRegular
global logkeep
logkeep=False
#public void AI()
ItemHolder.default=ItemHolder(0)
def findLinkedBracket(content,brackets={"[":"]","{":"}","(":")"},start=0):
	"""
		Finds the brackets linked to the one at the very start, and gives an index. If not found, returns -1
	"""
	depth=""
	if(content[start] not in brackets):
		start+=1
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
def findWhilstRespectingBrackets(content,search,brackets={"[":"]","{":"}","(":")"},start=0):
	"""
		Finds the brackets linked to the one at the very start, and gives an index. If not found, returns -1
	"""
	depth=""
	i=start
	while(True):
		if(i>=content.__len__()):
			return -1
		if(content[i] in brackets):
			depth+=content[i]
		elif(depth.__len__()==0):
			if(content[i:i+search.__len__()]==search):
				return i
		elif(content[i]==brackets[depth[-1]]):
			depth=depth[:-1]
		i=i+1
	return i-1;
def splitWhilstRespectingBrackets(content,search,brackets={"[":"]","{":"}","(":")"}):
	"""
		Finds the brackets linked to the one at the very start, and gives an index. If not found, returns -1
	"""
	result=[""]
	depth=""
	i=0
	while(True):
		if(i>=content.__len__()):
			return result
		if(content[i] in brackets):
			depth+=content[i]
		elif(depth.__len__()!=0):
			if(content[i]==brackets[depth[-1]]):
				depth=depth[:-1]
		if((depth.__len__()==0)&(content[i:i+search.__len__()]==search)):
			result.append("")
			i+=search.__len__()-1
		else:
			result[-1]+=content[i]
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
	y=classname.split("$")
	x=y[0].split(".")
	y=y[1:]
	f=open("C:/StuffAndThings/tmodloadercode/"+".".join(x[:-1])+"/"+x[-1]+".cs")
	c=f.read()
	f.close()
	for z in y:
		c=c[c.index("class "+z):]
		c=c[c.index("{"):]
		c=c[1:findLinkedBracket(c)]
	if(varnamewithtype+";" in c):
		return ""
	c=c[c.index(varnamewithtype+" ")+varnamewithtype.__len__():].strip()
	c=c[2:c.index(";")]
	return c;
def getVariablesOfType(classname,vartype):
	y=classname.split("$")
	x=y[0].split(".")
	y=y[1:]
	f=open("C:/StuffAndThings/tmodloadercode/"+".".join(x[:-1])+"/"+x[-1]+".cs")
	c=f.read()
	f.close()
	for z in y:
		c=c[c.index("class "+z):]
		c=c[c.index("{"):]
		c=c[1:findLinkedBracket(c)]
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
def getFuncsStartingWith(classname,what):
	x=classname.split(".")
	f=open("C:/StuffAndThings/tmodloadercode/"+".".join(x[:-1])+"/"+x[-1]+".cs")
	c=f.read()
	f.close()
	d=[]
	while(what in c):
		c=c[c.index(what):].strip()
		e=c[:c.index("{")].strip()
		c=c[what.__len__():].strip()
		d.append(e)
	return d;
def calcBoolConditionwhenvarisvalNormal(varname,value,cond,shortened=False):
	if(shortened==False):
		what2=""
		for i in cond:
			if((i in ["f","u"])&(what2[-1:] in [i for i in "0123456789"])):
				pass
			else:
				what2+=i
		cond=what2
		cond=cond.replace("(uint)","toUInt")
	cond=cond.strip()
	global tmpval
	global currentvars
	try:
		if(findWhilstRespectingBrackets(cond,"&&")!=-1):
			s=splitWhilstRespectingBrackets(cond,"&&")
			a=calcBoolConditionwhenvarisval(varname,value,s[0],True)
			b=calcBoolConditionwhenvarisval(varname,value,"&&".join(s[1:]),True)
			if(a==False):
				return False
			if(b==False):
				return False
			if(a==True):
				if(b==True):
					return True
				else:
					return b
			else:
				if(b==True):
					return a
				else:
					return a+"&&"+b
		if(findWhilstRespectingBrackets(cond,"||")!=-1):
			s=splitWhilstRespectingBrackets(cond,"||")
			a=calcBoolConditionwhenvarisval(varname,value,s[0],True)
			b=calcBoolConditionwhenvarisval(varname,value,"||".join(s[1:]),True)
			if(a==True):
				return True
			if(b==True):
				return True
			if(a==False):
				if(b==False):
					return False
				else:
					return b
			else:
				if(b==False):
					return a
				else:
					return a+"||"+b
		if((cond[0]=="(")&(cond[-1]==")")):
			return calcBoolConditionwhenvarisval(varname,value,cond[1:-1],True)
		exec("x=((("+cond.replace("&&",")&(").replace("||",")|(").replace(varname,str(value))+")))",{},currentvars)
		return currentvars['x']
	except KeyboardInterrupt as e:
		print(cond)
		raise e
	except Exception as e:
		#print("^",str(e)[0:50])
		return cond
calcBoolConditionwhenvarisval=calcBoolConditionwhenvarisvalNormal
def getItemInitLines(itemtype:int):
	x=getFunctionContents("Terraria.Item","void SetDefaults(int Type, ItemVariant variant = null)")
	print(keepOnlyContentsWhen(x,"this.type",itemtype)[0])
class NonCompareable:
	def __eq__(self, other):
		raise Exception
def keepOnlyContentsWhenSwitchStatement(block,varname,value,swc,switchvarnames,text=None):
	
	b=findWhilstRespectingBrackets(block,"case "+swc+":")
	if(b!=-1):
		startind=b
	else:
		b=findWhilstRespectingBrackets(block,"default:")
		if(b!=-1):
			startind=b
		else:
			startind=-1
	if(startind==-1):
		return ["",False]
	newcontents=""
	block=block[startind:]
	c=0
	while(c<block.__len__()):
		if(text!=None):
			drawbar(text[1]+(text[2]-text[1])*c/block.__len__(),text[3],text[0])
		ind1=[block.index(";",c) if ";" in block[c:] else -1][0]
		ind2=[block.index("{",c) if "{" in block[c:] else -1][0]
		if(block[c:c+5] in [" case","case ","\ncase"]):
			c=block.index(":",c)+1
		elif(block[c:c+8]=="default:"):
			c=block.index(":",c)+1
		elif((ind1>=0)&((ind1<ind2)|(ind2<0))):
			#; first, not a block
			#print(block[c:ind1])
			if(block[c:ind1].strip()=="break"):
				break
			if(block[c:ind1].strip()=="return"):
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
			if(ind2==-1):
				ind2=findWhilstRespectingBrackets(block,"{",brackets={"(":")"},start=c)
			#a block!
			v=block[c:ind2].strip()
			if(v.__len__()==0):
				d=findLinkedBracket(block,start=c)
				if block[c]!="{":
					c=c+1
				a=keepOnlyContentsWhen(block[c+1:d],varname,value,switchvarnames,text=remapText(text,c,d-c-1,block.__len__()))
				b="{\n\t"+a[0].replace("\n","\n\t")+"\n}"
				newcontents+=b
				if(a[1]):
					return [newcontents,True]
				else:
					c=d+1
			elif(True in [v[0:9+i.__len__()]=="switch ("+i+")" for i in switchvarnames]):
				exec("x="+[i for i in switchvarnames if (v[0:9+i.__len__()]=="switch ("+i+")")][0],{},currentvars)
				b2=block[ind2+2:findLinkedBracket(block,start=ind2)]
				y=keepOnlyContentsWhenSwitchStatement(b2,varname,value,str(currentvars['x']),switchvarnames,text=remapText(text,c,b2.__len__(),block.__len__()))
				c=findLinkedBracket(block,start=ind2)+2
				if(y[0].__len__()>0):
					newcontents+=y[0]+"\n"
				if(y[1]):
					return [newcontents,True]
			elif(v[0:8]=="switch ("):
				y=block[ind2+2:findLinkedBracket(block,start=ind2)]
				
				y=[i for i in splitWhilstRespectingBrackets(y,"case")]
				y=[i for j in y for i in splitWhilstRespectingBrackets(j,"default")]
				y=[i for i in y if i.strip().__len__()!=0]
				yb=["case "+i.split(":")[0]+":" if i[0]!=":" else "default:" for i in y]
				y=[(":".join(i.split(":")[1:])).strip() for i in y]
				newcontents+=v+"\n{"
				nc=findLinkedBracket(block,start=ind2)+1
				for i in range(y.__len__()):
					newcontents+=yb[i]+"\n\t"+keepOnlyContentsWhen(y[i],varname,value,switchvarnames,text=remapText(text,c+(nc-c)*i/y.__len__(),y[i].__len__(),block.__len__()))[0].replace("\n","\n\t")
				newcontents+="}\n"
					
				c=nc
				
			elif(v[0:3]=="try"):
				newcontents+=v+"{\n\t"+block[ind2+1:findLinkedBracket(block,start=ind2)].replace("\n","\n\t")[:-1]+"}\n"
				c=findLinkedBracket(block,start=ind2)+2;
				ind2=block.find("{",c)
				v=block[c:ind2].strip()
				newcontents+=v+"{\n\t"+block[ind2+1:findLinkedBracket(block,start=ind2)].replace("\n","\n\t")[:-1]+"}\n"
				c=findLinkedBracket(block,start=ind2)+2;
			elif(v[0:4] in ["for ","for("]):
				#print("%",v)
				g=v[v.index("(")+1:-1].split(";")
				callUsingThis(g[0].replace("int ",""))
				a=block[ind2+1:findLinkedBracket(block,start=ind2)].replace("\n","\n\t")[:-1]
				g[1]=g[1].replace(".Length",".__len__()")
				conditionvalue=calcBoolConditionwhenvarisval("notavaleither","",g[1])
				while(conditionvalue == True):
					keepOnlyContentsWhen(a,"thisstillisntavar",None)
					callUsingThis(g[2].replace("++","+=1").strip())
					conditionvalue=calcBoolConditionwhenvarisval("notavaleither","",g[1])
				#print(conditionvalue)
				newcontents+="\n"+v+"{"+block[ind2+1:findLinkedBracket(block,start=ind2)].replace("\n","\n\t")[:-1]+"}\n"
				c=findLinkedBracket(block,start=ind2)+2;
			elif(v[0:3] in ["if ","if("]):
				n=calcBoolConditionwhenvarisval(varname,value,v[2:])
				if(type(n)==type("string")):
					b2=block[ind2+1:findLinkedBracket(block,start=ind2)]
					k=keepOnlyContentsWhen(b2,varname,value,switchvarnames,text=remapText(text,c,b2.__len__(),block.__len__()))
					for i in k[0].split(";"):
						if "}" in i:
							i=i[i.index("}")+1:].strip()
						i=i.strip()
						if "=" in i:
							callUsingThis(i[:i.index("=")]+"=None")
					newcontents+="if("+n+")"+"{"+k[0].replace("\n","\n\t")[:-1]+"}\n"
					c=findLinkedBracket(block,start=ind2)+2;
					if(block[c:c+7]=="else if"):
						newcontents+="else "
						c=c+5
					elif(block[c:c+4]=="else"):
						ind1=block.find(";",c)
						ind2=block.find("{",c)
						b2=block[ind2+1:findLinkedBracket(block,start=ind2)]
						k=keepOnlyContentsWhen(b2,varname,value,switchvarnames,text=remapText(text,c,b2.__len__(),block.__len__()))
						for i in k[0].split(";"):
							if "}" in i:
								i=i[i.index("}")+1:].strip()
							i=i.strip()
							if "=" in i:
								currentvars["NonComparable"]=NonCompareable
								callUsingThis(i[:i.index("=")]+"=NonComparable()")
						newcontents+="else{\n\t"+k[0].replace("\n","\n\t")[:-1]+"}\n"
						c=findLinkedBracket(block,start=ind2)+2;
				elif(n==True):
					b2=block[ind2+1:findLinkedBracket(block,start=ind2)]
					m=keepOnlyContentsWhen(b2,varname,value,switchvarnames,text=remapText(text,c,b2.__len__(),block.__len__()))
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
						b2=block[c+6:findLinkedBracket(block,start=c+5)]
						newcontents+=keepOnlyContentsWhen(b2,varname,value,switchvarnames,text=remapText(text,c,b2.__len__(),block.__len__()))[0]
						c=findLinkedBracket(block,start=c+5)+2
			else:
				print("line",[i for i in block[:c] if i=="\n"].__len__())
				print("v",v)
				#print(block)
				raise Exception()
	return [newcontents,False]
def remapText(text,currentpos,sectionlen,blocklen):
	if(text==None):
		return text
	return [text[0],text[1]+(text[2]-text[1])*currentpos/blocklen,text[1]+(text[2]-text[1])*(currentpos+sectionlen)/blocklen,text[3]]

def keepOnlyContentsWhen(block,varname,value,switchvarnames=None,text=None):
	global logkeep
	global currentvars
	try:
		exec(varname+"="+str(value),{},currentvars)
	except KeyboardInterrupt as e:
		raise e
	except Exception:
		pass
	if(switchvarnames==None):
		switchvarnames=[varname]
	targetval=value
	block="\n".join([i for i in [j.strip() for j in block.split("\n")] if i[0:2]!="//"])
	newcontents=""
	c=0
	lastc=-1
	while(c<block.__len__()):
		if(lastc==c):
			print("+",block)
			raise Exception()
		lastc=c
		if(text!=None):
			drawbar(text[1]+(text[2]-text[1])*c/block.__len__(),text[3],text[0])
		ind1=findWhilstRespectingBrackets(block,";",brackets={"(":")"},start=c)#block.find(";",c)
		if(ind1==-1):
			ind2=findWhilstRespectingBrackets(block,"{",brackets={"(":")"},start=c)
		else:
			ind2=findWhilstRespectingBrackets(block[:ind1],"{",brackets={"(":")"},start=c)
		if((ind1>=0)&((ind1<ind2)|(ind2<0))&(block[c:c+3]!="for")):
			#print(block[c:ind1])
			if(block[c:ind1].strip()=="break"):
				break
			if(block[c:ind1].strip()=="return"):
				return [newcontents,True]
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
			if(ind2==-1):
				ind2=findWhilstRespectingBrackets(block,"{",brackets={"(":")"},start=c)
			#a block!
			v=block[c:ind2].strip()
			if(v.__len__()==0):
				d=findLinkedBracket(block,start=c)
				a=keepOnlyContentsWhen(block[c+1:d],varname,value,switchvarnames,text=remapText(text,c,d-c-1,block.__len__()))
				b="{\n\t"+a[0].replace("\n","\n\t")+"\n}"
				newcontents+=b
				if(a[1]):
					return [newcontents,True]
				else:
					c=d+1
			elif(True in [v[0:9+i.__len__()]=="switch ("+i+")" for i in switchvarnames]):
				exec("x="+[i for i in switchvarnames if (v[0:9+i.__len__()]=="switch ("+i+")")][0],{},currentvars)
				b2=block[ind2+2:findLinkedBracket(block,start=ind2)]
				y=keepOnlyContentsWhenSwitchStatement(b2,varname,value,str(currentvars['x']),switchvarnames,text=remapText(text,c,b2.__len__(),block.__len__()))
				c=findLinkedBracket(block,start=ind2)+2
				if(y[0].__len__()>0):
					newcontents+=y[0]+"\n"
				if(y[1]):
					return [newcontents,True]
			elif(v[0:8]=="switch ("):
				y=block[ind2+2:findLinkedBracket(block,start=ind2)]
				
				y=[i for i in splitWhilstRespectingBrackets(y,"case")]
				y=[i for j in y for i in splitWhilstRespectingBrackets(j,"default")]
				y=[i for i in y if i.strip().__len__()!=0]
				yb=["case "+i.split(":")[0]+":" if i[0]!=":" else "default:" for i in y]
				y=[(":".join(i.split(":")[1:])).strip() for i in y]
				newcontents+=v+"\n{"
				nc=findLinkedBracket(block,start=ind2)+1
				for i in range(y.__len__()):
					newcontents+=yb[i]+"\n\t"+keepOnlyContentsWhen(y[i],varname,value,switchvarnames,text=remapText(text,c+(nc-c)*i/y.__len__(),y[i].__len__(),block.__len__()))[0].replace("\n","\n\t")
				newcontents+="}\n"
					
				c=nc
				
			elif(v[0:3]=="try"):
				newcontents+=v+"{\n\t"+block[ind2+1:findLinkedBracket(block,start=ind2)].replace("\n","\n\t")[:-1]+"}\n"
				c=findLinkedBracket(block,start=ind2)+2;
				ind2=block.find("{",c)

				v=block[c:ind2].strip()
				newcontents+=v+"{\n\t"+block[ind2+1:findLinkedBracket(block,start=ind2)].replace("\n","\n\t")[:-1]+"}\n"
				c=findLinkedBracket(block,start=ind2)+2;
			elif(v[0:4] in ["for ","for("]):
				#print("%",v)
				g=v[v.index("(")+1:-1].split(";")
				callUsingThis(g[0].replace("int ",""))
				a=block[ind2+1:findLinkedBracket(block,start=ind2)].replace("\n","\n\t")[:-1]
				if(g.__len__()==3):
					g[1]=g[1].replace(".Length",".__len__()")
					conditionvalue=calcBoolConditionwhenvarisval("notavaleither","",g[1])
					while(conditionvalue == True):
						keepOnlyContentsWhen(a,"thisstillisntavar",None)
						callUsingThis(g[2].replace("++","+=1").strip())
						conditionvalue=calcBoolConditionwhenvarisval("notavaleither","",g[1])
				#print(conditionvalue)
				newcontents+="\n"+v+"{"+block[ind2+1:findLinkedBracket(block,start=ind2)].replace("\n","\n\t")[:-1]+"}\n"
				c=findLinkedBracket(block,start=ind2)+2;
			elif(v[0:3] in ["if ","if("]):
				n=calcBoolConditionwhenvarisval(varname,value,v[2:])
				if(type(n)==type("string")):
					b2=block[ind2+1:findLinkedBracket(block,start=ind2)]
					k=keepOnlyContentsWhen(b2,varname,value,switchvarnames,text=remapText(text,c,b2.__len__(),block.__len__()))
					for i in k[0].split(";"):
						if "}" in i:
							i=i[i.index("}")+1:].strip()
						i=i.strip()
						if "=" in i:
							callUsingThis(i[:i.index("=")]+"=None")
					newcontents+="if("+n+")"+"{"+k[0].replace("\n","\n\t")[:-1]+"}\n"
					c=findLinkedBracket(block,start=ind2)+2;
					if(block[c:c+7]=="else if"):
						newcontents+="else "
						c=c+5
					elif(block[c:c+4]=="else"):
						ind1=block.find(";",c)
						ind2=block.find("{",c)
						b2=block[ind2+1:findLinkedBracket(block,start=ind2)]
						k=keepOnlyContentsWhen(b2,varname,value,switchvarnames,text=remapText(text,c,b2.__len__(),block.__len__()))
						for i in k[0].split(";"):
							if "}" in i:
								i=i[i.index("}")+1:].strip()
							i=i.strip()
							if "=" in i:
								currentvars["NonComparable"]=NonCompareable
								callUsingThis(i[:i.index("=")]+"=NonComparable()")
						newcontents+="else{\n\t"+k[0].replace("\n","\n\t")[:-1]+"}\n"
						c=findLinkedBracket(block,start=ind2)+2;
				elif(n==True):
					b2=block[ind2+1:findLinkedBracket(block,start=ind2)]
					m=keepOnlyContentsWhen(b2,varname,value,switchvarnames,text=remapText(text,c,b2.__len__(),block.__len__()))
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
						b2=block[c+6:findLinkedBracket(block,start=c+5)]
						newcontents+=keepOnlyContentsWhen(b2,varname,value,switchvarnames,text=remapText(text,c,b2.__len__(),block.__len__()))[0]
						c=findLinkedBracket(block,start=c+5)+2
			else:
				print("line",[i for i in block[:c] if i=="\n"].__len__())
				print("v",v)
				#print(block)
				raise Exception()
	return [newcontents,False]
def indexListFromBoolSetCreator(x):
	return [int(i.strip()) for i in x["Sets.Factory.CreateBoolSet(".__len__():-1].split(",")]
currIdCount=None
def BoolListFromBoolSetCreator(x):
	if("Sets.Factory.CreateBoolSet" in x):
		x=[i.strip() for i in x["Sets.Factory.CreateBoolSet(".__len__():-1].split(",")]
		if(x.__len__()>0):
			if(x[0]==""):
				x=[]
			if(x.__len__()>0):
				if(x[0]=="true"):
					x=[int(i) for i in x[1:]]
					return [False==(i in x) for i in range(currIdCount)]
				elif(x[0]=="false"):
					x=[int(i) for i in x[1:]]
					return [True==(i in x) for i in range(currIdCount)]
				else:
					x=[int(i) for i in x]
					return [True==(i in x) for i in range(currIdCount)]
		return [False for i in range(currIdCount)]
def IntListFromIntSetCreator(x):
	x=x.strip()
	if("Sets.Factory.CreateIntSet" in x):
		x=[i.strip() for i in x["Sets.Factory.CreateIntSet(".__len__():-1].split(",")]
		if(x.__len__()>0):
			if(x[0]==""):
				x=[]
			if(x.__len__()%2==0):
				x=[-1]+x
			if(x.__len__()>0):
				outlist=[int(x[0]) for i in range(currIdCount)]
				for i in range(1,x.__len__(),2):
					outlist[int(x[i])]=int(x[i+1])
				return outlist
	return [-1 for i in range(currIdCount)]
class PartiallyLoadedArray:
	def __init__(this,func,len):
		this.storedValues=[None for i in range(len)]
		this.func=func
	def __getitem__(this,ind):
		if(this.storedValues[ind]==None):
			this.storedValues[ind]=this.func(ind)
		return this.storedValues[ind]
class GameShadersMethods:
	class Armor:
		createShaderLines=[i.strip() for i in getFunctionContents("Terraria.Initializers.DyeInitializer","private static void LoadArmorDyes()").split(";")]
		shaderIdByItemId=[int(i[i.index("(")+1:i.index(",")]) for i in createShaderLines if "GameShaders.Armor.BindShader" in i]
		shaderInfoByShaderId=[i[i.index(",")+1:-1] for i in createShaderLines if "GameShaders.Armor.BindShader" in i]
		@classmethod
		def GetShaderIdFromItemId(cls,itemid):
			print(vars(cls)['shaderIdByItemId'])
			n=vars(cls)['shaderIdByItemId']
			if(itemid in n):
				return n.index(itemid)
			else:
				return -1
		print(createShaderLines)
	class Hair:
		createShaderLines=[i.strip() for i in splitWhilstRespectingBrackets(getFunctionContents("Terraria.Initializers.DyeInitializer","private static void LoadLegacyHairdyes()"),";")+splitWhilstRespectingBrackets(getFunctionContents("Terraria.Initializers.DyeInitializer","private static void LoadHairDyes()"),";")]
		shaderIdByItemId=[int(i[i.index("(")+1:i.index(",")]) for i in createShaderLines if "GameShaders.Hair.BindShader" in i]
		shaderInfoByShaderId=[i[i.index(",")+1:-2] for i in createShaderLines if "GameShaders.Hair.BindShader" in i]
		@classmethod
		def GetShaderIdFromItemId(cls,itemid):
			n=vars(cls)['shaderIdByItemId']
			if(itemid in n):
				return n.index(itemid)
			else:
				return -1
class ItemID:
	Count=6145
currIdCount=6145
class ItemID:
	Count=6145
	OldCount=5456
	itemsByName={int(getVariable("Terraria.ID.ItemID","const short "+i).strip()):i for i in getVariablesOfType("Terraria.ID.ItemID","const short")}
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
		TextureCopyLoad=IntListFromIntSetCreator(getVariable("Terraria.ID.ItemID","public static int[] TextureCopyLoad"))
		
class ProjectileID:
	Count=1111
class ProjectileID:
	Count=1111
	OldCount=1021
	projectilesByName={int(getVariable("Terraria.ID.ProjectileID","const short "+i).strip()):i for i in getVariablesOfType("Terraria.ID.ProjectileID","const short")}
	class Sets:
		pass
class BuffID:
	Count=389
class BuffID:
	Count=389
	OldCount=355
	buffsByName={int(getVariable("Terraria.ID.BuffID","const int "+i).strip()):i for i in getVariablesOfType("Terraria.ID.BuffID","const int")}
	class Sets:
		pass
class NPCID:
	Count=697
class NPCID:
	Count=697
	OldCount=689
	npcsByName={int(getVariable("Terraria.ID.NPCID","const short "+i).strip()):i for i in getVariablesOfType("Terraria.ID.NPCID","const short")}
	class Sets:
		pass
class TileID:
	Count=753
class TileID:
	Count=753
	OldCount=687
	tilesByName={int(getVariable("Terraria.ID.TileID","const ushort "+i).strip()):i for i in getVariablesOfType("Terraria.ID.TileID","const ushort")}
	class Sets:
		pass
class WallID:
	Count=367
class WallID:
	Count=367
	OldCount=341
	wallsByName={int(getVariable("Terraria.ID.WallID","const ushort "+i).strip()):i for i in getVariablesOfType("Terraria.ID.WallID","const ushort")}
	class Sets:
		pass
class NPCHeadID:
	Count=81
class NPCHeadID:
	Count=81
	OldCount=81
	headsByName={int(getVariable("Terraria.ID.NPCHeadID","const int "+i).strip()):i for i in getVariablesOfType("Terraria.ID.NPCHeadID","const int")}
	class Sets:
		pass
class ChainID:
	Count=17
	OldCount=17
	chainsByName={int(getVariable("Terraria.ID.ChainID","const short "+i).strip()):i for i in getVariablesOfType("Terraria.ID.ChainID","const short")}
class GoreID:
	Count=1407
	OldCount=1383
	goresByName={int(getVariable("Terraria.ID.GoreID","const int "+i).strip()):i for i in getVariablesOfType("Terraria.ID.GoreID","const int")}
	class Sets:
		pass
class GlowMaskID:
	Count=379
	OldCount=353
	masksByName={int(getVariable("Terraria.ID.GlowMaskID","const short "+i).strip()):i for i in getVariablesOfType("Terraria.ID.GlowMaskID","const short")}
	class Sets:
		pass
class ExtrasID:
	Count=304
	OldCount=266
	extrasByName={int(getVariable("Terraria.ID.ExtrasID","const short "+i).strip()):i for i in getVariablesOfType("Terraria.ID.ExtrasID","const short")}
class RecipeGroupID:
	Count=25
	groupsByName={int(getVariable("Terraria.ID.RecipeGroupID","static int "+i).strip()):i for i in getVariablesOfType("Terraria.ID.RecipeGroupID","static int")}
class CloudID:
	Count=41
	OldCount=41
	extrasByName={int(getVariable("Terraria.ID.CloudID","const int "+i).strip()):i for i in getVariablesOfType("Terraria.ID.CloudID","const int")}
class ArmorIDs:
	class Head:
		Count=293
		OldCount=282
		idsByName={int(getVariable("Terraria.ID.ArmorIDs$Head","const int "+i).strip()):i for i in getVariablesOfType("Terraria.ID.ArmorIDs$Head","const int")}
		class Sets:
			pass
	class Body:
		Count=262
		OldCount=248
		#idsByName={int(getVariable("Terraria.ID.ArmorIDs$Head","const int "+i).strip()):i for i in getVariablesOfType("Terraria.ID.ArmorIDs$Head","const int")}
		class Sets:
			pass
	class Legs:
		Count=254
		OldCount=236
		#idsByName={int(getVariable("Terraria.ID.ArmorIDs$Head","const int "+i).strip()):i for i in getVariablesOfType("Terraria.ID.ArmorIDs$Head","const int")}
		class Sets:
			pass
	class HandOn:
		Count=25
		OldCount=25
		#idsByName={int(getVariable("Terraria.ID.ArmorIDs$Head","const int "+i).strip()):i for i in getVariablesOfType("Terraria.ID.ArmorIDs$Head","const int")}
		class Sets:
			pass
	class HandOff:
		Count=16
		OldCount=16
		#idsByName={int(getVariable("Terraria.ID.ArmorIDs$Head","const int "+i).strip()):i for i in getVariablesOfType("Terraria.ID.ArmorIDs$Head","const int")}
		class Sets:
			pass
	class Back:
		Count=40
		OldCount=37
		#idsByName={int(getVariable("Terraria.ID.ArmorIDs$Head","const int "+i).strip()):i for i in getVariablesOfType("Terraria.ID.ArmorIDs$Head","const int")}
		class Sets:
			pass
	class Front:
		Count=17
		OldCount=13
		idsByName={int(getVariable("Terraria.ID.ArmorIDs$Front","const sbyte "+i).strip()):i for i in getVariablesOfType("Terraria.ID.ArmorIDs$Front","const sbyte")}
		class Sets:
			pass
	class Shoe:
		Count=31
		OldCount=27
		idsByName={int(getVariable("Terraria.ID.ArmorIDs$Shoe","const sbyte "+i).strip()):i for i in getVariablesOfType("Terraria.ID.ArmorIDs$Shoe","const sbyte")}
		class Sets:
			pass
	class Waist:
		Count=17
		OldCount=17
		idsByName={int(getVariable("Terraria.ID.ArmorIDs$Waist","const sbyte "+i).strip()):i for i in getVariablesOfType("Terraria.ID.ArmorIDs$Waist","const sbyte")}
		class Sets:
			pass
	class Wing:
		Count=52
		OldCount=47
		idsByName={int(getVariable("Terraria.ID.ArmorIDs$Wing","const sbyte "+i).strip()):i for i in getVariablesOfType("Terraria.ID.ArmorIDs$Wing","const sbyte")}
		class Sets:
			pass
	class Shield:
		Count=10
		OldCount=10
		idsByName={int(getVariable("Terraria.ID.ArmorIDs$Shield","const sbyte "+i).strip()):i for i in getVariablesOfType("Terraria.ID.ArmorIDs$Shield","const sbyte")}
	class Neck:
		Count=13
		OldCount=13
		idsByName={int(getVariable("Terraria.ID.ArmorIDs$Neck","const sbyte "+i).strip()):i for i in getVariablesOfType("Terraria.ID.ArmorIDs$Neck","const sbyte")}
		class Sets:
			pass
	class Face:
		Count=24
		OldCount=23
		idsByName={int(getVariable("Terraria.ID.ArmorIDs$Face","const sbyte "+i).strip()):i for i in getVariablesOfType("Terraria.ID.ArmorIDs$Face","const sbyte")}
		class Sets:
			pass
	class Balloon:
		Count=20
		OldCount=20
		idsByName={int(getVariable("Terraria.ID.ArmorIDs$Balloon","const sbyte "+i).strip()):i for i in getVariablesOfType("Terraria.ID.ArmorIDs$Balloon","const sbyte")}
		class Sets:
			pass
	class Beard:
		Count=5
		OldCount=5
		idsByName={int(getVariable("Terraria.ID.ArmorIDs$Beard","const sbyte "+i).strip()):i for i in getVariablesOfType("Terraria.ID.ArmorIDs$Beard","const sbyte")}
		class Sets:
			pass
class ExtrasID:
	Count=304
	mountsByName={int(getVariable("Terraria.ID.ExtrasID","const short "+i).strip()):i for i in getVariablesOfType("Terraria.ID.ExtrasID","const short")}
class MountID:
	Count=64
currIdCount=64
class MountID:
	Count=64
	OldCount=54
	mountsByName={int(getVariable("Terraria.ID.MountID","const int "+i).strip()):i for i in getVariablesOfType("Terraria.ID.MountID","const int")}
	class Sets:
		CanUseHooks=BoolListFromBoolSetCreator(getVariable("Terraria.ID.MountID","public static bool[] CanUseHooks"))
		CanDash=BoolListFromBoolSetCreator(getVariable("Terraria.ID.MountID","public static bool[] CanDash"))
		DoesNotOverrideBodyFrames=BoolListFromBoolSetCreator(getVariable("Terraria.ID.MountID","public static bool[] DoesNotOverrideBodyFrames"))
		DoesNotOverrideLegFrames=BoolListFromBoolSetCreator(getVariable("Terraria.ID.MountID","public static bool[] DoesNotOverrideLegFrames"))
		DoesNotOverrideBackpackDraw=BoolListFromBoolSetCreator(getVariable("Terraria.ID.MountID","public static bool[] DoesNotOverrideBackpackDraw"))
		IsRollerSkates=BoolListFromBoolSetCreator(getVariable("Terraria.ID.MountID","public static bool[] IsRollerSkates"))
		Cart=BoolListFromBoolSetCreator(getVariable("Terraria.ID.MountID","public static bool[] Cart"))
		IsTransformationMount=BoolListFromBoolSetCreator(getVariable("Terraria.ID.MountID","public static bool[] IsTransformationMount"))
		PlayerIsHidden=BoolListFromBoolSetCreator(getVariable("Terraria.ID.MountID","public static bool[] PlayerIsHidden"))
		DontHoldItems=BoolListFromBoolSetCreator(getVariable("Terraria.ID.MountID","public static bool[] DontHoldItems"))
		DontDismountWhenCCed=BoolListFromBoolSetCreator(getVariable("Terraria.ID.MountID","public static bool[] DontDismountWhenCCed"))
from enum import Enum
class SoundType(Enum):
	Sound=0
	Ambient=1
	Music=2
class SoundStyle:
	def __init__(this,*args):
		if(type(args[0])==SoundType):
			this.initb1(*args)
		else:
			this.inita1(*args)
	def inita1(this,volume:float,pitchVariance:float,type:SoundType = SoundType.Sound):
		this._volume:float = volume;
		this._pitchVariance:float = pitchVariance;
		this._type:SoundType = type;
	def initb1(this,type:SoundType = SoundType.Sound):
		this._volume:float = 1;
		this._pitchVariance:float = 0;
		this._type:SoundType = type;
	@property
	def Type(this):
		return this._type
	@property
	def Volume(this):
		return this._volume
	@property
	def PitchVariance(this):
		return this._pitchVariance
	

class LegacySoundStyle(SoundStyle):
	def __init__(this,*args):
		if(args.__len__()==2):
			this.inita(*args)
			return
		if(type(args[2])==type(SoundType.Sound)):
			this.inita(*args)
			return
		if(args.__len__()==7):
			this.initc(*args)
			return
		this.initb(*args)
	def inita(this,soundId:int, style:int, type:SoundType = SoundType.Sound, maxTrackedInstances:int = 0):
		this.initb1(type)
		this._style = style;
		this.Variations = 1;
		this.SoundId = soundId;
		this._maxTrackedInstances = maxTrackedInstances;
	

	def initb(this,soundId:int, style:int, variations:int, type:SoundType = SoundType.Sound, maxTrackedInstances:int = 0):
		this.initb1(type)
		this._style = style;
		this.Variations = variations;
		this.SoundId = soundId;
		this._maxTrackedInstances = maxTrackedInstances;
	

	def initc(this,soundId:int,style:int,variations:int,type:SoundType,volume:float,pitchVariance:float,maxTrackedInstances:int):
		this.inita1(volume,pitchVariance,type)
		this._style = style;
		this.Variations = variations;
		this.SoundId = soundId;
		this._maxTrackedInstances = maxTrackedInstances;
	def toString(this):
		import shutil
		s=SoundID.idsByName[this.SoundId]+"_"+str(this._style)
		s2=s if this.SoundId!=42 else "Custom\\"+SoundID._trackableLegacySoundPathList[this._style]
		shutil.copy("C:\\StuffAndThings\\Downloads\\TerrariaAssets_1_4_5_6\\Sounds\\"+s2+".wav", "C:\\Users\\neroa\\OneDrive\\Documents\\My Games\\Terraria\\tModLoader\\ModSources\\BiggerAndBoulderContentBackport\\Content\\Sounds\\"+s+".wav")
		s="new SoundStyle(\"BiggerAndBoulderContentBackport\\Content\\Sounds\\"+s+".wav\")"
		s=s.replace("\\","\\\\")
		if(this._volume!=1):
			s+="{Volume="+str(this._volume)+"f}"
		if(this._pitchVariance!=0):
			s+="{PitchVariance="+str(this._pitchVariance)+"f}"
		s=s.replace("}{",",")
		return s
	def WithVolume(this,volume:float):
		return LegacySoundStyle(this.SoundId, this._style, this.Variations, this.Type, volume, this.PitchVariance, this.MaxTrackedInstances)
	def WithPitchVariance(this,pitchVariance:float):
		return LegacySoundStyle(this.SoundId, this._style, this.Variations, this.Type, this.Volume, pitchVariance, this.MaxTrackedInstances)
	def AsMusic(this):
		return LegacySoundStyle(this.SoundId, this._style, this.Variations, SoundType.Music, this.Volume, this.PitchVariance, this.MaxTrackedInstances)
	def AsAmbient(this):
		return LegacySoundStyle(this.SoundId, this._style, this.Variations, SoundType.Ambient, this.Volume, this.PitchVariance, this.MaxTrackedInstances)
	def AsSound(this):
		return LegacySoundStyle(this.SoundId, this._style, this.Variations, SoundType.Sound, this.Volume, this.PitchVariance, this.MaxTrackedInstances)
	@property
	def MaxTrackedInstances(this):
		return this._maxTrackedInstances

class SoundStyleDefaults:
	PitchVariance:float
	Volume:float
	Type:SoundType
	def __init__(this,volume:float, pitchVariance:float, type:SoundType = SoundType.Sound):
		this.PitchVariance = pitchVariance
		this.Volume = volume
		this.Type = type
	
class SoundID:
	_trackableLegacySoundPathList:list[str]=[]
	def CreateTrackable(name:str,*args):
		if(args.__len__()==0):
			return SoundID.CreateTrackablec(name)
		if(type(args[0])==SoundStyleDefaults):
			return SoundID.CreateTrackablea(name,*args)
		if(type(args[0])==SoundType):
			return SoundID.CreateTrackablec(name,*args)
		if(args.__len__()==1):
			return SoundID.CreateTrackablec(name)
		if(type(args[1])==SoundStyleDefaults):
			return SoundID.CreateTrackableb(name,*args)
		if(type(args[1])==SoundType):
			return SoundID.CreateTrackabled(name,*args)
	def CreateTrackablea(name:str, defaults:SoundStyleDefaults, maxInstances:int = 0):
		return SoundID.CreateTrackabled(name, 1, defaults.Type, maxInstances).WithPitchVariance(defaults.PitchVariance).WithVolume(defaults.Volume);
	def CreateTrackableb(name:str, variations:int, defaults:SoundStyleDefaults, maxInstances:int = 0):
		return SoundID.CreateTrackabled(name, variations, defaults.Type, maxInstances).WithPitchVariance(defaults.PitchVariance).WithVolume(defaults.Volume);
	def CreateTrackablec(name:str, type:SoundType = SoundType.Sound, maxInstances:int = 0):
		return SoundID.CreateTrackabled(name, 1, type, maxInstances)
	def CreateTrackabled(name:str, variations:int, type:SoundType = SoundType.Sound, maxInstances:int = 0)->LegacySoundStyle:
		if (SoundID._trackableLegacySoundPathList == None):
			SoundID._trackableLegacySoundPathList = [];
		
		count:int = SoundID._trackableLegacySoundPathList.__len__();
		if (variations == 1):
			SoundID._trackableLegacySoundPathList.append(name)
		else:
			for i in range(0,variations,1):
				SoundID._trackableLegacySoundPathList.append(name + "_" + str(i))
		return LegacySoundStyle(42, count, variations, type, maxInstances)
	
	DD2_BetsyFireballShot:SoundStyle=None
	DD2_BetsyFireballImpact:SoundStyle=None
	ItemDefaults:SoundStyleDefaults = SoundStyleDefaults(1, 0.06)
SoundID.DD2_BetsyFireballShot=SoundID.CreateTrackable("dd2_betsy_fireball_shot", 3)
SoundID.DD2_BetsyFireballImpact=SoundID.CreateTrackable("dd2_betsy_fireball_impact", 3)
class SoundID:
	_trackableLegacySoundPathList:list[str]=SoundID._trackableLegacySoundPathList
	idsByName={int(getVariable("Terraria.ID.SoundID","const int "+i).strip()):i for i in getVariablesOfType("Terraria.ID.SoundID","const int")}
	NPCHit1:SoundStyle=LegacySoundStyle(3, 1)
	NPCHit2:SoundStyle=LegacySoundStyle(3, 2)
	NPCHit3:SoundStyle=LegacySoundStyle(3, 3)
	NPCHit4:SoundStyle=LegacySoundStyle(3, 4)
	NPCHit5:SoundStyle=LegacySoundStyle(3, 5)
	NPCHit6:SoundStyle=LegacySoundStyle(3, 6)
	NPCHit7:SoundStyle=LegacySoundStyle(3, 7)
	NPCHit8:SoundStyle=LegacySoundStyle(3, 8)
	NPCHit9:SoundStyle=LegacySoundStyle(3, 9)
	NPCHit10:SoundStyle=LegacySoundStyle(3, 10)
	NPCHit11:SoundStyle=LegacySoundStyle(3, 11)
	NPCHit12:SoundStyle=LegacySoundStyle(3, 12)
	NPCHit13:SoundStyle=LegacySoundStyle(3, 13)
	NPCHit14:SoundStyle=LegacySoundStyle(3, 14)
	NPCHit15:SoundStyle=LegacySoundStyle(3, 15)
	NPCHit16:SoundStyle=LegacySoundStyle(3, 16)
	NPCHit17:SoundStyle=LegacySoundStyle(3, 17)
	NPCHit18:SoundStyle=LegacySoundStyle(3, 18)
	NPCHit19:SoundStyle=LegacySoundStyle(3, 19)
	NPCHit20:SoundStyle=LegacySoundStyle(3, 20)
	NPCHit21:SoundStyle=LegacySoundStyle(3, 21)
	NPCHit22:SoundStyle=LegacySoundStyle(3, 22)
	NPCHit23:SoundStyle=LegacySoundStyle(3, 23)
	NPCHit24:SoundStyle=LegacySoundStyle(3, 24)
	NPCHit25:SoundStyle=LegacySoundStyle(3, 25)
	NPCHit26:SoundStyle=LegacySoundStyle(3, 26)
	NPCHit27:SoundStyle=LegacySoundStyle(3, 27)
	NPCHit28:SoundStyle=LegacySoundStyle(3, 28)
	NPCHit29:SoundStyle=LegacySoundStyle(3, 29)
	NPCHit30:SoundStyle=LegacySoundStyle(3, 30)
	NPCHit31:SoundStyle=LegacySoundStyle(3, 31)
	NPCHit32:SoundStyle=LegacySoundStyle(3, 32)
	NPCHit33:SoundStyle=LegacySoundStyle(3, 33)
	NPCHit34:SoundStyle=LegacySoundStyle(3, 34)
	NPCHit35:SoundStyle=LegacySoundStyle(3, 35)
	NPCHit36:SoundStyle=LegacySoundStyle(3, 36)
	NPCHit37:SoundStyle=LegacySoundStyle(3, 37)
	NPCHit38:SoundStyle=LegacySoundStyle(3, 38)
	NPCHit39:SoundStyle=LegacySoundStyle(3, 39)
	NPCHit40:SoundStyle=LegacySoundStyle(3, 40)
	NPCHit41:SoundStyle=LegacySoundStyle(3, 41)
	NPCHit42:SoundStyle=LegacySoundStyle(3, 42)
	NPCHit43:SoundStyle=LegacySoundStyle(3, 43)
	NPCHit44:SoundStyle=LegacySoundStyle(3, 44)
	NPCHit45:SoundStyle=LegacySoundStyle(3, 45)
	NPCHit46:SoundStyle=LegacySoundStyle(3, 46)
	NPCHit47:SoundStyle=LegacySoundStyle(3, 47)
	NPCHit48:SoundStyle=LegacySoundStyle(3, 48)
	NPCHit49:SoundStyle=LegacySoundStyle(3, 49)
	NPCHit50:SoundStyle=LegacySoundStyle(3, 50)
	NPCHit51:SoundStyle=LegacySoundStyle(3, 51)
	NPCHit52:SoundStyle=LegacySoundStyle(3, 52)
	NPCHit53:SoundStyle=LegacySoundStyle(3, 53)
	NPCHit54:SoundStyle=LegacySoundStyle(3, 54)
	NPCHit55:SoundStyle=LegacySoundStyle(3, 55)
	NPCHit56:SoundStyle=LegacySoundStyle(3, 56)
	NPCHit57:SoundStyle=LegacySoundStyle(3, 57)
	NPCHit58:SoundStyle=LegacySoundStyle(3, 58)
	NPCDeath1:SoundStyle=LegacySoundStyle(4, 1)
	NPCDeath2:SoundStyle=LegacySoundStyle(4, 2)
	NPCDeath3:SoundStyle=LegacySoundStyle(4, 3)
	NPCDeath4:SoundStyle=LegacySoundStyle(4, 4)
	NPCDeath5:SoundStyle=LegacySoundStyle(4, 5)
	NPCDeath6:SoundStyle=LegacySoundStyle(4, 6)
	NPCDeath7:SoundStyle=LegacySoundStyle(4, 7)
	NPCDeath8:SoundStyle=LegacySoundStyle(4, 8)
	NPCDeath9:SoundStyle=LegacySoundStyle(4, 9)
	NPCDeath10:SoundStyle=LegacySoundStyle(4, 10)
	NPCDeath11:SoundStyle=LegacySoundStyle(4, 11)
	NPCDeath12:SoundStyle=LegacySoundStyle(4, 12)
	NPCDeath13:SoundStyle=LegacySoundStyle(4, 13)
	NPCDeath14:SoundStyle=LegacySoundStyle(4, 14)
	NPCDeath15:SoundStyle=LegacySoundStyle(4, 15)
	NPCDeath16:SoundStyle=LegacySoundStyle(4, 16)
	NPCDeath17:SoundStyle=LegacySoundStyle(4, 17)
	NPCDeath18:SoundStyle=LegacySoundStyle(4, 18)
	NPCDeath19:SoundStyle=LegacySoundStyle(4, 19)
	NPCDeath20:SoundStyle=LegacySoundStyle(4, 20)
	NPCDeath21:SoundStyle=LegacySoundStyle(4, 21)
	NPCDeath22:SoundStyle=LegacySoundStyle(4, 22)
	NPCDeath23:SoundStyle=LegacySoundStyle(4, 23)
	NPCDeath24:SoundStyle=LegacySoundStyle(4, 24)
	NPCDeath25:SoundStyle=LegacySoundStyle(4, 25)
	NPCDeath26:SoundStyle=LegacySoundStyle(4, 26)
	NPCDeath27:SoundStyle=LegacySoundStyle(4, 27)
	NPCDeath28:SoundStyle=LegacySoundStyle(4, 28)
	NPCDeath29:SoundStyle=LegacySoundStyle(4, 29)
	NPCDeath30:SoundStyle=LegacySoundStyle(4, 30)
	NPCDeath31:SoundStyle=LegacySoundStyle(4, 31)
	NPCDeath32:SoundStyle=LegacySoundStyle(4, 32)
	NPCDeath33:SoundStyle=LegacySoundStyle(4, 33)
	NPCDeath34:SoundStyle=LegacySoundStyle(4, 34)
	NPCDeath35:SoundStyle=LegacySoundStyle(4, 35)
	NPCDeath36:SoundStyle=LegacySoundStyle(4, 36)
	NPCDeath37:SoundStyle=LegacySoundStyle(4, 37)
	NPCDeath38:SoundStyle=LegacySoundStyle(4, 38)
	NPCDeath39:SoundStyle=LegacySoundStyle(4, 39)
	NPCDeath40:SoundStyle=LegacySoundStyle(4, 40)
	NPCDeath41:SoundStyle=LegacySoundStyle(4, 41)
	NPCDeath42:SoundStyle=LegacySoundStyle(4, 42)
	NPCDeath43:SoundStyle=LegacySoundStyle(4, 43)
	NPCDeath44:SoundStyle=LegacySoundStyle(4, 44)
	NPCDeath45:SoundStyle=LegacySoundStyle(4, 45)
	NPCDeath46:SoundStyle=LegacySoundStyle(4, 46)
	NPCDeath47:SoundStyle=LegacySoundStyle(4, 47)
	NPCDeath48:SoundStyle=LegacySoundStyle(4, 48)
	NPCDeath49:SoundStyle=LegacySoundStyle(4, 49)
	NPCDeath50:SoundStyle=LegacySoundStyle(4, 50)
	NPCDeath51:SoundStyle=LegacySoundStyle(4, 51)
	NPCDeath52:SoundStyle=LegacySoundStyle(4, 52)
	NPCDeath53:SoundStyle=LegacySoundStyle(4, 53)
	NPCDeath54:SoundStyle=LegacySoundStyle(4, 54)
	NPCDeath55:SoundStyle=LegacySoundStyle(4, 55)
	NPCDeath56:SoundStyle=LegacySoundStyle(4, 56)
	NPCDeath57:SoundStyle=LegacySoundStyle(4, 57)
	NPCDeath58:SoundStyle=LegacySoundStyle(4, 58)
	NPCDeath59:SoundStyle=LegacySoundStyle(4, 59)
	NPCDeath60:SoundStyle=LegacySoundStyle(4, 60)
	NPCDeath61:SoundStyle=LegacySoundStyle(4, 61)
	NPCDeath62:SoundStyle=LegacySoundStyle(4, 62)
	NPCDeath63:SoundStyle=LegacySoundStyle(4, 63)
	NPCDeath64:SoundStyle=LegacySoundStyle(4, 64)
	NPCDeath65:SoundStyle=LegacySoundStyle(4, 65)
	NPCDeath66:SoundStyle=LegacySoundStyle(4, 66)
	NPCDeath67:SoundStyle=LegacySoundStyle(4, 67)
	NPCDeath68:SoundStyle=LegacySoundStyle(4, 68)
	Item1:SoundStyle=LegacySoundStyle(2, 1)
	Item2:SoundStyle=LegacySoundStyle(2, 2)
	Item3:SoundStyle=LegacySoundStyle(2, 3)
	Item4:SoundStyle=LegacySoundStyle(2, 4)
	Item5:SoundStyle=LegacySoundStyle(2, 5)
	Item6:SoundStyle=LegacySoundStyle(2, 6)
	Item7:SoundStyle=LegacySoundStyle(2, 7)
	Item8:SoundStyle=LegacySoundStyle(2, 8)
	Item9:SoundStyle=LegacySoundStyle(2, 9)
	Item10:SoundStyle=LegacySoundStyle(2, 10)
	Item11:SoundStyle=LegacySoundStyle(2, 11)
	Item12:SoundStyle=LegacySoundStyle(2, 12)
	Item13:SoundStyle=LegacySoundStyle(2, 13)
	Item14:SoundStyle=LegacySoundStyle(2, 14)
	Item15:SoundStyle=LegacySoundStyle(2, 15)
	Item16:SoundStyle=LegacySoundStyle(2, 16)
	Item17:SoundStyle=LegacySoundStyle(2, 17)
	Item18:SoundStyle=LegacySoundStyle(2, 18)
	Item19:SoundStyle=LegacySoundStyle(2, 19)
	Item20:SoundStyle=LegacySoundStyle(2, 20)
	Item21:SoundStyle=LegacySoundStyle(2, 21)
	Item22:SoundStyle=LegacySoundStyle(2, 22)
	Item23:SoundStyle=LegacySoundStyle(2, 23)
	Item24:SoundStyle=LegacySoundStyle(2, 24)
	Item25:SoundStyle=LegacySoundStyle(2, 25)
	Item26:SoundStyle=LegacySoundStyle(2, 26)
	Item27:SoundStyle=LegacySoundStyle(2, 27)
	Item28:SoundStyle=LegacySoundStyle(2, 28)
	Item29:SoundStyle=LegacySoundStyle(2, 29)
	Item30:SoundStyle=LegacySoundStyle(2, 30)
	Item31:SoundStyle=LegacySoundStyle(2, 31)
	Item32:SoundStyle=LegacySoundStyle(2, 32)
	Item33:SoundStyle=LegacySoundStyle(2, 33)
	Item34:SoundStyle=LegacySoundStyle(2, 34)
	Item35:SoundStyle=LegacySoundStyle(2, 35)
	Item36:SoundStyle=LegacySoundStyle(2, 36)
	Item37:SoundStyle=LegacySoundStyle(2, 37)
	Item38:SoundStyle=LegacySoundStyle(2, 38)
	Item39:SoundStyle=LegacySoundStyle(2, 39)
	Item40:SoundStyle=LegacySoundStyle(2, 40)
	Item41:SoundStyle=LegacySoundStyle(2, 41)
	Item42:SoundStyle=LegacySoundStyle(2, 42)
	Item43:SoundStyle=LegacySoundStyle(2, 43)
	Item44:SoundStyle=LegacySoundStyle(2, 44)
	Item45:SoundStyle=LegacySoundStyle(2, 45)
	Item46:SoundStyle=LegacySoundStyle(2, 46)
	Item47:SoundStyle=LegacySoundStyle(2, 47)
	Item48:SoundStyle=LegacySoundStyle(2, 48)
	Item49:SoundStyle=LegacySoundStyle(2, 49)
	Item50:SoundStyle=LegacySoundStyle(2, 50)
	Item51:SoundStyle=LegacySoundStyle(2, 51)
	Item52:SoundStyle=LegacySoundStyle(2, 52)
	Item53:SoundStyle=LegacySoundStyle(2, 53)
	Item54:SoundStyle=LegacySoundStyle(2, 54)
	Item55:SoundStyle=LegacySoundStyle(2, 55)
	Item56:SoundStyle=LegacySoundStyle(2, 56)
	Item57:SoundStyle=LegacySoundStyle(2, 57)
	Item58:SoundStyle=LegacySoundStyle(2, 58)
	Item59:SoundStyle=LegacySoundStyle(2, 59)
	Item60:SoundStyle=LegacySoundStyle(2, 60)
	Item61:SoundStyle=LegacySoundStyle(2, 61)
	Item62:SoundStyle=LegacySoundStyle(2, 62)
	Item63:SoundStyle=LegacySoundStyle(2, 63)
	Item64:SoundStyle=LegacySoundStyle(2, 64)
	Item65:SoundStyle=LegacySoundStyle(2, 65)
	Item66:SoundStyle=LegacySoundStyle(2, 66)
	Item67:SoundStyle=LegacySoundStyle(2, 67)
	Item68:SoundStyle=LegacySoundStyle(2, 68)
	Item69:SoundStyle=LegacySoundStyle(2, 69)
	Item70:SoundStyle=LegacySoundStyle(2, 70)
	Item71:SoundStyle=LegacySoundStyle(2, 71)
	Item72:SoundStyle=LegacySoundStyle(2, 72)
	Item73:SoundStyle=LegacySoundStyle(2, 73)
	Item74:SoundStyle=LegacySoundStyle(2, 74)
	Item75:SoundStyle=LegacySoundStyle(2, 75)
	Item76:SoundStyle=LegacySoundStyle(2, 76)
	Item77:SoundStyle=LegacySoundStyle(2, 77)
	Item78:SoundStyle=LegacySoundStyle(2, 78)
	Item79:SoundStyle=LegacySoundStyle(2, 79)
	Item80:SoundStyle=LegacySoundStyle(2, 80)
	Item81:SoundStyle=LegacySoundStyle(2, 81)
	Item82:SoundStyle=LegacySoundStyle(2, 82)
	Item83:SoundStyle=LegacySoundStyle(2, 83)
	Item84:SoundStyle=LegacySoundStyle(2, 84)
	Item85:SoundStyle=LegacySoundStyle(2, 85)
	Item86:SoundStyle=LegacySoundStyle(2, 86)
	Item87:SoundStyle=LegacySoundStyle(2, 87)
	Item88:SoundStyle=LegacySoundStyle(2, 88)
	Item89:SoundStyle=LegacySoundStyle(2, 89)
	Item90:SoundStyle=LegacySoundStyle(2, 90)
	Item91:SoundStyle=LegacySoundStyle(2, 91)
	Item92:SoundStyle=LegacySoundStyle(2, 92)
	Item93:SoundStyle=LegacySoundStyle(2, 93)
	Item94:SoundStyle=LegacySoundStyle(2, 94)
	Item95:SoundStyle=LegacySoundStyle(2, 95)
	Item96:SoundStyle=LegacySoundStyle(2, 96)
	Item97:SoundStyle=LegacySoundStyle(2, 97)
	Item98:SoundStyle=LegacySoundStyle(2, 98)
	Item99:SoundStyle=LegacySoundStyle(2, 99)
	Item100:SoundStyle=LegacySoundStyle(2, 100)
	Item101:SoundStyle=LegacySoundStyle(2, 101)
	Item102:SoundStyle=LegacySoundStyle(2, 102)
	Item103:SoundStyle=LegacySoundStyle(2, 103)
	Item104:SoundStyle=LegacySoundStyle(2, 104)
	Item105:SoundStyle=LegacySoundStyle(2, 105)
	Item106:SoundStyle=LegacySoundStyle(2, 106)
	Item107:SoundStyle=LegacySoundStyle(2, 107)
	Item108:SoundStyle=LegacySoundStyle(2, 108)
	Item109:SoundStyle=LegacySoundStyle(2, 109)
	Item110:SoundStyle=LegacySoundStyle(2, 110)
	Item111:SoundStyle=LegacySoundStyle(2, 111)
	Item112:SoundStyle=LegacySoundStyle(2, 112)
	Item113:SoundStyle=LegacySoundStyle(2, 113)
	Item114:SoundStyle=LegacySoundStyle(2, 114)
	Item115:SoundStyle=LegacySoundStyle(2, 115)
	Item116:SoundStyle=LegacySoundStyle(2, 116)
	Item117:SoundStyle=LegacySoundStyle(2, 117)
	Item118:SoundStyle=LegacySoundStyle(2, 118)
	Item119:SoundStyle=LegacySoundStyle(2, 119)
	Item120:SoundStyle=LegacySoundStyle(2, 120)
	Item121:SoundStyle=LegacySoundStyle(2, 121)
	Item122:SoundStyle=LegacySoundStyle(2, 122)
	Item123:SoundStyle=LegacySoundStyle(2, 123)
	Item124:SoundStyle=LegacySoundStyle(2, 124)
	Item125:SoundStyle=LegacySoundStyle(2, 125)
	Item126:SoundStyle=LegacySoundStyle(2, 126)
	Item127:SoundStyle=LegacySoundStyle(2, 127)
	Item128:SoundStyle=LegacySoundStyle(2, 128)
	Item129:SoundStyle=LegacySoundStyle(2, 129)
	Item130:SoundStyle=LegacySoundStyle(2, 130)
	Item131:SoundStyle=LegacySoundStyle(2, 131)
	Item132:SoundStyle=LegacySoundStyle(2, 132)
	Item133:SoundStyle=LegacySoundStyle(2, 133)
	Item134:SoundStyle=LegacySoundStyle(2, 134)
	Item135:SoundStyle=LegacySoundStyle(2, 135)
	Item136:SoundStyle=LegacySoundStyle(2, 136)
	Item137:SoundStyle=LegacySoundStyle(2, 137)
	Item138:SoundStyle=LegacySoundStyle(2, 138)
	Item139:SoundStyle=LegacySoundStyle(2, 139)
	Item140:SoundStyle=LegacySoundStyle(2, 140)
	Item141:SoundStyle=LegacySoundStyle(2, 141)
	Item142:SoundStyle=LegacySoundStyle(2, 142)
	Item143:SoundStyle=LegacySoundStyle(2, 143)
	Item144:SoundStyle=LegacySoundStyle(2, 144)
	Item145:SoundStyle=LegacySoundStyle(2, 145)
	Item146:SoundStyle=LegacySoundStyle(2, 146)
	Item147:SoundStyle=LegacySoundStyle(2, 147)
	Item148:SoundStyle=LegacySoundStyle(2, 148)
	Item149:SoundStyle=LegacySoundStyle(2, 149)
	Item150:SoundStyle=LegacySoundStyle(2, 150)
	Item151:SoundStyle=LegacySoundStyle(2, 151)
	Item152:SoundStyle=LegacySoundStyle(2, 152)
	Item153:SoundStyle=LegacySoundStyle(2, 153)
	Item154:SoundStyle=LegacySoundStyle(2, 154)
	Item155:SoundStyle=LegacySoundStyle(2, 155)
	Item156:SoundStyle=LegacySoundStyle(2, 156)
	Item157:SoundStyle=LegacySoundStyle(2, 157)
	Item158:SoundStyle=LegacySoundStyle(2, 158)
	Item159:SoundStyle=LegacySoundStyle(2, 159)
	Item160:SoundStyle=LegacySoundStyle(2, 160)
	Item161:SoundStyle=LegacySoundStyle(2, 161)
	Item162:SoundStyle=LegacySoundStyle(2, 162)
	Item163:SoundStyle=LegacySoundStyle(2, 163)
	Item164:SoundStyle=LegacySoundStyle(2, 164)
	Item165:SoundStyle=LegacySoundStyle(2, 165)
	Item166:SoundStyle=LegacySoundStyle(2, 166)
	Item167:SoundStyle=LegacySoundStyle(2, 167)
	Item168:SoundStyle=LegacySoundStyle(2, 168)
	Item169:SoundStyle=LegacySoundStyle(2, 169)
	Item170:SoundStyle=LegacySoundStyle(2, 170)
	Item171:SoundStyle=LegacySoundStyle(2, 171)
	Item172:SoundStyle=LegacySoundStyle(2, 172)
	Item173:SoundStyle=LegacySoundStyle(2, 173)
	Item174:SoundStyle=LegacySoundStyle(2, 174)
	Item175:SoundStyle=LegacySoundStyle(2, 175)
	Item176:SoundStyle=LegacySoundStyle(2, 176)
	Item177:SoundStyle=LegacySoundStyle(2, 177)
	Item178:SoundStyle=LegacySoundStyle(2, 178)
	Item179:SoundStyle=LegacySoundStyle(2, 179).WithVolume(0.6)
	Item180:SoundStyle=LegacySoundStyle(2, 180)
	Item181:SoundStyle=LegacySoundStyle(2, 181)
	Item182:SoundStyle=LegacySoundStyle(2, 182)
	Item183:SoundStyle=LegacySoundStyle(2, 183)
	Item184:SoundStyle=LegacySoundStyle(2, 184)
	Item185:SoundStyle=LegacySoundStyle(2, 185)
	Item186:SoundStyle=LegacySoundStyle(2, 186)
	Item187:SoundStyle=LegacySoundStyle(2, 187)
	Item188:SoundStyle=LegacySoundStyle(2, 188)
	Item189:SoundStyle=LegacySoundStyle(2, 189)
	Item190:SoundStyle=LegacySoundStyle(2, 190)
	Item191:SoundStyle=LegacySoundStyle(2, 191)
	Item192:SoundStyle=LegacySoundStyle(2, 192)
	Item193:SoundStyle=LegacySoundStyle(2, 193)
	Item194:SoundStyle=LegacySoundStyle(2, 194)
	Item195:SoundStyle=LegacySoundStyle(2, 195)
	Item196:SoundStyle=LegacySoundStyle(2, 196)
	Item197:SoundStyle=LegacySoundStyle(2, 197)
	Item198:SoundStyle=LegacySoundStyle(2, 198)
	Item199:SoundStyle=LegacySoundStyle(2, 199)
	DD2_GoblinBomb:SoundStyle=LegacySoundStyle(2, 14).WithVolume(0.5)
	AchievementComplete:SoundStyle=SoundID.CreateTrackable("achievement_complete")
	BlizzardInsideBuildingLoop:SoundStyle=SoundID.CreateTrackable("blizzard_inside_building_loop", SoundType.Ambient)
	BlizzardStrongLoop:SoundStyle=SoundID.CreateTrackable("blizzard_strong_loop", SoundType.Ambient).WithVolume(0.5)
	LiquidsHoneyWater:SoundStyle=SoundID.CreateTrackable("liquids_honey_water", 3, SoundType.Ambient)
	LiquidsHoneyLava:SoundStyle=SoundID.CreateTrackable("liquids_honey_lava", 3, SoundType.Ambient)
	LiquidsWaterLava:SoundStyle=SoundID.CreateTrackable("liquids_water_lava", 3, SoundType.Ambient)
	DD2_BallistaTowerShot:SoundStyle=SoundID.CreateTrackable("dd2_ballista_tower_shot", 3)
	DD2_ExplosiveTrapExplode:SoundStyle=SoundID.CreateTrackable("dd2_explosive_trap_explode", 3)
	DD2_FlameburstTowerShot:SoundStyle=SoundID.CreateTrackable("dd2_flameburst_tower_shot", 3, SoundType.Sound, 6)
	DD2_LightningAuraZap:SoundStyle=SoundID.CreateTrackable("dd2_lightning_aura_zap", 4)
	DD2_DefenseTowerSpawn:SoundStyle=SoundID.CreateTrackable("dd2_defense_tower_spawn")
	DD2_BetsyDeath:SoundStyle=SoundID.CreateTrackable("dd2_betsy_death", 3)
	DD2_BetsyFireballShot:SoundStyle=SoundID.DD2_BetsyFireballShot
	DD2_BetsyFireballImpact:SoundStyle=SoundID.DD2_BetsyFireballImpact
	DD2_BetsyFlameBreath:SoundStyle=SoundID.CreateTrackable("dd2_betsy_flame_breath")
	DD2_BetsyFlyingCircleAttack:SoundStyle=SoundID.CreateTrackable("dd2_betsy_flying_circle_attack")
	DD2_BetsyHurt:SoundStyle=SoundID.CreateTrackable("dd2_betsy_hurt", 3)
	DD2_BetsyScream:SoundStyle=SoundID.CreateTrackable("dd2_betsy_scream")
	DD2_BetsySummon:SoundStyle=SoundID.CreateTrackable("dd2_betsy_summon", 3)
	DD2_BetsyWindAttack:SoundStyle=SoundID.CreateTrackable("dd2_betsy_wind_attack", 3)
	DD2_DarkMageAttack:SoundStyle=SoundID.CreateTrackable("dd2_dark_mage_attack", 3)
	DD2_DarkMageCastHeal:SoundStyle=SoundID.CreateTrackable("dd2_dark_mage_cast_heal", 3)
	DD2_DarkMageDeath:SoundStyle=SoundID.CreateTrackable("dd2_dark_mage_death", 3)
	DD2_DarkMageHealImpact:SoundStyle=SoundID.CreateTrackable("dd2_dark_mage_heal_impact", 3)
	DD2_DarkMageHurt:SoundStyle=SoundID.CreateTrackable("dd2_dark_mage_hurt", 3)
	DD2_DarkMageSummonSkeleton:SoundStyle=SoundID.CreateTrackable("dd2_dark_mage_summon_skeleton", 3)
	DD2_DrakinBreathIn:SoundStyle=SoundID.CreateTrackable("dd2_drakin_breath_in", 3)
	DD2_DrakinDeath:SoundStyle=SoundID.CreateTrackable("dd2_drakin_death", 3)
	DD2_DrakinHurt:SoundStyle=SoundID.CreateTrackable("dd2_drakin_hurt", 3)
	DD2_DrakinShot:SoundStyle=SoundID.CreateTrackable("dd2_drakin_shot", 3)
	DD2_GoblinDeath:SoundStyle=SoundID.CreateTrackable("dd2_goblin_death", 3)
	DD2_GoblinHurt:SoundStyle=SoundID.CreateTrackable("dd2_goblin_hurt", 6)
	DD2_GoblinScream:SoundStyle=SoundID.CreateTrackable("dd2_goblin_scream", 3)
	DD2_GoblinBomberDeath:SoundStyle=SoundID.CreateTrackable("dd2_goblin_bomber_death", 3)
	DD2_GoblinBomberHurt:SoundStyle=SoundID.CreateTrackable("dd2_goblin_bomber_hurt", 3)
	DD2_GoblinBomberScream:SoundStyle=SoundID.CreateTrackable("dd2_goblin_bomber_scream", 3)
	DD2_GoblinBomberThrow:SoundStyle=SoundID.CreateTrackable("dd2_goblin_bomber_throw", 3)
	DD2_JavelinThrowersAttack:SoundStyle=SoundID.CreateTrackable("dd2_javelin_throwers_attack", 3)
	DD2_JavelinThrowersDeath:SoundStyle=SoundID.CreateTrackable("dd2_javelin_throwers_death", 3)
	DD2_JavelinThrowersHurt:SoundStyle=SoundID.CreateTrackable("dd2_javelin_throwers_hurt", 3)
	DD2_JavelinThrowersTaunt:SoundStyle=SoundID.CreateTrackable("dd2_javelin_throwers_taunt", 3)
	DD2_KoboldDeath:SoundStyle=SoundID.CreateTrackable("dd2_kobold_death", 3)
	DD2_KoboldExplosion:SoundStyle=SoundID.CreateTrackable("dd2_kobold_explosion", 3)
	DD2_KoboldHurt:SoundStyle=SoundID.CreateTrackable("dd2_kobold_hurt", 3)
	DD2_KoboldIgnite:SoundStyle=SoundID.CreateTrackable("dd2_kobold_ignite")
	DD2_KoboldIgniteLoop:SoundStyle=SoundID.CreateTrackable("dd2_kobold_ignite_loop")
	DD2_KoboldScreamChargeLoop:SoundStyle=SoundID.CreateTrackable("dd2_kobold_scream_charge_loop")
	DD2_KoboldFlyerChargeScream:SoundStyle=SoundID.CreateTrackable("dd2_kobold_flyer_charge_scream", 3)
	DD2_KoboldFlyerDeath:SoundStyle=SoundID.CreateTrackable("dd2_kobold_flyer_death", 3)
	DD2_KoboldFlyerHurt:SoundStyle=SoundID.CreateTrackable("dd2_kobold_flyer_hurt", 3)
	DD2_LightningBugDeath:SoundStyle=SoundID.CreateTrackable("dd2_lightning_bug_death", 3)
	DD2_LightningBugHurt:SoundStyle=SoundID.CreateTrackable("dd2_lightning_bug_hurt", 3)
	DD2_LightningBugZap:SoundStyle=SoundID.CreateTrackable("dd2_lightning_bug_zap", 3)
	DD2_OgreAttack:SoundStyle=SoundID.CreateTrackable("dd2_ogre_attack", 3)
	DD2_OgreDeath:SoundStyle=SoundID.CreateTrackable("dd2_ogre_death", 3)
	DD2_OgreGroundPound:SoundStyle=SoundID.CreateTrackable("dd2_ogre_ground_pound")
	DD2_OgreHurt:SoundStyle=SoundID.CreateTrackable("dd2_ogre_hurt", 3)
	DD2_OgreRoar:SoundStyle=SoundID.CreateTrackable("dd2_ogre_roar", 3)
	DD2_OgreSpit:SoundStyle=SoundID.CreateTrackable("dd2_ogre_spit")
	DD2_SkeletonDeath:SoundStyle=SoundID.CreateTrackable("dd2_skeleton_death", 3)
	DD2_SkeletonHurt:SoundStyle=SoundID.CreateTrackable("dd2_skeleton_hurt", 3)
	DD2_SkeletonSummoned:SoundStyle=SoundID.CreateTrackable("dd2_skeleton_summoned")
	DD2_WitherBeastAuraPulse:SoundStyle=SoundID.CreateTrackable("dd2_wither_beast_aura_pulse", 2)
	DD2_WitherBeastCrystalImpact:SoundStyle=SoundID.CreateTrackable("dd2_wither_beast_crystal_impact", 3)
	DD2_WitherBeastDeath:SoundStyle=SoundID.CreateTrackable("dd2_wither_beast_death", 3)
	DD2_WitherBeastHurt:SoundStyle=SoundID.CreateTrackable("dd2_wither_beast_hurt", 3)
	DD2_WyvernDeath:SoundStyle=SoundID.CreateTrackable("dd2_wyvern_death", 3)
	DD2_WyvernHurt:SoundStyle=SoundID.CreateTrackable("dd2_wyvern_hurt", 3)
	DD2_WyvernScream:SoundStyle=SoundID.CreateTrackable("dd2_wyvern_scream", 3)
	DD2_WyvernDiveDown:SoundStyle=SoundID.CreateTrackable("dd2_wyvern_dive_down", 3)
	DD2_EtherianPortalDryadTouch:SoundStyle=SoundID.CreateTrackable("dd2_etherian_portal_dryad_touch")
	DD2_EtherianPortalIdleLoop:SoundStyle=SoundID.CreateTrackable("dd2_etherian_portal_idle_loop")
	DD2_EtherianPortalOpen:SoundStyle=SoundID.CreateTrackable("dd2_etherian_portal_open")
	DD2_EtherianPortalSpawnEnemy:SoundStyle=SoundID.CreateTrackable("dd2_etherian_portal_spawn_enemy", 3)
	DD2_CrystalCartImpact:SoundStyle=SoundID.CreateTrackable("dd2_crystal_cart_impact", 3)
	DD2_DefeatScene:SoundStyle=SoundID.CreateTrackable("dd2_defeat_scene")
	DD2_WinScene:SoundStyle=SoundID.CreateTrackable("dd2_win_scene")
	DD2_BetsysWrathShot:SoundStyle=SoundID.DD2_BetsyFireballShot.WithVolume(0.4)
	DD2_BetsysWrathImpact:SoundStyle=SoundID.DD2_BetsyFireballImpact.WithVolume(0.4)
	DD2_BookStaffCast:SoundStyle=SoundID.CreateTrackable("dd2_book_staff_cast", 3)
	DD2_BookStaffTwisterLoop:SoundStyle=SoundID.CreateTrackable("dd2_book_staff_twister_loop")
	DD2_GhastlyGlaiveImpactGhost:SoundStyle=SoundID.CreateTrackable("dd2_ghastly_glaive_impact_ghost", 3)
	DD2_GhastlyGlaivePierce:SoundStyle=SoundID.CreateTrackable("dd2_ghastly_glaive_pierce", 3)
	DD2_MonkStaffGroundImpact:SoundStyle=SoundID.CreateTrackable("dd2_monk_staff_ground_impact", 3)
	DD2_MonkStaffGroundMiss:SoundStyle=SoundID.CreateTrackable("dd2_monk_staff_ground_miss", 3)
	DD2_MonkStaffSwing:SoundStyle=SoundID.CreateTrackable("dd2_monk_staff_swing", 4)
	DD2_PhantomPhoenixShot:SoundStyle=SoundID.CreateTrackable("dd2_phantom_phoenix_shot", 3)
	DD2_SonicBoomBladeSlash:SoundStyle=SoundID.CreateTrackable("dd2_sonic_boom_blade_slash", 3, SoundID.ItemDefaults).WithVolume(0.5)
	DD2_SkyDragonsFuryCircle:SoundStyle=SoundID.CreateTrackable("dd2_sky_dragons_fury_circle", 3)
	DD2_SkyDragonsFuryShot:SoundStyle=SoundID.CreateTrackable("dd2_sky_dragons_fury_shot", 3)
	DD2_SkyDragonsFurySwing:SoundStyle=SoundID.CreateTrackable("dd2_sky_dragons_fury_swing", 4)
	PlayerHurt1:SoundStyle=LegacySoundStyle(1, 1)
	PlayerHurt2:SoundStyle=LegacySoundStyle(20, 1)
	LucyTheAxeTalk:SoundStyle=SoundID.CreateTrackable("lucyaxe_talk", 5).WithVolume(0.4).WithPitchVariance(0.1)
	DeerclopsHit:SoundStyle=SoundID.CreateTrackable("deerclops_hit", 3).WithVolume(0.3)
	DeerclopsDeath:SoundStyle=SoundID.CreateTrackable("deerclops_death")
	DeerclopsScream:SoundStyle=SoundID.CreateTrackable("deerclops_scream", 3)
	DeerclopsIceAttack:SoundStyle=SoundID.CreateTrackable("deerclops_ice_attack", 3).WithVolume(0.1)
	DeerclopsRubbleAttack:SoundStyle=SoundID.CreateTrackable("deerclops_rubble_attack").WithVolume(0.5)
	DeerclopsStep:SoundStyle=SoundID.CreateTrackable("deerclops_step").WithVolume(0.2)
	ChesterOpen:SoundStyle=SoundID.CreateTrackable("chester_open", 2)
	ChesterClose:SoundStyle=SoundID.CreateTrackable("chester_close", 2)
	AbigailSummon:SoundStyle=SoundID.CreateTrackable("abigail_summon")
	AbigailCry:SoundStyle=SoundID.CreateTrackable("abigail_cry", 3).WithVolume(0.4)
	AbigailAttack:SoundStyle=SoundID.CreateTrackable("abigail_attack").WithVolume(0.35)
	AbigailUpgrade:SoundStyle=SoundID.CreateTrackable("abigail_upgrade", 3).WithVolume(0.5)
	GlommerBounce:SoundStyle=SoundID.CreateTrackable("glommer_bounce", 2).WithVolume(0.5)
	DSTMaleHurt:SoundStyle=SoundID.CreateTrackable("dst_male_hit", 3).WithVolume(0.1)
	DSTFemaleHurt:SoundStyle=SoundID.CreateTrackable("dst_female_hit", 3).WithVolume(0.1)
	JimsDrone:SoundStyle=SoundID.CreateTrackable("Drone").WithVolume(0.1)
	RCCar:SoundStyle=SoundID.CreateTrackable("rccar").WithVolume(0.015)
	VampireSizzle:SoundStyle=SoundID.CreateTrackable("sizzle").WithVolume(1)
	RainbowBoulder:SoundStyle=SoundID.CreateTrackable("rainbow_boulder")
	MenuAccept:SoundStyle=SoundID.CreateTrackable("menu_accept")
	Hungry:SoundStyle=SoundID.CreateTrackable("hungry")
	PalSummon:SoundStyle=SoundID.CreateTrackable("pal_summon").WithVolume(0.15)
	PalCattiva:SoundStyle=SoundID.CreateTrackable("pal_cattiva").WithVolume(0.35)
	PalCattivaPain:SoundStyle=SoundID.CreateTrackable("pal_cattiva_pain").WithVolume(0.35)
	PalCattivaJoy:SoundStyle=SoundID.CreateTrackable("pal_cattiva_joy").WithVolume(0.35)
	PalChillet:SoundStyle=SoundID.CreateTrackable("pal_chillet").WithVolume(0.35)
	PalChilletJoy:SoundStyle=SoundID.CreateTrackable("pal_chillet_joy").WithVolume(0.35)
	PalChilletAttack:SoundStyle=SoundID.CreateTrackable("pal_chillet_attack").WithVolume(0.35)
	PalFoxparks:SoundStyle=SoundID.CreateTrackable("pal_foxparks").WithVolume(0.35)
	PalFoxparksPain:SoundStyle=SoundID.CreateTrackable("pal_foxparks_pain").WithVolume(0.35)
	PalFoxparksJoy:SoundStyle=SoundID.CreateTrackable("pal_foxparks_joy").WithVolume(0.35)
	PalFoxparksAttack:SoundStyle=SoundID.CreateTrackable("pal_foxparks_attack").WithVolume(0.18)
	PalDigtoise:SoundStyle=SoundID.CreateTrackable("pal_digtoise").WithVolume(0.35)
	PalDigtoiseJoy:SoundStyle=SoundID.CreateTrackable("pal_digtoise_joy").WithVolume(0.35)
	FoxparksFlame:SoundStyle=LegacySoundStyle(2, 34).WithVolume(0.15)
	LeafBlower:SoundStyle=LegacySoundStyle(2, 34).WithVolume(0.13)
	DeadCellsBarrelLauncherFire:SoundStyle=SoundID.CreateTrackable("deadcells_barrel_launcher_fire").WithVolume(0.5)
	DeadCellsBarrelLauncherExplode:SoundStyle=SoundID.CreateTrackable("deadcells_barrel_launcher_explode").WithVolume(0.6)
	DeadCellsMushroomSummon:SoundStyle=SoundID.CreateTrackable("deadcells_mushroom_summon").WithVolume(0.35)
	DeadCellsMushroomLand:SoundStyle=SoundID.CreateTrackable("deadcells_mushroom_land").WithVolume(0.35)
	DeadCellsMushroomJump:SoundStyle=SoundID.CreateTrackable("deadcells_mushroom_jump").WithVolume(0.35)
	DeadCellsMushroomExplode:SoundStyle=SoundID.CreateTrackable("deadcells_mushroom_explode").WithVolume(0.15)
	DeadCellsFlintCharge:SoundStyle=SoundID.CreateTrackable("deadcells_flint_charge").WithVolume(0.5)
	DeadCellsFlintRelease:SoundStyle=SoundID.CreateTrackable("deadcells_flint_release").WithVolume(0.5)
	DeadCellsFlintWave:SoundStyle=SoundID.CreateTrackable("deadcells_flint_wave").WithVolume(0.1)
	MeteorShower:SoundStyle=SoundID.CreateTrackable("meteor_shower", 6).WithVolume(0.8).WithPitchVariance(0.3)
	BestReforge:SoundStyle=SoundID.CreateTrackable("best_reforge").WithPitchVariance(0.1)
	TrashItem:SoundStyle=SoundID.CreateTrackable("trash_item", 2).WithVolume(0.55).WithPitchVariance(0.25)
	InstantThunder:SoundStyle=SoundID.CreateTrackable("instant_thunder", 3)
	SonarPotion:SoundStyle=SoundID.CreateTrackable("sonar_potion").WithVolume(0.65).WithPitchVariance(0.03)
	StatueMimicScare:SoundStyle=SoundID.CreateTrackable("statuemimic_scare").WithVolume(0.8).WithPitchVariance(0.1)
	StatueMimicJump:SoundStyle=SoundID.CreateTrackable("statuemimic_jump").WithVolume(0.3).WithPitchVariance(0.1)
	StatueMimicLaugh:SoundStyle=SoundID.CreateTrackable("statuemimic_laugh", 3).WithVolume(0.8).WithPitchVariance(0.1)
	DefaultPlayerHurt:SoundStyle=SoundID.CreateTrackable("player_hit_default").WithVolume(0.9).WithPitchVariance(0.2)
	BellHurt:SoundStyle=LegacySoundStyle(2, 35).WithPitchVariance(0.4)
	ChickenHurt:SoundStyle=SoundID.CreateTrackable("player_hit_chicken").WithVolume(0.8).WithPitchVariance(0.4)
	ChickenHurtRare:SoundStyle=SoundID.CreateTrackable("player_hit_chicken_rare").WithVolume(0.5).WithPitchVariance(0.4)
	FrogHurt:SoundStyle=SoundID.CreateTrackable("player_hit_frog").WithVolume(0.5).WithPitchVariance(0.4)
	GoatHurt:SoundStyle=SoundID.CreateTrackable("player_hit_goat").WithVolume(0.5).WithPitchVariance(0.4)
	RetroHurt:SoundStyle=SoundID.CreateTrackable("player_hit_retro").WithVolume(0.5).WithPitchVariance(0.4)
	RetroDeath:SoundStyle=SoundID.CreateTrackable("player_death_retro").WithVolume(0.5).WithPitchVariance(0.4)
	CatHurt:SoundStyle=SoundID.CreateTrackable("player_hit_cat").WithVolume(0.5).WithPitchVariance(0.4)
	DogHurt:SoundStyle=SoundID.CreateTrackable("player_hit_dog").WithVolume(0.5).WithPitchVariance(0.4)
	TurkeyHurt:SoundStyle=SoundID.CreateTrackable("player_hit_turkey").WithVolume(0.5).WithPitchVariance(0.4)
	GoblinHurt:SoundStyle=SoundID.CreateTrackable("player_hit_goblin").WithVolume(0.5).WithPitchVariance(0.4)
	CrowHurt:SoundStyle=SoundID.CreateTrackable("player_hit_crow").WithVolume(0.5).WithPitchVariance(0.4)
	BalloonHurt:SoundStyle=SoundID.CreateTrackable("player_hit_balloon").WithVolume(0.5).WithPitchVariance(0.4)
	BalloonDeath:SoundStyle=SoundID.CreateTrackable("player_hit_balloon").WithVolume(0.8).WithPitchVariance(0.4)
	UndeadHurt:SoundStyle=SoundID.CreateTrackable("player_hit_undead").WithVolume(0.5).WithPitchVariance(0.4)
	VampireHurt:SoundStyle=SoundID.CreateTrackable("player_hit_vampire").WithVolume(0.5).WithPitchVariance(0.4)
	FairyHurt:SoundStyle=SoundID.CreateTrackable("player_hit_fairy").WithVolume(0.5).WithPitchVariance(0.4)
	FishSplash:SoundStyle=SoundID.CreateTrackable("fish_splash").WithVolume(1).WithPitchVariance(0.02)
	EOWDiggin:SoundStyle=SoundID.CreateTrackable("eow_dig").WithVolume(1).WithPitchVariance(0.02)
	BombFuse:SoundStyle=SoundID.CreateTrackable("fuse").WithVolume(0.2)
	def CreateTrackable(name:str,*args):
		if(args.__len__()==0):
				return SoundID.CreateTrackablec(name)
		if(type(args[0])==SoundStyleDefaults):
			return SoundID.CreateTrackablea(name,*args)
		if(type(args[0])==SoundType):
			return SoundID.CreateTrackablec(name,*args)
		if(args.__len__()==0):
			return SoundID.CreateTrackablec(name)
		if(type(args[1])==SoundStyleDefaults):
			return SoundID.CreateTrackableb(name,*args)
		if(type(args[1])==SoundType):
			return SoundID.CreateTrackabled(name,*args)
	def CreateTrackablea(name:str, defaults:SoundStyleDefaults, maxInstances:int = 0):
		return SoundID.CreateTrackabled(name, 1, defaults.Type, maxInstances).WithPitchVariance(defaults.PitchVariance).WithVolume(defaults.Volume);
	def CreateTrackableb(name:str, variations:int, defaults:SoundStyleDefaults, maxInstances:int = 0):
		return SoundID.CreateTrackabled(name, variations, defaults.Type, maxInstances).WithPitchVariance(defaults.PitchVariance).WithVolume(defaults.Volume);
	def CreateTrackablec(name:str, type:SoundType = SoundType.Sound, maxInstances:int = 0):
		return SoundID.CreateTrackabled(name, 1, type, maxInstances)
	def CreateTrackabled(name:str, variations:int, type:SoundType = SoundType.Sound, maxInstances:int = 0)->LegacySoundStyle:
		if (SoundID._trackableLegacySoundPathList == None):
			SoundID._trackableLegacySoundPathList = [];
		
		count:int = SoundID._trackableLegacySoundPathList.__len__();
		if (variations == 1):
			SoundID._trackableLegacySoundPathList.append(name)
		else:
			for i in range(0,variations,1):
				SoundID._trackableLegacySoundPathList.append(name + "_" + str(i))
		return LegacySoundStyle(42, count, variations, type, maxInstances)


from typing import Final
class List(list,Generic[TypeVar('T')]):
	def Add(self,value):
		self.append(value)
	@property
	def Length(self):
		return self.__len__()
class Main:
	townNPCCanSpawn:list[bool]=[False for i in range(NPCID.Count)]
	projHostile:list[bool]=[False for i in range(ProjectileID.Count)]
	projHook:list[bool]=[False for i in range(ProjectileID.Count)]
	pvpBuff:list[bool]=[False for i in range(BuffID.Count)]
	persistentBuff:list[bool]=[False for i in range(BuffID.Count)]
	vanityPet:list[bool]=[False for i in range(BuffID.Count)]
	lightPet:list[bool]=[False for i in range(BuffID.Count)]
	meleeBuff:list[bool]=[False for i in range(BuffID.Count)]
	debuff:list[bool]=[False for i in range(BuffID.Count)]
	buffNoSave:list[bool]=[False for i in range(BuffID.Count)]
	buffNoTimeDisplay:list[bool]=[False for i in range(BuffID.Count)]
	buffDoubleApply:list[bool]=[False for i in range(BuffID.Count)]
	slimeRainNPC:list[bool]=[False for i in range(NPCID.Count)]
	projPet:list[bool]=[False for i in range(ProjectileID.Count)]
	tileLighted:list[bool]=[False for i in range(TileID.Count)]
	tileMergeDirt:list[bool]=[False for i in range(TileID.Count)]
	tileCut:list[bool]=[False for i in range(TileID.Count)]
	tileAlch:list[bool]=[False for i in range(TileID.Count)]
	tileShine2:list[bool]=[False for i in range(TileID.Count)]
	wallHouse:list[bool]=[False for i in range(WallID.Count)]
	wallDungeon:list[bool]=[False for i in range(WallID.Count)]
	wallLight:list[bool]=[False for i in range(WallID.Count)]
	tileStone:list[bool]=[False for i in range(TileID.Count)]
	tileAxe:list[bool]=[False for i in range(TileID.Count)]
	tileHammer:list[bool]=[False for i in range(TileID.Count)]
	tileWaterDeath:list[bool]=[False for i in range(TileID.Count)]
	tileLavaDeath:list[bool]=[False for i in range(TileID.Count)]
	tileTable:list[bool]=[False for i in range(TileID.Count)]
	tileBlockLight:list[bool]=[False for i in range(TileID.Count)]
	tileNoSunLight:list[bool]=[False for i in range(TileID.Count)]
	tileDungeon:list[bool]=[False for i in range(TileID.Count)]
	tileSpelunker:list[bool]=[False for i in range(TileID.Count)]
	tileSolidTop:list[bool]=[False for i in range(TileID.Count)]
	tileSolid:list[bool]=[False for i in range(TileID.Count)]
	tileBouncy:list[bool]=[False for i in range(TileID.Count)]
	tileRope:list[bool]=[False for i in range(TileID.Count)]
	tileBrick:list[bool]=[False for i in range(TileID.Count)]
	tileMoss:list[bool]=[False for i in range(TileID.Count)]
	tileNoAttach:list[bool]=[False for i in range(TileID.Count)]
	tileNoFail:list[bool]=[False for i in range(TileID.Count)]
	tileCracked:list[bool]=[False for i in range(TileID.Count)]
	tileObsidianKill:list[bool]=[False for i in range(TileID.Count)]
	tileFrameImportant:list[bool]=[False for i in range(TileID.Count)]
	tilePile:list[bool]=[False for i in range(TileID.Count)]
	tileBlendAll:list[bool]=[False for i in range(TileID.Count)]
	tileContainer:list[bool]=[False for i in range(TileID.Count)]
	tileSign:list[bool]=[False for i in range(TileID.Count)]
	tileSand:list[bool]=[False for i in range(TileID.Count)]
	tileFlame:list[bool]=[False for i in range(TileID.Count)]
	npcCatchable:list[bool]=[False for i in range(NPCID.Count)]
	maxBackgrounds:Final = 344
	recipe:List["RecipeInstance"]=[None for i in range(3600)]
	netMode=1
from typing import Union
class RecipeGroup:
	recipeGroups:dict[int,"RecipeGroup"]={}
	nextRecipeGroupIndex:int=0
	def __init__(this,getName:Union[function,str], *validItems:int):
		if type(getName)==type("str"):
			getName=RecipeGroup.WithDefaultCombineFormat(getName)
		this.ValidItems:set[int]=set[int]()
		this.Items:List[int]=List[int]()
		this.DecraftItemId:int=0
		this.RegisteredId:int=-1
		this.getText:function=getName
		for validItem in validItems:
			this.Add(validItem)
	def Register(this)->"RecipeGroup":
		if (this.RegisteredId >= 0):
			raise Exception("Already registered")
		this.RegisteredId = RecipeGroup.nextRecipeGroupIndex
		key:int = this.RegisteredId
		RecipeGroup.nextRecipeGroupIndex+=1
		RecipeGroup.recipeGroups[key]=this
		return this
	def WithDefaultCombineFormat(key:str)->function:
		return lambda:key
	def Add(this,itemID:int, isPreferred:Union[function,None] = None):
		this.ValidItems.add(itemID)
		this.Items.Add(itemID)
		return this
	
class RecipeGroups:
	Birds:RecipeGroup=None
	Scorpions:RecipeGroup=None
	Bugs:RecipeGroup=None
	Ducks:RecipeGroup=None
	Squirrels:RecipeGroup=None
	Butterflies:RecipeGroup=None
	Fireflies:RecipeGroup=None
	Snails:RecipeGroup=None
	FishForDinner:RecipeGroup=None
	GoldenCritter:RecipeGroup=None
	Dragonflies:RecipeGroup=None
	Turtles:RecipeGroup=None
	Fruit:RecipeGroup=None
	Balloons:RecipeGroup=None
	Wood:RecipeGroup=None
	Sand:RecipeGroup=None
	IronBar:RecipeGroup=None
	Fragment:RecipeGroup=None
	PressurePlate:RecipeGroup=None
	Macaws:RecipeGroup=None
	Cockatiels:RecipeGroup=None
	CloudBalloons:RecipeGroup=None
	BlizzardBalloons:RecipeGroup=None
	SandstormBalloons:RecipeGroup=None
	CritterGuides:RecipeGroup=None
	NatureGuides:RecipeGroup=None
	Seashells:RecipeGroup=None
	Stone:RecipeGroup=None
	CobaltBar:RecipeGroup=None
	MythrilBar:RecipeGroup=None
	AdamantiteBar:RecipeGroup=None
	GemCritter:RecipeGroup=None
	MagicMirror:RecipeGroup=None
	Jellyfish:RecipeGroup=None
class RecipeInstance:
	class ItemStackHolder:
		def __init__(this):
			this._item=0
			this.count=-1
		def SetDefaults(this,id):
			this._item=id
			this.count=1
	def __init__(self):
		self.createItem=RecipeInstance.ItemStackHolder()
		self.requiredItem=[RecipeInstance.ItemStackHolder() for i in range(15)]
		self.requiredTile:int=-1
		self.acceptedGroups=[-1 for i in range(15)]
		self.customShimmerResults:List[RecipeInstance.ItemStackHolder]=List[RecipeInstance.ItemStackHolder]()
		self.needHoney=False
		self.needWater=False
		self.needLava=False
		self.needTorchGodsFavor=False
		self.alchemy=False
		self.needSnowBiome=False
		self.needGraveyardBiome=False
		self.needMechdusa=False
		self.notDecraftable=False
		self.crimson=False
		self.corruption=False
	def AddCustomShimmerResult(this,itemType:int, itemStack:int = 1):
		if (this.customShimmerResults == None):
			this.customShimmerResults = List[RecipeInstance.ItemStackHolder]()
		
		item:RecipeInstance.ItemStackHolder = RecipeInstance.ItemStackHolder()
		item.SetDefaults(itemType)
		item.stack = itemStack
		this.customShimmerResults.Add(item)
		return item
	def SetCraftingStation(this,tileType:int):
		this.requiredTile=tileType
	def SetIngredients(this,*ingredients:int):
		ingredients=List(ingredients)
		if (ingredients.Length == 1):
			ingredients = List([
				ingredients[0],
				1
			])
		
		if (ingredients.Length % 2 != 0):
			raise Exception("Bad ingredients amount")
		
		for i in range(0,ingredients.Length,2):
			num:int = int(i / 2)
			this.requiredItem[num].SetDefaults(ingredients[i])
			this.requiredItem[num].stack = ingredients[i + 1]
	def RequireGroup(this,group:RecipeGroup):
		for i in range(Recipe.maxRequirements):
			if (this.acceptedGroups[i] == -1):
				this.acceptedGroups[i] = group.RegisteredId
				break
	def Stringify(this):
		s="CreateRecipe("+str(this.createItem.count)+")\n"
		for i in range(15):
			if(this.acceptedGroups[i]!=-1):
				s+=".AddRecipeGroup(RecipeGroupID."+RecipeGroupID.groupsByName[this.acceptedGroups[i]]+", "+str(this.requiredItem[i].count)+")\n"
			elif(this.requiredItem[i].count!=-1):
				j=this.requiredItem[i]._item
				if(j<ItemID.OldCount):
					s+=".AddIngredient(ItemID."+ItemID.itemsByName[j]+", "+str(this.requiredItem[i].count)+")\n"
				else:
					s+=".AddIngredient(ModContent.ItemType<"+ItemID.itemsByName[j]+">(), "+str(this.requiredItem[i].count)+")\n"
		if(this.requiredTile!=-1):
			s+=".AddTile(TileID."+TileID.tilesByName[this.requiredTile]+")\n"
		if(this.notDecraftable):
			s+=".DisableDecraft()"
		s+=".Register();"
		return s
class Lang:
	class langentry:
		def __init__(this):
			this.Key=""
	misc=[]
Lang.misc=[Lang.langentry() for i in range(201)]
class Recipe:
	currentRecipe:RecipeInstance=RecipeInstance()
	numRecipes:int=0
	TileUsedInRecipes:List[int]=[False for i in range(TileID.Count)]
	maxRequirements:int=15
	def AddRecipe():
		if (Recipe.currentRecipe.requiredTile == 13):
			Recipe.currentRecipe.alchemy = true
		Main.recipe[Recipe.numRecipes] = Recipe.currentRecipe
		if (Recipe.currentRecipe.requiredTile >= 0):
			Recipe.TileUsedInRecipes[Recipe.currentRecipe.requiredTile] = true
		Recipe.currentRecipe = RecipeInstance()
		Recipe.numRecipes+=1
	def AddStandardFurnitureSetRecipes(primaryMaterial:int,bathtub:int, bed:int, bookcase:int, candelabra:int, candle:int, chair:int, chandelier:int, chest:int, clock:int, door:int, dresser:int, lamp:int, lantern:int, piano:int, sink:int, sofa:int, table:int, toilet:int, workbench:int, fake_chest:int, overrideStation:int = -1):
		global currentvars
		currentvars['callmethodoutput']=None
		v=[primaryMaterial,bathtub,bed,bookcase,candelabra,candle,chair,chandelier,chest,clock,door,dresser,lamp,lantern,piano,sink,sofa,table,toilet,workbench,fake_chest,overrideStation]
		v2=["primaryMaterial","bathtub","bed","bookcase","candelabra","candle","chair","chandelier","chest","clock","door","dresser","lamp","lantern","piano","sink","sofa","table","toilet","workbench","fake_chest","overrideStation"]
		for i in range(v.__len__()):
			currentvars[v2[i]]=v[i]
		x=getFunctionContents("Terraria.Recipe","private static void AddStandardFurnitureSetRecipes(int primaryMaterial, int bathtub, int bed, int bookcase, int candelabra, int candle, int chair, int chandelier, int chest, int clock, int door, int dresser, int lamp, int lantern, int piano, int sink, int sofa, int table, int toilet, int workbench, int fake_chest, int overrideStation = -1)")
		#print("a")
		#currentvars['callmethodoutput']=x#keepOnlyContentsWhen(x,"thisisntavar",None)[0]
		keepOnlyContentsWhen(x,"thisisntavar",None)[0]
	def CreateReversePlatformRecipes():
		global currentvars
		currentvars['callmethodoutput']=None
		#for i in ["primaryMaterial","bathtub","bed","bookcase","candelabra","candle","chair","chandelier","chest","clock","door","dresser","lamp","lantern","piano","sink","sofa","table","toilet","workbench","fake_chest","overrideStation"]:
		#	currentvars[i]=vars()[i]
		x=getFunctionContents("Terraria.Recipe","private static void CreateReversePlatformRecipes()")
		#print("a")
		#currentvars['callmethodoutput']=x#keepOnlyContentsWhen(x,"thisisntavar",None)[0]
		keepOnlyContentsWhen(x,"thisisntavar",None)[0]
	def CreateReverseWallRecipes():
		global currentvars
		currentvars['callmethodoutput']=None
		x=getFunctionContents("Terraria.Recipe","private static void CreateReverseWallRecipes()")
		keepOnlyContentsWhen(x,"thisisntavar",None)[0]
	def AddBoulderFurniture():
		global currentvars
		currentvars['callmethodoutput']=None
		x=getFunctionContents("Terraria.Recipe","private static void AddBoulderFurniture()")
		keepOnlyContentsWhen(x,"thisisntavar",None)[0]
	def AddWaterFurniture():
		global currentvars
		currentvars['callmethodoutput']=None
		x=getFunctionContents("Terraria.Recipe","private static void AddWaterFurniture()")
		keepOnlyContentsWhen(x,"thisisntavar",None)[0]
	def AddForbiddenFurniture():
		global currentvars
		currentvars['callmethodoutput']=None
		x=getFunctionContents("Terraria.Recipe","private static void AddForbiddenFurniture()")
		keepOnlyContentsWhen(x,"thisisntavar",None)[0]
	def AddOfficeFurniture():
		global currentvars
		currentvars['callmethodoutput']=None
		x=getFunctionContents("Terraria.Recipe","private static void AddOfficeFurniture()")
		keepOnlyContentsWhen(x,"thisisntavar",None)[0]
	def AddSpikeFurniture():
		global currentvars
		currentvars['callmethodoutput']=None
		x=getFunctionContents("Terraria.Recipe","private static void AddSpikeFurniture()")
		keepOnlyContentsWhen(x,"thisisntavar",None)[0]
	def AddLibrarianFurniture():
		global currentvars
		currentvars['callmethodoutput']=None
		x=getFunctionContents("Terraria.Recipe","private static void AddLibrarianFurniture()")
		keepOnlyContentsWhen(x,"thisisntavar",None)[0]
	def AddMoonplateFurniture():
		global currentvars
		currentvars['callmethodoutput']=None
		x=getFunctionContents("Terraria.Recipe","private static void AddMoonplateFurniture()")
		keepOnlyContentsWhen(x,"thisisntavar",None)[0]
	def AddCloudFurniture():
		global currentvars
		currentvars['callmethodoutput']=None
		x=getFunctionContents("Terraria.Recipe","private static void AddCloudFurniture()")
		keepOnlyContentsWhen(x,"thisisntavar",None)[0]
	def AddHarpyFurniture():
		global currentvars
		currentvars['callmethodoutput']=None
		x=getFunctionContents("Terraria.Recipe","private static void AddHarpyFurniture()")
		keepOnlyContentsWhen(x,"thisisntavar",None)[0]
	def AddJellyfishFurniture():
		global currentvars
		currentvars['callmethodoutput']=None
		x=getFunctionContents("Terraria.Recipe","private static void AddJellyfishFurniture()")
		keepOnlyContentsWhen(x,"thisisntavar",None)[0]
	def AddStoneFurniture():
		global currentvars
		currentvars['callmethodoutput']=None
		x=getFunctionContents("Terraria.Recipe","private static void AddStoneFurniture()")
		keepOnlyContentsWhen(x,"thisisntavar",None)[0]
	def AddPineFurniture():
		global currentvars
		currentvars['callmethodoutput']=None
		x=getFunctionContents("Terraria.Recipe","private static void AddPineFurniture()")
		keepOnlyContentsWhen(x,"thisisntavar",None)[0]
	def AddFlinxFurFurniture():
		global currentvars
		currentvars['callmethodoutput']=None
		x=getFunctionContents("Terraria.Recipe","private static void AddFlinxFurFurniture()")
		keepOnlyContentsWhen(x,"thisisntavar",None)[0]
	def AddSnowFurniture():
		global currentvars
		currentvars['callmethodoutput']=None
		x=getFunctionContents("Terraria.Recipe","private static void AddSnowFurniture()")
		keepOnlyContentsWhen(x,"thisisntavar",None)[0]
	def AddCrimtaneFurniture():
		global currentvars
		currentvars['callmethodoutput']=None
		x=getFunctionContents("Terraria.Recipe","private static void AddCrimtaneFurniture()")
		keepOnlyContentsWhen(x,"thisisntavar",None)[0]
	def AddDemoniteFurniture():
		global currentvars
		currentvars['callmethodoutput']=None
		x=getFunctionContents("Terraria.Recipe","private static void AddDemoniteFurniture()")
		keepOnlyContentsWhen(x,"thisisntavar",None)[0]
	def AddGothicFurniture():
		global currentvars
		currentvars['callmethodoutput']=None
		x=getFunctionContents("Terraria.Recipe","private static void AddGothicFurniture()")
		keepOnlyContentsWhen(x,"thisisntavar",None)[0]
	def AddEasterFurniture():
		global currentvars
		currentvars['callmethodoutput']=None
		x=getFunctionContents("Terraria.Recipe","private static void AddEasterFurniture()")
		keepOnlyContentsWhen(x,"thisisntavar",None)[0]
	def AddHallowedFurniture():
		global currentvars
		currentvars['callmethodoutput']=None
		x=getFunctionContents("Terraria.Recipe","private static void AddHallowedFurniture()")
		keepOnlyContentsWhen(x,"thisisntavar",None)[0]
	def AddFeywoodFurniture():
		global currentvars
		currentvars['callmethodoutput']=None
		x=getFunctionContents("Terraria.Recipe","private static void AddFeywoodFurniture()")
		keepOnlyContentsWhen(x,"thisisntavar",None)[0]
	def AddFallenStarFurniture():
		global currentvars
		currentvars['callmethodoutput']=None
		x=getFunctionContents("Terraria.Recipe","private static void AddFallenStarFurniture()")
		keepOnlyContentsWhen(x,"thisisntavar",None)[0]
	def AddAetheriumFurniture():
		global currentvars
		currentvars['callmethodoutput']=None
		x=getFunctionContents("Terraria.Recipe","private static void AddAetheriumFurniture()")
		keepOnlyContentsWhen(x,"thisisntavar",None)[0]
	def AddAshWoodFurnitureArmorAndItems():
		global currentvars
		currentvars['callmethodoutput']=None
		x=getFunctionContents("Terraria.Recipe","private static void AddAshWoodFurnitureArmorAndItems()")
		keepOnlyContentsWhen(x,"thisisntavar",None)[0]
	def AddBalloonFurniture():
		global currentvars
		currentvars['callmethodoutput']=None
		x=getFunctionContents("Terraria.Recipe","private static void AddBalloonFurniture()")
		keepOnlyContentsWhen(x,"thisisntavar",None)[0]
	def AddCoralFurniture():
		global currentvars
		currentvars['callmethodoutput']=None
		x=getFunctionContents("Terraria.Recipe","private static void AddCoralFurniture()")
		keepOnlyContentsWhen(x,"thisisntavar",None)[0]
	def AddBambooFurniture():
		global currentvars
		currentvars['callmethodoutput']=None
		x=getFunctionContents("Terraria.Recipe","private static void AddBambooFurniture()")
		keepOnlyContentsWhen(x,"thisisntavar",None)[0]
	def AddSandstoneFurniture():
		global currentvars
		currentvars['callmethodoutput']=None
		x=getFunctionContents("Terraria.Recipe","private static void AddSandstoneFurniture()")
		keepOnlyContentsWhen(x,"thisisntavar",None)[0]
	def AddLesionFurniture():
		global currentvars
		currentvars['callmethodoutput']=None
		x=getFunctionContents("Terraria.Recipe","private static void AddLesionFurniture()")
		keepOnlyContentsWhen(x,"thisisntavar",None)[0]
	def AddSpiderFurniture():
		global currentvars
		currentvars['callmethodoutput']=None
		x=getFunctionContents("Terraria.Recipe","private static void AddSpiderFurniture()")
		keepOnlyContentsWhen(x,"thisisntavar",None)[0]
	def AddStardustFurniture():
		global currentvars
		currentvars['callmethodoutput']=None
		x=getFunctionContents("Terraria.Recipe","private static void AddStardustFurniture()")
		keepOnlyContentsWhen(x,"thisisntavar",None)[0]
	def AddNebulaFurniture():
		global currentvars
		currentvars['callmethodoutput']=None
		x=getFunctionContents("Terraria.Recipe","private static void AddNebulaFurniture()")
		keepOnlyContentsWhen(x,"thisisntavar",None)[0]
	def AddVortexFurniture():
		global currentvars
		currentvars['callmethodoutput']=None
		x=getFunctionContents("Terraria.Recipe","private static void AddVortexFurniture()")
		keepOnlyContentsWhen(x,"thisisntavar",None)[0]
	def AddSolarFurniture():
		global currentvars
		currentvars['callmethodoutput']=None
		x=getFunctionContents("Terraria.Recipe","private static void AddSolarFurniture()")
		keepOnlyContentsWhen(x,"thisisntavar",None)[0]
	def SetupRecipeGroups():
		global currentvars
		currentvars['callmethodoutput']=None
		x=getFunctionContents("Terraria.Recipe","static void SetupRecipeGroups()")
		keepOnlyContentsWhen(x,"thisisntavar",None)[0]
	def SetupRecipes():
		global currentvars
		currentvars['callmethodoutput']=None
		x=getFunctionContents("Terraria.Recipe","public static void SetupRecipes()")
		x=x.replace('\t',"").replace('    ',"").replace("""int[,] array = new int[36, 2]
		{
			{ 3886, 3884 },
			{ 3887, 3885 },
			{ 3950, 3939 },
			{ 3976, 3965 },
			{ 4164, 4153 },
			{ 4185, 4174 },
			{ 4206, 4195 },
			{ 4227, 4216 },
			{ 4266, 4265 },
			{ 4268, 4267 },
			{ 4585, 4574 },
			{ 4713, 4712 },
			{ 5167, 5156 },
			{ 5188, 5177 },
			{ 5209, 5198 },
			{ 5567, 5556 },
			{ 5620, 5609 },
			{ 5708, 5697 },
			{ 5731, 5720 },
			{ 5754, 5745 },
			{ 5776, 5763 },
			{ 5797, 5784 },
			{ 5818, 5805 },
			{ 5839, 5826 },
			{ 5857, 5846 },
			{ 5878, 5865 },
			{ 5897, 5886 },
			{ 5918, 5905 },
			{ 5952, 5939 },
			{ 5974, 5962 },
			{ 5995, 5982 },
			{ 6018, 6005 },
			{ 6041, 6028 },
			{ 6064, 6051 },
			{ 6087, 6074 },
			{ 6131, 6118 }
		};""".replace('\t','').replace('    ',''),"""array:List[list[int]] = [
			[ 3886, 3884 ],
			[ 3887, 3885 ],
			[ 3950, 3939 ],
			[ 3976, 3965 ],
			[ 4164, 4153 ],
			[ 4185, 4174 ],
			[ 4206, 4195 ],
			[ 4227, 4216 ],
			[ 4266, 4265 ],
			[ 4268, 4267 ],
			[ 4585, 4574 ],
			[ 4713, 4712 ],
			[ 5167, 5156 ],
			[ 5188, 5177 ],
			[ 5209, 5198 ],
			[ 5567, 5556 ],
			[ 5620, 5609 ],
			[ 5708, 5697 ],
			[ 5731, 5720 ],
			[ 5754, 5745 ],
			[ 5776, 5763 ],
			[ 5797, 5784 ],
			[ 5818, 5805 ],
			[ 5839, 5826 ],
			[ 5857, 5846 ],
			[ 5878, 5865 ],
			[ 5897, 5886 ],
			[ 5918, 5905 ],
			[ 5952, 5939 ],
			[ 5974, 5962 ],
			[ 5995, 5982 ],
			[ 6018, 6005 ],
			[ 6041, 6028 ],
			[ 6064, 6051 ],
			[ 6087, 6074 ],
			[ 6131, 6118 ]
		];""").replace(".GetLength(0)",".__len__()").replace("foreach (RecipeGroup value in RecipeGroup.recipeGroups.Values)","for (value in [RecipeGroup.recipeGroups[i] for i in RecipeGroup.recipeGroups])")
		keepOnlyContentsWhen(x,"thisisntavar",None)[0]
	
	
currentvars={"x":None,"this":None,"true":True,"false":False,"Item":ItemMethods,"ItemID":ItemID,"null":None,"variant":None,"GameShaders":GameShadersMethods,"Main":Main,"Recipe":Recipe,"RecipeGroup":RecipeGroup,"RecipeGroups":RecipeGroups,"Lang":Lang}
Recipe.SetupRecipeGroups()
Recipe.SetupRecipes()
Main=currentvars['Main']
x=getFunctionContents("Terraria.Main","private static void Initialize_TileAndNPCData1()")
y2=keepOnlyContentsWhen(x,"this",None)[0]
x=getFunctionContents("Terraria.Main","private static void Initialize_TileAndNPCData2()")
y2=keepOnlyContentsWhen(x,"this",None)[0]
class ContentSamplesMethods:
	"""A holder class for Terraria.ID.ContentSamples"""
	internallazyarrayItems=PartiallyLoadedArray(ItemHolder.fromTypeInd,ItemID.Count)
	ItemsByType=PartiallyLoadedArray((lambda ind:ContentSamplesMethods.internallazyarrayItems[ind][0]),ItemID.Count)
	ItemDefLinesByType=PartiallyLoadedArray((lambda ind:ContentSamplesMethods.internallazyarrayItems[ind][1]),ItemID.Count)
	internallazyarrayProjectiles=PartiallyLoadedArray(ProjectileHolder.fromTypeInd,ProjectileID.Count)
	ProjectilesByType=PartiallyLoadedArray((lambda ind:ContentSamplesMethods.internallazyarrayProjectiles[ind][0]),ProjectileID.Count)
	ProjectileDefLinesByType=PartiallyLoadedArray((lambda ind:ContentSamplesMethods.internallazyarrayProjectiles[ind][1]),ProjectileID.Count)
	mounts=PartiallyLoadedArray((lambda ind:MountHolder.mounts[ind]),MountID.Count)
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
	for i in getVariablesOfType("Terraria.Projectile","public "+vt):
		print(i)
		if(i[0]=="?"):
			y=getVariable("Terraria.Projectile","public "+vt+i)
			if(y.__len__()==0):
				tmp+=i[2:]+":"+vartypes[vt][0]+"|None=None\n"
			else:
				tmp+=i[2:]+":"+vartypes[vt][0]+"|None="+y+"\n"
		if(i[0]=="["):
			y=getVariable("Terraria.Projectile","public "+vt+i)
			if(y.__len__()==0):
				tmp+=i[2:]+":list["+vartypes[vt][0]+"]=[]\n"
			else:
				tmp+=i[2:]+":list["+vartypes[vt][0]+"]="+y+"\n"
		else:
			y=getVariable("Terraria.Projectile","public "+vt+" "+i)
			if(y.__len__()==0):
				tmp+=i+":"+vartypes[vt][0]+"="+str(vartypes[vt][1])+"#default value\n"
			else:
				tmp+=i+":"+vartypes[vt][0]+"="+y+"\n"
print(tmp.replace("\n","\nthis."))"""
"""
tmp=""
for i in getFuncsStartingWith("Terraria.Projectile","private void AI"):
	n="keepOnlyContentsWhen(x,\"this.type\",this.type)[0]"
	y="def "+i[i.index("AI"):i.index("(")+1]+"this"
	for j in i[i.index("(")+1:-1].split(','):
		if(j.strip().__len__()!=0):
			y+=", "+j.strip().split(" ")[-1]
			n="keepOnlyContentsWhen("+n+",\""+j.strip().split(" ")[-1]+"\","+j.strip().split(" ")[-1]+")[0]"
	y+="):\n    x=getFunctionContents(\"Terraria.Projectile\",\""+i+"\")\n    return "+n+"\n"
	print(y,end="")#"""
"""tmp=""
for i in getVariablesOfType("Terraria.Main","public static bool[]"):
	if(i[0]!='['):
		y=getVariable("Terraria.Main","public static bool[] "+i)
		tmp+=i+":list[bool]=[False for i in range("+y[y.index("[")+1:y.index("]")]+")]\n"
print(tmp)"""
x=""""""
x=x.split("new Asset<Texture2D>[")[0]+"".join(["[None for i in range("+i[0][:i[1]-1]+")]"+i[0][i[1]:] for i in [[i,findLinkedBracket("["+i)] for i in x.split("new Asset<Texture2D>[")[1:]]])


Asset.Empty=Asset("",None)
vartypes={"float":("float",0),
		 "int":("int",0),
		 "short":("short",0),
		 "sbyte":("sbyte",0),
		 "byte":("byte",0),
		 "bool":("bool",False),
		 "Color":("any",None),
		 "LegacySoundStyle":("any",None),
		 "Asset[Texture2D]":("Asset[Texture2D]",None),
		 "Asset<Texture2D>":("Asset[Texture2D]",None),
		 "Vector2":("Vector2",None),
		 "Vector3":("Vector3",None),
		 "MountDelegatesData":("MountDelegatesData",None),
		 "MountData":("MountData",None),
		 "object":("any",None)}
class TextureAssets:
	InfoIcon:list[Asset[Texture2D]]=[None for i in range(14)]
	WireUi:list[Asset[Texture2D]]=[None for i in range(12)]
	BuilderAcc:Asset[Texture2D]=None# default value
	QuicksIcon:Asset[Texture2D]=None# default value
	Clothes:list[Asset[Texture2D]]=[None for i in range(6)]
	MapIcon:list[Asset[Texture2D]]=[None for i in range(9)]
	Underworld:list[Asset[Texture2D]]=[None for i in range(14)]
	MapPing:Asset[Texture2D]=None# default value
	Map:Asset[Texture2D]=None# default value
	MapBGs:list[Asset[Texture2D]]=[None for i in range(42)]
	Hue:Asset[Texture2D]=None# default value
	FlameRing:Asset[Texture2D]=None# default value
	MapDeath:Asset[Texture2D]=None# default value
	ColorSlider:Asset[Texture2D]=None# default value
	ColorBar:Asset[Texture2D]=None# default value
	ColorBlip:Asset[Texture2D]=None# default value
	SmartDig:Asset[Texture2D]=None# default value
	SmartCursorArrow:Asset[Texture2D]=None# default value
	ColorHighlight:Asset[Texture2D]=None# default value
	TileCrack:Asset[Texture2D]=None# default value
	LockOnCursor:Asset[Texture2D]=None# default value
	IceBarrier:Asset[Texture2D]=None# default value
	ChestStack:list[Asset[Texture2D]]=[None for i in range(4)]
	NpcHead:list[Asset[Texture2D]]=[None for i in range(NPCHeadID.Count)]
	NpcHeadBoss:list[Asset[Texture2D]]=[None for i in range(40)]
	CraftToggle:list[Asset[Texture2D]]=[None for i in range(6)]
	ChestCraft:list[Asset[Texture2D]]=[None for i in range(4)]
	BannerToggle:list[Asset[Texture2D]]=[None for i in range(4)]
	InventorySort:list[Asset[Texture2D]]=[None for i in range(2)]
	TextGlyph:list[Asset[Texture2D]]=[None for i in range(1)]
	HotbarRadial:list[Asset[Texture2D]]=[None for i in range(3)]
	CraftUpButton:Asset[Texture2D]=None# default value
	CraftDownButton:Asset[Texture2D]=None# default value
	ScrollLeftButton:Asset[Texture2D]=None# default value
	ScrollRightButton:Asset[Texture2D]=None# default value
	Frozen:Asset[Texture2D]=None# default value
	MagicPixel:Asset[Texture2D]=None# default value
	SettingsPanel:Asset[Texture2D]=None# default value
	SettingsPanel2:Asset[Texture2D]=None# default value
	Dest:list[Asset[Texture2D]]=[None for i in range(3)]
	Gem:list[Asset[Texture2D]]=[None for i in range(7)]
	RudolphMount:list[Asset[Texture2D]]=[None for i in range(3)]
	BunnyMount:Asset[Texture2D]=None# default value
	PigronMount:Asset[Texture2D]=None# default value
	SlimeMount:Asset[Texture2D]=None# default value
	MinecartMount:Asset[Texture2D]=None# default value
	TurtleMount:Asset[Texture2D]=None# default value
	DesertMinecartMount:Asset[Texture2D]=None# default value
	FishMinecartMount:Asset[Texture2D]=None# default value
	BeeMount:list[Asset[Texture2D]]=[None for i in range(2)]
	UfoMount:list[Asset[Texture2D]]=[None for i in range(2)]
	DrillMount:list[Asset[Texture2D]]=[None for i in range(6)]
	ScutlixMount:list[Asset[Texture2D]]=[None for i in range(3)]
	UnicornMount:Asset[Texture2D]=None# default value
	BasiliskMount:Asset[Texture2D]=None# default value
	MinecartMechMount:list[Asset[Texture2D]]=[None for i in range(2)]
	CuteFishronMount:list[Asset[Texture2D]]=[None for i in range(2)]
	MinecartWoodMount:Asset[Texture2D]=None# default value
	Wings:list[Asset[Texture2D]]=[None for i in range(ArmorIDs.Wing.Count)]
	ArmorHead:list[Asset[Texture2D]]=[None for i in range(ArmorIDs.Head.Count)]
	ArmorBody:list[Asset[Texture2D]]=[None for i in range(ArmorIDs.Body.Count)]
	ArmorBodyComposite:list[Asset[Texture2D]]=[None for i in range(ArmorIDs.Body.Count)]
	FemaleBody:list[Asset[Texture2D]]=[None for i in range(ArmorIDs.Body.Count)]
	ArmorArm:list[Asset[Texture2D]]=[None for i in range(ArmorIDs.Body.Count)]
	ArmorLeg:list[Asset[Texture2D]]=[None for i in range(ArmorIDs.Legs.Count)]
	AccHandsOn:list[Asset[Texture2D]]=[None for i in range(ArmorIDs.HandOn.Count)]
	AccHandsOnComposite:list[Asset[Texture2D]]=[None for i in range(ArmorIDs.HandOn.Count)]
	AccHandsOff:list[Asset[Texture2D]]=[None for i in range(ArmorIDs.HandOff.Count)]
	AccHandsOffComposite:list[Asset[Texture2D]]=[None for i in range(ArmorIDs.HandOff.Count)]
	AccBack:list[Asset[Texture2D]]=[None for i in range(ArmorIDs.Back.Count)]
	AccFront:list[Asset[Texture2D]]=[None for i in range(ArmorIDs.Front.Count)]
	AccShoes:list[Asset[Texture2D]]=[None for i in range(ArmorIDs.Shoe.Count)]
	AccWaist:list[Asset[Texture2D]]=[None for i in range(ArmorIDs.Waist.Count)]
	AccShield:list[Asset[Texture2D]]=[None for i in range(ArmorIDs.Shield.Count)]
	AccNeck:list[Asset[Texture2D]]=[None for i in range(ArmorIDs.Neck.Count)]
	AccFace:list[Asset[Texture2D]]=[None for i in range(ArmorIDs.Face.Count)]
	AccBalloon:list[Asset[Texture2D]]=[None for i in range(ArmorIDs.Balloon.Count)]
	AccBeard:list[Asset[Texture2D]]=[None for i in range(ArmorIDs.Beard.Count)]
	Pulley:Asset[Texture2D]=None# default value
	XmasTree:list[Asset[Texture2D]]=[None for i in range(5)]
	Flames:list[Asset[Texture2D]]=[None for i in range(18)]
	Timer:Asset[Texture2D]=None# default value
	Reforge:list[Asset[Texture2D]]=[None for i in range(2)]
	EmoteMenuButton:Asset[Texture2D]=None# default value
	BestiaryMenuButton:Asset[Texture2D]=None# default value
	WallOutline:Asset[Texture2D]=None# default value
	Actuator:Asset[Texture2D]=None# default value
	Wire:Asset[Texture2D]=None# default value
	Wire2:Asset[Texture2D]=None# default value
	Wire3:Asset[Texture2D]=None# default value
	Wire4:Asset[Texture2D]=None# default value
	WireNew:Asset[Texture2D]=None# default value
	Camera:list[Asset[Texture2D]]=[None for i in range(8)]
	FlyingCarpet:Asset[Texture2D]=None# default value
	Grid:Asset[Texture2D]=None# default value
	LightDisc:Asset[Texture2D]=None# default value
	EyeLaser:Asset[Texture2D]=None# default value
	BoneEyes:Asset[Texture2D]=None# default value
	BoneLaser:Asset[Texture2D]=None# default value
	Trash:Asset[Texture2D]=None# default value
	FishingLine:Asset[Texture2D]=None# default value
	Beetle:Asset[Texture2D]=None# default value
	Probe:Asset[Texture2D]=None# default value
	EyeLaserSmall:Asset[Texture2D]=None# default value
	XmasLight:Asset[Texture2D]=None# default value
	Golem:list[Asset[Texture2D]]=[None for i in range(4)]
	Confuse:Asset[Texture2D]=None# default value
	SunOrb:Asset[Texture2D]=None# default value
	SunAltar:Asset[Texture2D]=None# default value
	Chains:list[Asset[Texture2D]]=[None for i in range(ChainID.Count)]
	Chain:Asset[Texture2D]=None# default value
	GemChain:list[Asset[Texture2D]]=[None for i in range(7)]
	Chain2:Asset[Texture2D]=None# default value
	Chain3:Asset[Texture2D]=None# default value
	Chain4:Asset[Texture2D]=None# default value
	Chain5:Asset[Texture2D]=None# default value
	Chain6:Asset[Texture2D]=None# default value
	Chain7:Asset[Texture2D]=None# default value
	Chain8:Asset[Texture2D]=None# default value
	Chain9:Asset[Texture2D]=None# default value
	Chain10:Asset[Texture2D]=None# default value
	Chain11:Asset[Texture2D]=None# default value
	Chain12:Asset[Texture2D]=None# default value
	Chain13:Asset[Texture2D]=None# default value
	Chain14:Asset[Texture2D]=None# default value
	Chain15:Asset[Texture2D]=None# default value
	Chain16:Asset[Texture2D]=None# default value
	Chain17:Asset[Texture2D]=None# default value
	Chain18:Asset[Texture2D]=None# default value
	Chain19:Asset[Texture2D]=None# default value
	Chain20:Asset[Texture2D]=None# default value
	Chain21:Asset[Texture2D]=None# default value
	Chain22:Asset[Texture2D]=None# default value
	Chain23:Asset[Texture2D]=None# default value
	Chain24:Asset[Texture2D]=None# default value
	Chain25:Asset[Texture2D]=None# default value
	Chain26:Asset[Texture2D]=None# default value
	Chain27:Asset[Texture2D]=None# default value
	Chain28:Asset[Texture2D]=None# default value
	Chain29:Asset[Texture2D]=None# default value
	Chain30:Asset[Texture2D]=None# default value
	Chain31:Asset[Texture2D]=None# default value
	Chain32:Asset[Texture2D]=None# default value
	Chain33:Asset[Texture2D]=None# default value
	Chain34:Asset[Texture2D]=None# default value
	Chain35:Asset[Texture2D]=None# default value
	Chain36:Asset[Texture2D]=None# default value
	Chain37:Asset[Texture2D]=None# default value
	Chain38:Asset[Texture2D]=None# default value
	Chain39:Asset[Texture2D]=None# default value
	Chain40:Asset[Texture2D]=None# default value
	Chain41:Asset[Texture2D]=None# default value
	Chain42:Asset[Texture2D]=None# default value
	Chain43:Asset[Texture2D]=None# default value
	Hb1:Asset[Texture2D]=None# default value
	Hb2:Asset[Texture2D]=None# default value
	Chaos:Asset[Texture2D]=None# default value
	Cd:Asset[Texture2D]=None# default value
	Wof:Asset[Texture2D]=None# default value
	BoneArm:Asset[Texture2D]=None# default value
	BoneArm2:Asset[Texture2D]=None# default value
	BoneArm3:Asset[Texture2D]=None# default value
	PumpkingArm:Asset[Texture2D]=None# default value
	PumpkingCloak:Asset[Texture2D]=None# default value
	EquipPage:list[Asset[Texture2D]]=[None for i in range(11)]
	HouseBanner:Asset[Texture2D]=None# default value
	NPCHappiness:Asset[Texture2D]=None# default value
	Pvp:list[Asset[Texture2D]]=[None for i in range(3)]
	NpcToggle:list[Asset[Texture2D]]=[None for i in range(2)]
	HbLock:list[Asset[Texture2D]]=[None for i in range(2)]
	blockReplaceIcon:list[Asset[Texture2D]]=[None for i in range(2)]
	Buff:list[Asset[Texture2D]]=[None for i in range(BuffID.Count)]
	Item:list[Asset[Texture2D]]=[None for i in range(ItemID.Count)]
	ItemFlame:list[Asset[Texture2D]]=[None for i in range(ItemID.Count)]
	Npc:list[Asset[Texture2D]]=[None for i in range(NPCID.Count)]
	Projectile:list[Asset[Texture2D]]=[None for i in range(ProjectileID.Count)]
	Gore:list[Asset[Texture2D]]=[None for i in range(GoreID.Count)]
	BackPack:list[Asset[Texture2D]]=[None for i in range(10)]
	Rain:Asset[Texture2D]=None# default value
	GlowMask:list[Asset[Texture2D]]=[None for i in range(GlowMaskID.Count)]
	Extra:list[Asset[Texture2D]]=[None for i in range(ExtrasID.Count)]
	HighlightMask:list[Asset[Texture2D]]=[None for i in range(TileID.Count)]
	Coin:list[Asset[Texture2D]]=[None for i in range(4)]
	Cursors:list[Asset[Texture2D]]=[None for i in range(18)]
	CursorRadial:Asset[Texture2D]=None# default value
	Dust:Asset[Texture2D]=None# default value
	Sun:Asset[Texture2D]=None# default value
	Sun2:Asset[Texture2D]=None# default value
	Sun3:Asset[Texture2D]=None# default value
	Moon:list[Asset[Texture2D]]=[None for i in range(9)]
	SmileyMoon:Asset[Texture2D]=None# default value
	PumpkinMoon:Asset[Texture2D]=None# default value
	SnowMoon:Asset[Texture2D]=None# default value
	OneDropLogo:Asset[Texture2D]=None# default value
	Tile:list[Asset[Texture2D]]=[None for i in range(TileID.Count)]
	BlackTile:Asset[Texture2D]=None# default value
	Wall:list[Asset[Texture2D]]=[None for i in range(WallID.Count)]
	Background:list[Asset[Texture2D]]=[None for i in range(Main.maxBackgrounds)]
	Cloud:list[Asset[Texture2D]]=[None for i in range(CloudID.Count)]
	Star:list[Asset[Texture2D]]=[None for i in range(4)]
	Liquid:list[Asset[Texture2D]]=[None for i in range(15)]
	LiquidSlope:list[Asset[Texture2D]]=[None for i in range(15)]
	Heart:Asset[Texture2D]=None# default value
	Heart2:Asset[Texture2D]=None# default value
	Mana:Asset[Texture2D]=None# default value
	Bubble:Asset[Texture2D]=None# default value
	Flame:Asset[Texture2D]=None# default value
	CageTop:list[Asset[Texture2D]]=[None for i in range(5)]
	TreeTop:list[Asset[Texture2D]]=[None for i in range(32)]
	TreeBranch:list[Asset[Texture2D]]=[None for i in range(32)]
	Wood:list[Asset[Texture2D]]=[None for i in range(7)]
	ShroomCap:Asset[Texture2D]=None# default value
	InventoryBack:Asset[Texture2D]=None# default value
	InventoryBack2:Asset[Texture2D]=None# default value
	InventoryBack3:Asset[Texture2D]=None# default value
	InventoryBack4:Asset[Texture2D]=None# default value
	InventoryBack5:Asset[Texture2D]=None# default value
	InventoryBack6:Asset[Texture2D]=None# default value
	InventoryBack7:Asset[Texture2D]=None# default value
	InventoryBack8:Asset[Texture2D]=None# default value
	InventoryBack9:Asset[Texture2D]=None# default value
	InventoryBack10:Asset[Texture2D]=None# default value
	InventoryBack11:Asset[Texture2D]=None# default value
	InventoryBack12:Asset[Texture2D]=None# default value
	InventoryBack13:Asset[Texture2D]=None# default value
	InventoryBack14:Asset[Texture2D]=None# default value
	InventoryBack15:Asset[Texture2D]=None# default value
	InventoryBack16:Asset[Texture2D]=None# default value
	InventoryBack17:Asset[Texture2D]=None# default value
	InventoryBack18:Asset[Texture2D]=None# default value
	InventoryBack19:Asset[Texture2D]=None# default value
	InventoryBack20:Asset[Texture2D]=None# default value
	InventoryBack21:Asset[Texture2D]=None# default value
	InventoryBack22:Asset[Texture2D]=None# default value
	InventoryBack23:Asset[Texture2D]=None# default value
	InventoryBack24:Asset[Texture2D]=None# default value
	HairStyleBack:Asset[Texture2D]=None# default value
	ClothesStyleBack:Asset[Texture2D]=None# default value
	InventoryTickOn:Asset[Texture2D]=None# default value
	InventoryTickOff:Asset[Texture2D]=None# default value
	SplashTexture16x9:Asset[Texture2D]=None# default value
	SplashTexture4x3:Asset[Texture2D]=None# default value
	SplashTextureLegoBack:Asset[Texture2D]=None# default value
	SplashTextureLegoResonanace:Asset[Texture2D]=None# default value
	SplashTextureLegoTree:Asset[Texture2D]=None# default value
	SplashTextureLegoFront:Asset[Texture2D]=None# default value
	Logo:Asset[Texture2D]=None# default value
	Logo2:Asset[Texture2D]=None# default value
	Logo3:Asset[Texture2D]=None# default value
	Logo4:Asset[Texture2D]=None# default value
	Logo5:Asset[Texture2D]=None# default value
	Logo6:Asset[Texture2D]=None# default value
	TextBack:Asset[Texture2D]=None# default value
	Chat:Asset[Texture2D]=None# default value
	Chat2:Asset[Texture2D]=None# default value
	ChatBack:Asset[Texture2D]=None# default value
	Team:Asset[Texture2D]=None# default value
	Re:Asset[Texture2D]=None# default value
	Ra:Asset[Texture2D]=None# default value
	Splash:Asset[Texture2D]=None# default value
	Fade:Asset[Texture2D]=None# default value
	Ninja:Asset[Texture2D]=None# default value
	AntLion:Asset[Texture2D]=None# default value
	SpikeBase:Asset[Texture2D]=None# default value
	Ghost:Asset[Texture2D]=None# default value
	EvilCactus:Asset[Texture2D]=None# default value
	GoodCactus:Asset[Texture2D]=None# default value
	CrimsonCactus:Asset[Texture2D]=None# default value
	WraithEye:Asset[Texture2D]=None# default value
	Firefly:Asset[Texture2D]=None# default value
	FireflyJar:Asset[Texture2D]=None# default value
	Lightningbug:Asset[Texture2D]=None# default value
	LightningbugJar:Asset[Texture2D]=None# default value
	JellyfishBowl:list[Asset[Texture2D]]=[None for i in range(3)]
	GlowSnail:Asset[Texture2D]=None# default value
	IceQueen:Asset[Texture2D]=None# default value
	SantaTank:Asset[Texture2D]=None# default value
	ReaperEye:Asset[Texture2D]=None# default value
	JackHat:Asset[Texture2D]=None# default value
	TreeFace:Asset[Texture2D]=None# default value
	PumpkingFace:Asset[Texture2D]=None# default value
	DukeFishron:Asset[Texture2D]=None# default value
	PlayerHair:list[Asset[Texture2D]]=[None for i in range(228)]
	PlayerHairAlt:list[Asset[Texture2D]]=[None for i in range(228)]
	LoadingSunflower:Asset[Texture2D]=None# default value
	GolfSwingBarPanel:Asset[Texture2D]=None# default value
	GolfSwingBarFill:Asset[Texture2D]=None# default value
	SpawnPoint:Asset[Texture2D]=None# default value
	SpawnBed:Asset[Texture2D]=None# default value
	GolfBallArrow:Asset[Texture2D]=None# default value
	GolfBallArrowShadow:Asset[Texture2D]=None# default value
	GolfBallOutline:Asset[Texture2D]=None# default value
	TexturePackButtons:Asset[Texture2D]=None# default value
	NpcPortraitBackground:Asset[Texture2D]=None# default value
x=getFunctionContents("Terraria.Initializers.AssetInitializer","private static void LoadTextures(AssetRequestMode mode)").replace("AssetInitializer.LoadAsset<Texture2D>","Asset[Texture2D]")
#print(x)
x=x.replace("(AssetRequestMode)","")
currentvars={"x":None,"this":None,"true":True,"false":False,"Item":ItemMethods,"ItemID":ItemID,"TileID":TileID,"null":None,"variant":None,"GameShaders":GameShadersMethods,"Main":Main,"Mount":MountHolder,"MountData":MountData,"MountID":MountID,"MountDelegatesData":MountDelegatesData,"TextureAssets":TextureAssets,"Vector2":Vector2,"Vector3":Vector3,"Asset":Asset,"Texture2D":Texture2D,"mode":None,"BuffID":BuffID,"ExtrasID":ExtrasID}
#print("\n"*50)
y2=keepOnlyContentsWhen(x,"_sodnbsoidh","")[0]
"""s=""
for i in getVariablesOfType("Terraria.ID.SoundID","public static readonly LegacySoundStyle "):
	x=getVariable("Terraria.ID.SoundID","public static readonly LegacySoundStyle "+i)
	if("CreateTrackable" in x):
		s+="#"
	s+=(i+":SoundStyle="+x.replace("new ","")+"\n")
for i in range(10):
	s=s.replace(str(i)+"f",str(i))
import pyperclip
pyperclip.copy(s)
raise Exception"""
#print(currentvars['TextureAssets'].Chain35)
#print(currentvars['TextureAssets'].Tile)
#raise Exception
for i in [i for i in vartypes]:
	vartypes[i+"[]"]=("list["+vartypes[i][0]+"]",None)
	vartypes["List<"+i+">"]=("List["+vartypes[i][0]+"]",None)

"""x=[i for i in [j.strip() for i in x.split("public") for j in i.split("private")] if i.__len__()!=0]
x=["\n".join([j for j in [j.strip() for j in i.split("\n")] if j[0:2]!="//"]) for i in x]
y=""
y_s=""
y_f=""
for i in x:
	if(i[-1]==';'):
		i=i[:-1]
		if(i[0:3]!='for'):
			if("=>" in i):
				if(i.split(" ")[0] in ["static"]):
					i=" ".join(i.split(" ")[1:])
				y_f+="@property\ndef "+i.split(" ")[1]+"(this)->"+vartypes[i.split(" ")[0]][0]+":\n\treturn "+i.split("=>")[1].strip()+"\n"
			else:
				if(i.split(" ")[0] in ["static","const"]):
					i=" ".join(i.split(" ")[1:])
					y_s+=i.split(" ")[1]+":"+vartypes[i.split(" ")[0]][0]+"="+(i.split("=")[1].strip() if "=" in i else (str(vartypes[i.split(" ")[0]][1])+"# default value"))+"\n"
				else:
					y+="this."+i.split(" ")[1]+":"+vartypes[i.split(" ")[0]][0]+"="+(i.split("=")[1].strip() if "=" in i else (str(vartypes[i.split(" ")[0]][1])+"# default value"))+"\n"
	elif(i[-1]=="}"):
		j=splitWhilstRespectingBrackets(i," ")[-1]
		j=j[1:-1].strip()
		if(j[0:3]=="get"):
			j=j[3:].strip()
			y_f+="@property\ndef "+i.split(" ")[1]+"()->"+vartypes[i.split(" ")[0]][0]+":\n\t"+j[1:-1].replace("\n\t\t","\n")+"\n"
print(y_s)
print("-----")
print(y)
print("-----")
print(y_f)"""

#getItemInitLines(3005)
#raise Exception#"""
x=getFunctionContents("Terraria.Mount","public static void Initialize()").replace("Asset<Texture2D>","Asset[Texture2D]")
x="\n".join([i for i in x.split("\n") if "ref " not in i])
x=x.split("new MountData[")[0]+"".join(["[None for i in range("+i[0][:i[1]-1]+")]"+i[0][i[1]:] for i in [[i,findLinkedBracket("["+i)] for i in x.split("new MountData[")[1:]]])
x=x.split("new int[")[0]+"".join(["[0 for i in range("+i[0][:i[1]-1]+")]"+i[0][i[1]:] for i in [[i,findLinkedBracket("["+i)] for i in x.split("new int[")[1:]]])
x=x.split("new Vector2[")[0]+"".join(["[None for i in range("+i[0][:i[1]-1]+")]"+i[0][i[1]:] for i in [[i,findLinkedBracket("["+i)] for i in x.split("new Vector2[")[1:]]])
x=x.replace("throw new Exception","//")
#print(x)

y2=keepOnlyContentsWhen(x,"thisisntavar",None)[0]
#print(currentvars)
MountHolder=currentvars["Mount"]
#print(vars(MountHolder.mounts[54]))
#v=vars(y[0])
#v2=vars(ItemHolder.default)
#print({i:v[i] for i in v if v[i]!=v2[i]})
#print(ContentSamplesMethods.ItemsByType[1037])
#print(ItemID.itemsByName[1037])
#MountHolder.fromTypeInd(54)
#print(ContentSamplesMethods.mounts[54].UpdateFrameMethod)
#print("----")
#print(ContentSamplesMethods.mounts[54].SetMountMethod)
#print(MountID.mountsByName[54])
#print("C:\\StuffAndThings\\itemportgen")

#raise Exception
mountBase="""using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using ReLogic.Content;
using System;
using System.Collections.Generic;
using System.Linq;
using Terraria;
using Terraria.DataStructures;
using Terraria.ModLoader;
using Terraria.ID;

namespace BiggerAndBoulderContentBackport.Content.Items.Mounts
{
	public class &__0_ : ModMount
	{
		&__1_

		public override void SetStaticDefaults() {
			&__2_

			if (!Main.dedServ) {
				//MountData.textureWidth = MountData.backTexture.Width();
				//MountData.textureHeight = MountData.backTexture.Height();
			}
		}

		public override void UpdateEffects(Player mountedPlayer) {
			&__3_
		}

		public override void SetMount(Player mountedPlayer, ref bool skipDust) {
			&__4_
		}
		public override bool UpdateFrame(Player mountedPlayer, int state, Vector2 velocity) {
			&__5_
		}
	}
}"""

contentDir=r"C:\\StuffAndThings\\Downloads\\TerrariaAssets_1_4_5_6\\"


import shutil
print("\n\n\n") 
drawbar(0,3,"-")
drawbar(0,2,"-")
drawbar(0,1,"-")
drawbar(0,3,"Porting Tiles",0.5)
tilesDir=r"C:\Users\neroa\OneDrive\Documents\My Games\Terraria\tModLoader\ModSources\BiggerAndBoulderContentBackport\Content\Tiles"+"\\"
for i in range(TileID.OldCount,TileID.Count):
	drawbar((i-TileID.OldCount)/(TileID.Count-TileID.OldCount),2,"Porting "+TileID.tilesByName[i])
	v="using Microsoft.Xna.Framework;\nusing Terraria;\nusing Terraria.ID;\nusing Terraria.ModLoader;\n\nnamespace BiggerAndBoulderContentBackport.Content.Tiles\n{\n\tpublic class "+TileID.tilesByName[i]+" : ModTile\n\t{\n\t\tpublic override void SetStaticDefaults() {"
	for j in ["tileLighted","tileMergeDirt","tileCut","tileAlch","tileShine2","tileStone","tileAxe","tileHammer","tileWaterDeath","tileLavaDeath","tileTable","tileBlockLight","tileNoSunLight","tileDungeon","tileSpelunker","tileSolidTop","tileSolid","tileBouncy","tileRope","tileBrick","tileMoss","tileNoAttach","tileNoFail","tileCracked","tileObsidianKill","tileFrameImportant","tilePile","tileBlendAll","tileContainer","tileSign","tileSand","tileFlame"]:
		if(vars(Main)[j][i]==True):
			v+="\n\t\t\tMain."+j+"[Type] = true;"
	v+="\n"+"\n\t\t\tAddMapEntry(new Color(200, 200, 200));\n\t\t}\n\t}\n}"
	n=open(tilesDir+TileID.tilesByName[i]+".cs","w")
	n.write("//Tiles are currently incomplete.")
	#n.write(v)
	n.close()
	
	shutil.copy(contentDir+TextureAssets.Tile[i]._name.replace("Images/","")+".png", tilesDir+TileID.tilesByName[i]+".png")
drawbar(0.5,3,"Porting Items",1)
itemsDir=r"C:\Users\neroa\OneDrive\Documents\My Games\Terraria\tModLoader\ModSources\BiggerAndBoulderContentBackport\Content\Items"+"\\"
itemssuccess=0
itemsfail=0
itemstotal=(ItemID.Count-ItemID.OldCount)
for i in range(ItemID.OldCount,ItemID.Count):
	drawbarwithLosses((itemssuccess)/(itemstotal),2,"Porting "+ItemID.itemsByName[i],(itemsfail)/(itemstotal))
	z=ContentSamplesMethods.ItemDefLinesByType[i]
	if(ContentSamplesMethods.ItemsByType[i].shoot!=0):
		n=open(itemsDir+ItemID.itemsByName[i]+".cs","w")
		n.write("//Projectiles spawning items are not supported at this moment")
		n.close()
		itemsfail+=1
		#itemssuccess-=1
		continue
	if(ContentSamplesMethods.ItemsByType[i].mountType!=-1):
		t=ContentSamplesMethods.ItemsByType[i].mountType
		MountHolder.fromTypeInd(t,"Loading Mount "+MountID.mountsByName[t])
		v=vars(ContentSamplesMethods.mounts[t])
		v={i:v[i] for i in v if i not in ["extraFall","walkingGraceTimeMax","dismountsOnItemUse","CanRideMinecartTracks","CanUseWings"]}
		b=None if MountHolder.mounts[t].buff==0 else BuffID.buffsByName[MountHolder.mounts[t].buff]
		c=mountBase.replace("&__0_",MountID.mountsByName[t]).replace("&__1_","").replace("&__2_","\n\t\t\t".join(["MountData."+j+" = "+str(v[j])+";" for j in v if ((j!="buff")|(b==None))&(type(v[j])==type(56))]+
		                                                                                                       ["MountData."+j+" = "+str(v[j])+"f;" for j in v if isinstance(v[j],float)]+
																											   ["MountData."+j+" = true;" if v[j]==True else "MountData."+j+" = false;" for j in v if type(v[j])==type(True)]+
																											   ["MountData."+j+" = "+str(v[j])+";" for j in v if isinstance(v[j],list)]+
																											   [i for i in ["MountData.buff = ModContent.BuffType<Buffs."+b+">();" if b!=None else None] if i!=None])).replace("&__3_",ContentSamplesMethods.mounts[t].UpdateEffectsMethod.replace("\n","\n\t\t\t").replace("this","mountedPlayer.mount").replace("mountedPlayer.IsAllowedToHoldItems = false;","//mountedPlayer.IsAllowedToHoldItems = false;")).replace("&__4_",ContentSamplesMethods.mounts[t].SetMountMethod.replace("\n","\n\t\t\t").replace("this","mountedPlayer.mount").replace("player","mountedPlayer").split("mountedPlayer.mount._flipDraw = false;")[1].replace("MountDelegatesData.OverrideSizeMethod mountedPlayerSize = mountedPlayer.mount._data.delegations.PlayerSize;","ExtraMountDelegates.OverrideSizeMethod mountedPlayerSize = ExtraMountDelegates.PlayerSize(ModContent.MountType<"+MountID.mountsByName[t]+">());").replace("mountedPlayer.mount.DoSpawnDust(mountedPlayer, isDismounting: false);","")).replace("&__5_",ContentSamplesMethods.mounts[t].UpdateFrameMethod[:ContentSamplesMethods.mounts[t].UpdateFrameMethod.index("switch (state)")].replace("\n","\n\t\t\t").replace("this","mountedPlayer.mount").split("mountedPlayer.mount._walkingGraceTimeLeft = 0;")[1].strip()[1:]+"\n\t\t\treturn false;")
		#n=open(itemsDir.replace("Items\\","Mount\\")+MountID.mountsByName[t]+".cs","w")
		#n.write(c)
		#n.close()
		m=ContentSamplesMethods.mounts[t]
		if(m.backTexture!=None):
			if (m.backTexture._name!=""):
				shutil.copy(contentDir+m.backTexture._name.replace("Images\\","")+".png", itemsDir.replace("Items\\","Items\\Mounts\\")+MountID.mountsByName[t]+"_Back.png")
		if(m.frontTexture!=None):
			if (m.frontTexture._name!=""):
				shutil.copy(contentDir+m.frontTexture._name.replace("Images\\","")+".png", itemsDir.replace("Items\\","Items\\Mounts\\")+MountID.mountsByName[t]+"_Front.png")
		if(m.backTextureExtra!=None):
			if (m.backTextureExtra._name!=""):
				shutil.copy(contentDir+m.backTexture._name.replace("Images\\","")+".png", itemsDir.replace("Items\\","Items\\Mounts\\")+MountID.mountsByName[t]+"_BackExtra.png")
		if(m.frontTextureExtra!=None):
			if (m.frontTextureExtra._name!=""):
				shutil.copy(contentDir+m.frontTexture._name.replace("Images\\","")+".png", itemsDir.replace("Items\\","Items\\Mounts\\")+MountID.mountsByName[t]+"_FrontExtra.png")
		if(b!=None):
			drawbar(0.5,1,"Loading Buff "+BuffID.buffsByName[MountHolder.mounts[t].buff])
			n=open(itemsDir.replace("Items\\","Buffs\\")+b+".cs","w")
			n.write("""using Terraria;
using Terraria.ModLoader;
using BiggerAndBoulderContentBackport.Content.Items.Mounts;

namespace BiggerAndBoulderContentBackport.Content.Buffs
{
	public class """+b+""" : ModBuff
	{
		public override void SetStaticDefaults() {
			Main.buffNoTimeDisplay[Type] = true; // The time remaining won't display on this buff
			Main.buffNoSave[Type] = true; // This buff won't save when you exit the world
		}

		public override void Update(Player player, ref int buffIndex) {
			player.mount.SetMount(ModContent.MountType<"""+MountID.mountsByName[t]+""">(), player);
			player.buffTime[buffIndex] = 10; // reset buff time
		}
	}
}""")
			n.close()
			shutil.copy(contentDir+TextureAssets.Buff[MountHolder.mounts[t].buff]._name.replace("Images\\","")+".png", itemsDir.replace("Items\\","Buffs\\")+BuffID.buffsByName[MountHolder.mounts[t].buff]+".png")
			drawbar(0,1,"-")
		
		#continue
	if(("DefaultToPlaceableTile" in z)|(ContentSamplesMethods.ItemsByType[i].createTile!=-1)):
		n=open(itemsDir+ItemID.itemsByName[i]+".cs","w")
		n.write("//Tile items are not supported at this moment")
		n.close()
		itemsfail+=1
		#itemssuccess-=1
		continue
	if(("DefaultToPlaceableWall" in z)|(ContentSamplesMethods.ItemsByType[i].createWall!=-1)):
		n=open(itemsDir+ItemID.itemsByName[i]+".cs","w")
		n.write("//wall items are not supported at this moment")
		n.close()
		itemsfail+=1
		#itemssuccess-=1
		continue
	if(("DefaultToWhip" in z)):
		n=open(itemsDir+ItemID.itemsByName[i]+".cs","w")
		n.write("//whips are not supported at this moment")
		n.close()
		itemsfail+=1
		#itemssuccess-=1
		continue
	if(("DefaultToRangedWeapon" in z)):
		n=open(itemsDir+ItemID.itemsByName[i]+".cs","w")
		n.write("//ranged weapons are not supported at this moment")
		n.close()
		itemsfail+=1
		#itemssuccess-=1
		continue
	if(("DefaultToMonolith" in z)):
		n=open(itemsDir+ItemID.itemsByName[i]+".cs","w")
		n.write("//monoliths are not supported at this moment")
		n.close()
		itemsfail+=1
		#itemssuccess-=1
		continue
	if(("DefaultToVanitypet" in z)):
		n=open(itemsDir+ItemID.itemsByName[i]+".cs","w")
		n.write("//vanity pets are not supported at this moment")
		n.close()
		itemsfail+=1
		#itemssuccess-=1
		continue
	if(("DefaultToVoiceOverrideAccessory" in z)):
		n=open(itemsDir+ItemID.itemsByName[i]+".cs","w")
		n.write("//voice change items are not supported at this moment")
		n.close()
		itemsfail+=1
		#itemssuccess-=1
		continue
	if(("DefaultToMusicBox" in z)):
		n=open(itemsDir+ItemID.itemsByName[i]+".cs","w")
		n.write("//music boxes are not supported at this moment")
		n.close()
		itemsfail+=1
		#itemssuccess-=1
		continue
	if(("DefaultToCapturedCritter" in z)):
		n=open(itemsDir+ItemID.itemsByName[i]+".cs","w")
		n.write("//captured critters are not supported at this moment")
		n.close()
		itemsfail+=1
		#itemssuccess-=1
		continue
	if(("DefaultToBomb" in z)):
		n=open(itemsDir+ItemID.itemsByName[i]+".cs","w")
		n.write("//explosives are, unfortunately, not supported at this moment")
		n.close()
		itemsfail+=1
		#itemssuccess-=1
		continue
	if(("DefaultToBody" in z)):
		n=open(itemsDir+ItemID.itemsByName[i]+".cs","w")
		n.write("//shirts are not supported at this moment")
		n.close()
		itemsfail+=1
		#itemssuccess-=1
		continue
	if(("DefaultToHead" in z)):
		n=open(itemsDir+ItemID.itemsByName[i]+".cs","w")
		n.write("//hats are not supported at this moment")
		n.close()
		itemsfail+=1
		#itemssuccess-=1
		continue
	if(("DefaultToLegs" in z)):
		n=open(itemsDir+ItemID.itemsByName[i]+".cs","w")
		n.write("//leggings are not supported at this moment")
		n.close()
		itemsfail+=1
		#itemssuccess-=1
		continue
	if(("DefaultToBanner" in z)):
		n=open(itemsDir+ItemID.itemsByName[i]+".cs","w")
		n.write("//mob banners are not supported at this moment")
		n.close()
		itemsfail+=1
		#itemssuccess-=1
		continue
	
	if((".accessory =" in z)):
		n=open(itemsDir+ItemID.itemsByName[i]+".cs","w")
		n.write("//accessories are not supported at this moment")
		n.close()
		itemsfail+=1
		#itemssuccess-=1
		continue
	slots=["handOnSlot","handOffSlot","backSlot","frontSlot","shoeSlot","waistSlot","wingSlot","shieldSlot","neckSlot","faceSlot","balloonSlot","beardSlot","bodySlot","legSlot","headSlot"]
	sc=False
	for slot in slots:
		if(vars(ContentSamplesMethods.ItemsByType[i])[slot]!=-1):
			n=open(itemsDir+ItemID.itemsByName[i]+".cs","w")
			n.write("//items with "+slot+" are not supported at this moment")
			n.close()
			sc=True
			break
	if(sc):
		itemsfail+=1
		#itemssuccess-=1
		continue
	v="using Microsoft.Xna.Framework;\nusing Terraria;\nusing Terraria.ID;\nusing Terraria.Enums;\nusing Terraria.ModLoader;\nusing Terraria.Audio;\nusing BiggerAndBoulderContentBackport.Content.Items.Mounts;\n\nnamespace BiggerAndBoulderContentBackport.Content.Items\n{\n\tpublic class "+ItemID.itemsByName[i]+" : ModItem\n\t{\n\t\tpublic override void SetDefaults() {"
	
	z=z.split(";")
	for j in range(z.__len__()):
		z[j]=z[j].strip()
		if("this.DefaultToRangedWeapon(" in z[j]):
			z[j]=z[j].replace("this.DefaultToRangedWeapon("+z[j][z[j].index("(")+1:z[j].index(",") if "," in z[j] else -1],"this.DefaultToRangedWeapon(ModContent.ProjectileType<Projectiles."+ProjectileID.projectilesByName[int(z[j][z[j].index("(")+1:z[j].index(",") if "," in z[j] else -1])]+">()")
		if("this.DefaultToPlaceableTile(" in z[j]):
			z[j]=z[j].replace("this.DefaultToPlaceableTile("+z[j][z[j].index("(")+1:z[j].index(",") if "," in z[j] else -1],"this.DefaultToPlaceableTile(ModContent.TileType<Tiles."+TileID.tilesByName[calcformula(z[j][z[j].index("(")+1:z[j].index(",") if "," in z[j] else -1].replace("(ushort)",""))]+">()")
	z=";\n".join(z)
	if("this.mountType" in z):
		z=z.replace("this.mountType = "+str(ContentSamplesMethods.ItemsByType[i].mountType)+";","Item.mountType = ModContent.MountType<"+MountID.mountsByName[t]+">();")
	if("this.UseSound =") in z:
		z=z.split("this.UseSound =")
		a=(z[1].split(";")[0])
		if(ContentSamplesMethods.ItemsByType[i].UseSound==None):
			currentvars['SoundID']=SoundID
			ContentSamplesMethods.ItemsByType[i].UseSound=calcformula(a.strip())
		if(ContentSamplesMethods.ItemsByType[i].UseSound==None):
			print(a.strip())
		z=("this.UseSound = "+ContentSamplesMethods.ItemsByType[i].UseSound.toString()+";").join([z[0],";".join(z[1].split(";")[1:])])
	z=z.replace("this.dye = (byte)GameShaders.Armor.GetShaderIdFromItemId(this.type);\n","this.dye = "+str(ContentSamplesMethods.ItemsByType[i].dye)+";\n" if ContentSamplesMethods.ItemsByType[i].dye!=-1 else "")
	z=z.replace("this.hairDye = GameShaders.Hair.GetShaderIdFromItemId(this.type);\n","this.hairDye = "+str(ContentSamplesMethods.ItemsByType[i].hairDye)+";\n" if ContentSamplesMethods.ItemsByType[i].hairDye!=-1 else "")
	
	z=z.replace("this.","Item.")
	v+=z
	v+="\n"+"\n\t\t}"
	v+="\n\t\tpublic override void SetStaticDefaults() {"
	l=vars(ItemID.Sets)
	for j in l:
		if(j not in ["DualEquipArmor","ReceivesDiagonalCorrectionAsFakeFish","ShootsOnUseRelease","NoMeleeSpeedBonus","RapidAttackBonusDamage","CanBeExtractinated","Moss","ShimmerPostMoonlord","PlaceTileOnAltUse","SummonerWeaponThatScalesWithAttackSpeed","FakeFishInanimate","IsBasicFish","IsAVoiceChangeItem","IsQuestFish","ErrorWorldChestSwapImmunity","NeverLocksOn","Campfires","HasItemSwap","RecoverableImportantItem","HasRightFire","IsWireableStatue"]):
			if(type(l[j])==type([1,2,3])):
				if(l[j][i]==True):
					v+="\n\t\t\tItemID.Sets."+j+"[Type] = true;"
				elif(l[j][i]==False):
					v+="\n\t\t\tItemID.Sets."+j+"[Type] = false;"
	v+="\n\t\t}"
	v+="\n\t\tpublic override void AddRecipes(){"
	for recipe in Main.recipe:
		if(recipe!=None):
			if(recipe.createItem._item==i):
				v+=recipe.Stringify()
	v+="\n\t\t}"
	v+="\n\t}\n}"
	#print(itemsDir+ItemID.itemsByName[i]+".cs")
	#if("acorn" in ItemID.itemsByName[i].lower()):
	#	raise Exception()
	n=open(itemsDir+ItemID.itemsByName[i]+".cs","w")
	n.write(v)
	n.close()
	shutil.copy(contentDir+TextureAssets.Item[i]._name.replace("Images/","")+".png", itemsDir+ItemID.itemsByName[i]+".png")
	itemssuccess+=1
drawbar(1,3,"Porting Done")
