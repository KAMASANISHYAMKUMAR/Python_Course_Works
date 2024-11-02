




#{<exp> for variable in iterable if test } -> dic object
#exp should be in the form of key and value pair

d={i:i for i in range(1,4)}
print("Type is : ",type(d))
print("Data is : ",d)
print("=============================")

d2={ i: i*i for i in range(1,5) }
print("Result : ",d2)
print("==============================")

import math
d3={i:math.factorial(i) for i in range(1,5)}
print("Result is : ",d3)
print("===============================")























