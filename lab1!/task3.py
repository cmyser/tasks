klet_n = int(input('введите первую цифру клетки 1 '))
klet_m = int(input('введите вторую цифру клетки 1 '))
klet_q = int(input('введите первую цифру клетки 2 '))
klet_w = int(input('введите вторую цифру клетки 2 '))

if abs(klet_n - klet_m) == abs(klet_q - klet_w) :
    print('YES')
else:
    print('NO')