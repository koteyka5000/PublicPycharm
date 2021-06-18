q = input()
listq = list(q)
l = 0
u = 0
for lol in listq:
    if lol.islower():
        l += 1
    elif lol.isupper():
        u += 1
print(f'Строчные: {l}, Заглавные: {u}')
