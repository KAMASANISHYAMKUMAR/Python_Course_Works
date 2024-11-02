



#map(func,*iterables) -> map object | iterable
import time

lst_rad=[1.2,3.3,2.34]

for i in map( lambda rad: 3.14*rad*rad ,lst_rad) :
    time.sleep(.2)
    print(i)
