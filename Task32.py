num = int(input('Enter a four-digit natural number:'))
if num <=999:
    print ('Number is not a four-digit natural number')
elif num >9999:
    print ('Number is not a four-digit natural number')
else:
    num1 = num//1000 
    num2 = num//100-num1*10
    num3 = num//10-num1*100-num2*10
    num4 = num%10
    mult = num1*num2*num3*num4
    print (mult)
    num5 = str(num)
    print (num5[-1:-5:-1])