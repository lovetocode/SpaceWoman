# None->String
# displayes the intro to spacewoman
# def intro() "welcome"
# given None, expects "Hello and welcome to SpaceWoman
def intro():
	print("------------SPACEwOMAN VERSION ALPHA O.1---------------\n")
	print("You are about to embark on the adventures of Hanna Zoes")
	print("An amateur detective and space traveler")
	print("Your first mission is to travel to mars")
	print("Do you want to take a rocket or spacefreighter\n")
	choice = input("Rocket or Freighter?\n>")
	rocket_freighter(choice)
	# What does Hanna need to do on mars?

# string->String
# determines the players choice of rocket spacefreighter
# def Rocket_freighter "r": "s"
#given rocket, expect rocket()
#given spaceFreighter expects spaceFreighter
def rocket_freighter(c):
	if c.lower() == "rocket":
		rocket()
	elif c.lower() == "freighter":
		freighter()
	
		
# String->String
# Takes the player to mars on a rocket
# def rocket(): "string
# Tests
def rocket():
	print("It will take you 2 months to arrive on the moon")
	print("you are the captain of the rocket and are able")
	print("to make it go up, down, left, right\n")
	print("There will be black holes and other obstacles along the way")
	
# None->string
# the player takes a freighter to mars
# def freighter(): string
# tests
def freighter():
	print("You are a passenger of a freighter captained by someone else")
	print("you can sit back and enjoy the sights and environment of the")
	print("freighter.\n")
	print("There will be many obstacles for you to over come.")
	
# String->String
# a black is an obsticle for the player in the game
# def black_hole(): string
# tests
# template
def black_hole():
	print("oh, no you have hit a black hole.")
	print("You are being quick.y sucked into it")
	print("what do you want to do:")
	print("Thrusters back, left, right, forward")
	direction = input("<")
	if direction == "left":
		print("You have gone in the wrong direction")
		print("You were sucked into the black hole")
		print("Game over")
	elif direction == "right": 
		print("Yes you have made a good choice and are", end="")
		print("are on your way back to the moon")
	elif direction == "back":
		print("Can't go backward here")
		print("game over")
	elif direction == "forward":
		print("You are back on your way to the moon")
	else: print("error")

# String -> String
# a tractor beam
# def Tractor_beam((): string
# tests
# template
def black_hole():
	print("Something is pulling you toward a planet You will not survive if you keep")
	print(" going toward the planet To bad you loose")
	
black_hole()

		
		
