s = str(input())
no_digits = []
digits = []

odddigits = []
evendigit = []

for i in s:
    if not i.isdigit():
        no_digits.append(i)
    else:
        digits.append(i)
for j in digits:
    if (int(j) % 2)==0:
        evendigit.append(j)
    else:
        odddigits.append(j)

result = ''.join(no_digits)
result1 = sorted(result,key=lambda x:x.lower())
result2=''.join(result1)
new_result1 = ''.join(odddigits)
new_result2 = ''.join(evendigit)
new_result3 = new_result1 + new_result2
print(result2+new_result3)
# result=result[::-1]
#print(str(result1) + new_result3)
