# from turtle import Turtle, Screen

# timy = Turtle()
# scrn = Screen()
# timy.shape("turtle")
# timy.color("green")
# timy.forward(100)
# print(scrn.canvheight)
# scrn.exitonclick

class Animal:
    def __init__(self, legs, horns):
        self.legs = legs
        self.horns = horns

    def can_walk(self):
        if self.legs == 4:
            print("the animal can walk")
        else:
            print("probably fly")
    def has_wings(self):
        if self.legs == 2:
            print("the animal having wings")
            if self.horn == 0:
                print("can fly")
    def is_turle(self, body):
        if self.legs == 2:
            if self.horns == 0:
                if body == "stone":
                    print ("is a turtle")
                    self.has_wings
                else:
                    print("not a turtle")
                    self.can_walk

animal = Animal(legs = 2, horns = 0)
animal.is_turle('plate')

class Reptiles(Animal):
    def __init__(self,legs):
        self.legs = legs
r= Reptiles(3)
r.can_walk()
    

        
