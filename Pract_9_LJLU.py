#Practical 9: Design a program to implement Loop Jamming and Loop Unrolling#

##9A Loop Jamming##

import time

def main():
    array1 = [10, 20, 30]
    array2 = [20, 10, 30]
    array3 = [40, 40, 10]

    # Version 1: loop over each array separately.
    start_time = time.time()
    for _ in range(10_000_000):
        sum_value = sum(array1) + sum(array2) + sum(array3)
        if sum_value != 210:
            print(False)
    end_time = time.time()

    # Version 2: jam loops together.
    start_time_jammed = time.time()
    for _ in range(10_000_000):
        sum_value = sum(a + b + c for a, b, c in zip(array1, array2, array3))
        if sum_value != 210:
            print(False)
    end_time_jammed = time.time()

    # ... Times.
    print("Before loop jamming ---->", (end_time - start_time) * 1000)  # Convert to milliseconds
    print("After loop jamming ---->", (end_time_jammed - end_time) * 1000)  # Convert to milliseconds

if __name__ == "__main__":
    main()

  
##9B Loop Unrolling##

import time

def main():
    array1 = [0] * 5  # Initialize an array of length 5 with zeroes

    # Version 1: assign elements in a loop.
    start_time = time.time()
    for _ in range(10_000_000):
        for x in range(len(array1)):
            array1[x] = x
    end_time = time.time()

    # Version 2: unroll the loop and use a list of statements.
    start_time_unrolled = time.time()
    for _ in range(10_000_000):
        array1[0] = 0
        array1[1] = 1
        array1[2] = 2
        array1[3] = 3
        array1[4] = 4
    end_time_unrolled = time.time()

    # ... Times.
    print("Time taken by processor before loop unrolling: -->", (end_time - start_time) * 1000)  # Convert to milliseconds
    print("Time taken by processor after loop unrolling: -->", (end_time_unrolled - end_time) * 1000)  # Convert to milliseconds

if __name__ == "__main__":
    main()
