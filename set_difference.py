

n = int(input())
a = list(map(int, input().strip().split()))[:n]
c=set(a)
m= int(input())
b = list(map(int, input().strip().split()))[:m]
d=set(b)
z=c.difference(d)
print(len(z))
