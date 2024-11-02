
class Father:
    def house(self):
        print("house from Father")

class Son(Father):
    def bike(self):
        print("bike from son")

#calling
s=Son()
s.bike()
s.house()
