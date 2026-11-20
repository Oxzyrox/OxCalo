# MY PROGRAM CALCOLATOR :-)
# version : 0.4v

operations = [
    lambda x, y: x + y,
    lambda x, y: x - y,
    lambda x, y: x * y,
    lambda x, y: x / y
]
list_opr = ["+" , "-" , "*" , "/"]

Running = True
while Running :
    try :
        first_number = float(input("Enter first number : "))
        opr = input("Enter an operation (+ , - , * , /) : ")
        second_number= float(input("Enter second number : "))
        status = False
        for i in range(len(list_opr) - 1):
            if list_opr[i]==opr:
                print(f"{first_number} {opr} {second_number} = {operations[i](first_number,second_number)}")
                status = not status
                Running = not Running
                
        if not status :
            print("Please Enter valid opertion !!!")
    except ValueError :
        print("Please Enter Valid number !!!")
