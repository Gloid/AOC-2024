test_file_path = "C:/Users/peter/Documents/GitHub/advent-of-code/2024/day4/test.txt"
input_file_path = "C:/Users/peter/Documents/GitHub/advent-of-code/2024/day4/input.txt"

matrix = [[list(chars) for chars in line.split()][0] for line in open(input_file_path).read().splitlines()]


#print(matrix)
def checkUp(r, c):
    if r < 3:
        return False
    if matrix[r - 1][c] == 'M' and matrix[r - 2][c] == 'A' and matrix[r - 3][c] == 'S':
        return True
    return False

def checkDown(r, c):
    if r > len(matrix) - 4:
        return False
    if matrix[r + 1][c] == 'M' and matrix[r + 2][c] == 'A' and matrix[r + 3][c] == 'S':
        return True
    return False

def checkRight(r, c):
    if c > len(matrix[r]) - 4:
        return False
    if matrix[r][c + 1] == 'M' and matrix[r][c + 2] == 'A' and matrix[r][c + 3] == 'S':
        return True
    return False

def checkLeft(r, c):
    if c < 3:
        return False
    if matrix[r][c - 1] == 'M' and matrix[r][c - 2] == 'A' and matrix[r][c - 3] == 'S':
        return True
    return False

def checkDiagUpRight(r, c):
    if r < 3 or c > len(matrix[r]) - 4:
        return False
    if matrix[r - 1][c + 1] == 'M' and matrix[r - 2][c + 2] == 'A' and matrix[r - 3][c + 3] == 'S':
        return True
    return False

def checkDiagUpLeft(r, c):
    if r < 3 or c < 3:
        return False
    if matrix[r - 1][c - 1] == 'M' and matrix[r - 2][c - 2] == 'A' and matrix[r - 3][c - 3] == 'S':
        return True
    return False

def checkDiagDownRight(r, c):
    if r > len(matrix) - 4 or c > len(matrix[r]) - 4:
        return False
    if matrix[r + 1][c + 1] == 'M' and matrix[r + 2][c + 2] == 'A' and matrix[r + 3][c + 3] == 'S':
        return True
    return False

def checkDiagDownLeft(r, c):
    if r > len(matrix) - 4 or c < 3:
        return False
    if matrix[r + 1][c - 1] == 'M' and matrix[r + 2][c - 2] == 'A' and matrix[r + 3][c - 3] == 'S':
        return True
    return False

def check_XMAS():
    nbr_of_XMAS = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'X':
                if checkUp(i,j):
                    nbr_of_XMAS+=1
                if checkDown(i,j):
                    nbr_of_XMAS+=1
                if checkRight(i,j):
                    nbr_of_XMAS+=1
                if checkLeft(i,j):
                    nbr_of_XMAS+=1
                if checkDiagUpRight(i,j):
                    nbr_of_XMAS+=1
                if checkDiagUpLeft(i,j):
                    nbr_of_XMAS+=1
                if checkDiagDownRight(i,j):
                    nbr_of_XMAS+=1
                if checkDiagDownLeft(i,j):
                    nbr_of_XMAS+=1
    print(nbr_of_XMAS)
#check_XMAS()

def check_X_MAS():
    nbr_of_X_MAS = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'A':
                if i == 0 or j == 0 or i == len(matrix)-1 or j == len(matrix[i])-1:
                    continue
                count = 0
                for d1 in [-1,1]:
                    
                    if matrix[i-d1][j+d1] == 'M' and matrix[i+d1][j-d1] == 'S':
                        count+=1
                    if matrix[i+d1][j+d1] == 'M' and matrix[i-d1][j-d1] == 'S':
                        count+=1
                if count == 2:
                    nbr_of_X_MAS+=1
    print(nbr_of_X_MAS)                 
check_X_MAS()