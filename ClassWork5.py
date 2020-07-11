print ('====ClassWork #1====')
integer = [int(input('Number of numbers: ')) for i in range(int(input('Enter integer: ')))]
print (f"Min_number: {min(integer)}, Max_number: {max(integer)}")


print ('====ClassWork #2====')
num2 = []
num3 = []
num23 =[]
for i in range (1,11):
    if i%2==0:
        num2.append(i)
    elif i%3==0:
        num3.append(i)
    else:
        num23.append(i)
print (f'Numbers are divisible by 2:{num2}\nnumbers are divisible by 3:{num3}\nnumbers are not divisible by 2 and 3:{num23}')


print ('====ClassWork #3====')
num = int(input('input number: '))
a = 0
b = 1
for count in range(num):
    a += 1
    b *= a
print (num, '! -', b,)


print ('====ClassWork #4====')
login = input ('Enter Login:')
while login == 'First':
    print ('Greeting! Login is correct')
    break
else:
    print ('Login is not correct')


print ('====ClassWork #5====')
num = int(input('Enter number: '))
while num !=0:
    if num <0:
        print ('This is a negative number')
        break
    else:
        num = int(input('Enter number: '))

