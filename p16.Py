def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

print("Simple Calculator")
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
choice = input("Enter choice(1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"{num1} - {num2} = {sub(num1, num2)}")
elif choice == '3':
    print(f"{num1} * {num2} = {mul(num1, num2)}")
elif choice == '4':
    print(f"{num1} / {num2} = {div(num1, num2)}")
else:
    print("Invalid input")
