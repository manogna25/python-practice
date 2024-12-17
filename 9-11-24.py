#strong number
#the sum of factorials of digits are equal to the original number is called strong number
'''num=int(input("Enter a number: "))
sum_of_factorials=0
temp=num
while num>0:
    digit=num%10
    factorial=1
    for i in range(1,digit+1):
        factorial=factorial*i
    sum_of_factorials+=factorial
    num=num//10
if sum_of_factorials==temp:
    print("Strong number")
else:
    print("not a strong number")
'''
#Armstrong number
#sum of the powers of the digit = original num
'''n=int(input("enter a num: "))
length=len(str(n))
sum_of_digits=0
temp=n
while(n>0):
    r=n%10
    sum_of_digits+=pow(r,length)
    n=n//10
if(sum_of_digits==temp):
    print("Armstrong")
else:
    print("not an ArmStrong")
'''
