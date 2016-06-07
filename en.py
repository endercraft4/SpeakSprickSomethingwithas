
#change to zero.wav, "one.wav with the folder in the mainPy file.  
#sound1 = "/sounds/" + ? enSounds.(word)    JJFOASFJOS(sound1)
enList = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "HI", "ALL", "HOW", "ARE", "YOU" "LOVE" ]
EnSounds = ["/sounds/zero.wav", "/sounds/one.wav"]
def enLang():
  #En or ENList? should name?
  if (En.index(word)): 
    #space where word is
    wordS = En.index(word)
	  
	  
	#English
	if lang2.upper == "ENGLIS" #add English equivilant
      newsentance = newsentance + enList[wordS]
	  
	elif lang2.upper == "RUSSIAN": #else add Russian equivilant
	  newsentance = newsentance + RUssianList[wordS]
		
	elif lang2.upper == "GERMAN": #add German e
      newsentance = newsentance + DeList[wordS]

		#add languages from english 2 new here
def enLangound():
  if (En.index(word)):
    #uses RUssian space 1,2,4,5?
	wordS = En.index(word)
    if lang2.upper == "ENGLIS" #add English equivilant
    soundfile = newsentance + EnSounds[wordS]
		  
    elif lang2.upper == "RUSSIAN": #else add Russian equivilant
    soundfile = newsentance + RUssianSoundsList[wordS]
			
	elif lang2.upper == "GERMAN": #add German e
	soundfile = newsentance + DeSounds[wordS]
	
	
	return soundfile
