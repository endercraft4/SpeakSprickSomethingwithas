def Desteps():
  if (DeList.index(word)):
	#uses German (De) space see english and Russian
	wordS = DeList.index(word)
	if lang2.upper == "ENGLIS" #add English equivilant
	newsentance = newsentance + enList[wordS]
		  
	elif lang2.upper == "RUSSIAN": #else add Russian equivilant
	newsentance = newsentance + RUssianList[wordS]
			
	elif lang2.upper == "GERMAN": #add German e
	newsentance = newsentance + DeList[wordS]

def DeSoundsStuff():
  if (DeList.index(word)):
    #uses RUssian space 1,2,4,5?
	wordS = DeList.index(word)
    if lang2.upper == "ENGLIS" #add English equivilant
    soundfile = newsentance + EnSounds[wordS]
		  
    elif lang2.upper == "RUSSIAN": #else add Russian equivilant
    soundfile = newsentance + RUssianSoundsList[wordS]
			
	elif lang2.upper == "GERMAN": #add German e
	soundfile = newsentance + DeSounds[wordS]
	
	return soundfile
