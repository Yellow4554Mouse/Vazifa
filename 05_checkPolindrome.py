# ABCDCBA<-->ABCDCBA bundan ko'rinshda bo'ladi
# ABDA<-->ADBA bu ko'rinish xato
def comma_checkPolindrome(str):
    ln= int(len(str)/2)
    for i in range(ln):
        if str[i] != str[len(str)-i-1]:
            return False
        return True
comma= True
while   comma:
    pie = input('so\'z yozing: ')
    if pie == 'stop':
        comma = False
    else:  
        print(comma_checkPolindrome(pie))