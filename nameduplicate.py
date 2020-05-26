from collections import OrderedDict,namedtuple

d=OrderedDict()
n=int(input())
for i in range(n):
    ID,MARKS,NAME,CLASS=str(input()).split()
    Point = namedtuple('Point', 'x')
    print(sum(MARKS)/len(MARKS))
