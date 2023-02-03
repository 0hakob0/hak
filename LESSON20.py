# def task2():
#     k = 1
#     n = int(input('n ==> '))
#     for i in range(10, 51):
#         if i % n == 0:
#             k *= i
#             print(k)


# task2()

#
# def task(num):
#     if(num>0):
#        result=num+task(num-1)
#        print(result)
#     else:
#         result=0
#     return result
#
# task(20)
#
#
# def main():
#     task()
#     task1()
# main()
#
# n = 5


# def outer():
#     n = 5
#
#     def inner():
#         nonlocal n
#         n += 1
#         print(n)
#
#     return inner
#
#
# fn = outer()
#
#
# fn()
# fn()
# fn()


# n = int(input('==> '))
# count = 0
# while n != 0:
#     count += 1
#     x = n % 10
#     y = n // 10
#     n = y
#     print(x)

"""1"""


# def task1():
#     n = int(input('==> '))
#
#     def task11():
#         nonlocal n
#         while n != 0:
#             x = n % 10
#             y = n // 10
#             n = y
#             print(x)
#     return task11
#
#
# fn = task1()
# fn()


"""2"""


# def task1():
#     n = int(input('==> '))
#     z = 0
#
#     def task11():
#         nonlocal n
#         nonlocal z
#         while n != 0:
#             x = n % 10
#             y = n // 10
#             n = y
#             z += 1
#         print(z)
#     return task11
#
#
# fn = task1()
# fn()


"""3"""


# def task1():
#     n = int(input('==> '))
#     z = 0
#
#     def task11():
#         nonlocal n
#         nonlocal z
#         while n != 0:
#             x = n % 10
#             y = n // 10
#             n = y
#             z += x
#         print(z)
#     return task11
#
#
# fn = task1()
# fn()


"""4"""


# def task1():
#     n = int(input('==> '))
#     z = 1
#     def task11():
#         nonlocal n
#         nonlocal z
#         while n != 0:
#             x = n % 10
#             y = n // 10
#             n = y
#             z *= x
#         print(z)
#     return task11
#
#
# fn = task1()
#
# fn()


"""7"""


# def task1():
#     n = int(input('==> '))
#
#     def task11():
#         nonlocal n
#         while n != 0:
#             x = n % 10
#             y = n // 10
#             n = y
#             print(x, end= '')
#     return task11
#
#
# fn = task1()
# fn()


"""8"""


# def task1():
#     n = int(input('==> '))
#
#     def task11():
#         nonlocal n
#         while n != 0:
#             x = n % 10
#             y = n // 10
#             n = y
#             if x == 3:
#                 print(True)
#                 break
#         else:
#             print(False)
#
#     return task11
#
#
# fn = task1()
# fn()


"""10"""


# def task1():
#     n = int(input('==> '))
#
#     def task11():
#         nonlocal n
#         while n != 0:
#             x = n % 10
#             y = n // 10
#             n = y
#             if x % 2 == 0:
#                 print(True)
#                 break
#         else:
#             print(False)
#
#     return task11
#
#
# fn = task1()
# fn()


"""11"""


# def task1():
#     n = int(input('==> '))
#     z = 0
#     l = 0
#
#     def task11():
#         nonlocal n
#         nonlocal z
#         nonlocal l
#         while n != 0:
#             x = n % 10
#             y = n // 10
#             n = y
#             if x % 2 != 0:
#                 z += x
#             elif x % 2 == 0:
#                 l += x
#             if z == l:
#                 print(True)
#                 break
#         else:
#             print(False)
#
#     return task11
#
#
# fn = task1()
# fn()


"""12"""


# def task1():
#     n = int(input('==> '))
#     z = 0
#     l = 0
#
#     def task11():
#         nonlocal n
#         nonlocal z
#         nonlocal l
#         while n != 0:
#             x = n % 10
#             y = n // 10
#             n = y
#             if x % 2 != 0:
#                 z += 1
#             elif x % 2 == 0:
#                 l += 1
#         if z == l:
#             print(True)
#
#         else:
#             print(False)
#
#     return task11
#
#
# fn = task1()
# fn()
#

"""6"""


# def task1():
#     n = int(input('==> '))
#     count = 0
#     k = 0
#
#     def task11():
#         nonlocal n
#         nonlocal count
#         nonlocal k
#         while n != 0:
#             x = n % 10
#             y = n // 10
#             n = y
#             k += x * (10 ** count)
#             count += 1
#         print(k)
#     return task11
#
#
# fn = task1()
# fn()
