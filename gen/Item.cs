true=True

class ItemID:
	Count=6145
	NumItemsInPrevVersion=5456
class ItemID:
	Count=6145
	NumItemsInPrevVersion=5456
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
y=ItemHolder.fromTypeInd(5456)
v=vars(y)
v2=vars(ItemHolder.default)
print({i:v[i] for i in v if v[i]!=v2[i]})
print(ItemID.itemsByName[5456])
print("C:\\StuffAndThings\\itemportgen")
