# Python code to demonstrate math.factorial()
n = int(input())
i = n
sum = 1
while i >= 1:
    sum *= i
    i -= 1
print(sum)
