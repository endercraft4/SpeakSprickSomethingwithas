def Desteps():
  if (de_list.index(word)):
	#uses German (De) space see english and Russian
	word_index = de_list.index(word)
	if lang2.upper == "ENGLIS" #add English equivilant
	new_sentance = new_sentance + en_list[word_index]
		  
	elif lang2.upper == "RUSSIAN": #else add Russian equivilant
	new_sentance = new_sentance + russian_list[word_index]
			
	elif lang2.upper == "GERMAN": #add German e
	new_sentance = new_sentance + de_list[word_index]
	return new_sentance

def DeSoundsStuff():
  if (de_list.index(word)):
    #uses RUssian space 1,2,4,5?
	word_index = de_list.index(word)
    if lang2.upper == "ENGLIS" #add English equivilant
    sound_file = new_sentance + en_sounds[word_index]
		  
    elif lang2.upper == "RUSSIAN": #else add Russian equivilant
    sound_file = newsentance + RUssianSoundsList[word]
			
	elif lang2.upper == "GERMAN": #add German e
	sound_file = newsentance + DeSounds[wordS]
	
	return soundfile
