# farangeytdan tempiratura o'tqazish uchun--\/--
def comma_converts(f):
    T = f*9/5+32
    print('Tempuratura = ', T)

comma= True
while comma:
    pie = int(input('Farangeyt: '))
    if pie == 'stop':
        comma =False
    else:
        print(comma_converts(pie))

