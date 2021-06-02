def odn(n):
    count = 1
    s = 0
    for i in n:
        if s == i:
            count += 1
        s = i

    print(count)

odn([1,1,1,1,1,1,1,45,465,676,786,8])