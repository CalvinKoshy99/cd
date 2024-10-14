#Practical 7: Design a program to generate Directed Acyclic Graph (DAG).#

class DAG:
    def __init__(self):
        self.str = []
        self.table = [[""] * 10 for _ in range(10)]
        self.count = -1

        print("Enter The Sequence of code:")
        print("Enter 'q' to Quit")
        while len(self.str) < 10:
            line = input()
            if line == 'q':
                break
            self.str.append(line)
            self.count += 1

        print("The Sequence of code are:")
        for line in self.str:
            if line == 'q':
                break
            print(line)

    def tablestruct(self):
        for i in range(self.count + 1):
            if len(self.str[i]) == 3:  # D=A
                self.table[i] = [self.str[i][0], self.str[i][1], self.str[i][2]]
            elif len(self.str[i]) == 5:  # A=B+C
                self.table[i] = [self.str[i][0], self.str[i][3], self.str[i][2], self.str[i][4]]

        for i in range(self.count + 1):
            for j in range(i + 1, self.count + 1):
                if len(self.str[i]) == 5 and len(self.str[j]) == 5:
                    if self.str[i][2:5] == self.str[j][2:5]:
                        self.table[i][0] += f",{self.str[j][0]}{self.str[j][4]}"
                        self.table[j] = [""] * 10

                if len(self.str[i]) == 3:
                    if i == self.count:
                        for j in range(self.count - 1, -1, -1):
                            if self.str[i][2] == self.str[j][0]:
                                self.table[j][0] += f",{self.str[i][0]}"
                                self.table[i] = [""] * 10
                    else:
                        for j in range(i + 1, self.count + 1):
                            if self.str[i][2] == self.str[j][0]:
                                self.table[i][0] += f",{self.str[j][0]}"
                                self.table[j] = [""] * 10

        print("\nLabel\t\tOperator\tLeft\tRight")
        for i in range(self.count + 1):
            print("\t".join(self.table[i]))

if __name__ == "__main__":
    dag = DAG()
    dag.tablestruct()
