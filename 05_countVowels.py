# so'zlarni unlilarini topib sanash
def comma_countVowels(word):
    count= 0
    str= set('a,u,i,o,e')
    for x in word:
        if x in str:
            count += 1
    return count
comma = True
while comma:
    pie = input("so'zni kiriting: ")
    if pie == 'stop':
        comma = False
    else:
        print(comma_countVowels(pie))