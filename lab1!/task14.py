n = int(input())

b1 = b2 = 1
for i in range(2, n):
    b1, b2 = b2, b1 + b2
    print(b2, end=' ')