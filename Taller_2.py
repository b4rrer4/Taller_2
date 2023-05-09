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
    