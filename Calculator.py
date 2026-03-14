num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operation = input("Enter operation ('+, -, *, /'): ")

if operation == '+':
    print("Result :", num1+num2)
elif operation == '-':
    print("Result :", num1-num2)
elif operation == '*':
    print("Result :", num1*num2)
elif operation == '/':
    if num2 !=0:
        print("Result :", num1/num2)
    else:
        print('Devided by zero not allowed')
else:
    print("Invalid Operation")
