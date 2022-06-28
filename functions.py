def greeting(name): # def is the keyword for creating a function
    print("Hello,", name)

input_name = input("Enter your name:\n")
greeting(input_name)

def addition(a, b):
    return a + b

def main():
    num1 = float(input("Enter your first number:\n"))
    num2 = float(input("Enter your second number:\n"))
    
    result = addition(num1, num2)
    print("The resultis:", result)

main()