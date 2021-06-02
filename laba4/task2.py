n = int(input(' i need a value: '))


n = format(n, 'b')
print(type(n))
count = 0
for i in n:

    if i == '1':
        count += 1
print(count)