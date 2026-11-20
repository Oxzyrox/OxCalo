# MY PROGRAM CALCOLATOR :-)
# version : 0.1v


first_number = float(input("Enter First Number : "))
opr = input("Enter An opration (+ , - , / , *) : ")
second_number = float(input("Enter Second Number : "))

if opr == "+":
    print(f"{first_number} + {second_number} = {first_number + second_number}")
elif opr == "-":
    print(f"{first_number} - {second_number} = {first_number - second_number}")
elif opr == "/":
    print(f"{first_number} / {second_number} = {first_number / second_number}")
elif opr == "*":
    print(f"{first_number} * {second_number} = {first_number * second_number}")

else :
    print("Please Enter valid operation !!!")

