import numpy


m,n = list(map(int,input().strip().split()))
print(numpy.eye(m,n,k=0))
# Below line read inputs from user using map() function
#a = list(map(int, input().strip().split()))[:m]
#b = list(map(int, input().strip().split()))[:n]

#print(str(numpy.eye(*map(int,input().split()))).replace('1',' 1').replace('0',' 0'))



