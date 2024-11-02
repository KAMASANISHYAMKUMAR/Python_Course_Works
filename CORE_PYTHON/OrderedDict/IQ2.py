
D=dict()
D.update({"sno":101})
D.update({"sname":"ramesh"})
D.update({"scity":"hyd"})
print("Dict : ",D)

import time
for k,d in D.items():
    time.sleep(1)
    print(k,d,sep=' >>> ')
print("======================")

import collections
od=collections.OrderedDict()
od.update({"sno":101})
od.update({"sname":"ramesh"})
od.update({"scity":"hyd"})
print("OrderedDict : ",od)

for k,d in od.items():
    time.sleep(1)
    print(k,d,sep=' <<<>>> ')











