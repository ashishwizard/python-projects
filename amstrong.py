# xyz=x^n+y^n+z^n where n= no. of digits, ex- 153=1^3+5^3+3^3=153 so, an amstrong no.
num = int(input("enter a no.\n"))
sum = 0
order = len(str(num))
# as num=num//10 so eventually its value stored will be zero so to compare sum=num we need num original value so we need to make a copy of it.
copy_num = num
while(num > 0):
    digit = num % 10  # it will give one one digits ex 153- 1,5,3 #remainder
    sum += digit**order
    num = num//10  # it will reduce it to 0 for ending program #quotient 153//10=15,15//10=1,1//10=0
if (sum == copy_num):
    print("It is an amstrong number")
else:
    print('not an amstrong number')
