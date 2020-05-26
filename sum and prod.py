import numpy

m,n = list(map(int,input().strip().split()))

# Below line read inputs from user using map() function
a = list(map(int, input().strip().split()))[:m]
b = list(map(int, input().strip().split()))[:n]

c=numpy.array([[a],[b]])
print(c)
x = numpy.sum(c, axis=0)
print(numpy.prod(x))
