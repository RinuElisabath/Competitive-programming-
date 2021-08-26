#count number of vowels in string

string1=input("enter string:")
string2="aeiou"
string3="AEIOU"
count=0
for chara in string1:
    if chara in string2 or chara in string3:
        count+=1
print(count)        
