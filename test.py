num = [2, -19, 14, 0, 9.14, -1.9]


def apply_to_each(l, f):
    for i in range(len(l)):
        l[i] = f(l[i])
    return l


def change_direction(q):
    q *= -1
    return q


apply_to_each(num, change_direction)
print(num)
