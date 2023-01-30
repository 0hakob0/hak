# def pr():
#     print("python")
#
#     pr()
# pr()


# def say_hello():
#     print("Hello")
#
#
# message = say_hello
# message()

# def sum(a, b):
#     return a + b
#
# operation = sum
# result = operation(6, 7)
#
# print(result)

# def do_operation(a, b, operation):
#     result = operation(a, b)
#     print(f"result = {result}")
#
#
# def sum(a, b):
#     return a + b
#
# do_operation(5, 4, sum)


"""1"""

# import math

# def task():
#     a = int(input('4==> '))
#     b = int(input('5==> '))
#
#     am = a % 10
#     at = a % 100 // 10
#
#     bh = b % 1000 // 100
#     bhz = b // 10000
#     if am + at == bh + bhz:
#         print(True)
#     else:
#         print(False)
#
#
# task()


"""Return"""
# def task():
#     a = int(input('4==> '))
#     b = int(input('5==> '))
#
#     am = a % 10
#     at = a % 100 // 10
#
#     bh = b % 1000 // 100
#     bhz = b // 10000
#     if am + at == bh + bhz:
#         return True
#     else:
#         return False
#
#
# print(task())

"""2"""

# def task():
#     a = int(input('4==> '))
#     b = int(input('5==> '))
#
#     if a < 7000:
#         print(b // 1000 % 10 + b % 1000 // 100)
#     else:
#         print(a - b)
#
#
# task()


"""Return"""

# def task():
#     a = int(input('4==> '))
#     b = int(input('5==> '))
#
#     if a < 7000:
#         return b // 1000 % 10 + b % 1000 // 100
#     else:
#         return a - b
#
#
# print(task())


"""3"""

# def task():
#     a = int(input('4==> '))
#     b = int(input('5==> '))
#
#     ahz = a // 1000
#     ah = a // 100 % 10
#     at = a % 100 // 10
#     am = a % 10
#
#     if ahz == 1 or ah == 1 or at == 1 or am == 1:
#         print(b // 10000)
#     else:
#         print(ahz)
#
#
# task()

"""Return"""

# def task():
#     a = int(input('4==> '))
#     b = int(input('5==> '))
#
#     ahz = a // 1000
#     ah = a // 100 % 10
#     at = a % 100 // 10
#     am = a % 10
#
#     if ahz == 1 or ah == 1 or at == 1 or am == 1:
#         return b // 10000
#     else:
#         return ahz
#
#
# print(task())


"""4"""

# def task():
#     a = int(input('4==> '))
#     b = int(input('5==> '))
#     if (a % 100 // 10) * (a % 10) == b % 1000 // 100 * b % 1000 // 10:
#         print(f'{(a % 100 // 10) * (a % 10) } = { b % 1000 // 100 * b % 1000 // 10} s')
#     else:
#         print(f'{(a % 100 // 10) * (a % 10) } = { b % 1000 // 100 * b % 1000 // 10} d')
#
#
# task()


"""Return"""

# def task():
#     a = int(input('4==> '))
#     b = int(input('5==> '))
#     if (a % 100 // 10) * (a % 10) == b % 1000 // 100 * b % 1000 // 10:
#         return f'{(a % 100 // 10) * (a % 10) } = { b % 1000 // 100 * b % 1000 // 10} s'
#     else:
#         return f'{(a % 100 // 10) * (a % 10) } = { b % 1000 // 100 * b % 1000 // 10} d'
#
#
# print(task())


"""5"""

# def task():
#     a = int(input('4==> '))
#     b = int(input('5==> '))
#
#     if (a % 10) * (a % 100 // 10) == (b // 10000) * (b % 10):
#         print('y = 12')
#     else:
#         print('y = 0')
#
#
# task()


"""Return"""

# def task():
#     a = int(input('4==> '))
#     b = int(input('5==> '))
#
#     if (a % 10) * (a % 100 // 10) == (b // 10000) * (b % 10):
#         return 'y = 12'
#     else:
#         return 'y = 0'
#
#
# print(task())


"""6"""

# def task():
#     a = int(input('4==> '))
#     b = int(input('5==> '))
#
#     if (a // 1000) == (b // 10000) or (a // 1000) == (b % 10) or (a % 10) == (b // 10000) or (a % 10) == (b % 10):
#         print('LOGIN')
#     else:
#         print('PASSWORD')
#
#
# task()


"""Return"""

# def task():
#     a = int(input('4==> '))
#     b = int(input('5==> '))
#
#     if (a // 1000) == (b // 10000) or (a // 1000) == (b % 10) or (a % 10) == (b // 10000) or (a % 10) == (b % 10):
#         return 'LOGIN'
#     else:
#         return 'PASSWORD'
#
#
# print(task())

"""7"""

# def task():
#     a = int(input('4==> '))
#     b = int(input('5==> '))
#
#     if a == ((b // 10000) + (b // 1000 % 10) + (b // 100 % 10) + (b // 10 % 10) + (b % 10)) ** 2:
#         print(f'Yes')
#         print(True)
#     else:
#         print(False)
#
#
# task()


"""Return"""

# def task():
#     a = int(input('4==> '))
#     b = int(input('5==> '))
#
#     if a == ((b // 10000) + (b // 1000 % 10) + (b // 100 % 10) + (b // 10 % 10) + (b % 10)) ** 2:
#         return f'Yes'
#     else:
#         return False
#
#
# print(task())


"""8"""

# def task():
#     a = int(input('4==> '))
#     b = int(input('5==> '))
#
#     if b % 10 > a // 10 % 10:
#         print(b)
#     else:
#         print(a // 1000)
#
#
# task()


"""Return"""

# def task():
#     a = int(input('4==> '))
#     b = int(input('5==> '))
#
#     if b % 10 > a // 10 % 10:
#         return b
#     else:
#         return a // 1000
#
#
# print(task())


"""9"""

# def task():
#     a = int(input('4==> '))
#     b = int(input('5==> '))
#     y = 1
#     if (a // 1000) + (a // 100 % 10) + (a // 10 % 10) + (a % 10) >= (b // 10000) + (b // 1000 % 10) + (b // 100 % 10) + (b // 10 % 10) + (b % 10):
#         print(y)
#     else:
#         y = 0
#         print(y)
#
#
# task()


"""Return"""

# def task():
#     a = int(input('4==> '))
#     b = int(input('5==> '))
#     y = 1
#     if (a // 1000) + (a // 100 % 10) + (a // 10 % 10) + (a % 10) >= (b // 10000) + (b // 1000 % 10) + (b // 100 % 10) + (b // 10 % 10) + (b % 10):
#         return y
#     else:
#         y = 0
#         return y
#
#
# print(task())


"""10"""

# def task():
#     a = int(input('4==> '))
#     b = int(input('5==> '))
#     if (a // 1000) * (a // 100 % 10) * (a // 10 % 10) * (a % 10) > b:
#         y = 0
#         print(y)
#     else:
#         y = 1
#         print(y)
#
#
# task()


"""Return"""

# def task():
#     a = int(input('4==> '))
#     b = int(input('5==> '))
#     if (a // 1000) * (a // 100 % 10) * (a // 10 % 10) * (a % 10) > b:
#         y = 0
#         return y
#     else:
#         y = 1
#         return y
#
#
# print(task())


"""15"""

# import math
#
# x = int(input('===>'))
#
#
# def task(x, pop):
#
#     pop1 = pop(x)
#
#     print(pop1)
#
#
# def task1(x):
#
#
#     if -2 <= x < 0:
#         return f'y = {math.tan(x) / (x - 3)}'
#     elif 0 <= x <= 2:
#         return f'y = {math.log(10, x) * math.sin(x)}'
#
#
# task(x, task1)


"""16"""

# import math
#
# y = int(input('===> '))
#
#
# def task(x, pop):
#     pop1 = pop(x)
#
#     print(pop1)
#
#
# def task1(x):
#     if 1 <= x < 2:
#         return f'y = {(1 / math.atan(x)) + (math.pi / 3)}'
#     elif 2 <= x <= 3:
#         return f'y = {(1 - (5 * x)) * math.sqrt(math.sin(x))}'
#
#
# task(y, task1)


"""17"""

# import math
#
# y = int(input('==> '))
#
#
# def task(x, pop):
#     a = (math.sin(0.1 * x) / (x - 2)) + math.sqrt(x)
#     b = (math.cos(x)) - x ** 3.5
#     pop1 = pop(x)
#     print(pop1)
#
#
# def task1(x):
#     a = (math.sin(0.1 * x) / (x - 2)) + math.sqrt(x)
#     b = (math.cos(x)) - x ** 3.5
#
#     if 10 <= x < 20:
#         return f'y = {a}'
#     if 20 <= x <= 30:
#         return f'y = {b}'
#
#
# task(y, task1)


"""18"""

# import math
# y = int(input('==> '))
#
#
# def task(x, pop):
#
#     pop1 = pop(x)
#     print(pop1)
#
#
# def task1(x):
#     a = math.log(10, abs(1 + (2 * x)))
#     b = math.exp(1 / math.atan(x))
#     bb = math.sin(x) / (1 + (1 / x))
#     if -5 <= x < 0:
#         return f'y = {a}'
#     elif 0 <= x <= 5:
#         return f'y = {b * bb}'
#
#
# task(y, task1)


"""19"""
# import  math
# y = int(input('==> '))
#
#
# def task(x, pop):
#     pop1 = pop(x)
#     print(pop1)
#
#
# def task1(x):
#     a = math.tan(x) / (1 + math.tan(2 * x))
#     b = math.log(10, x) ** 2.5
#
#     if -2 <= x <= 1:
#         return f'y = {a}'
#     elif 1 < x <= 4:
#         return f'y = {b}'
#
#
# task(y, task1)


"""20"""

# import math
#
# y = float(input('==> '))
#
#
# def task(x, pop):
#     pop1 = pop(x)
#     print(pop1)
#
#
# def task1(x):
#     if 0.1 <= x <= 1:
#         return f'y = {math.sin(x) / (x + math.cos(x))}'
#     elif 1 < x <= 1.9:
#         return f'y = {(x**3) + (2 * (x ** 2)) + (3 * x) + 4}'
#
#
# task(y, task1)


"""21"""
# import math
# y = float(input('==> '))
#
#
# def task(x, pop):
#
#     pop1 = pop(x)
#     print(pop1)
#
#
# def task1(x):
#     a = 1 - (x / ((1 + x) ** 1/5))
#     b = 100 * (math.log(10, x) + math.sin(x))
#     bb = ((2 * x) - 3) ** 2
#
#     if 1.5 <= x <= 2.5:
#         return f'y = {a}'
#     if 2.5 < x <= 3.5:
#         return f'y = {b / bb}'
#
#
# task(y, task1)


"""22"""
# import math
#
# y = float(input('==> '))
#
#
# def task(x, pop):
#     pop1 = pop(x)
#     print(pop1)
#
#
# def task1(x):
#     a = math.log(10, (3 + x) * (x ** 2))
#     aa = math.cos(math.pi * x)
#     b = x ** 5 - math.tan(x)
#     bb = math.log(10, x)
#     if 0.2 <= x <= 0.4:
#         return f'y = {a / aa}'
#     elif 0.4 < x <= 0.6:
#         return f'y = {b / bb}'
#
#
# task(y, task1)


"""23"""

# import math
# y = float(input('==> '))
#
#
# def task(x, pop):
#     pop1 = pop(x)
#     print(pop1)
#
#
# def task1(x):
#     a = (5 * x) - math.exp(3 * x) + math.cos(x)
#     aa = 1 + math.log(10, x)
#     b = (1 + x) ** 6
#     if 0.3 <= x <= 0.4:
#         return f'y = {100 * (a / aa)}'
#     elif 0.4 < x <= 0.6:
#         return f'y = {b}'
#
#
# task(y, task1)


# """24"""
# import math
# y = float(input('==> '))
#
#
# def task(x, pop):
#     pop1 = pop(x)
#     print(pop1)
#
#
# def task1(x):
#     a = ((1 + x) ** (1 / 6))
#     b = ((2 / 3) - (3 ** (2 * x))) * math.cos(x)
#     bb = math.sqrt(x + 2)
#     if 2 <= x <= 3:
#         return f'y = {a}'
#     elif 3 < x <= 4:
#         return f'y = {b / bb}'
#
#
# task(y, task1)


"""1"""


# def task1():
#     n = int(input('n ==> '))
#     for i in range(100, 201):
#         if i % n == 0:
#             print(i)
#
#
# task1()


"""2"""


# def task2():
#     k = 1
#     n = int(input('n ==> '))
#     for i in range(10, 51):
#         if i % n == 0:
#             k *= i
#             print(k)
#
#
# task2()

"""3"""


# def task3():
#     k = 0
#     n = int(input('n ==> '))
#     for i in range(200, 501):
#         if i % n == 2:
#             k += i
#             print(k)
#
#
# task3()


"""4"""


# def task4():
#     k = 1
#     n = int(input('n ==> '))
#     for i in range(-20, 20):
#         if i % n == 3:
#             k *= i
#             print(k)
#
#
# task4()


"""5"""


# def task5():
#     k = 0
#     for i in range(10, 100):
#         if i % 2 == 0:
#             k += i
#     print(k)
#
#
# task5()


"""6"""


# def task6():
#     k = 1
#     for i in range(20, 71):
#         if i % 2 == 0 and i % 4 == 0:
#             k *= i
#     print(k)
#
#
# task6()


"""7"""


# def task7():
#     k = 0
#     n = int(input('n ==> '))
#     for i in range(1, 100):
#         if i % n == 0:
#             k += i
#     print(k)
#
#
# task7()


"""8"""


# def task8():
#     k = 1
#     n = int(input('n ==> '))
#     for i in range(1, 100):
#         if i % n == 0:
#             k *= i
#     print(k)
#
#
# task8()


"""9"""


# def task9():
#     k = 0
#     n = int(input('n ==> '))
#     for i in range(1000, 2001):
#         if i % n == 2:
#             k += i
#     print(k)
#
#
# task9()


"""10"""


# def task10():
#     k = 1
#     n = int(input('n ==> '))
#     for i in range(2, 103):
#         if i % n == 3:
#             k *= i
#     print(k)
#
#
# task10()


"""11"""


# def task11():
#     k = 0
#     for i in range(100, 1000):
#         if i % 3 == 0:
#             k += i
#     print(k)
#
#
# task11()


"""12"""


# def task12():
#     k = 1
#     for i in range(1000, 10000):
#         if i % 3 == 0 and i % 5 == 0:
#             k *= i
#             print(k)
#
#
# task12()