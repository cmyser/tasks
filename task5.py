m = list(input())

print(m)
m = m[::-1]
print(m)
n = ''
for i in m:
    n += i

print(int(n))