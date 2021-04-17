n1 = int(input('first number '))
n2 = int(input('second number '))
if (n1 % 2 == 0) and (n2 % 2 == 0):
    print('both are even numbers')
elif (n1 % 2 == 0) and (n2 % 2 != 0):
    print('num 1 is even num 2 is odd')
elif (n1 % 2 != 0) and (n2 % 2 == 0):
    print('num 1 is odd num 2 is even')
else:
    print('both are odd numbers')
