test_file_path = "C:/Users/peter/Documents/GitHub/advent-of-code/2024/day3/test.txt"
input_file_path = "C:/Users/peter/Documents/GitHub/advent-of-code/2024/day3/input.txt"

string = open(input_file_path).read()
total = 0
enable = True

for i, c in enumerate(string):
    invalid=False
    if string[i:i+4] == "do()":
        enable = True
    if string[i:i+7] == "don't()":
        enable = False
    if string[i:i+4] == "mul(" and enable == True:
        search = string[i+4]
        startIndex = i+4
        nextIndex = startIndex
        while search != ',':
            if not search.isdigit():
                invalid = True
            nextIndex += 1
            search = string[nextIndex]

        if invalid: continue
        int1 = int(string[i+4:nextIndex])
        startIndex = nextIndex
        search = string[nextIndex+1]
        while search != ')':
            if not search.isdigit():
                invalid = True
            nextIndex += 1

            search = string[nextIndex]
        if invalid: continue
        int2 = int(string[startIndex+1:nextIndex])
        total+=int1*int2

print(total)