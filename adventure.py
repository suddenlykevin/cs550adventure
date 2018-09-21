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
stupidSelf = ["How could I be so stupid?", "AGAINNNN????", "Why can't I just enter anything? It's my dream.", "This is what I get for pursuing a liberal arts education.", "What the hell was I thinking?", "I wonder if America's Got Talent is on tonight?", "This is why I have no friends.", "I knew I should've listened in school!", "This darn brain of mine is so rusty.", "Duh. Brainfart."]

def titles(): # setting the stage and call to action
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
	# time.sleep(1)
	print("""             	     _                 _                         _                 _                  
	            | |               (_)                       | |               | |                 
	  __ _   ___| | ___  ___ _ __  _ _ __   __ _    __ _  __| |_   _____ _ __ | |_ _   _ _ __ ___ 
	 / _` | / __| |/ _ \\/ _ \\ '_ \\| | '_ \\ / _` |  / _` |/ _` \\ \\ / / _ \\ '_ \\| __| | | | '__/ _ \\ 
	| (_| | \\__ \\ |  __/  __/ |_) | | | | | (_| | | (_| | (_| |\\ V /  __/ | | | |_| |_| | | |  __/
	 \\__,_| |___/_|\\___|\\___| .__/|_|_| |_|\\__, |  \\__,_|\\__,_| \\_/ \\___|_| |_|\\__|\\__,_|_|  \\___|
	                        | |             __/ |                                                 
	                        |_|            |___/                 """)
	# time.sleep(3)
	start()

def start():
	global name
	print("\n\n\n\nH-Hello?")
	# time.sleep(1.2)
	print("Who's there?")
	# time.sleep(1.2)
	print("\n\n...")
	# time.sleep(0.7)
	name = input("[enter your chosen name]\n>>> ").title() # title function: https://stackoverflow.com/questions/9257094/how-to-change-a-string-into-uppercase
	# time.sleep(1.5)
	print("\n\n..."+name+"?! You shouldn't be here. Why haven't you woken up yet?")
	# time.sleep(2)
	print("...what do you mean, you don't know where you are? You're in the dream world! You're going to be late for work.")
	# time.sleep(2)
	print("\n\n[Your alarm isn't working. You look at your watch. There is a countdown on its display.]")
	# time.sleep(2)
	watchLook()
	# time.sleep(2)
	print("\n\nSuddenly, a deep, bellowing voice is heard from afar: \""+name+"! I have you in my sights! You won't escape this time!\"")
	# time.sleep(2)
	teamUp()

def teamUp(): # first call to action (mandatory yes.)
	print("\n\n[You immediately recognize the voice. It's the Sandman! How did he find you? Is it finally time to assemble the team?")
	choice=check("yes","no")
	if choice == "yes":
		# time.sleep(2)
		armoryScene()
	elif choice == "no":
		# time.sleep(2)
		print("\n[You decide to go alone]")

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
	print("""\n\n[THE ARMORY]\n         *                 *                  *              *
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
	# time.sleep(2)
	print("\n[What would you like to do?\n1: Assemble the team.\n2: Gather supplies.\n3: Talk to the locals.")
	choice = checkNum(1,3)
	# time.sleep(2)
	if choice == 1:
		teamMembers()
	elif choice == 2:
		suppliesGather()
	elif choice == 3:
		talkLocals()
	else:
		print("plea")

def suppliesGather():
	global countdown, stupidSelf
	#time.sleep(2)
	countdown -= 3
	print("\n[Whaddayaknow? The supply room is empty. Programmers must've run out of time. Return to the Armory?")
	choice = check("yes","no")
	if choice == "yes":
		#time.sleep(2)
		armoryScene()
	elif choice == "no":
		#time.sleep(1)
		countdown -= 1
		print("\n[You wait patiently for a few moments. It seems stupid. \"" + random.choice(stupidSelf) + "\" You think to yourself. Return to armory?]")
		choice = check("yes", "no")
		if choice == "yes":
			#time.sleep(2)
			armoryScene()
		elif choice == "no":
			#time.sleep(4)
			countdown -= 5
			print("\n[Suddenly, a small toad-shaped gnome leaps from behind a cabinet.]\n\n\nYou seem to be looking for something! Is it me? Have you come to turn me back into a toad? \n\n[What do you say? \n1. Yes \n2. Nope \n3. Aren't you already a toad?")
			choice = checkNum(1,3)
			if choice == 1:
				#time.sleep(0.7)
				print("\n\nOh I never thought this day would come! KISS ME, YOU ENCHANTED LOVER!")
			elif choice == 2:
				#time.sleep(0.7)
				print("\n\nThis angers me. Time to die.")

def teamMembers():
	global teamSize
	if teamSize>0:
		choice = input("""[Choose another team member.""")
	else:
		choice = input("""[Choose a team member.""")

def check(*argv): # variable arguments https://www.geeksforgeeks.org/args-kwargs-python/
	global stupidSelf
	print("Choose between", end = " ") # print without newline: https://www.geeksforgeeks.org/print-without-newline-python/
	for arg in argv:
		print(arg, end = "")
		if argv.index(arg) < (len(argv)-2):
			print(", ", end = " ")
		elif argv.index(arg) == (len(argv)-2):
			print(", or", end = " ")
		elif argv.index(arg) == (len(argv)-1):
			print(".]")
	choice = input(">>> ")
	for arg in argv:
		if choice.lower() == arg.lower(): # lowercase conversion: https://stackoverflow.com/questions/9257094/how-to-change-a-string-into-uppercase
			return choice.lower()
			break
	print("\n[That wasn't one of the choices! \""+random.choice(stupidSelf)+"\" You think to yourself. Try again.") # random function choice: https://stackoverflow.com/questions/5465455/syntax-to-call-random-function-from-a-list
	choice = check(*argv) # loops around -- in first trials, if the function loops, it returns None as a result since it is ending without returning after the nested loop parses. You have to set the choice to the nested loop and then return that choice in order to receive the correct value. Oof.
	return choice.lower()


def checkNum(a,b):
	global stupidSelf # quips
	while True: # basic error check for whether choice is a number
		try:
			choice = int(input("Enter a choice from "+str(a)+" to "+str(b)+".]\n>>> ")) 
		except ValueError:
			print("\n[That's not even a number. \""+random.choice(stupidSelf)+"\" You think to yourself. Try again.") 
		else:
			break # no errors in format (is an int), move on
	if a<=choice<=b: # basic error check that int is within parameters
		return choice
	else:
		print("\n[You need a number from "+str(a)+" to "+str(b)+". \""+random.choice(stupidSelf)+"\" You think to yourself. Try again.")
		choice = checkNum(a,b) # same as above, solution for loops returning None.
		return choice


titles() # the adventure begins!