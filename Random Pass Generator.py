import random
str=""
n=int(input("Enter password length: "))

l=input("Do you want to add lowercase characters (Yes/No): ")
if l=="Yes" or l=="yes" or l=="YES":
    str+="abcdefghijklmnopqrstuvwxyz"

u=input("Do you want to add uppercase characters (Yes/No): ")
if u=="Yes" or u=="yes" or u=="YES":
    str+="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

nu=input("Do you want to add numbers (Yes/No): ")
if nu=="Yes" or nu=="yes" or nu=="YES":
    str+="1234567890"

sy=input("Do you want to add Symbols(Yes/No): ")
if sy=="yes" or sy=="YES" or sy=="Yes":
    str+="!@#$%&*+-^/"

password=""
for x in range(n):
    a=random.choice(str)
    password+=a

print(f"Your Password is {password}")


