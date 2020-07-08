print ('====ClassWork #1====')
num1 = int(input('input number #1: '))
num2 = int(input('input number #2: '))
if num1 > num2:
    print (num1,'more than', num2)
elif num1 == num2:
    print (num1,'is equal', num2)
else:
    num1 < num2
    print (num2,'more than', num1)

print ('====ClassWork #2====')
num = int(input('input number: '))
if num%2 == 0:
    print (num,'is even number')
else:
    print (num,'is odd number')


print ('====ClassWork #3====')
num = int(input('input number: '))
a = 0
b = 1
for count in range(num):
    a += 1
    b *= a
print (num, '! -', b,)