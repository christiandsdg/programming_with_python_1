import sys

# Define the mathematical functions.

def add(a: float, b: float) -> float:
    return a + b

def sub(a: float, b: float) -> float:
    return a - b

def mul(a: float, b: float) -> float:
    return a * b

def div(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError('Cannot divide by zero.')
    return a / b

# Test mathematical functions with asserts.

assert add(1, 2) == 3
assert sub(5, 3) == 2
assert mul(2, 3) == 6
assert div(12, 4) == 3

print('\n'+'SIMPLE CALCULATOR'.center(100))
print('Written by: Christian Da Silva De Goes'.center(100) + '\n')

def main():  # Main Menu
    while True:
        print('\n1.Sum\n2.Sub\n3.Mul\n4.Div\n5.Exit\n')
        menu_selection = input('Type the name of the operation you wish to do. > ').strip().lower()

        if menu_selection == 'sum':     #Addition sub-menu
            try:
                a = float(input('Enter first number > '))
                b = float(input('Enter second number > '))
                print('Result: ' + str(add(a, b)))
            except ValueError:
                print('Please enter a number.')
                continue
            continue

        elif menu_selection == 'sub':   #Subtraction sub-menu
            try:
                a = float(input('Enter first number > '))
                b = float(input('Enter second number > '))
                print('Result: ' + str(sub(a, b)))
            except ValueError:
                print('Please enter a number.')
                continue
            continue

        elif menu_selection == 'mul':   #Multiplication sub-menu
            try:
                a = float(input('Enter first number > '))
                b = float(input('Enter second number > '))
                print('Result: ' + str(mul(a, b)))
            except ValueError:
                print('Please enter a number.')
                continue
            continue

        elif menu_selection == 'div':   #Division sub-menu
            try:
                a = float(input('Enter first number > '))
                b = float(input('Enter second number > '))
                print('Result: ' + str(div(a, b)))
            except ValueError:
                print('Please enter a number.')
                continue
            except ZeroDivisionError:
                print('Cannot divide by zero.')
                continue
            continue

        elif menu_selection == 'exit':  #Exit program sub-menu
            sys.exit()

        print('\nPlease enter a valid selection.\n')    #Message if menu-selection is invalid.
        continue

if __name__ == '__main__':
    main()