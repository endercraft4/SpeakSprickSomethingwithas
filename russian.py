#Russian
def RussianLangs():
  if (RUssianList.index(word)):
    #uses RUssian space 1,2,4,5?
	wordS = RUssianList.index(word)
    if lang2.upper == "ENGLIS" #add English equivilant
    newsentance = newsentance + enList[wordS]
		  
    elif lang2.upper == "RUSSIAN": #else add Russian equivilant
    newsentance = newsentance + RUssianList[wordS]
			
	elif lang2.upper == "GERMAN": #add German e
	newsentance = newsentance + DeList[wordS]
		  
		#add NEw Russian 2 ? new words here

def RussianLangsAudio():
  if (RUssianList.index(word)):
    #uses RUssian space 1,2,4,5?
	wordS = RUssianList.index(word)
    if lang2.upper == "ENGLIS" #add English equivilant
    soundfile = newsentance + EnSounds[wordS]
		  
    elif lang2.upper == "RUSSIAN": #else add Russian equivilant
    soundfile = newsentance + RUssianSoundsList[wordS]
			
	elif lang2.upper == "GERMAN": #add German e
	soundfile = newsentance + DeSounds[wordS]
	
	return soundfile

class SLangs:
  
  # Langs
  def __init__(self, self.one = "one", self.two = "two", three, four, five, six, seven, eight, nine, ten, eleven, twelve):
    self.one = one
    self.two = two

  #sounds
  def RussianAudi(self,soundfile = "\sounds"):
	self.soundfile = soundfile
	
	playFile = WaveObject.from_wav_file(self.soundfile)
	
	  
	  

#Russian	
russians = Slangs("what is", "" "and so on")
