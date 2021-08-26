#check if 2 strings are anagrams or not
#Strings are said to be anagrams only if all the characters present in 1st string are also present in 2nd string and no single characters should be more or less
str1=input("enter string:")
str2=input("enter string:")
flag=1
if len(str1)==len(str2):
    for i in str1:
        if i in str2:
            pass
        else:
            print("not anagram")
            flag=0
else:
    flag=0
    print("not anagram")           
if flag==1:
    print("anagram")