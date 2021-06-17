import sys
from random import randrange
sys.setrecursionlimit(60000)

hunger_threshold = 10
boredom_threshold = 5
animals=[]
sounds=[]

#User defined class begins...
#
#
class Pet() :
	def __init__(self,name) :  #CONSTRUCTOR for a new class instance
		self.name = name
		animals.append(self.name)
		self.hunger = randrange(hunger_threshold)
		self.boredom = randrange(boredom_threshold)
		self.prsnl_sound=sounds[:]
		
	def clock_tick(self) :  #CLOCK_TICK function 
		self.hunger+=1
		self.boredom+=1
		
	def Teach(self,word) :  #function to teach the pet a new word
		self.prsnl_sound.append(word)
		self.clock_tick()
		self.boredom-=1
		return self.__str__()
		
	def Hi(self) :  #function to GREET the pet
		self.clock_tick()
		self.boredom-=1
		if (len(self.prsnl_sound)==0) :
			return "Sorry, :( I don't know anything "
		return self.prsnl_sound[randrange(len(self.prsnl_sound))]
		
	def Feed(self) :  #function to feed the pet 
		self.clock_tick()
		self.hunger-=2
		return self.__str__()
		
	def __str__(self) :  #Chating Pet 
		if (self.hunger>=hunger_threshold) and (self.boredom>=boredom_threshold) :
			return "UnHappy :( "
		elif (self.hunger>=hunger_threshold) :
			return "Hungry :P  "
		elif (self.boredom>=boredom_threshold) :
			return "Bored :/ "
		else :
			return "Happy :) "
#
#			
#End of the user defined class


# Making game easy for non-programmers (end-users)
#
#
def inList(pet_list, name) :
	for pet in pet_list :
		if pet==name :
			return pet
		else :
			return None
				
def play() :
	initial="Adopt <enter the name of your pet> \nGreet <your pet name> \nFeed  <your pet name> \nTeach <your pet name..space..word to be taught> \nQuit\n"
	while (True) :
		response=input(initial).title()
		words=response.split()
		print("\n")
		if words[0]=="Adopt" :  # ADOPT a pet
			if inList(animals, words[1]) :
				print("Alas! The pet is already adopted :( \nTry adopting someone else :)")
			else :
				pet=Pet(words[1])
		elif words[0]=="Greet" :  # GREET a pet
			if inList(animals, words[1]) :
				print(pet.Hi()) 
			else :
				print("I did not understand which pet to greet :(\nTry again...")
		elif words[0]=="Feed" :  # FEED a pet 
			if inList(animals, words[1]) :
				pet.Feed()
			else :
				print("I did not understand which pet to feed :(\nTry again...")
		elif words[0]=="Teach" :  # TEACH a pet 
			if inList(animals, words[1]) :
				pet.Teach(words[2]) 
			else :
				print("I did not understand which pet to teach :(\nTry again...")
		elif words[0]=="Quit" :  # EXIT game
			print("Have a nice day, Good Bye !! :) ;) ")
			break
		else :
			print("I did not understand :(\nTry again...")
		print(pet)
		print("\n")	
#
#
# Easy Making Done ;)

play() 
