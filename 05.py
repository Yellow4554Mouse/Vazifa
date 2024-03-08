# ABCDCBA<-->ABCDCBA bundan ko'rinshda bo'ladi
# ABDA<-->ADBA bu ko'rinish xato
def comma_checkPolindrome(str):
    ln= int(len(str)/2)
    for i in range(ln):
        if str[i] != str[len(str)-i-1]:
            return False
        return True
print(comma_checkPolindrome(input('so\'z yozing: ')))

# def comma_countVowels(str):
#     return int

# so'zlarni sanash uchun--\/--
def comma_findLength(s):
    count =0
    for x in s:
        count+=1
    return count
pie =input( 'Word: ')
print(comma_findLength(pie))

# so'zni chappa qilish uchun--\/--
def comma_reversed(str):
    s = ""
    for i in range(len(str)):
        s+= str[len(str)-1-i]
    return s
print(comma_reversed(input('so\'z kiriting: ')))

# farangeytdan tempiratura o'tqazish uchun--\/--
def comma_converts(f):
    T = f*9/5+32
    print('T= ', T)
a = int(input('F: '))
comma_converts(a)