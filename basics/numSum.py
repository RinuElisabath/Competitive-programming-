#sum of numbers in a string

str1=input("enter string")
sum=0
for chara in str1:
    if chara.isdigit():
        sum=sum+int(chara)

print(sum)