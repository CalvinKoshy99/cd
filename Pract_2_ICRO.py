#Practical 2: Design a program to check given input is identifier, constants, reserved keywords, and operators.

##2A Identifier##

def is_valid_identifier(s):
    if not (s[0].isalpha()):  # First character must be a letter
        return False
    return all(c.isalnum() or c == '_' for c in s)  # Check rest of the characters

if __name__ == "__main__":
    s = input("Enter a string: ")
    print("Identifier" if is_valid_identifier(s) else "Not an Identifier")

##2B Constant##

def check_constant():
    s = input("Enter the string: ")
    if s.isdigit():  # Checks if all characters are digits
        print("Constant")
    else:
        print("Not a Constant")

if __name__ == "__main__":
    check_constant()

##2C Reserved Keyword##

import keyword
def check_reserved_keyword():
    s = input("Enter the string: ")

    if keyword.iskeyword(s):
        print("Reserved Keyword")
    else:
        print("Not a Reserved Keyword")

if __name__ == "__main__":
    check_reserved_keyword()

##2D Operator##

import operator

def check_operator():
    operators = {"+", "-", "/", "*", "<=", ">=", "<", ">", "==", "!="}
    s = input("Enter the operator: ")

    if s in operators:
        print("Operator")
    else:
        print("Not an Operator")

if __name__ == "__main__":
    check_operator()
