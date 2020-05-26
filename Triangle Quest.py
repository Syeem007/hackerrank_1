
'''
for i in range(1, 5):
    print("")
    for j in range(i):
        print(i,end="")
'''

for i in range(1, int(input())):
    print(round((10 ** i - 1) / 9) * i)
