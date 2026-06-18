# 1

weight = float(input("Enter weight(KG): "))
height = float(input("Enter height(CM): "))

bmi = weight / (height * height)

print(bmi)

if bmi < 19:
    print("underweight")

elif bmi >= 19 and bmi <= 25:
    print("normalweight")

else:
    print("overweight")

# 2

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operator = input("Enter operator: ")

if operator == "+":
    print(num1 + num2)

elif operator == "-":
    print(num1 - num2)

elif operator == "*":
    print(num1 * num2)

elif operator == "/":
    print(num1 / num2)

else:
    print("Wrong operator")

    # 2. Simple Calculator

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operator = input("Enter operator: ")

if operator == "+":
    print(num1 + num2)

elif operator == "-":
    print(num1 - num2)

elif operator == "*":
    print(num1 * num2)

elif operator == "/":
    print(num1 / num2)

else:
    print("Wrong operator")

# 3

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 > num2 and num1 > num3:
    print(num1)

elif num2 > num1 and num2 > num3:
    print(num2)

else:
    print(num3)
