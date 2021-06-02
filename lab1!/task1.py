klet_n = int(input('введите первую цифру клетки 1 '))
klet_m = int(input('введите вторую цифру клетки 1 '))
klet_q = int(input('введите первую цифру клетки 2 '))
klet_w = int(input('введите вторую цифру клетки 2 '))

kl1 = ''
kl2 = ''

if klet_n % 2 == 0 and klet_m % 2 == 0 or klet_m % 2 == 1 and klet_n % 2 == 1:

    kl1 = 'black'
else:
    kl1 = 'white'

if klet_q % 2 == 0 and klet_w % 2 == 0 or klet_q % 2 == 1 and klet_w % 2 == 1:

    kl2 = 'black'
else:
    kl2 = 'white'


if kl1 == kl2:
    print('YES')
else:
    print('NO')

