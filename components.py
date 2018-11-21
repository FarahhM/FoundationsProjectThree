# CLASSES AND METHODS
class Person():
    def __init__(self, name, bio, age):
        # your code goes here!
        self.name= name
        self.bio= bio
        self.age= age


class Club():
    #people=[]
    def __init__(self, name, description):
        # your code goes here!
        self.name= name
        self.description= description
        self.people=[]
        self.president= None

    def assign_president(self, person):
        # your code goes here!
        
        if person in self.people:
            self.president= person
        else:
            print("this person can't be a president, for he is not a member!")


    def recruit_member(self, person):
        # your code goes here!
        if person not in self.people:
            self.people.append(person)

    def Average(self):
        age=0
        for p in self.people:
            age+= p.age
        avg= age/len(self.people)
        return avg
        
        
    def print_member_list(self):
        # your code goes here!
        print("Members:")

        for p in self.people:
            if p is self.president:
                print("-%s (%s years old, President) -%s"% (p.name, p.age, p.bio))
            else:
                print("-%s (%s years old) -%s"% (p.name, p.age, p.bio))
        print("Average age in this Club: %syear" % self.Average())
        print("-----------------------------------")

