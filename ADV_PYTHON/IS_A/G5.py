
class GFather:
    def house(self):
        print("house from GFather")

class Father(GFather):
    def car(self):
        print("car from Father")

class Son(Father):
    def bike(self):
        print("bike from son")

    def properties(self):
        self.house()
        self.car()
        self.bike()

#calling
s=Son()
s.properties()
        
