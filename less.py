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


# խնդիր 139


morze = {
    'a': '•—', 
    'b': '—•••', 
    'c': '—•—•', 
    'd': '—••', 
    'e': '•', 
    'f': '••—•', 
    'g': '——•', 
    'h': '••••', 
    'i': '••', 
    'j': '•———', 
    'k': '—•—', 
    'l': '•—••', 
    'm': '——', 
    'n': '—•', 
    'o': '———', 
    'p': '•——•', 
    'q': '——•—', 
    'r': '•—•', 
    's': '•••', 
    't': '—', 
    'u': '••—', 
    'v': '•••—', 
    'w': '•——', 
    'x': '—••—', 
    'y': '—•——', 
    'z': '——••'
    }

a = input()
a = a.lower()
g = []
j=0
 
for i in a:
    k = morze.get(i,'\t')
    if k != '\t':
        j = k+" "
        g.append(j)
    else:
        j ='\t'
        g.append(j)
print("".join(g))