
#float type casting using float( )

#int -> float 
x=12
y=float(x)
print(type(x)," ----> ", type(y) )
print("x : ",x," ----> ","y : ",y)
print("=====================")

#complex -> float
x=10+20j
'''y=float(x)
TypeError: float() argument must be a string or
a real number, not 'complex'
'''

# str -> float
x="123.1212"
y=float(x)
print(type(x)," ----> ", type(y) )
print("x : ",x," ----> ","y : ",y)
print("=====================")

#bool -> float   True -> 1 -> 1.0 | False -> 0 -> 0.0
x=True
y=float(x)
print(type(x)," ----> ", type(y) )
print("x : ",x," ----> ","y : ",y)
print("=====================")






















