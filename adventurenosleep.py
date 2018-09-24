# REM: A sleeping adventure (No pauses version for debugging)
# Kevin Xie CS550 Created 09/17/2018
#
# Description:
# REM is a text-based adventure game that definitely reflects my experience in having dreams.
# I was inspired by RPG games to try to make the game have as many choice branches as possible.
# This led to many NPCs and optional items that resulted in different endings or interactions.
# It also resulted in the bulk of the programming being scripting, which is how I ended up with
# so many lines of code. I also intermittently use time delays to make the game feel more natural,
# which contributes to the size of the code. The story is inspired by the weirdness of dreams. 
# For the story, I basically decided I wanted to make it as off-beat as possible, where player statistics 
# and NPC interactions changed on the fly. I also wanted some kind of twist so:
#
# [ SPOILERS ]
# I made the final boss the victim (which I know is cliche, but hmm.)
# The basic story is as follows: the player is trapped in his dream by the Sandman, who is
# hunting him down. He must find a way to leave the dream or he will be late for school! Or die! 
# Through many trials and tribulations, the player and the Sandman face off, only to come
# to the revelation that the player stole the Sandman's sandbags (oh no!) and is the villain.
# [ SPOILERS ]
#
# I was also inspired by the fact that I always oversleep and want to have cool dreams. So. That.
# I used various sources to find new commands as well as incorporate the functions we learned
# in class. I commented on these functions and commands to the best of my ability.
#
# Sources:
# 	ASCII Art: https://www.asciiart.eu/
#	ASCII Art: http://ascii.co.uk/art/traffic
#	ASCII Text: https://patorjk.com/software/taag/
#	title function and lowercase function: https://stackoverflow.com/questions/9257094/how-to-change-a-string-into-uppercase
#	variable arguments for a function: https://www.geeksforgeeks.org/args-kwargs-python/
#	print without newline: https://www.geeksforgeeks.org/print-without-newline-python/
#	random function choice: https://stackoverflow.com/questions/5465455/syntax-to-call-random-function-from-a-list
#	exit program: https://stackoverflow.com/questions/48129942/python-restart-program
#	restart self: https://stackoverflow.com/questions/11329917/restart-python-script-from-within-itself
#	catch file name changes: https://stackoverflow.com/questions/32536129/python-try-except-oserror-errno-2, https://docs.python.org/2/library/os.path.html#os.path.isfile
#	playtesters: 
# On my Honor, I have neither given nor received unauthorized aid.

import random # for RNG game mechanics
import time # pauses for more human storytelling
import os # entering commands to restart program
import sys # to exit program

name = None # global variable that can be used in any function (to refer to player)
countdown = 45 # player's ticking timer mechanic
teamSize = 0 # size of team (chosen number of team members)
stupidSelf = ["How could I be so stupid?", "AGAINNNN????", "Why can't I just enter anything? It's my dream.", "This is what I get for pursuing a liberal arts education.", "What the hell was I thinking?", "I wonder if America's Got Talent is on tonight?", "This is why I have no friends.", "I knew I should've listened in school!", "This darn brain of mine is so rusty.", "Duh. Brainfart.", "I wonder what 'dipagilated' means.", "This is literally the worst game I've ever played.", "Did my mom throw out my comic book collection?", "Asparagus is disgusting. Or is it?", "For increaseth knowledge, increaseth sorrow.", "Am I a bad enough dude to rescue the President?", "Why am I so dumb.", "Herp derp.", "Wow, that... was expected.", "Huh. Nice.", "Welp, didn't hurt to try."] # just a couple randomized "thoughts"
stupidSelfThoughts = ["How could I be so stupid?", "AGAINNNN????", "This is what I get for pursuing a liberal arts education.", "What the hell was I thinking?", "I wonder if America's Got Talent is on tonight?", "This is why I have no friends.", "I knew I should've listened in school!", "This darn brain of mine is so rusty.", "Duh. Brainfart.", "I wonder what 'dipagilated' means.", "Did my mom throw out my comic book collection?", "Asparagus is disgusting. Or is it?", "For increaseth knowledge, increaseth sorrow.", "Am I a bad enough dude to rescue the President?", "Why am I so dumb.", "Herp derp.", "Wow, that... was expected.", "Huh. Nice.", "Welp, didn't hurt to try."] # just a couple randomized "thoughts"
HP = 10 # Health Points
toadPower = 0 # Gag Power
dumbWeapon = ["a sharpened toothbrush", "the Master Sword", "the Blue Shell", "a Gravity Gun", "a Taser", "a rusty key", "an unbent paper clip", "a freeze-dried strawberry shiv", "an uncooked spaghetti", "an expired fortune cookie", "a shiv", "a large pebble", "a blue marble", "a knockoff iron man figurine", "a pair of Beats by Dre", "a postal worker", "a Garbage Truck", "a sharpened metal nail"] # array of weapons used with and against you
nameRates = ["Sounds like your parents didn't love you. 10/10.", "That's... a name. 5/10.", "Wow, never heard that one before. 7/10.", "Sounds fine by me. 5/10.", "OH. MY. GOD. That's the most beautiful name I've ever heard! 11/10.", "Is there a silent k somewhere in there? If so, 8/10."]  # name rating quotes
quips = ["Even in dark times, we cannot relinquish the things that make us... human.","What is better? To be born good or to overcome your evil nature through great effort?","How can we know that we are living when we haven't even felt death?", "We are all dying, slowly.", "When the dust settles, where will I stand?", "Can't make an omelette without breaking a couple eggs!", "It's funny we're all here laughing while children are dying.", "But where do antimicrobial wipes get disinfected?", "There are no choices. Nothing but a straight line.", "We impose order on the Chaos of organic evolution. You exist because we allow it, and you will end because we demand it.", "We all make choices in life, but in the end, our choices make us."] # un-funny quotes
itemOfChoice = 0 # item chosen in armory
items = ["Sand Bag", "Red Brick", "Super Soaker"] # item chosen in armory
rubberChicken = 0 # rubber chicken (obviously)
threat = ["HERE I COME, I'MA KILL YA, ", "BRING ME A BUCKET, AND I'LL SHOW YOU A BUCKET, ","WATCH THAT SKIN OF YOURS, ", "I AM GOTHAM'S RECKONING, ", "I WANT TO STOMP ON ", "WHERE DID YOU GO? ", "I DON'T NEED A GUN TO BE DEADLY, ", "THE FLOWERS DON'T BLOOM WHERE YOU'RE GOING, ", "WHY ARE YOU RUNNING? ", "I TOLD YOU: YOU'LL DIE FOR THAT, "] # Sandman threats
heros = ["Andaria the Sausage Warrior", "Campy the Campy Mage", "Trotus the Terrible Horse", "Jack, your old boss", "Terry Crews", "Benjamin the Oversized Baby", "Betelgeuse the Jester", "Timmy Tenfingers, the guy with Ten Fingers", "Akmaran the Wise", "Alex, your wingman from High School", "Master Chief the Master Chief", "Pikachu", "Chell the Playtester", "Akhmenrah the Fighting Pharoah", "Tony Two-Times, who repeats himself two times", "Nil the Sorcerer on Probation", "Estrellia the All-Seeing Psychic under House Arrest"]  # Possible Heroes
eulogy = ["They will be remembered kindly", "Rest in Peace.", "That wasn't unexpected.", "They were the weakest anyways.", "You put some respect on that.", "Love and prayers to their family.", "Or they're just taking an eternal nap.", "Never liked them anyways.", "They were the strongest member of the team.", "Oof."] # touching eulogies for fallen team members
member1 = None # team member names
member2 = None # team member names
member3 = None # team member names
armourRep = 0 # keeps track of whether player has been to armory
sandmanHP = 20 # Boss Health Points

# START
# Functions that introduce the game

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
	global name # calling global variable to be edited
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
	print("\n\n[You immediately recognize the voice. It's the Sandman! How did he find you? Is it time to head to the armory?]")
	choice=check("yes","no")
	if choice == "yes":
		# time.sleep(2)
		armoryScene()
	elif choice == "no":
		print("\n[Are you sure? There's no turning back!]")
		choice=check("yes","no")
		if choice == "yes":
			# time.sleep(2)
			print("\n[You decide to skip the armory (Good luck!)]")
			roadFork(0)
		else:
			teamUp()

# ARMORY
# all functions that take place in (or loop back to) the Armory

def armoryScene(): # anything that happens in the armory starts here. armourRep is just to keep track of whether the player has already been here
	global countdown, armourRep # calling global variables to be edited
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
____0_____0__\\|/__@@@@__@@@__________|_\\|/__|___\\|/__\\|/___________|_|_""") # Art by Donovan Bake https://www.asciiart.eu/space/spaceships
	if armourRep == 0: # only introductory quote
		print("[You arrive at the armory short of breath, everyone is already getting ready to go.]")
	armourRep+=1
	watchLook()
	# time.sleep(2)
	print("\n[What would you like to do?\n1: Assemble a team.\n2: Gather supplies.\n3: Talk to the locals. \n4: Proceed to the fight!]")
	choice = checkNum(1,4)
	# time.sleep(2)
	print("\n\n")
	if choice == 1:
		if teamSize>0:
			print("[Halfway to the warrior rooom, you realize: You've already done this! The group of "+str(teamSize)+" warriors stare at you awkwardly. You return to the Armory.]")
			# time.sleep(0.5)
			armoryScene()
		teamMembers()
	elif choice == 2:
		suppliesGather()
	elif choice == 3:
		talkLocals()
	elif choice == 4:
		if teamSize>0:
			roadFork(0)
		else:
			print("\n[You decide to proceed alone.]")	
			roadFork(0)

def suppliesGather(): # Where the player chooses his item of choice and can interact with a toad
	global countdown, HP, toadPower, itemOfChoice
	# time.sleep(0.7)
	countdown -= 3
	watchLook()
	if itemOfChoice!=0:
		print("[Whaddayaknow? The supply room is empty now. Programmers must've run out of time. Return to the Armory?]")
		choice = check("yes","no")
		if choice == "yes":
			# time.sleep(0.7)
			armoryScene()
		elif choice == "no": # little easter egg for the patient ones.
			# time.sleep(1)
			countdown -= 1
			print("\n[You wait patiently for a few moments. It seems stupid. \"" + random.choice(stupidSelfThoughts) + "\" You think to yourself. Return to armory?]")
			choice = check("yes", "no")
			if choice == "yes":
				# time.sleep(0.7)
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
						toadPower = 1
						# time.sleep(0.7)
						armoryScene()
					elif choice == "no":
						# time.sleep(0.7)
						print("\n\nThis angers me. Prepare to die.")
						# time.sleep(0.5)
						print("\n[The gnome-toad (he's just a toad, isn't he?) strikes swiftly, and using "+random.choice(dumbWeapon) + " from behind its back, impales you. You lose 1 HP and flee to the Armory.]")
						HP -= 1
						# time.sleep(0.7)
						armoryScene()
				elif choice == 2:
					# time.sleep(0.7)
					print("\n\nThis angers me. Prepare to die.")
					# time.sleep(0.5)
					print("\n[The gnome-toad (he's just a toad, isn't he?) strikes swiftly, and using "+random.choice(dumbWeapon) + " from behind its back, impales you. You lose 1 HP and flee to the Armory.]")
					HP -= 1
					# time.sleep(0.7)
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
					# time.sleep(0.7)
					armoryScene()
	else:
		print("[There are three items in front of you. You only have room for one. Which do you take? \n1: The Sand Bag \n2: The Red Brick \n3: The Super Soaker]")
		itemOfChoice = checkNum(1,3)
		# time.sleep(1)
		print("\n[You take the "+items[itemOfChoice-1]+". Now what? \n1: Return to Armory \n2: Keep looking]")
		choice = checkNum(1,2)
		if choice == 1:
			# time.sleep(0.7)
			armoryScene()
		else:
			suppliesGather()

def talkLocals(): # interactions with most NPCs take place here for advice and changing player statistics.
	global countdown, name, rubberChicken
	# time.sleep(0.7)
	countdown -= 1
	watchLook()
	print("[Who would you like to speak to? \n1: Pupnout, The Name Rater \n2: Kraklin', The Janitor \n3: Fitibis, The Cartographer \n4: Quippy, the Living Peanut \n5: Dirtcheap, The Programmer]")
	choice = checkNum(1,5)
	# time.sleep(1)
	if choice == 1:
		print("\n\nHowdiedo? I'm Pupnout, the famed Name Rater. Would you like me to rate your name?")
		choice = check("yes", "no")
		if choice == "yes":
			# time.sleep(0.7)
			print("\n\n"+name+"? "+random.choice(nameRates)+" Would you like to change your name?\n")
			choice = check("yes","no")
			if choice == "yes":
				# time.sleep(0.5)
				name = input("\n\nWhat would you like me to change it to?\n\n>>> ").title() # players are given the option to change their name
				# time.sleep(0.5)
				print("\n\nAlrighty, "+name+". It's done!")
		if choice == "no":
			# time.sleep(0.5)
			print("\n\nThen I guess my work here is done.")
	elif choice == 2:
		print("\n\nWhat's the word, bird? I'm Kraklin' the coooool janitor. Want some advice? Keep the sand outta this town and I won't break your neck. Now shoo.")
	elif choice == 3:
		print("\n\nHey, "+name+", glad we finally met! I understand you're going on a perilous journey. Want some directions?")
		choice = check("yes","no")
		# time.sleep(0.7)
		if choice == "yes":
			print("\n\nDon't ask me how I know this, but the fastest way to the Sandman is through the Oregon Trail and N Elm Street. Good luck.")
		else:
			print("\n\nAlright. Godspeed. (Except in school zones.)")
	elif choice == 4:
		print("\n\nI'M QUIPPY THE LIVING PEANUT! WANNA HEAR A QUIP?")
		# time.sleep(2)
		print("\nDOESN'T MATTER, DON'T CARE! HERE IT IS:")
		# time.sleep(0.7)
		print("\n"+random.choice(quips))
	elif choice == 5:
		if rubberChicken == 0:
			print("\n\nYou must be the player. Do you know how much blood and sweat went into this? Do you know how much they pay me? None. This is why I'll break this game. Take this.")
			# time.sleep(2)
			print("\n[Dirtcheap handed you a rubber chicken!]")
			rubberChicken = 1
			# time.sleep(1)
			print("\n\nAlright, now go use that. Good luck.")
		elif rubberChicken == 1:
			print("\n\nWelcome back, "+name+". I already gave you everything I can. Good luck.")
	# time.sleep(1)
	print("\n[What would you like to do now? \n1: Return to the Armory \n2: Talk to another local]")
	choice = checkNum(1,2)
	if choice == 1:
		# time.sleep(0.7)
		armoryScene()
	else:
		talkLocals()

def teamMembers(): # player chooses (mostly useless) team members
	global countdown, teamSize, member1, member2, member3
	# time.sleep(0.7)
	countdown-=3
	watchLook()
	print("[How many team members would you like? (Up to 3)]")
	teamSize = checkNum(1,3)
	print("[You have chosen the following worthy warriors: ")
	# time.sleep(0.7)
	for t in range(teamSize): # to make sure there is no two identical randomly chosen teammates, I use this for loop, which re-chooses team members until all are unique.
		if member2 != None:
			member3 = random.choice(heros)
			while (member3==member2) or (member3==member1): # if one is identical to the other, it is re-chosen
				member3 = random.choice(heros)
			print(member3)
		elif member1 != None:
			member2 = random.choice(heros)
			while member2==member1:
				member2 = random.choice(heros)
			print(member2)
		else:
			member1 = random.choice(heros)
			print(member1)
		# time.sleep(0.7)
	print("...What a great team!!]")
	# time.sleep(0.7)
	print("\n[What do you want to do now? \n1: Return to Armory \n2: Proceed to the fight!]")
	choice = checkNum(1,2)
	if choice == 1:
		# time.sleep(0.7)
		armoryScene()
	else:
		# time.sleep(2)
		roadFork(0)

# ROAD TO SANDMAN
# functions that contribute to the path taken (and bulk of the game progression)

def roadFork(rep): # a way to induce choice between paths, rep indicates which choices are given
	global countdown
	# time.sleep(2)
	print("""\n\n\n[FORK IN THE ROAD]
      .-.  .-.
       \\ \\/ / 
        }  {  
        `--'  """)
	countdown+=4
	watchLook()
	# time.sleep(0.7)
	print("\n\n\""+random.choice(threat)+name.upper()+"!\"")
	# time.sleep(0.7)
	print("\n[The Sandman's voice booms in the distance.]") 
	if rubberChicken == 1:
		print("[The rubber chicken you took from Dirtcheap begins to glow. Use it?]")
		choice = check("yes","no")
		if choice == "yes":
			deaths(3)
		else:
			print("[You put the rubber chicken away. Not today, rubber industry. Not today.]")
	# time.sleep(1)
	print("[You come to a fork in the road. It looks familiar. Which path do you choose?")
	if rep == 0:
		print("1: \"The Oregon Trail\"\n2: \"Sesame Street\"]")
		choice = checkNum(1,2)
		countdown -= 3
		# time.sleep(1)
		print("\n\n")
		watchLook()
		if choice == 1:
			oregonTrail()
		else:
			sesameStreet()
	elif rep == 1:
		print("1: \"Boulevard of Broken Dreams\"\n2: \"The Yellow Brick Road\"]")
		countdown += 1
		# time.sleep(1)
		print("\n\n")
		watchLook()
		choice = checkNum(1,2)
		if choice == 1:
			boulevard()
		else:
			yellowBrick()
	elif rep == 2:
		print("1: \"Rainbow Road\" \n2: \"N Elm Street\"]")
		countdown -= 4
		# time.sleep(1)
		print("\n\n")
		watchLook()
		choice = checkNum(1,2)
		if choice == 1:
			rainbowRoad()
		else:
			elmSt()

def oregonTrail(): # most complex path very loosely inspired by game of the same name (it only matters if you chose the Red Brick, though.)
	global countdown, HP
	print("""___       ___     __   __   ___  __   __          ___  __              
 |  |__| |__     /  \\ |__) |__  / _` /  \\ |\\ |     |  |__)  /\\  | |    
 |  |  | |___    \\__/ |  \\ |___ \\__> \\__/ | \\|     |  |  \\ /~~\\ | |___ 
                                                                       """) # ASCII text generator:http://patorjk.com/software/taag/#p=display&h=2&v=2&f=ANSI%20Shadow&t=Weather%3A%20cold%0AHealth%3A%20good%0APace%3A%20steady%0ARations%3A%20fillinghttp://patorjk.com/software/taag/#p=display&h=2&v=2&f=ANSI%20Shadow&t=Weather%3A%20cold%0AHealth%3A%20good%0APace%3A%20steady%0ARations%3A%20filling
	# time.sleep(1)
	print("""██╗    ██╗███████╗ █████╗ ████████╗██╗  ██╗███████╗██████╗         ██████╗ ██████╗ ██╗     ██████╗             
██║    ██║██╔════╝██╔══██╗╚══██╔══╝██║  ██║██╔════╝██╔══██╗██╗    ██╔════╝██╔═══██╗██║     ██╔══██╗            
██║ █╗ ██║█████╗  ███████║   ██║   ███████║█████╗  ██████╔╝╚═╝    ██║     ██║   ██║██║     ██║  ██║            
██║███╗██║██╔══╝  ██╔══██║   ██║   ██╔══██║██╔══╝  ██╔══██╗██╗    ██║     ██║   ██║██║     ██║  ██║            
╚███╔███╔╝███████╗██║  ██║   ██║   ██║  ██║███████╗██║  ██║╚═╝    ╚██████╗╚██████╔╝███████╗██████╔╝            
 ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝        ╚═════╝ ╚═════╝ ╚══════╝╚═════╝             
██╗  ██╗███████╗ █████╗ ██╗  ████████╗██╗  ██╗        ██████╗  ██████╗  ██████╗ ██████╗                        
██║  ██║██╔════╝██╔══██╗██║  ╚══██╔══╝██║  ██║██╗    ██╔════╝ ██╔═══██╗██╔═══██╗██╔══██╗                       
███████║█████╗  ███████║██║     ██║   ███████║╚═╝    ██║  ███╗██║   ██║██║   ██║██║  ██║                       
██╔══██║██╔══╝  ██╔══██║██║     ██║   ██╔══██║██╗    ██║   ██║██║   ██║██║   ██║██║  ██║                       
██║  ██║███████╗██║  ██║███████╗██║   ██║  ██║╚═╝    ╚██████╔╝╚██████╔╝╚██████╔╝██████╔╝                       
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝   ╚═╝  ╚═╝        ╚═════╝  ╚═════╝  ╚═════╝ ╚═════╝                        
██████╗  █████╗  ██████╗███████╗       ███████╗████████╗███████╗ █████╗ ██████╗ ██╗   ██╗                      
██╔══██╗██╔══██╗██╔════╝██╔════╝██╗    ██╔════╝╚══██╔══╝██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝                      
██████╔╝███████║██║     █████╗  ╚═╝    ███████╗   ██║   █████╗  ███████║██║  ██║ ╚████╔╝                       
██╔═══╝ ██╔══██║██║     ██╔══╝  ██╗    ╚════██║   ██║   ██╔══╝  ██╔══██║██║  ██║  ╚██╔╝                        
██║     ██║  ██║╚██████╗███████╗╚═╝    ███████║   ██║   ███████╗██║  ██║██████╔╝   ██║                         
╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝       ╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═════╝    ╚═╝                         
██████╗  █████╗ ████████╗██╗ ██████╗ ███╗   ██╗███████╗       ███████╗██╗██╗     ██╗     ██╗███╗   ██╗ ██████╗ 
██╔══██╗██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║██╔════╝██╗    ██╔════╝██║██║     ██║     ██║████╗  ██║██╔════╝ 
██████╔╝███████║   ██║   ██║██║   ██║██╔██╗ ██║███████╗╚═╝    █████╗  ██║██║     ██║     ██║██╔██╗ ██║██║  ███╗
██╔══██╗██╔══██║   ██║   ██║██║   ██║██║╚██╗██║╚════██║██╗    ██╔══╝  ██║██║     ██║     ██║██║╚██╗██║██║   ██║
██║  ██║██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║███████║╚═╝    ██║     ██║███████╗███████╗██║██║ ╚████║╚██████╔╝
╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝       ╚═╝     ╚═╝╚══════╝╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ """) 
	# time.sleep(1)
	print("\n[You continue on the trail.]")
	# time.sleep(1)
	print("\n[Suddenly, the Cheshire Cat appears in the distance. He looks like he needs help. What do you do? \n1: Continue on trail \n2: Help him \n3: Threaten him for supplies]")
	choice = checkNum(1,3)
	# time.sleep(2)
	if choice == 1:
		print("\n[That was easy! You continue on the trail, as if nothing has happened. The Cheshire Cat glares at you and disappears. You lose 1HP out of shame.]")
		HP -= 1
		roadFork(2)
	elif choice == 2:
		print("""\n\n
 _._     _,-'""`-._
(,-.`._,'(       |\\`-/|
    `-.-' \\ )-`( , o o)
          `-    \\`_`"'-
Who are you? ...the famous """+name+"? What do YOU want?") # https://www.asciiart.eu/animals/cats
		# time.sleep(1)
		print("\nI was attacked by a ferocious caterpillar. If you help me, I can help you too. You need to get out of this dream, right?")
		choice1 = check("yes","no")
		# time.sleep(1)
		print("\n\nWell, all I'll need is a red brick to murder that darned caterpillar.")
		if choice1 == "yes":
			print("Then I can get you out of here before your "+str(countdown)+" minutes runs out.")
		elif choice1 == "no":
			print("You will be handsomely rewarded.")
			# time.sleep(1)
		if itemOfChoice != 2:
			print("You don't have a red brick? That's too bad. Carry on.")
			countdown += 2
			roadFork(2)
		else:
			print("I see you have a red brick there, can I have it?")
			choice = check("yes","no")
			if choice == "yes":
				print("\n\nThank you kindly!")
				itemofChoice = 0
				# time.sleep(0.5)
				if choice1 == "yes":
					print("You are now released from this realm! Go! Be free!")
					# time.sleep(1)
					deaths(4)
				if choice1 == "no":
					print("Here is your gift: free passage straight to the Sandman! Do you accept?")
					choice = check("yes","no")
					# time.sleep(0.5)
					if choice == "yes":
						print("\n[The Cheshire Cat waves its arms wildly in the air. You are being teleported, but in the process, you lose 2HP]")
						HP -= 2
						elmSt()
					elif choice == "no":
						print("Very well. Have some health.")
						# time.sleep(1)
						print("[The Cheshire Cat boosts you 2HP and sends you away.]")
						HP+=2
						countdown -=2
						roadFork(2)
			elif choice == "no":
				# time.sleep(1)
				print("Very well. Carry on.")
				countdown += 4
				roadFork(2)
	else:
		print("\n\n[You approach the Cheshire Cat with your "+str(teamSize)+" team members, weapons drawn.]")
		# time.sleep(2)
		print("[Little did you know, the Cheshire Cat is diseased and ferocious! He attacks with projectile vomit.]")
		# time.sleep(2)
		deaths(5)

def sesameStreet(): # incorporating my guessing game practice
	global countdown, HP
	print("[You march calmly through Sesame Street until you come accross Grouch.]")
	# time.sleep(1.2)
	print("""               ____ 
   ___________//__\\\\__________
  /___________________________\
  I___I___I___I___I___I___I___I
        < ,wWWWWwwWWWWw, >
       <  WW( 0 )( 0 )WW  >
      <      '-'  '-'      >
     <    ,._.--""--._.,    >
     <   ' \\   .--.   / `   >
      <     './__\\_\\.'     >
    ___<.-.____________.-.>___
   (___/   \\__________/   \\___)
    |  \\,_,/          \\,_,/  |
  .-|/^\\ /^\\ /^\\ /^\\ /^\\ /^\\ |-.
 / (|/\\| | | | | | | | | | /\\|) \
 '.___/| | | | | | | | | | \\___.'
    || | | | | | | | | | | | |
    || | | | | | | | | | | | |
    || | | | | | | | | | | | |
    || | | | | | | | | | | | |
    || | | | | | | | | | | | |
    || | | | | | | | | | | | |
    || | | | | | | | | | | | |
    || | | | | | | | | | | | |
    || | | | | | | | | | | | |
jgs |\\_/ \\_/ \\_/ \\_/ \\_/ \\_/ |
    |                        |
    `""""""""""""""""""""""""`""") # source: https://www.asciiart.eu/television/sesame-street
	print("\nHey "+name+"! Guess how many cookies I stole today!\n\n")
	answer = random.randint(0,60)
	while True:
		guess = checkNum(0,60)
		if int(guess) > answer:
			print("\n\nDo I really look that fat? Lower.")
		elif int(guess) < answer:
			print("\n\nYou underestimate my skills! Higher.")
		else:
			print("\n\nRight on the money, lil' human. But I've got room for one more!")
			break
	# time.sleep(0.5)
	print("You passed my test, my dude. Here's your reward!")
	# time.sleep(1)
	print("\n\n[Grouch awarded you with an extra 10 minutes!]")
	countdown += 10
	roadFork(1)
	

def boulevard(): # Green Day! Can separate player from team
	global countdown, teamSize
	print("""[BOULEVARD OF BROKEN DREAMS]
   ______________________________________________________
   [[]]-[[]]-[[]]-[[]]-[[]]-[[]]-[[]]-[[]]-[[]]-[[]]-[[]]
   .-.`| `-/-.__/.-'\\_.-._,'/`-._'\\_.-._`-'_/-._.'|/.-'\\-
   \\_.-`./`-._'\\__.-`-.__.-`--._/--.`-._\\`-._\\__.-)`-'._/
   `._-'.\\_.---._-.\\_`-..`\\_.---._`-.__.-`'._.--./`-'._,'
   __/`.-/       `.'_`./`.'       '.\\__.-`.'    (_.-\\_,-.
   `._-/'          |._.-|           |.'`.|       `(_.`-._
   .-',`)          | /`.|           |`-/`|         ;.-'_/
   `\\,-/           |\\.-'|           |\\-'`|          ;\\_,-
    -./`._        [[[[[[[[         [[[[[[[[         .',-'
    `.`--.~~-^_~-/.`-._`-.\\^~-_~-^/`-.'-,.'\\^~-~_^"'`-.'_
    -,.'"-"~^-~_~- - - _- -~^-_.~ - -_ - - -~- . "'"-"-""
    ""-'"-""-"~- _~.^-~-^.-^_.- .^~.-  ~-. ~^_-""-""-"'-"
    jgs ""-'"-"    ~- ^. - ~ -~^ - ~  ^~- ~     ""-"'-'""") # source: https://www.asciiart.eu/buildings-and-places/bridges
	watchLook()
	# time.sleep(1)
	print("[You come across a sign: You may only press this button if you have 1 or more teammates.]")
	if teamSize>=1:
		print("[Press the button?]")
		choice = checkNum("yes", "no")
		# time.sleep(0.5)
		if choice == "yes":
			print("\n[A small entrance opens up beneath you, forever separating you from your team. You land at a fork in the road.]")
			teamSize=0
			roadfork(2)
		else:
			print("\n[You continue with your team.]")
	else:
		# time.sleep(1)
		print("[...it doesn't seem like you're qualified. You proceed along. The sound of Green Day music plays in the distance...]")
	countdown += 2
	roadFork(1)


def yellowBrick(): # Free pass road
	print("""[YELLOW BRICK ROAD]
 (              ````                                            
;`             ;;                                               
 ;;  -""-.   ;;                 -;'  -.                         
   ""     ``                      `.   `.                       
                                    ;    `                      
           `;                  -          ;         -.        ;`
             `-  `.         .'`  .-'             .--`  ;     ;  
              ;    `-.   ;    `-'             .;`     ;       `.
              .        ``                                       
               `            .--------.             .'           
             ...        .--'``````````'--.        ;.            
            `      . .-' .``          ``. '-. .      `.         
          ;-.;  .  .' .`                  `. '.  .    ;         
              .' .' .`                      `. '. '.    .       
_____/'.-..___________________________ mvn,, ___________________
                             )\\     nMmIEFooPTn                 
                            ( (    Li1iiJl1ItTIjp               
                             ) \\  i i_BP_LWmKK`  J  `           
`                .          /  (   i1 LL 1I`L            .      
             ..             \\   \\  i   X  Y o1                  
                        .    )   )  `   l   p      ..           
;                           /   (,      l(@) l                ..
  q      ` .  '            (     \\.     i    p   R          .;  
   \\  t            ;        )     \\`   j,.. ,.q,/Pqoj          `
    \\/            `       ./       \\`;     `'     `          .. 
  '-     \\;            -'.'    ;    \\ `                     `. `
.--.`.; ,-.. ,.-, ;' `.-'       `    `.'.   .--.""-._        .; 
    `............---""     ;_.         )   (  '=    /         `-
 ~                                    /     `------'     .      
                 ~                  ,'  \\|//            `'      
                ~           ~       ; `. ""                   ..
                                     `.  )     \\\"       .--\"\"\"""") # source: https://www.asciiart.eu/nature/landscapes
	watchLook()
	# time.sleep(2)
	print("[The road is empty. There are footsteps ahead of you in the shape of ruby slippers, lion paws, tin cans, and wooden dowels. You wonder what happened here.]")
	forkRoad(2)

def rainbowRoad(): # rainbow road to skip to boss battle or end the game.
	global countdown, HP
	print("""\n\n[RAINBOW ROAD]
 _/__|_,\\__                 aaaah                   _O
|,-.___,-. )    _____      _o'   @           __     (`
( O ) ( O )   _/__|_,\\__   /` __( `>    ____|_,\\_   |>
,`-'/_~`-'/) |,-.___,-._) />  )-.)/\\-. |,-.___,-.| ,|.
`===---===-'  `-'   `-'       `-'  `-'  `-'   `-'  `-'""") # source: http://ascii.co.uk/art/traffic
	watchLook()
	# time.sleep(1)
	print("[Mariokarts speed past you. You are unable to keep your bearings and fall off the edge.]")
	# time.sleep(1)
	print("[Lakitu appears to save the day!]\n\nHey there,"+name+"! Need a hand?")
	# time.sleep(1)
	print("[Lakitu gives you three options:\n1: Proceed to the final fight in exchange for 2HP \n2: Proceed on this road for free. \n3: Attempt a riddle to be released from the dream world]")
	choice = checkNum(1,3)
	# time.sleep(0.5)
	if choice == 1:
		print("[Lakitu accepts your offer of blood. He graciously offers his magic fishing rod in return. It begins to glow...]")
		HP-=2
		# time.sleep(1)
		print("""     _.-\"\"\"\"`-._ 
   ,' _-"\"\"\"`-_ `.
  / ,'.-'\"\"\"`-.`. \\
 | / / ,'\"\"\"`. \\ \\ |
| | | | ,'\"`. | | | |
| | | | |   | | | | |""")
		elmSt()
	elif choice == 2:
		print("[You proceed along the road free of charge. Lakitu looks at you funny.]")
		roadFork(2)
	else:
		answer = input("\n\nWhat starts with an 'e', ends with an 'e,' and contains one letter?\n\n[one word]\n>>> ")
		# time.sleep(0.5)
		if answer.lower() == "letter":
			print("\n\nCorrect! Here you go....")
			# time.sleep(1)
			deaths(6)
		else:
			print("\n\nIncorrect... Better luck next time! Carry on my wayward son.")
			countdown -= 8
			roadFork(2)

def elmSt(): # introduction to boss battle
	global name
	print("""[N ELM STREET]
                                                           |>>>
                   _                      _                |
    ____________ .' '.    _____/----/-\\ .' './========\\   / \
   //// ////// /V_.-._\\  |.-.-.|===| _ |-----| u    u |  /___\
  // /// // ///==\\ u |.  || | ||===||||| |T| |   ||   | .| u |_ _ _ _ _ _
 ///////-\\////====\\==|:::::::::::::::::::::::::::::::::::|u u| U U U U U
 |----/\\u |--|++++|..|'''''''''''::::::::::::::''''''''''|+++|+-+-+-+-+-+
 |u u|u | |u ||||||..|              '::::::::'           |===|>=== _ _ ==
 |===|  |u|==|++++|==|              .::::::::.           | T |....| V |..
 |u u|u | |u ||HH||         \\|/    .::::::::::.
 |===|_.|u|_.|+HH+|_              .::::::::::::.              _
                __(_)___         .::::::::::::::.         ___(_)__
---------------/  / \\  /|       .:::::;;;:::;;:::.       |\\  / \\  \\-------
______________/_______/ |      .::::::;;:::::;;:::.      | \\_______\\________
|       |     [===  =] /|     .:::::;;;::::::;;;:::.     |\\ [==  = ]   |
|_______|_____[ = == ]/ |    .:::::;;;:::::::;;;::::.    | \\[ ===  ]___|____
     |       |[  === ] /|   .:::::;;;::::::::;;;:::::.   |\\ [=  ===] |
_____|_______|[== = =]/ |  .:::::;;;::::::::::;;;:::::.  | \\[ ==  =]_|______
 |       |    [ == = ] /| .::::::;;:::::::::::;;;::::::. |\\ [== == ]      |
_|_______|____[=  == ]/ |.::::::;;:::::::::::::;;;::::::.| \\[  === ]______|_
   |       |  [ === =] /.::::::;;::::::::::::::;;;:::::::.\\ [===  =]   |
___|_______|__[ == ==]/.::::::;;;:::::::::::::::;;;:::::::.\\[=  == ]___|_____""") # source: https://www.asciiart.eu/buildings-and-places/cities
	# time.sleep(1)
	print("[The road is eerily quiet. The Sandman's footsteps rumble nearby.]")
	# time.sleep(3)
	print("[Suddenly, the Sandman approaches from behind the clouds!]\n\n\""+random.choice(threat)+name.upper()+"!\"")
	# time.sleep(1)
	print("\n\n")
	finalFight()

# FIGHTING SANDMAN
# Functions relating to the battle with Sandman

def finalFight(): # Sandman initiating battle, Gag power activates
	print("""[THE SANDMAN]
                                __....__
                        :._  .-:::::::::\" .:
                        '::\"\"::::::::::::::'
                      .-\"\"\":::_:::::::::::'/;
                     .:-._.::| \"\"-::::;'|:;/.--.
                   .:::::::-"'-._o.--.o-': . ':::.
               _.=::::::\"  .-\":  \":..::   .   ::::.
             -:::::::::|    .(     'T'  -._.  ::::::.
            -:::::::/::'      |T--\"\"\"\"\"--:|  .:::::::::.
     ...    .:::::'.::|       ':         :'  ::''':::::;.
     ':::. .:::::' :::'                     :'     \"::::;
        :: ::::'   ::|                     .:        ::::.
 .:::::. :::::'    ::|                     :'        '::::
:::':::::::::' ... ::|               __.' .:          ':::.     ..:::.
 '    \"::::::::::' :::.            \"\"     :'           ':::   .:::::''
        ':''::''   '::|                  .:            .:::..::::..
                    ::|                 .:            .:::::''':::::.
                    ::|                .:         ':::::''       '''
                    ::|               .:'           '''
                    :::.            .:'
                   .:::|          .::'
                   ::::|        .::::.
               ._.::::::.    ..:::::::.
               '::::::::::'''':::::::::
                 '':::::'      ':::::::.
                 .::::'          ::::::'
                 '':::.         .::::'
            ....    ':::.      .:::'     ....
           ::::::::::::::'    '::::::::::::::::.
           '::::::::::'''       '''''':::::::::'
           grp'''                           ''""")
	# time.sleep(1)
	print("\"I've finally caught you!\"\n\n[The Sandman's guffaws send shivers down yours neck.]")
	if toadPower == 1:
		# time.sleep(2)
		print("\n[YOUR TOAD POWER ACTIVATES!]")
		# time.sleep(1)
		print("\n\nWhat? You actually tried to use the power? HAH! I ain't gonna get involved in this!")
		print("\n\n[THE TOAD'S VOICE ECHOES THROUGH YOUR MIND. IT DOES NOTHING...]")
	attackMan(0)


def attackMan(value): # attack loop. Once attack begins, it doesn't stop until Sandman is near death.
	global sandmanHP, HP, countdown, teamSize
	# time.sleep(0.7)
	print("\n\n")
	countdown-=4
	watchLook()
	if value == 0:
		print("[What would you like to do? \n1: Attack \n2: Talk it out]")
		choice = checkNum(1,2)
	else:
		print()
		print("[The Sandman strikes back!]\n")
		# time.sleep(0.7)
		choice = 1
		if teamSize == 3:
			print("\"I'VE GOT YOU NOW, "+name+"!\" \n\n[But the Sandman misses, instead killing "+member3+". "+random.choice(eulogy))
			teamSize = 2
		elif teamSize == 2:
			print("\"THIS IS IT, YOU'RE DEAD, "+name+"!\" \n\n[The Sandman's arm dislodges, instead killing "+member2+". "+random.choice(eulogy))
			teamSize = 1
			countdown+= 3
		elif teamSize == 1:
			print("\"YOU'RE DEAD, "+name+"!\" \n\n[But the Sandman's aim is hindered, instead killing "+member1+". "+random.choice(eulogy))
			teamSize = 0
		else:
			print("\"TAKE THIS!\" [The Sandman smites you where you stand]")
			countdown+=1
			HP -= random.choice([1,2])
	if choice==1:
		# time.sleep(1)
		print("\n\n")
		if teamSize == 3:
			print("["+random.choice([member1+"strikes",member2+"strikes",member3+"strikes","You strike"])+" the Sandman with "+random.choice(dumbWeapon)+". It inflicts visible damage.]")
			countdown+=1
		elif teamSize == 2:
			print("["+random.choice([member1+"strikes",member2+"strikes",member3+"strikes","You strike"])+" the Sandman with "+random.choice(dumbWeapon)+". It inflicts visible damage.]")
		elif teamSize == 1:
			print("["+random.choice([member1+"strikes","You strike"])+" the Sandman with "+random.choice(dumbWeapon)+". It inflicts visible damage.]")
			countdown+=2 
		else:
			print("[You strike the Sandman with "+random.choice(dumbWeapon)+". It inflicts visible damage.]")
		sandmanHP -= random.choice([2,3,4])
	else:
		altConv()
	if sandmanHP > 5:
		print("[The Sandman has "+str(sandmanHP)+"HP remaining.]")
		attackMan(1)
	# time.sleep(3)
	finalConv()

def finalConv(): # final confrontation with Sandman (REVELATIONS!) Leads to "good ending" if you chose the Sand Bag
	print("\n\n")
	watchLook()
	print("[The Sandman collapses to the ground.]")
	# time.sleep(1)
	print("\"OH GOOOOOD\" \n\n[The Sandman is visibly near death.]")
	# time.sleep(2)
	print("\"I didn't want this...")
	# time.sleep(1)
	print("You... you...")
	# time.sleep(1)
	print("You did this.\"")
	# time.sleep(0.5)
	print("\n[1: What are you talking about?")
	if itemOfChoice==2 or itemOfChoice==3 or itemOfChoice==0:
		print("2: Finish Him.]")
	else:
		print("2: I don't understand.]")
	choice = checkNum(1,2)
	if (choice==1) or (choice==2 and itemOfChoice==1):
		# time.sleep(1)
		print("\n\n\"You... took it.")
		# time.sleep(1)
		print("You stole my sandbag for yourself. Why did you do that?\"")
		# time.sleep(3)
		print("...")
		# time.sleep(0.5)
		input("\n>>> ")
		# time.sleep(2)
		print("\n\n\"No excuses. You're a selfish person.")
		# time.sleep(1)
		print("You took away everyone else's good dreams so that you could have them all.")
		# time.sleep(1)
		print("Do you know how many people are out there having nightmares right now?")
		# time.sleep(2)
		print("Millions.")
		# time.sleep(1)
		print("But you don't care. Do what you must.")
		# time.sleep(2)
		print("\n[1: Finish Him.")
		if itemOfChoice == 1:
			print("2: Return the Sand Bag]")
		else: 
			print("2: Walk away.]")
		choice = checkNum(1,2)
		if choice == 1:
			deaths(10)
		elif choice==2 and itemOfChoice==1:
			deaths(11)
		else:
			deaths(12)
	else:
		print("\n\n\"you--")
		if itemOfChoice == 2:
			deaths(7)
		elif itemOfChoice == 3:
			deaths(8)
		else:
			deaths(9)

def altConv(): # if fight choice = talk it out (REVELATIONS!)
	# time.sleep(2)
	print("\"I didn't want this...")
	# time.sleep(1)
	print("You did this.\"")
	print("\n[1: What are you talking about?")
	if itemOfChoice==2 or itemOfChoice==3 or itemOfChoice==0:
		print("2: Attack Him.]")
	else:
		print("2: I don't understand.]")
	choice = checkNum(1,2)
	if (choice==1) or (choice==2 and itemOfChoice==1):
		# time.sleep(1)
		print("\n\n\"You... took it.")
		# time.sleep(1)
		print("You stole my sandbag for yourself. Why did you do that?\"")
		# time.sleep(3)
		print("...")
		# time.sleep(0.5)
		input("\n>>> ")
		# time.sleep(2)
		print("\n\n\"No excuses. You're a selfish person.")
		# time.sleep(1)
		print("You took away everyone else's good dreams so that you could have them all.")
		# time.sleep(1)
		print("Do you know how many people are out there having nightmares right now?")
		# time.sleep(2)
		print("Billions.")
		# time.sleep(1)
		print("But you don't care. Do what you must.")
		# time.sleep(2)
		print("\n[1: Attack Him.")
		if itemOfChoice == 1:
			print("2: Return the Sand Bag]")
		else: 
			print("2: Walk away.]")
		choice = checkNum(1,2)
		if choice == 1:
			attackMan(1)
		elif choice==2 and itemOfChoice==1:
			deaths(11)
		else:
			deaths(12)
	else:
		print("\n\n\"you--")
		attackman(1)

# ENDINGS
# All the endings and ending option functions

def deaths(number): # player death dialogues
	print("\n\n")
	if number == 1:
		print("[The dream world around you fades as you feel a gentle beeping in your mind. The countdown has run out. You wake up 3 hours late.]")
		# time.sleep(2)
		print("[on a Sunday.]")
		# time.sleep(2)
		print("[Yet the Sandman knows no mercy! A plume of sand descends upon you, suffocating you. You die.]")
	elif number == 2:
		print("[Your HP has run out. You have died, both in your dream and in the real world. Shame.]")
	elif number == 3:
		print("[You swing the rubber chicken wildly until its cries fill the dense air. You wake up, relieved, yet strangely unsatisfied. Boring.]")
	elif number == 4:
		print("[The Cheshire Cat waves its arms wildly and dissolves into the air. You wake up, relieved, yet strangely unsatisfied.]")
	elif number == 5:
		print("[The world arounds you slowly fades away. You have died of dysentery.]")
	elif number == 6:
		print("[Lakitu raises his glowing fishing rod and yanks you high into the air. You wake up, exhilerated by the ride.]")
	elif number == 7:
		print("[You use your Red Brick to bash the Sandman's head in, lifting his curse. You wake up, satisfied.]")
	elif number == 8:
		print("[You use your Super Soaker to soak the Sandman's body. He caves into himself and disappears. You wake up, satisfied.]")
	elif number==9 or number==10:
		print("[You jab your fist into the Sandman's chest. He looks up at you with welling eyes. He is dead. You wake up, satisfied.]")
	elif number == 11:
		print("[You return the Sand Bag to the Sandman.]")
		# time.sleep(1)
		print("\n\n\"Thank you. This means a lot. You seem to have changed.")
		# time.sleep(1)
		print("...as a result. I will lift my curse.")
		# time.sleep(2)
		print("\n\n[You feel the curse finally lifted from you. The Sandman has finally forgiven you. You wake up, transformed. You learned your lesson: Don't steal the Sandman's stuff.]")
	else:
		print("[You walk away]")
		# time.sleep(2)
		print("\n\n\"What? Not going to finish the job?")
		# time.sleep(1)
		print("I'm grateful. I hope you learned a lesson.")
		# time.sleep(1)
		print("I won't forgive you until you return my Sand Bag, but I see no point in keeping you around if you don't have it.\"")
		# time.sleep(1)
		print("\n\n[The Sandman snaps his fingers. You wake up, confused. Did you learn your lesson? Only time will tell.]")
	# time.sleep(2)
	print("""      ___________
     /=//==//=/  \\
    |=||==||=|    |
    |=||==||=|~-, |
    |=||==||=|^.`;|
jgs  \\=\\\\==\\\\=\\`=.:
      `"""""""`^-,`.
               `.~,'
              ',~^:,
              `.^;`.
               ^-.~=;.
                  `.^.:`.

[You died/completed the game with """+str(countdown)+" minutes and "+str(HP)+"HP to spare! Play again?]")
	choice = check("yes","no","credits")
	if choice == "yes":
		restart()
	if choice == "no":
		sys.exit(0) # exit program: https://stackoverflow.com/questions/48129942/python-restart-program Uses sys.exit to exit cleanly w/o KeyboardInterrupt
	else:
		credits()

def credits(): # end credits
	# time.sleep(1)
	print("\nWriting and Programming: Kevin Xie")
	# time.sleep(1)
	print("\nArt: ASCIIART.eu, ASCII.co.uk, and PatorJK")
	# time.sleep(1)
	print("\nSoftware: The Python Software Foundation")
	# time.sleep(1)
	print("\nProgramming Advisors: Ms. Healey, StackOverflow, and GeeksforGeeks")
	# time.sleep(2)
	print("\n\nPlaytesting: You")
	# time.sleep(1)
	os.exit(0)

def restart(): # function for restarting the program (calling python file again)
	pyName = "adventure.py"
	while os.path.isfile(pyName) == False: # catches if file name is changed. https://stackoverflow.com/questions/32536129/python-try-except-oserror-errno-2 and https://docs.python.org/2/library/os.path.html#os.path.isfile uses the os library function isfile to check if the .py filename is indeed real. Doesn't leave loop unless it is.
		pyName = input("\n[Restart failed! What is the full name of the python file currently running? (incl. the .py extension)] \n\n>>> ")
		print("\nThank you.")
	else: # if filename does exist
		print("\n\nRestarting...")
		# time.sleep(1)
		os.system("python "+pyName) # restart from within self using os library (contingent on name of program not being changed -- haven't tested this in systems with multiple Python versions!!!): https://stackoverflow.com/questions/11329917/restart-python-script-from-within-itself

# CHECK TOOLS
# multiple-use functions for checking answer-related errors and player statistics

def watchLook(): #to report player statistics from time to time
	if countdown<=0: # if the player timer or HP falls below 0, then the game ends.
		deaths(1)
	elif HP<= 0:
		deaths(2)
	else:
		print("["+str(countdown)+" minutes and "+str(HP)+"HP remaining. Time moves unpredictably in the dream world.]")

def check(*argv): # variable arguments https://www.geeksforgeeks.org/args-kwargs-python/ argv is taken from geeksforgeeks, but should be able to be anything, right? * indicates variability
	global stupidSelf
	print("[Choose between", end = " ") # print without newline: https://www.geeksforgeeks.org/print-without-newline-python/ uses second argument in print
	for arg in argv: # adds an option for every argument in the function (underutilized, but hey, it's there!)
		print(arg, end = "")
		if argv.index(arg) < (len(argv)-2):
			print(", ", end = " ")
		elif argv.index(arg) == (len(argv)-2):
			print(", or", end = " ")
		elif argv.index(arg) == (len(argv)-1):
			print(".]")
	choice = input(">>> ")
	for arg in argv:
		if choice.lower() == arg.lower(): # lowercase conversion: https://stackoverflow.com/questions/9257094/how-to-change-a-string-into-uppercase useful for if the user types in capitals etc. it will still accept
			return choice.lower()
			break
	print("\n[That wasn't one of the choices! \""+random.choice(stupidSelf)+"\" You think to yourself. Try again.]") # random function choice: https://stackoverflow.com/questions/5465455/syntax-to-call-random-function-from-a-list
	choice = check(*argv) # loops around -- in first trials, if the function loops, it returns None as a result since it is ending without returning after the nested loop parses. You have to set the choice to the nested loop and then return that choice in order to receive the correct value. Oof.
	return choice


def checkNum(a,b):
	global stupidSelf # quips
	while True: # basic error check for whether choice is a number, only breaks once the entered variable is an integer.
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

# THE ONLY LINE OF CODE!

titles() # the adventure begins!