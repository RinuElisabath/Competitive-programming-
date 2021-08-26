#remove spaces from a string

str1=input("enter string:")
str2=str()
for chara in str1:
    if chara!=" ":
        str2=str2+chara
print(str2)        
