# Practical 1: Design a program to convert the given Right Linear Grammar into Left Linear Grammar.

def print_productions():
    n = int(input("\nEnter the number of productions you want to convert: "))

    productions = []
    for i in range(n):
        prod = input(f"\nEnter production number {i + 1} in the form of (X = bY): ")
        productions.append(prod)

    print("\n\nThe number of productions are as below:")
    for i, prod in enumerate(productions, 1):
        print(f"{i}) {prod}")

    print("\n\nLeft linear grammar is -->")
    for prod in productions:
        left, right = prod.split('=')
        print(f"{left.strip()} --> {right.strip()}")

if __name__ == "__main__":
    print_productions()
