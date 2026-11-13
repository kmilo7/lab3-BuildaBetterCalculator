def read_numbers():
    number = []
    while True:
        text = input("Enter a number (or press Enter to finish): ")
        if text == "":
            break
        numbers.append(float(text))
    return number

def addmultiplenumbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def multiplymultiplenumbers(numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

def isitaninteger(num):
    if num == int(num):
        print(f"The number {num} is an integer.")
        return True
    else:
        print(f"The number {num} isn't an integer.")
        return False

def isiteven(num):
    if isitaninteger(num) == False:
        return False
    elif num % 2 == 0:
        print(f"The number {num} is even.")
        return True
    else:
        print(f"The number {num} is odd.")
        return False
        
def general_calculator():
    result = float(input("Enter the first number: "))

    while True:
        operator = input(f"+ \n- \n* \n/ \n% \n=\n---------\n--- {result} ---\nEnter the operator: ")

        if operator == "=":
            print(f"The final result is: {result}")
            break
        elif operator in ["+", "-", "*", "/", "%"]:
            numberB = float(input("Enter the next number: "))

            if (operator == "/" or operator == "%") and numberB == 0:
                print("!!! You can't divide by zero. Try again.")
                continue

            if operator == "+":
                result += numberB
            elif operator == "-":
                result -= numberB
            elif operator == "*":
                result *= numberB
            elif operator == "/":
                result /= numberB
            elif operator == "%":
                result %= numberB
        else:
            print("!!! Invalid operator. Please try again.")

def main():
    print("Welcome to the Kmilo's Calculator! \n----------------------")

    while True:
        print("----------------------")
        print("1. General calculator (+ - * / %)")
        print("2. Add multiple numbers")
        print("3. Multiply multiple numbers")
        print("4. Is it even?")
        print("5. Is it an integer?")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            general_calculator()
        elif choice == "2":
            numbers = read_numbers()
            print(f"The sum is: {addmultiplenumbers(numbers)}")
        elif choice == "3":
            numbers = read_numbers()
            print(f"The product is: {multiplymultiplenumbers(numbers)}")
        elif choice == "4":
            num = float(input("Enter a number: "))
            print(isiteven(num))
        elif choice == "5":
            num = float(input("Enter a number: "))
            print(isitaninteger(num))
        elif choice == "0":
            break
        else:
            print("!!! Invalid option. Please try again.")

    print("----------------------\nThanks for using Kmilo's Calculator!")

if __name__ == "__main__":
    main()