#Practical 8: Design a program to convert any expression into Three Address Code.#

class ThreeAddressCodeGenerator:
    def __init__(self):
        self.stack = []  # Stack to hold operands
        self.code = []   # Three-address code
        self.temp_count = 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def generate_code(self, postfix_expr):
        print("\nThree Address Code For Given Expression \n")
        for char in postfix_expr:
            if char.isalpha() or char.isdigit():
                self.push(char)
            elif char in '+-*/':
                right_operand = self.pop()  # Right operand
                left_operand = self.pop()    # Left operand
                self.temp_count += 1
                temp_var = f"T{self.temp_count}"
                expression = f"{left_operand} {char} {right_operand}"
                self.code.append(f"{temp_var} = {expression}")
                print(f"{temp_var} = {expression}")  # Output the three-address code
                self.push(temp_var)  # Push the result back to the stack

if __name__ == "__main__":
    postfix_expr = input("Enter The Postfix Expression: ")
    generator = ThreeAddressCodeGenerator()
    generator.generate_code(postfix_expr)
