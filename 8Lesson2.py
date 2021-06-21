q = int(input())
for i in range(1, q - (q // 2) + 1): print('*' * i)
for i in range(q - (q // 2) - 1, 0, -1): print('*' * i)