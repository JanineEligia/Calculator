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
    print (num1 / num2)

else:
    print("Synthax Error.")