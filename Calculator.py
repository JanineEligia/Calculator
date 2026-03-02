num1 = int(input("Enter the First Number: "))
opt = input("Enter an Operation (+, -, *, /): ")
num2 = int(input("Enter the Second Number: "))

if opt == '+':
    print (num1 + num2)

elif opt == '-':
    print (num1 - num2)

elif opt == '*':
    print (num1 * num2)

elif opt == '/':

    try:
        print (num1 / num2)

    except ZeroDivisionError:
        print("Ekkkk! Dividing by zero is not allowed.")

else:
    print("Synthax Error")