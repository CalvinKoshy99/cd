#Practical 6: Design a program to develop Operator Precedence Matrix (OPM).#

class Production:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

def display(mat, sym):
    print(' '.join(sym))
    for i in range(len(sym)):
        print(f"{sym[i]} {' '.join(str(mat[i][j]) for j in range(len(sym)))}")

productions = []
ans = 'y'

# Collect multiple productions
while ans.lower() == 'y':
    lhs, rhs = input("\n\n Enter production (LHS RHS): ").split()
    productions.append(Production(lhs, rhs))
    ans = input("\n Continue? (y/n): ")

# Display the entered productions
print("\n\n Productions are :")
for prod in productions:
    print(f"\n {prod.lhs} -> {prod.rhs}")

# Collect symbols from productions
sym = {productions[0].lhs}
for prod in productions:
    sym.add(prod.lhs)
    sym.update(prod.rhs)

# Display the collected symbols
print("\n\n Final Symbols:")
print('\t' + '\t'.join(sym))

# Initialize matrices
size = 20
first = [[0] * size for _ in range(size)]
firstp = [[0] * size for _ in range(size)]
firsts = [[0] * size for _ in range(size)]
last = [[0] * size for _ in range(size)]
lastp = [[0] * size for _ in range(size)]
lasts = [[0] * size for _ in range(size)]
equals = [[0] * size for _ in range(size)]
lt = [[0] * size for _ in range(size)]
gt = [[0] * size for _ in range(size)]
opm = [['0'] * size for _ in range(size)]

# Placeholder for processing logic
print("\n\n FIRST MATRIX: ")
display(first, list(sym))

print("\n\n FIRST PLUS MATRIX: ")
display(firstp, list(sym))

print("\n\n FIRST STAR MATRIX: ")
display(firsts, list(sym))

print("\n\n LAST MATRIX: ")
display(last, list(sym))

print("\n\n LAST PLUS MATRIX: ")
display(lastp, list(sym))

print("\n\n LAST STAR MATRIX: ")
display(lasts, list(sym))

print("\n\n EQUALS MATRIX: ")
display(equals, list(sym))

print("\n\n FIRST TERM MATRIX: ")
display(lt, list(sym))

print("\n\n LAST TERM MATRIX: ")
display(gt, list(sym))

print("\n\n LESS THAN MATRIX: ")
display(lt, list(sym))

print("\n\n GREATER THAN MATRIX: ")
display(gt, list(sym))

print("\n\n OPERATOR PRECEDENCE MATRIX: ")
for i in range(len(sym)):
    print(' '.join(opm[i]))
