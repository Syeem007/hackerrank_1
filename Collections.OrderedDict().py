from collections import OrderedDict

d = OrderedDict()

for i in range(int(input())):
    key,space,values=input().rpartition(" ")
    d[key] = d.get(key,0)+int(values)
for key,values in d.items():
    print(key,values)
'''
from collections import OrderedDict
d = OrderedDict()
for _ in range(int(input())):
    item, space, quantity = input().rpartition(' ')
    d[item] = d.get(item, 0) + int(quantity)
for item, quantity in d.items():
    print(item, quantity)
'''










