'''BASIC CALCULATOR'''
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
op=input("Enter operator: ")

match(op):      #use of match case
    case '+':
        print(f"Sum of numbers is {a+b}")
    case '-':
        print(f"Difference of numbers is {a-b}")
    case '*':
        print(f"Product of numbers is {a*b}")
    case '^':
        print(f"value of {a}^{b} is {a**b}")
    case '%':
        print(f"Value of {a}%{b} is {a%b}")
    case '/':
        try:
            print(f"Value of Quotient  is {a/b}")
        except(ArithmeticError):
            print("ERROR\nValue of divisor is 0")
    case _:
        print("INVALID OPERATOR")
