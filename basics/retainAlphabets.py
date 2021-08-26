#remove all chara from string except alphabets

str1=input("enter string:")
str2=str()
for chara in str1:
    if chara.isalpha():
        str2=str2+chara
print(str2)       



'''
str1=input("enter string:")
str2=str()
for chara in str1:
    if (chara>='A' and chara<='Z') or (chara>='a' and chara<='z'):
        str2=str2+chara
print(str2)
'''