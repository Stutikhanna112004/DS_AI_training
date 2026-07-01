try:
    numerator = float(input("enter the first value"))
    denominator = float(input("enter the second value"))
    
    #attemp division 

    result = numerator/denominator
    print(f"result: {result}" )
except ZeroDivisionError:
    print("Error: You cannot divide by zero")
except ValueError:
    print("Error: Please enter valid number")