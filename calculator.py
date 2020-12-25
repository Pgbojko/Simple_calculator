def is_number(str):
    try:
        int(str)
        return True

    except ValueError:
        return False

def is_valid_operator(operator):
    operators = ["+", "-", "/", "*"]
    if operator in operators:
        return True
    else:

        return False

def ask_for_a_number(force_valid_input):
    while True:
        user_input = input("Please provide your number: ")
        if is_number(user_input):
            return float(user_input)
        else:
            if not force_valid_input:
                return None
            print("It is not a number.... Try again!: ")

def ask_for_an_operator(force_valid_input):
    while True:
        user_input = input("Please provide your operator ( /, *, +, - ): ")
        if is_valid_operator(user_input):
            return user_input
        else:
            if not force_valid_input:
                return None
            print("It is not an operator.... Try again!: ")



def calc(operator, a, b):

    if not is_valid_operator(operator) or not is_number(a) or not is_number(b):
        return None
    result = None
    if operator == "+":
        result = a + b

    elif operator == "-":
        result = a - b

    elif operator == "*":
        result = a * b

    elif operator == "/":
        if b != 0:
            result = a / b
    else:
        print("You can't divide by 0! ")

    return result

def simple_calculator():
    print("Welcome to my simple calculator! ")
    while True:
        a = ask_for_a_number(force_valid_input=False)
        if not a:
            print("This is not a number")
            continue
        op = ask_for_an_operator(force_valid_input=True)
        b = ask_for_a_number(force_valid_input=True)
        result = calc(op, a, b)
        if result:
            print(f"Your result is {calc(op, a, b)}")

if __name__ == '__main__':
    simple_calculator()
