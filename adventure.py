# REM: A sleeping adventure
# Kevin Xie CS550 Created 09/17/2018

# Sources:
# 	ASCII Art: https://www.asciiart.eu/
#	ASCII Text: https://patorjk.com/software/taag/
#	title function and lowercase function: https://stackoverflow.com/questions/9257094/how-to-change-a-string-into-uppercase
#	variable arguments for a function: https://www.geeksforgeeks.org/args-kwargs-python/
#	print without newline: https://www.geeksforgeeks.org/print-without-newline-python/
#	random function choice: https://stackoverflow.com/questions/5465455/syntax-to-call-random-function-from-a-list
# On my Honor, I have neither given nor received unauthorized aid.

import random # for RNG game mechanics
import time # pauses for more human storytelling

name = None # global variable that can be used in any function (to refer to player)
countdown = 45 # player's ticking timer mechanic
location = "spawn" # current location
locations = ["spawn", "armory"] # array of possible locations
teamSize = 0
stupidSelf = ["How could I be so stupid?", "AGAINNNN????", "Why can't I just enter anything? It's my dream.", "This is what I get for pursuing a liberal arts education.", "What the hell was I thinking?", "I wonder if America's Got Talent is on tonight?", "This is why I have no friends.", "I knew I should've listened in school!", "This darn brain of mine is so rusty.", "Duh. Brainfart."]
HP = 10
toadPower = 0
dumbWeapon = ["sharpened toothbrush", "rusty key", "unbent paper clip", "freeze-dried strawberry shiv", "expired fortune cookie", "shiv", "large pebble"]
nameRates = ["Sounds like your parents didn't love you. 10/10.", "That's... a name. 5/10.", "Wow, never heard that one before. 7/10.", "Sounds fine by me. 5/10.", "OH. MY. GOD. That's the most beautiful name I've ever heard! 11/10.", "Is there a silent k somewhere in there? If so, 8/10."]
quips = ["How can we know that we are living when we haven't even felt death?", "We are all dying, slowly."]

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
	print("\n\n[You immediately recognize the voice. It's the Sandman! How did he find you? Is it finally time to assemble the team?]")
	choice=check("yes","no")
	if choice == "yes":
		# time.sleep(2)
		armoryScene()
	elif choice == "no":
		# time.sleep(2)
		print("\n[You decide to go alone]")
		roadFork(1)

def deaths(person,number): # player and teammate deaths
	if person == 1:
		if number == 1:
			print("[The dream world around you fades as you feel a gentle beeping in your mind. The countdown has run out. You wake up 3 hours late.]")
			#time.sleep(2)
			print("[on a Sunday.]")
			#time.sleep(2)
			print("[Yet the Sandman knows no mercy! A plume of sand descends upon you, suffocating you. You die. Play again?]")
		elif number == 2:
			print("[Your HP has run out. You have died, both in your dream and in the real world. Shame. Play again?]")
		#time.sleep(0.7)
		choice = check("yes","no")

def watchLook(): #when player checks watch (check watch)
	global countdown, HP
	if countdown<=0:
		deaths(1,1)
	elif HP<= 0:
		deaths(1,2)
	else:
		print("["+str(countdown)+" minutes and "+str(HP)+"HP remaining. Time moves unpredictably in the dream world.]")

def armoryScene(): #anything that happens in the armory
	global countdown, location, locations, HP # calling global variables to be edited
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
[You arrive at the armory short of breath, everyone is already getting ready to go]""") # Art by Donovan Bake https://www.asciiart.eu/space/spaceships
	watchLook()
	# time.sleep(2)
	print("\n[What would you like to do?\n1: Assemble the team.\n2: Gather supplies.\n3: Talk to the locals. \n4: Go it alone.]")
	choice = checkNum(1,4)
	# time.sleep(2)
	if choice == 1:
		teamMembers()
	elif choice == 2:
		suppliesGather()
	elif choice == 3:
		talkLocals()
	elif choice == 4:
		roadFork(1)

def suppliesGather():
	global countdown, stupidSelf, HP, specialPower, dumbWeapon
	# time.sleep(2)
	countdown -= 3
	watchLook()
	print("\n[Whaddayaknow? The supply room is empty. Programmers must've run out of time. Return to the Armory?]")
	choice = check("yes","no")
	if choice == "yes":
		# time.sleep(2)
		armoryScene()
	elif choice == "no":
		# time.sleep(1)
		countdown -= 1
		print("\n[You wait patiently for a few moments. It seems stupid. \"" + random.choice(stupidSelf) + "\" You think to yourself. Return to armory?]")
		choice = check("yes", "no")
		if choice == "yes":
			# time.sleep(2)
			armoryScene()
		elif choice == "no":
			# time.sleep(4)
			countdown -= 5
			print("\n[Suddenly, a small toad-shaped gnome leaps from behind a cabinet.]")
			# time.sleep(0.7)
			print("\n\nYou seem to be looking for something! Is it me? Have you come to turn me back into a toad?")
			# time.sleep(0.7)
			print("\n[What do you say? \n1: Yes \n2: Nope \n3: Aren't you already a toad?]")
			choice = checkNum(1,3)
			if choice == 1:
				# time.sleep(0.7)
				print("\n\nOh I never thought this day would come! KISS ME, YOU ENCHANTED LOVER!")
				# time.sleep(0.7)
				print("[Do you kiss the gnome-toad?]")
				choice = check("yes","no")
				if choice == "yes":
					print("\n[You've already committed at this point, so you lean in and kiss the gnome-toad]")
					# time.sleep(1.2)
					print("\n\nGet pranked. I was always a toad. There's no such thing as a gnome-toad!")
					# time.sleep(0.7)
					print("But since you were such a good sport. I will imbue you with a special power.")
					# time.sleep(1)
					print("\n[You feel an unidentified force pulse through you. You're being transported back to the armory!]")
					specialPower = 1
					# time.sleep(2)
					armoryScene()
				elif choice == "no":
					# time.sleep(0.7)
					print("\n\nThis angers me. Prepare to die.")
					# time.sleep(0.5)
					print("\n[The gnome-toad (he's just a toad, isn't he?) strikes swiftly, and using a "+random.choice(dumbWeapon) + " from behind its back, impales you. You lose 1 HP and flee to the Armory.]")
					HP -= 1
					# time.sleep(2)
					armoryScene()
			elif choice == 2:
				# time.sleep(0.7)
				print("\n\nThis angers me. Prepare to die.")
				# time.sleep(0.5)
				print("\n[The gnome-toad (he's just a toad, isn't he?) strikes swiftly, and using a "+random.choice(dumbWeapon) + " from behind its back, impales you. You lose 1 HP and flee to the Armory.]")
				HP -= 1
				# time.sleep(2)
				armoryScene()
			elif choice == 3:
				# time.sleep(1)
				print("\n\nI'm a toad-shaped gnome. There's a difference. I can't... um... ")
				# time.sleep(2)
				print("multiply like them. I want to... multiply")
				# time.sleep(1)
				print("\n[The gnome-toad (he's totally a toad.) stands awkwardly. \"Why does he want to learn math so badly? I bet I could teach him.\" You think to yourself.]")
				# time.sleep(3)
				print("[You slowly back away from the now silent gnome-toad. He looks ashamed. Back to the armory it is!]")
				# time.sleep(1)
				armoryScene()

def talkLocals():
	global countdown, name, nameRates,quips
	# time.sleep(1)
	countdown -= 1
	print("\n")
	watchLook()
	print("[Who would you like to speak to? \n1: Pupnout, The Name Rater \n2: Kraklin', The Janitor \n3: Fitibis, The Cartographer \n4: Quippy, the Living Peanut \n5: Dirtcheap, The Programmer]")
	choice = checkNum(1,5)
	# time.sleep(1)
	if choice == 1:
		print("\n\nHowdiedo? I'm Pupnout, the famed Name Rater. Would you like me to rate your name?")
		choice = check("yes", "no")
		if choice == "yes":
			print("\n\n"+name+"? "+random.choice(nameRates)+" Would you like to change your name?\n")
			choice = check("yes","no")
			if choice == "yes":
				name = input("\n\nWhat would you like me to change it to?\n\n>>> ")
				print("\n\nAlrighty, "+name+". It's done!")
		if choice == "no":
			print("\n\nThen I guess my work here is done.")
	elif choice == 2:
		print("\n\nWhat's the word, bird? I'm Kraklin' the coooool janitor. Want some advice? Keep the sand outta this town and I won't break your neck. Now shoo.")
	elif choice == 3:
		print("\n\nHey, "+name+", glad we finally met! I understand you're going on a perilous journey. Want some directions?")
		choice = check("yes","no")
		if choice == "yes":
			print("\n\nDon't ask me how I know this, but the fastest way to the Sandman is through the Oregon Trail and N Elm Street. Good luck.")
		else:
			print("\n\nAlright. Godspeed. (Except in school zones.)")
	elif choice == 4:
		print("I'M QUIPPY THE LIVING PEANUT! WANNA HEAR A QUIP?")
		# time.sleep(2)
		print("\nDOESN'T MATTER, DON'T CARE! HERE IT IS: \n"+random.choice(quips))
	elif choice == 5:
		pass
	print("\n[What would you like to do now? \n1: Return to the Armory \n2: Talk to another local]")
	choice = checkNum(1,2)
	if choice == 1:
		armoryScene()
	else:
		talkLocals()

def teamMembers():
	global teamSize
	if teamSize>0:
		choice = input("""[Choose another team member.""")
	else:
		choice = input("""[Choose a team member.""")

def check(*argv): # variable arguments https://www.geeksforgeeks.org/args-kwargs-python/
	global stupidSelf
	print("[Choose between", end = " ") # print without newline: https://www.geeksforgeeks.org/print-without-newline-python/
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
	print("\n[That wasn't one of the choices! \""+random.choice(stupidSelf)+"\" You think to yourself. Try again.]") # random function choice: https://stackoverflow.com/questions/5465455/syntax-to-call-random-function-from-a-list
	choice = check(*argv) # loops around -- in first trials, if the function loops, it returns None as a result since it is ending without returning after the nested loop parses. You have to set the choice to the nested loop and then return that choice in order to receive the correct value. Oof.
	return choice


def checkNum(a,b):
	global stupidSelf # quips
	while True: # basic error check for whether choice is a number
		try:
			choice = int(input("[Enter a choice from "+str(a)+" to "+str(b)+".]\n>>> ")) 
		except ValueError:
			print("\n[That's not even a number. \""+random.choice(stupidSelf)+"\" You think to yourself. Try again.]") 
		else:
			break # no errors in format (is an int), move on
	if a<=choice<=b: # basic error check that int is within parameters
		return choice
	else:
		print("\n[You need a number from "+str(a)+" to "+str(b)+". \""+random.choice(stupidSelf)+"\" You think to yourself. Try again.]")
		choice = checkNum(a,b) # same as above, solution for loops returning None.
		return choice

titles() # the adventure begins!