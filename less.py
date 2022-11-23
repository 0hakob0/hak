# խնդիր 136   split- ի մեջ ոնց մի քանի հրաման տամ


# x=input('===> ')
# dict = {
#     'anun' : 'Aram',
#     'mail' : 'a@maill.ru',
#     'tariq': 33,
#     'taretiv': 1989
# }
# z =x.split()

# for i in z:
#     print(dict[i])






# Խնդիր 138


# x =(input('===> ')).upper()
# y = ''
# dict = {
#     '.' : 1, 
#     ',' : 11,
#     '?' : 111,
#     '!' : 1111,
#     ':' : 11111,
#     'A' : 2,
#     'B' : 22,
#     'C' : 222,
#     'D' : 3,
#     'E' : 33,
#     'F' : 333,
#     'G' : 4,
#     'H' : 44,
#     'I' : 444,
#     'J' : 5,
#     'K' : 55,
#     'L' : 555,
#     'M' : 6,
#     'N' : 66,
#     'O' : 666,
#     'P' : 7,
#     'Q' : 77,
#     'R' : 777,
#     'S' : 7777,
#     'T' : 8,
#     'U' : 88,
#     'V' : 888,
#     'W' : 9,
#     'X' : 99,
#     'y' : 999,
#     'z' : 9999,
#     ' ' : 0
# }
# for i in x:
#     z = (dict[i])
#     y += str(z)
# print(y)









# Խնդիր 139
# morze = {
#     'a': '.- ', 
#     'b': '-... ', 
#     'c': '-.-. ', 
#     'd': '-.. ', 
#     'e': '. ', 
#     'f': '..-. ',
#     'g': '--. ', 
#     'h': '.... ', 
#     'i': '.. ', 
#     'j': '.--- ', 
#     'k': '-.- ', 
#     'l': '.-.. ', 
#     'm': '-- ', 
#     'n': '-. ', 
#     'o': '--- ', 
#     'p': '.--. ', 
#     'q': '--.- ', 
#     'r': '.-. ', 
#     's': '... ', 
#     't': '- ', 
#     'u': '..- ', 
#     'v': '...- ', 
#     'w': '.-- ', 
#     'x': '-..- ', 
#     'y': '-.-- ', 
#     'z': '--.. ',
#     ' ' : '',
#     '!' : '',
#     ',' : '',
#     '0' : '---- ',
#     '1' : '.---- ',
#     '2' : '..--- ',
#     '3' : '...-- ',
#     '4' : '....- ',
#     '5' : '..... ',
#     '6' : '-.... ',
#     '7' : '--... ',
#     '8' : '---.. ',
#     '9' : '----. '
#     }


# x = input().lower()
# list = []
# z = ''
# for i in x:
#     y = morze.get(i)
#     if y == '':
#         continue
#     else:
#         z += str(y)
# print(''.join(z))


# Խնդիր 142

# x = input('===> ')
# list = []
# m = -1
# for i in x:
#    list.append(i)	
# while m < len(list)-1:
#     m += 1
#     if list.count(list[m]) > 1:
#        list.pop(m)
#        m -= 1
#     else:
#        print(len(list))

# Խնդիր 143
# n = 0
# list = []
# while n < 2:
#     n +=1
#     x =str(input('===> '))
#     list.append(x)
# if list[0] == list[0] [::-1]:
#     print ('aaa')
# if list[1] == list[1] [::-1]:
#     print ('bbb')


#----------------------------------------------------------------------------------------------------------------------


# '''Խնդիր 63'''


# a = 0
# b = 0

# while True:
#     x = int (input('Գրեք թիվը ===> '))
#     if x == 0:
#         break

#     else:
#         a += x
#         b += 1
#         z = (a/b)
#         print(z)


# '''Խնդիր 64'''

# a=0
# g=-0.5
# while True:
#     if a == 5:
#         break
#     else:
#         a += 1
#         g +=5
#         print (f'հին գին = {g}   նոր գին = {g-(g*60/100):.2f}')
       

# '''Խնդիր 69'''


# a = 0
# b = 0
# c = 0
# d = 0


# while True:
#     x =input('Գրեք տարիքը ===> ')
#     if x=='':
#      break
#     if int(x) >= 2:
#         a += 1
#     if int(x)>=3 and int(x)<=12:
#         b += 1
#     if int(x)>=13 and int(x)<=65:    
#        c += 1
#     if int(x) > 65:
#          d += 1

#     print (f'               Մինչև 2 տարեկան {a*0}$\n               3-12 տարեկան {b*14}$\n               13-65 տարեկան {c*23}$\n               65+ տարեկան {d*18}$')




# '''Խնդիր 98'''
# list = []
# x = int(input('===> '))
# n = 0
# while x>n:
#     n +=1
#     if x % n == 0:
#         list.append(n)
#         print(list)
# if len(list) == 2:
#     print('True')
# else:
#     print('False')



# '''Խնդիր 99'''
# list = []
# x = int(input('===> '))
# n = 0

# while 'a':
#     x += 1
#     break

# while x>n:
#     n +=1
#     if x % n == 0:
#         list.append(n)
#         # print(list)
#         if len(list)>2:
#             n = 0
#             list =[]
#             x +=1
#             continue
# if len(list) == 2:
#     print(list[1])

# import random
# set = {}
# z = ''
# list = []
# while len(set) < 10:
#     x = random.randint (33, 127)

# mylist = [1, 1, 2, 3, 7, 4, 5, 1, 2]
# print(list(set(mylist)))




# '''Խնդիր 100'''

# import random

# z = ''
# list = []
# while len(set(list)) < 10:
#     x = random.randint (33, 126)
#     list.append(chr(x).lower())
# print(set(list))



# '''Խնդիր 101'''

# import random
# list = []
# list1 = []
# list2 = []
# s3 = ''
# s4 = ''
# n = -1

# while n < 2:
#     n+=1
    
#     x = random.randint (48, 57)
#     y = random.randint (65, 90)
#     list.append(chr(y))
#     list1.append(chr(x))
#     list2 = list+list1
# for i in list2:
#     s3 += i

# if n == 2:
#     list.clear()
#     list1.clear()
#     list2.clear()
#     n = 0
#     while n < 4:
#         n+=1
#         x = random.randint (48, 57)
#         y = random.randint (65, 90)
#         list.append(chr(y))
#         list1.append(chr(x))
#         list2 = list1+list[:3]
#     for i in list2:
#         s4 += i
# print(s3,s4)


# '''Խնդիր 146'''

# '''Խնդիր 77'''
bb = 0
ii = 0
nn = 0
gg = 0
oo = 0
listb = []
listi = []
listn =[]
listg =[]
listo =[]

import random

# print (f' {" ":>0}', end='' )

# for i in range(1, 11):
#     print(f'{i:>3}', end='')
#     # print('\n')




# while bb<15:
#     bb += 1
#     bbb = random.randint(1, 15)
#     listb.append(bbb)
# for b in listb:
#     print(f'{b :>7}', end ='')

# while ii < 15:
#     ii += 1
#     iii = random.randint(16, 30)
#     listi.append(iii)
# print (f' {"  ":>7}', end='' )
# print('\n')
# for i in listi:
#     print(f'{i :>7}', end ='')

# while nn < 15:
#     nn += 1
#     nnn = random.randint(31, 45)
#     listn.append(nnn)
# print (f' {"  ":>4}', end='' )
# print('\n')
# for n in listn:
#     print(f'{n :>7}', end ='')

# while gg < 15:
#     gg += 1
#     ggg = random.randint(46, 60)
#     listg.append(ggg)
# print (f' {"  ":>4}', end='' )
# print('\n')
# for g in listg:
#     print(f'{g :>7}', end ='')

# while oo < 15:
#     oo += 1
#     ooo = random.randint(61, 75)
#     listo.append(ooo)
# print (f' {"  ":>4}', end='' )
# print('\n')
# for o in listo:
#     print(f'{o :>7}', end ='')




