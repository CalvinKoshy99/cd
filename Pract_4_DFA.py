#Practical 4: Design a program to minimize the given DFA.#

def state_no(cc, dfa):
    for i, row in enumerate(dfa):
        if row[0] == cc:
            return i
    return -1  # Return -1 if state not found

def main():
    dfa = [["A", "B", "C"], ["B", "B", "D"], ["C", "B", "C"], ["D", "B", "E"], ["E", "B", "C"]]
    final_state = ['E']
    group = []

    print("*** DFA ***")
    print("\t" + "\t".join(dfa[0][1:]))  # Print headers

    for row in dfa:
        print("\t".join(row))

    # Finding final states
    for row in dfa:
        if row[1] == final_state[0] or row[2] == final_state[0]:
            final_state.append(row[0])

    print("\nGive Final State =", " ".join(final_state))

    # Finding equivalent states for minimized DFA
    for i in range(len(dfa)):
        for j in range(i + 1, len(dfa)):
            if dfa[i][1:] == dfa[j][1:]:
                group.append([dfa[i][0], dfa[j][0]])

    print("\n\n**** MIN DFA *****")
    print("\t" + "\t".join(dfa[0][1:]))  # Print headers for minimized DFA

    for fs in final_state:
        ff = state_no(fs, dfa)
        if ff != -1:
            print(f"{fs}\t{dfa[ff][1]}\t{dfa[ff][2]}")

if __name__ == "__main__":
    main()

