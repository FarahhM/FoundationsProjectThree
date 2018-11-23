# UTILS AND FUNCTIONALITY
from data import  population, clubs
from components import Club, Person

my_name = "Farah"
my_age = 22
my_bio = "Live happily & tell no one, people ruin beautiful things!"
myself = Person(my_name, my_bio, my_age)


def introduction():
	print("Hello, %s. Welcome to our portal." % my_name)


def options():
	# your code goes here!
	
	cond=True
	#user_choice=int(input(">"))
	user_choice=""
	while user_choice!=-1:
		print("-----------------------------------")
		print("What would you like to:\n")
		print("1)Creat a club.\n or:\n")
		print("2)Browse and join clubs\n or:\n")
		print("3)View existing clubs\n or:\n")
		print("4)Display members of a club\n or:\n")
		print("-1)close application\n")
		user_choice=int(input(">"))
		
		if user_choice==1:
			create_club()
		elif user_choice==2:
			join_clubs()
		elif user_choice==3:
			view_clubs()
		elif user_choice==4:
			view_club_members()
		elif user_choice==-1:
			quit()



def Members():
	print("-----------------------------------")
	index=0
	for p in population:
		print ("[%s] %s" %(index+1, p.name))
		index+=1
		
		

def create_club():

	# your code goes here!
	club_name= input("Pick a name for your awesome new club: \n")
	about= input("What is your club about? \n")
	
	club1=Club(club_name, about)
	club1.recruit_member(myself)
	club1.assign_president(myself)
	clubs.append(club1)
	print("Enter number of the people you would like to recruit to your new club.(-1 to stop):\n")
	#while int(m_choice) != -1:
	index=0
	for p in population:
		print ("[%s] %s" %(index+1, p.name))
		index+=1

	m_choice=int(input())
	
	while m_choice!=-1:
		
		m_choice=int(input())
		if m_choice==1:
			m1=population[0]
			club1.recruit_member(m1)
		elif m_choice==2:
			m1=population[1]
			club1.recruit_member(m1)
		elif m_choice==3:
			m1=population[2]
			club1.recruit_member(m1)
		elif m_choice==4:
			m1=population[3]
			club1.recruit_member(m1)
		elif m_choice==5:
			m1=population[4]
			club1.recruit_member(m1)
		elif m_choice==6:
			m1=population[5]
			club1.recruit_member(m1)
		elif m_choice==7:
			m1=population[6]
			club1.recruit_member(m1)
		elif m_choice==8:
			m1=population[7]
			club1.recruit_member(m1)
		elif m_choice==9:
			m1=population[8]
			club1.recruit_member(m1)
		elif m_choice==10:
			m1=population[9]
			club1.recruit_member(m1)
		elif m_choice==11:
			m1=population[10]
			club1.recruit_member(m1)
		elif m_choice==12:
			m1=population[11]
			club1.recruit_member(m1)
		elif m_choice==13:
			m1=population[12]
			club1.recruit_member(m1)
		elif m_choice==14:
			m1=population[13]
			club1.recruit_member(m1)
		elif m_choice==15:
			m1=population[14]
			club1.recruit_member(m1)
		
	print("Here's your club:\n%s\n%s" % (club_name, about))
	club1.print_member_list()
	#you have to ADD A COND TO CHECK THAT THE USER TYPES an int not just a space or enter!!
	#if m_choice.isdigit() and m_choice<=len(population)
		
	

def view_clubs():
	# your code goes here!
	for club in clubs:
		print("\tName: %s\n \tDescreption: %s\n \tMembers: %s\n" % (club.name, club.description, len(club.people)))
		
		

def view_club_members():
	# your code goes here!
	view_clubs()
	cond=False
	while not cond:
		c_name=input("Enter the name of the club whose members you'd like to see:\n")
		for club in clubs:
			if c_name==club.name:
				club.print_member_list()
				cond=True
			

def join_clubs():
	# your code goes here!
	view_clubs()
	choice=input("Enter the name of the club you'd like to join:\t")
	for club in clubs:
		if choice == club.name:
			club.recruit_member(myself)
			print("%s just joined %s!"% (myself.name, club.name))
			print("-----------------------------------")

	

def application():
	introduction()
	options()
	# your code goes here!
	
