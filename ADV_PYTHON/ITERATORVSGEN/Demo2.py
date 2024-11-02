
import time

'''
for i in range(1,10):
    time.sleep(1)
    print(i)
'''



class MyRange(object):
    def __init__(self,start,end,step=1):
        self.start=start
        self.end=end
        self.step=step

    def __iter__(self):
        return self

    def __next__(self):
        self.cur=self.start
        if self.start>self.end:
            raise StopIteration()
        self.start=self.start+self.step
        return self.cur

for i in MyRange(1,10,2):
    time.sleep(1)
    print(i)












    

    
    
