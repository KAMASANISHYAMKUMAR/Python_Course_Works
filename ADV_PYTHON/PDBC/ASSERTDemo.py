
#assert <condition>,"message"
import time
def sq(x):
    s=x*x
    return s

#calling
assert sq(2)==4,"Sq(2) should be 4 but not...."
r=sq(2)
print("Result is : ",r)

time.sleep(2)
assert sq(3)==9,"sq(3) should be 9 but not...."
r=sq(3)
print("Result is : ",r)

time.sleep(2)
assert sq(4)==16,"sq(4) should be 16 But not...."
r=sq(4)
print("Result is : ",r)





