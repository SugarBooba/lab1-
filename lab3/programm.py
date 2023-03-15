def func(arg):
    e = -457
    z = 171
    ac = arg

    if ac <= 0:
        if ac > e:
            ac *= 3
            ac -= z
        else:
            ac = e
    else:
        ac = e
    return ac


b, c, d = int(input()), int(input()), int(input())
ac = 0
a = ac

ac = b-1
ac = func(ac)
ac+=a
a = ac

ac = c+1
ac = func(ac)
ac-=a
a = ac

ac = d
ac = func(ac)+1
ac-=a
a = ac


