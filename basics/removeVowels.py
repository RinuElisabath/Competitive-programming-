#remove vowels from string
string1=input("enter string:")
string2="aeiou"
string3="AEIOU"
newstring=str()
for chara in string1:
    if (chara not in string2) and (chara not in string3):
        newstring=newstring+chara
print(newstring)     
