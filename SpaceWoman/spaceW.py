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
	choice = input("Rocket or SpaceFreighter?\n>")
	# What does Hanna need to do on mars?

# string->String
# determines the players choice of rocket spacefreighter
# def Rocket_freighter "r": "s"
#given rocket, expect rocket()
#given spaceFreighter expects spaceFreighter
def rocket_freighter(c):
	if c.lower() == "rocket":
		rocket()
	elif c.lower() == spacefreighter:
		space_freighter
