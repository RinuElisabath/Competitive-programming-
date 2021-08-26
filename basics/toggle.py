#toggle each character in a string

string1=input("enter string:")
string2=str()
for i in string1:
    if i.islower():
        i=i.upper()
        string2=string2+i
    else:
        i=i.lower()
        string2=string2+i
print(string2)            

