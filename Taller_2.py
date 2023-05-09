excercise = int(input('Enter the number that you want see (17-29): '))
if excercise == 17:

    # numero negativo y positivo
    number = int(input('enter the number: '))
    if number > 0:
        print(f'the number {number} is positive')
    elif number < 0:
        print('The number ' + str(number) + ' is negative')

    else:
        print('the number ' + str(number) + ' is neutral')

elif excercise == 18:
    # menor y mayor
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter the other number: '))
    if num1 > num2:
        print(str(num1) + ' is the largest and ' + str(num2) + ' is the lowest')
    elif num1 < num2:
        print(str(num2) + ' is the largest and ' + str(num1) + ' is the lowest')
    else:
        print('The numbers are the same')

elif excercise == 19:
    # menor y mayor de 3 numeros
    Num1 = int(input('Enter the first number: '))
    Num2 = int(input('Enter the second number: '))
    Num3 = int(input('Enter the third number: '))
    if Num1 > Num2 > Num3:
        print(str(Num1) + ' is the major, ' + str(Num2) + ' is the middle and ' + str(Num3) + ' is the minor')
    elif Num1 > Num3 > Num2:
        print(str(Num1) + ' is the major, ' + str(Num3) + ' is the middle and ' + str(Num2) + ' is the minor')
    elif Num2 > Num1 > Num3:
        print(str(Num2) + ' is the major, ' + str(Num1) + ' is the middle and ' + str(Num3) + ' is the minor')
    elif Num2 > Num3 > Num1:
        print(str(Num2) + ' is the major, ' + str(Num3) + ' is the middle and ' + str(Num1) + ' is the minor')
    elif Num3 > Num2 > Num1:
        print(str(Num3) + ' is the major, ' + str(Num2) + ' is the middle and ' + str(Num1) + ' is the minor')
    elif Num3 > Num1 > Num2:
        print(str(Num3) + ' is the major, ' + str(Num1) + ' is the middle and ' + str(Num2) + ' is the minor')
    else:
        print('The numbers are the same')

elif excercise == 20:
    # calcular el sueldo de los empleados
    name = input('Welcome, enter the employees name: ')
    hours_1 = int(input('Enter hours worked: '))
    hours_2 = int(input('Enter overtime worked: '))
    pay = (hours_1 * 4) + (hours_2 * 8)
    print('The pay of ' + str(name) + ' is $' + str(pay))

elif excercise == 21:
    # dos numeros  si los voy a sumar
    d1 = int(input('Enter the first number: '))
    d2 = int(input('Enter the second number: '))
    if d1 < d2:
        result = d1 + d2
        print('the result is: ' + str(result))
    else:
        result2 = d1 - d2
        print('the result is: ' + str(result2))

elif excercise == 22:
    # divicion entre 0
    c1 = int(input('Enter the dividend: '))
    c2 = int(input('Enter the divisor: '))
    if c2 == 0:
        print('this division cant make')
    else:
        res = c1 // c2
        print('the result is: ' + str(res))

elif excercise == 23:
    # dia de la semana
    day_week = int(input('Enter a number (1-7): '))
    if day_week == 1:
        print('the number 1 is MONDAY')
    elif day_week == 2:
        print('the number 2 is TUESDAY')
    elif day_week == 3:
        print('the number 3 is WEDNESDAY')
    elif day_week == 4:
        print('teh number 4 is THURSDAY')
    elif day_week == 5:
        print('teh number 4 is FRIDAY')
    elif day_week == 6:
        print('teh number 4 is SATURDAY')
    elif day_week == 7:
        print('teh number 4 is SUNDAY')
    else:
        print('this number is not available')

elif excercise == 24:
    # logitudes de triangulo
    lado_1 = int(input('Enter the first side of the triangle: '))
    lado_2 = int(input('Enter the second side of the triangle: '))
    lado_3 = int(input('Enter the third side of the triangle: '))
    if lado_1 == lado_2 == lado_3:
        print('this triangle is equilateral')
    elif lado_1 == lado_2 != lado_3:
        print('this triangle is isosceles')
    elif lado_1 != lado_2 != lado_3:
        print('this triangle is scalene')
    else:
        print('this triangle is isosceles')

if excercise == 25:
    # sumar per si es negativo multiplicar
    num_1 = int(input('Enter the first number: '))
    num_2 = int(input('Enter the second number: '))
    if num_1 < 0 or num_2 < 0:
        res_1 = num_1 + num_2
        print('the result is: ' + str(res_1))
    else:
        res_2 = num_1 * num_2
        print('the result is: ' + str(res_2))

if excercise == 26:
    # signo zodiacal
    day = int(input('Enter your day of birth: '))
    mount = int(input('Enter your mount of birth: '))
    if (mount==3 and day>=21) or (mount==4 and day<=20):
        print('Aries')
    elif (mount==4 and day>=21) or (mount==5 and day<=20):
        print('Tauro')
    elif (mount == 5 and day >= 21) or (mount == 6 and day <= 20):
        print('Geminis')
    elif (mount==6 and day>=21) or (mount==7 and day<=22):
        print('Cancer')
    elif (mount==7 and day>=23) or (mount==8 and day<=23):
        print('Leo')
    elif (mount==8 and day>=24) or (mount==9 and day<=22):
        print('Virgo')
    elif (mount==9 and day>=21) or (mount==10 and day<=20):
        print('Libra')
    elif (mount==10 and day>=24) or (mount==11 and day<=22):
        print('Escorpio')
    elif (mount==11 and day>=21) or (mount==12 and day<=22):
        print('Sagitario')
    elif (mount==12 and day>=22) or (mount==1 and day<=20):
        print('Capricornio')
    elif (mount==1 and day>=21) or (mount==2 and day<=19):
        print('Acuario')
    elif (mount==2 and day>=20) or (mount==3 and day<=20):
        print('Piscis')
    else:
        print('this number is not available ')

if excercise == 27:
    #cuadrado o rectangulo
    base = int(input('Enter the base of the quadrilateral: '))
    height = int(input('enter the height of the quadrilateral: '))
    area= base*height
    perimeter = base + height + base +height
    if base != height:
        print('its a rectangle')
    else:
        print('its a square')
    print('the area is: '+ str(area))
    print('the perimeter is: '+ str(perimeter))

if excercise == 28:
    #descuentos en tienda
    purchase=float(input('Enter the purchase price: '))
    if purchase<100:
        price_off=purchase*0.05
        price_total=purchase-price_off
        print('the total price is: $' + str(price_total))
    elif purchase>200:
        price_off = purchase * 0.15
        price_total = purchase - price_off
        print('the total price is: $' + str(price_total))
    else:
        price_off = purchase * 0.10
        price_total = purchase - price_off
        print('the total price is: $' + str(price_total))
if excercise==29:
    #saber si el año es bisiesto
    year=int(input('Enter the year that you want see: '))
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print('this year is a leap year')
    else:
        print('this year is not a leap year')
else:
    print('this exerciser is not available')
