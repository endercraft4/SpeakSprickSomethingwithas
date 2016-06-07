#!
import Adafruit_CharLCD as LCD
import time
import Langs as langs

def __init__():
	# Raspberry Pi pin configuration:
  lcd_rs        = 27  # Note this might need to be changed to 21 for older revision Pi's.
  lcd_en        = 22
  lcd_d4        = 25
  lcd_d5        = 24
  lcd_d6        = 23
  lcd_d7        = 18
  lcd_backlight = 4


  # Define LCD column and row size for 16x2 LCD.
  lcd_columns = 16
  lcd_rows    = 2

  # Initialize the LCD using the pins above.
  lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                             lcd_columns, lcd_rows, lcd_backlight)



#Not Needed?
#def langFiles():
  
  #file
  
  #start of program
def getLangs():
  #starting Language and their"2" lang
  langUsing = input(lcd.message("Start Lang?\n")
    
  lcd.clear()
  lang2 = input(lcd.message("their Lang?")
  lcd.clear()

def sup():
  while (true):
	#sets up the albility to restart without powering down
	stopprogram = 0
	
    while(!stopprogram):
	
      stringInput = (lcd.message('Start Typing'))
    
	  if inputStuff.lower == "stop"
		!stopprogram = True
		break
      #separate the string in spaces
      inputStuff = stringInput.separate (" ")
    
      #
      #make lower or use lowercase
      for word in inputStuff.upper:
		
#Todo, Separate #Sure is spelled right Separate #  segmants into defs in another file for ease and sigh


		  #use file to find array? wie? How? add new lang here with check for word
		  #Not in lists
	    if (!word in enList and !word in RUList and !word in DeList):
		  lcd.message("Does not exit.")
		  delay(200)
		  lcd.clear()
		  addis = input("Type ADD 2 ADD \n or No")
		  #Add Three, English, Russian and G
		  #If not sure ?
			
			#Replace with top of enLang() then enLang, remove
		#English
		if (En.index(word)):
	      enLang()
	   
			
			
	    #Russian
	    elif (RussianList.index(word)):
		  RussianLangs()
		
		
		elif (DEList.index(word)):
		  Desteps()
	  	  
	  	
	  #Shows new sentance
	  #TODO add Scrolling
	  lcd.message(newsentance)
	  
	  
	  #asks if play
	  playSno = input(lcd.message("Play audio?"))
		# != and instead of or
	  if playSno.lower != "n" and playSno.lower != "no":
	    playAudio()
	    
	    
	stopprogram = False
  return 0
  
def playAudio():
  for word in inputStuff.upper():
	  #similar to the enLang() and RussianLangs() stuff
    if (En.
    sounds = WaveObject.from_wav_file(enLangounds())
  
    #Russian
    elif (RUssianList.index(word)):
    sounds = WaveObject.from_wav_file(russianLangsAudio())
  
    #German de
    else:
	    #check spe
	  if (DElist.index(word)):
        sounds = WaveObject.from_wav_file(DesoundsList())
  
      #USE?
    #sounds = WaveObject.from_wav_file(soundfile)
    sounds.play()
    if (PlayObject.Playing != True):
	  #stops ALL incase it is
	  
  #whenfinished 
    #return True
  
  
  
getLangs()
sup()
