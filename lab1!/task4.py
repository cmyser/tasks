klet_n = int(input('введите первую цифру клетки 1 '))
klet_m = int(input('введите вторую цифру клетки 1 '))
klet_q = int(input('введите первую цифру клетки 2 '))
klet_w = int(input('введите вторую цифру клетки 2 '))
dn = abs(klet_n - klet_q)
dq = abs(klet_q - klet_w)
mw = abs(klet_m - klet_w)
if dn == 1 and dq == 2 or dn == 2 and mw == 1 or mw == 2:
    print('YES')
else:
    print('NO')