import sys
from typing import Any, List, Tuple

def getMatrix(rows: int, cols: int, input: List[str], line: int) -> List[List[float]]:
    mat = []

    for i in range(rows):
        row = []
        row_str = input[line + i].split()
        for s in row_str:
            row.append(float(s))
        mat.append(row)
    
    return mat

def parseInput(file: str) -> Tuple[List[List[float]], List[List[float]], List[List[float]], List[List[float]], List[float]]:
    # Initialize array that contains all lines of input
    input = None

    # Open file and read all lines
    with open(file) as f:
        input = f.readlines()

    # Strip all newline characters and spaces
    input = [x.strip() for x in input]

    # Remove commented lines and blank lines
    input = list(filter(lambda x: len(x) > 0 and x[0] != "#", input))

    # Initialize variable to keep track of current line
    line = 0

    # Get size of A matrix
    A_row, A_col = input[line].split()
    line += 1
    # Read A matrix
    A = getMatrix(int(A_row), int(A_col), input, line)
    line += int(A_row)

    # Get size of B matrix
    B_row, B_col = input[line].split()
    line += 1
    # Read B matrix
    B = getMatrix(int(B_row), int(B_col), input, line)
    line += int(B_row)

    # Get size of C matrix
    C_row, C_col = input[line].split()
    line += 1
    # Read C matrix
    C = getMatrix(int(C_row), int(C_col), input, line)
    line += int(C_row)

    # Get size of D matrix
    D_row, D_col = input[line].split()
    line += 1
    # Read D matrix
    D = getMatrix(int(D_row), int(D_col), input, line)
    line += int(D_row)

    # Read number of discrete timesteps to calculate for
    timesteps = int(input[line])
    line += 1

    # Initialze all input values to 0
    x = [0.0 for i in range(timesteps)]
    while line < len(input):
        lineData = input[line].split()
        n, x_n = int(lineData[0]), float(lineData[1])
        x[n] = x_n
        line += 1
    
    return (A, B, C, D, x)

if __name__ == "__main__":
    args = len(sys.argv)

    if args == 1:
        print("Error: No input file given!")
        sys.exit(1)
    
    for i in range(1,args):
        # Process each input file

        A, B, C, D, x = parseInput(sys.argv[i])

        print(A, B, C, D, x)
    
