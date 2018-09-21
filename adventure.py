# REM: A sleeping adventure
# Kevin Xie CS550 Created 09/17/2018

# Sources:
# 	ASCII Art: https://www.asciiart.eu/
#	ASCII Text: https://patorjk.com/software/taag/
# On my Honor, I have neither given nor received unauthorized aid.

import random # for RNG game mechanics
import time # pauses for more human storytelling

name = None # global variable that can be used in any function (to refer to player)
countdown = 45 # player's ticking timer mechanic
location = "spawn" # current location
locations = ["spawn", "armory"] # array of possible locations
teamSize = 0

def start(): # setting the stage and call to action
	global name
	print("""\n\n\n\n                             Z             
	                       Z                   
	        .,.,        z           
	      (((((())    z             
	     ((('_  _`) '               
	     ((G   \\ |)                 
	    (((`   " ,                  
	     .((\\.:~:          .--------------.    
	     __.| `"'.__      | \\              |     
	  .~~   `---'   ~.    |  .             :     
	 /                `   |   `-.__________)     
	|             ~       |  :             :   
	|                     |  :  |              
	|    _                |     |   [ ##   :   
	 \\    ~~-.            |  ,   oo_______.'   
	  `_   ( \\) _____/~~~~ `--___              
	  | ~`-)  ) `-.   `---   ( - a:f -         
	  |   '///`  | `-.                         
	  |     | |  |    `-.                      
	  |     | |  |       `-.                   
	  |     | |\\ |                             
	  |     | | \\|                             
	   `-.  | |  |                             
	      `-| ')

	   ▄████████    ▄████████   ▄▄▄▄███▄▄▄▄   
	  ███    ███   ███    ███ ▄██▀▀▀███▀▀▀██▄ 
	  ███    ███   ███    █▀  ███   ███   ███ 
	 ▄███▄▄▄▄██▀  ▄███▄▄▄     ███   ███   ███ 
	▀▀███▀▀▀▀▀   ▀▀███▀▀▀     ███   ███   ███ 
	▀███████████   ███    █▄  ███   ███   ███ 
	  ███    ███   ███    ███ ███   ███   ███ 
	  ███    ███   ██████████  ▀█   ███   █▀   
	  ███    ███                              
	""") # https://www.asciiart.eu/people/sleeping
	time.sleep(1)
	print("""             	     _                 _                         _                 _                  
	            | |               (_)                       | |               | |                 
	  __ _   ___| | ___  ___ _ __  _ _ __   __ _    __ _  __| |_   _____ _ __ | |_ _   _ _ __ ___ 
	 / _` | / __| |/ _ \\/ _ \\ '_ \\| | '_ \\ / _` |  / _` |/ _` \\ \\ / / _ \\ '_ \\| __| | | | '__/ _ \\ 
	| (_| | \\__ \\ |  __/  __/ |_) | | | | | (_| | | (_| | (_| |\\ V /  __/ | | | |_| |_| | | |  __/
	 \\__,_| |___/_|\\___|\\___| .__/|_|_| |_|\\__, |  \\__,_|\\__,_| \\_/ \\___|_| |_|\\__|\\__,_|_|  \\___|
	                        | |             __/ |                                                 
	                        |_|            |___/                 """)
	time.sleep(3)
	print("\n\n\n\nH-Hello?")
	time.sleep(1.2)
	print("Who's there?")
	time.sleep(1.2)
	print("\n\n...")
	time.sleep(0.7)
	name = input("[enter your chosen name]\n>>> ")
	time.sleep(1.5)
	print("\n\n..."+name+"?! You shouldn't be here. Why haven't you woken up yet?")
	time.sleep(2)
	print("...what do you mean, you don't know where you are? You're in the dream world! You're going to be late for work.")
	time.sleep(2)
	print("\n\n[Your alarm isn't working. You look at your watch. There is a countdown on its display.]")
	time.sleep(2)
	watchLook()
	time.sleep(2)
	print("\n\nSuddenly, a deep, bellowing voice is heard from afar: \""+name+"! I have you in my sights! You won't escape this time!\"")
	time.sleep(2)
	teamUp()

def teamUp(): # first call to action (mandatory yes.)
	teamYes = input("\n\n[You immediately recognize the voice. It's the Sandman! He has come for revenge! Is it finally time to assemble the team? (yes or no)] \n>>> ")
	if teamYes == "yes":
		time.sleep(2)
		armoryScene()
	elif teamYes == "no":
		time.sleep(2)
		print("[You decide to go alone]")
	else:
		print("[that's not a valid command. try yes or no.]")
		teamUp()

def deaths(person,number): # player and teammate deaths
	if person == 1:
		if number == 1:
			pass

def watchLook(): #when player checks watch (check watch)
	print("["+str(countdown)+" minutes remaining. Time moves unpredictably in the dream world.]")

def armoryScene(): #anything that happens in the armory
	global countdown, location, locations # calling global variables to be edited
	location = locations[1]
	countdown -= 2
	print("""[THE ARMORY]\n         *                 *                  *              *
                                                      *             *
                        *            *                             ___
  *               *                                          |     | |
        *              _________##                 *        / \\    | |
                      @\\\\\\\\\\\\\\\\\\##    *     |              |--o|===|-|
  *                  @@@\\\\\\\\\\\\\\\\##\\       \\|/|/            |---|   |d|
                    @@ @@\\\\\\\\\\\\\\\\\\\\\\     \\|\\|//|/     *   /     \\  |w|
             *     @@@@@@@\\\\\\\\\\\\\\\\\\\\\\    \\|\\|/|/         |  U    | |b|
                  @@@@@@@@@----------|    \\|//           |  S    |=| |
       __         @@ @@@ @@__________|     \\|/           |  A    | | |
  ____|_@|_       @@@@@@@@@__________|     \\|/           |_______| |_|
=|__ _____ |=     @@@@ .@@@__________|      |             |@| |@|  | |
____0_____0__\\|/__@@@@__@@@__________|_\\|/__|___\\|/__\\|/___________|_|_
[You arrive at the armory short of breath, everyone is already getting ready to go]
[You have """+str(countdown)+" minutes remaining.]") # Art by Donovan Bake https://www.asciiart.eu/space/spaceships
	time.sleep(2)
	choice = input("\n[What would you like to do?\n1: Assemble the team\n2: Gather supplies\n3: Talk to the locals]\n>>> ")
	time.sleep(2)
	while
	if choice == "1":
		teamMembers()
	elif choice == "2":
		suppliesGather()
	elif choice == "3":
		talkLocals()
	else:
		print("plea")

def teamMembers():
	global teamSize
	if teamSize>0:
		choice = input("""[Choose another team member.""")
	else:
		choice = input("""[Choose a team member.""")

def check(choice,a,b):
	while 

start() # the adventure begins!