import random

# None->String
# displayes the intro to spacewoman
# def intro() "welcome"
# given None, expects strings
def intro():
	print("------------SPACEwOMAN VERSION ALPHA 2.0---------------\n")
    print("You are Hanna Zoes traveling in computer city in 1950. You are about to go on ")
    print("a mediocure adventure writen by a subpar programmer. Play this game ")
    print("at the risk of severe bordom.")

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
def tractorBeam():
	print("Something is pulling you toward a planet You will not survive if you keep")
	print(" going toward the planet To bad you loose")

#  None -> string
# tells the player that they have made a safe passage to mars
# def safePass(): s
# tests
# templates
def safePass():
	print("Oh, no you have made a safe passage to mars , unfortunatly you win the game.")
	print("next time figure out how to lose. Thats an order")
	
# None -> string
# tells the user he/she is on mars
# def mars(): string
# tests
# template
def mars():
	print("I still need to write one more function. If you have made it this far in the game thank you.")
	print("If you have not made it this far in the game, I guess you wont be reading this.")
	print("good morning")

while True:
    intro()
    choice = input(">")
    rocket_freighter(choice)
    obsticle = random.randint(0, 2)
    if obsticle == 1:
	    safePass()
    elif obsticle == 2:
	    tractorBeam()
    elif obsticle == 0:
	    black_hole()
    else: 
        print("you should not be here")
    
    print("Do you want to play again?")
    
    
	
   


	
	