


#complex type casting using

#complex(x)
#x-rep real part | where imag always remains 0
x=123
x=12.12
x=True
x="123"
y=complex(x)
print(type(x)," ----> ", type(y) )
print("x : ",x," ----> ","y : ",y)
print("=====================")


#complex(x,y)
#x-rep real part | where y rep imag part
#string with other combinations are not supported.
