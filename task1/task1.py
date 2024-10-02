a = int(input())
b = int(input())
if a % 2 == b % 2:
    print(abs(b - a) // 2)
elif a % 2 == 1:
    print(abs(a - b + 1) // 2)
else:
    print(abs(a - b - 1) // 2)
