#Public,Private and Protected access modifiers
#public can be modified anywhere 
#Usage eg: self.abc
#private can only be modified in main class 
#Usage eg: self.__abc
#protected can only be modified in sub class
#Usage eg: self._abc


class car:
    def __init__(self,window,door,enginetype):
        self.windows=window
        self.doors=door
        self.enginetype=enginetype

    def type(self):
        print("This is a {} car".format(self.enginetype))

class mod(car):
    def __init__(self, window, door, enginetype,horsepower):
        super().__init__(window, door, enginetype)
        self.horsepower=horsepower


car1 = car(4,4,'petrol')
car2 = car(4,5,'diesel')
car3 = car(5,5,'diesel')

#car4 = mod(4,4,'petrol',560) #-- protected modifier

print(car3.doors)
#print(car4.horsepower) 
car1.type()

