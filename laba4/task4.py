en = int(input("Введите xисло одно: "))
print(en)
e = '2.71828182845904523536028747135266249775724709369995957496696762772407663035354759457138217852516642742'
s = ''
count = 0
for i in e:
    count += 1
    s += i
    if count == en:
        break



print(s)
print(e)
