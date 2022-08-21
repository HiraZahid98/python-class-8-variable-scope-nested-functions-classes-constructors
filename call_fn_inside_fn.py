def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def calculator(num1, num2, op):
    if op == '+':
        print(add(num1, num2))
    elif op == '-':
        print(subtract(num1, num2))
    else:
        print('bad operator')


calculator(1, 4, '-')