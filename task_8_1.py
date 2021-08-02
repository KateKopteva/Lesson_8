def fact_2(n):
    if (n == 0 or n == 1):
        return 1

    return n * fact_2(n - 2)

p = [5, 6, 7, 8, 9]
for i in p:
    print('Двойной факториал равен:', fact_2(i))