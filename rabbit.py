# def fib(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
# print(fib(90))
#
#
# def fib_memoize(n, d):
#     if n in d:
#         return d[n]
#     else:
#         ans = fib_memoize(n - 1, d) + fib_memoize(n - 2, d)
#         d[n] = ans
#         return ans
# base_case = {0: 1, 1: 1}
# print(fib_memoize(996, base_case))


def hanoi(q, fromq, to, buf):  # Сделано из викимедии:
    if q != 0:  # https://upload.wikimedia.org/wikipedia/commons/1/11/Hanoi_flow_chart.ru.svg
        hanoi(q - 1, fromq, buf, to)
        print(f'Передвигаем с {fromq} на {to}')
        hanoi(q - 1, buf, to, fromq)


hanoi(4, '1', '3', '2')
