n=int(input())
for i in range(0,n-1):
    r,t=map(int,input().strip().split())
    try:
        x=(r/t)
    except ZeroDivisionError:
        print('Error Code: integer division or modulo by zero')
        try:
            r, t = map(int, input().strip().split())
            x = (r / t)
        except ValueError:
            print("Error Code: invalid literal for int() with base 10: '$'")



