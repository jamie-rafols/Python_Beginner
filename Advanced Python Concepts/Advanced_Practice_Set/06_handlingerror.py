
try:
    
    num1 = int(input("Enter number: "))
    x = 10/0
except ValueError:
    print("Invalid")
        
except ZeroDivisionError:
    print("Cannot divide 0")