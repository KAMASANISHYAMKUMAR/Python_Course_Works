
Logical Operators
    In Other Languages :
           and - && | or - || | not - !           
     
  x,y,z=10,20,30

  if x>y and x>z then x is big
  if y>x and y>z then y is big
  if z>x and z>y then z is big

       logical and
 exp1    exp2     Result
 True     False    False
 False   True     False
 False    False   False
 True     True     True

         logical and
      x,y,z=10,20,30
      
  exp1     exp2        Result
  x>y F    x>z F        (x>y and x>z)   F and F -> F
  y>x T    y>z F        (y>x and y>z)  T and F -> F
  z>x T    z>y T        (z>x and z>y)   T and T -> T
  
   
          logical or
exp1    exp2     Result
 True     False    True
 False   True     True
 True     True     True
False   False   False
 
 
logical not
x,y=10,20
r=x>y
print(r)  #False

r=not x>y
print(r) #True













  




     
