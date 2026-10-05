import sys

# Define mathematical functions.

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

print('\n'+'SIMPLE CALCULATOR'.center(100) + '\n')

def main():  # Main Menu
    while True:
        print('\n1.Sum\n2.Sub\n3.Mul\n4.Div\n5.Exit\n')
        menu_selection = input('What would you like to do? > ').strip().lower()

        if menu_selection == 'sum':
            try:
                a = float(input('Enter first number > '))
            except ValueError:
                print('Please enter a number.')
                continue
            try:
                b = float(input('Enter second number > '))
            except ValueError:
                print('Please enter a number.')
                continue
            print('Result: ' + str(add(a,b)))
            continue

        elif menu_selection == 'sub':
            try:
                a = float(input('Enter first number > '))
            except ValueError:
                print('Please enter a number.')
                continue
            try:
                b = float(input('Enter second number > '))
            except ValueError:
                print('Please enter a number.')
                continue
            print(sub(a,b))
            continue

        elif menu_selection == 'mul':
            try:
                a = float(input('Enter first number > '))
            except ValueError:
                print('Please enter a number.')
                continue
            try:
                b = float(input('Enter second number > '))
            except ValueError:
                print('Please enter a number.')
                continue
            print('Result: ' + str(mul(a,b)))
            continue

        elif menu_selection == 'div':
            try:
                a = float(input('Enter first number > '))
            except ValueError:
                print('Please enter a number.')
                continue
            try:
                b = float(input('Enter second number > '))
            except ValueError:
                print('Please enter a number.')
                continue
            print('Result: ' + str(div(a,b)))
            continue

        elif menu_selection == 'exit':
            sys.exit()

        print('\nPlease enter a valid selection.\n')
        continue

if __name__ == '__main__':
    main()