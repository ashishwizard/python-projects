#printing stars in small to big rows
n= int (input("enter no. of rows "))
for i in range (n):
    for j in range (i+1):
        print("*",end=" ")
    print()

#printing same in reverse order
n= int (input("enter no. of rows "))
for i in range (n):
    for j in range (n-i):
        print("*",end=" ")
    print()

#printing abcd in star pattern
n= int (input("enter no. of rows "))
num=65 #ascii value of A
for i in range (n):
    for j in range (i+1):
        ch=chr(num)        #ch to change ascii to its character value
        print(ch,end=" ") 
        num=num+1
    print("")
