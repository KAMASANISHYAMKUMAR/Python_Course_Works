




small=lambda x,y,z: x if x<y and x<z else
                                      y if y<x and y<z else
                                      z
s=small(10,2,1)
print("Small : ",s)
