class Biggest:
    def setData(self,x,y):
        self.x=x
        self.y=y

    def findBiggest(self):
        if self.x>self.y:
            print("Biggest is : ",self.x)
        else:
            print("Bigges is : ",self.y)

#calling
b=Biggest( )
b.setData(10,20)
b.findBiggest( )

        
