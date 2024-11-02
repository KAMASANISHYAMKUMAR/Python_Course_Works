class Mother:
    def color(self):
        print("Color From Mother ")

class Father:
    def height(self):
        print("Height From Father ")

class Son(Father,Mother):
    def attitute(self):
        print("A From Son")

#calling
s=Son()
s.height()
s.color()
s.attitute()
    
