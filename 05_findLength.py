# so'zlarni sanash uchun--\/--
def comma_findLength(s):
    count =0
    for x in s:
        count+=1
    return count

ing = True
while ing:
    pie =input( 'Word: ')
    if pie == 'stop':
        ing =False
    else:
        print(comma_findLength(pie))