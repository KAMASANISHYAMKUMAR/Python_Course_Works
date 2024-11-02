
class Sample:
    pass

#calling
Sample.x=10
print("static x : ",Sample.x) #10

s=Sample()
s.x=20
print('Inst x : ',s.x) #20

Sample.x=99
print("static x : ",Sample.x)  #99

del s.x
del Sample.x
