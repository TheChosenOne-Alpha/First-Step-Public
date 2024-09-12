import sys

sys.set_int_max_str_digits(2147483647)


def error_message():
    print("ERROR: input a proper value")

while True:
    print("     ({[CALCULATOR]})")
    num1 = int(input("choose your first number: "))
    symbol = input("choose your math symbol (+ , - , x , /, ^): ")
    num2 = int(input("choose your second number: "))
    if symbol == "+":
        answer = num1 + num2
        print(num1, symbol, num2, "=", answer)
    elif symbol == "-":
        answer = num1 - num2
        print(num1, symbol, num2, "=", answer)
    elif symbol == "x":
        answer = num1 * num2
        print(num1, symbol, num2, "=", answer)
    elif symbol == "/":
        answer = num1 / num2
        print(num1, symbol, num2, "=", answer)
    elif symbol == "^":
        answer = num1 ** num2
        print(num1, symbol, num2, "=", answer)
    else:
        error_message()
        break
    again = input("want to do it again? (y/n): ")
    if again == "n":
        break
    elif again == "y":
        continue
    else:
        error_message()
        break
    