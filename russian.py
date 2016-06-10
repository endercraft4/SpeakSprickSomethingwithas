#Russian
def russian_langs(word):
	#see if word is in russian 
    if (russian_list.index(word)):
        #uses RUssian space 1,2,4,5?
	    word_index = russian_list.index(word)
        if lang2.upper == "ENGLIS" #add English equivilant
            new_sentance = new_sentance + en_list[wordS]
		  
        elif lang2.upper == "RUSSIAN": #else add Russian equivilant
            newsentance = newsentance + russian_list[wordS]
			
	    elif lang2.upper == "GERMAN": #add German e
	        new_sentance = new_sentance + de_list[wordS]
		  
		    #add NEw Russian 2 ? new words here



def russian_langs_Audio(word):
	''' Selects audio file from a list
		Russian'''
	
    if (russian_list.index(word)):
        #uses RUssian space 1,2,4,5?
	    word_index = russian_list.index(word)
        if lang2.upper == "ENGLIS" #add English equivilant
            sound_file = new_sentance + en_sounds[word_index]
		  
        elif lang2.upper == "RUSSIAN": #else add Russian equivilant
            sound_file = new_sentance + russian_sounds_list[word_index]
			
	    elif lang2.upper == "GERMAN": #add German e
	        sound_file = new_sentance + de_sounds[word_index]
	
	    return sound_file


class SLangs:
  
    # Langs
    def __init__(self, self.one = "one", self.two = "two", three, four, five, six, seven, eight, nine, ten, eleven, twelve):
      self.one = one
      self.two = two

    #sounds
    def russian_Audi(self,sound_file = "\sounds"):
	  self.sound_file = sound_file
	
	  play_File = WaveObject.from_wav_file(self.soundfile)
	
	  
	  

#Russian	
russians = Slangs("what is", "" "and so on")
