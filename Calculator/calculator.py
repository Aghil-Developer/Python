from calculator_utils import calculate

n1 = float(input("What is the first number? "))
toContinue = True

n2 = 0
while toContinue:
    print("+\n-\n*\n/")
    operator = input("Pick an operator: ")
    n2 = float(input("What is the second number? "))
    calculation = calculate(n1, operator, n2)
    print(f"{n1} {operator} {n2} = {calculation}")
    toContinue = input(f"Type 'y' to continue calculating with {n2}, or type 'n' to start a new calculation: ")
    if toContinue == 'y':
        n1 = calculation
    elif toContinue == 'n':
        toContinue = False
