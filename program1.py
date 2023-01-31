s=input("enter any string")
j=-1
flag=0
for i in s:
    if i!=s[j]:
                flag=1
                break
j=j-1
if flag==1:
    print(s,"this string is  palindrome")
else:
    print(s,"this string is not palindrome")

    
                

        