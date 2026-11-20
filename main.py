# MY PROGRAM CALCOLATOR :-)
# version : 0.2v


first_number = float(input("Enter First Number : "))
opr = input("Enter An opration (+ , - , / , *) : ")
second_number = float(input("Enter Second Number : "))

match opr :
    case "+":
        print(f"{first_number} + {second_number} = {first_number + second_number}")
    case "-":
        print(f"{first_number} - {second_number} = {first_number - second_number}")
    case "*":
        print(f"{first_number} * {second_number} = {first_number * second_number}")
    case "/":
        print(f"{first_number} / {second_number} = {first_number / second_number}")
    case _:
        print("Please Enter valid operation !!!")


