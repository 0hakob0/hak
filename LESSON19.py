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

import math

x= int(input('===>'))


def task(x, pop):
    pop1 = pop(x)

    print(pop1)

def task1(x):


    if -2 <= x < 0:
        return f'y = {math.tan(x) / (x - 3)}'
    elif 0 <= x <= 2:
        return f'y = {math.log(10, x) * math.sin(x)}'


task(x, task1)


