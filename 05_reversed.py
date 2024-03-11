# so'zni chappa qilish uchun--\/--
def comma_reversed(str):
    s = ""
    for i in range(len(str)):
        s+= str[len(str)-1-i]
    return s
comma =True
while comma:
    pie = input('so\'z kiriting: ')
    if pie == 'stop':
        comma = False
    else:
        print(comma_reversed(pie),"\nchiqarish uchun 'stop' yozing!")