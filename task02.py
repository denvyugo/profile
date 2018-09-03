import cProfile

def erat_sieve(p):
    n = p
    while True:
        a = [0] * n  # создание массива с n количеством элементов
        for i in range(n):  # заполнение массива ...
            a[i] = i  # значениями от 0 до n-1
        # вторым элементом является единица, которую не считают простым числом
        # забиваем ее нулем.
        a[1] = 0
        m = 2  # замена на 0 начинается с 3-го элемента (первые два уже нули)
        while m < n:  # перебор всех элементов до заданного числа
            if a[m] != 0:  # если он не равен нулю, то
                j = m * 2  # увеличить в два раза (текущий элемент - простое число)
                while j < n:
                    a[j] = 0  # заменить на 0
                    j = j + m  # перейти в позицию на m больше
            m += 1
        # вывод простых чисел на экран (может быть реализован как угодно)
        b = []
        for i in a:
            if a[i] != 0:
                b.append(a[i])
        del a
        if len(b) >= p:
            print(b)
            break
        else:
            n *= 2
    print(f'искомое {p}-ое простое число: {b[p-1]}')

# python -m timeit -n 100 -s "import task02" "task02.erat_sieve(15)"
# 100 loops, best of 5: 937 usec per loop
# python -m timeit -n 100 -s "import task02" "task02.erat_sieve(150)"
# 100 loops, best of 5: 2.48 msec per loop
# cProfile.run("erat_sieve(1500)")
# 42 function calls in 0.000 seconds
# 412 function calls in 0.001 seconds
# 5569 function calls in 0.034 seconds


def find_simple(p):
    b = [2]
    i = 0
    while True:
        if len(b) == p:
            print(b)
            break
        n = b[i] + 1
        while True:
            for j in range(2, n):
                if n % j == 0:
                    n += 1
                    break
            else:
                b.append(n)
                i += 1
                break
    print(f'искомое {p}-ое простое число: {b[p-1]}')

# python -m timeit -n 100 -s "import task02" "task02.find_simple(15)"
# 100 loops, best of 5: 934 usec per loop
# python -m timeit -n 100 -s "import task02" "task02.find_simple(150)"
# 100 loops, best of 5: 5.48 msec per loop
# cProfile.run("find_simple(1500)")
# 35 function calls in 0.000 seconds
# 305 function calls in 0.009 seconds
# 3005 function calls in 0.866 seconds

# if __name__ == '__main__':
#     n = int(input("поиск простого числа номер: "))
#     erat_sieve(n)
#     find_simple(n)