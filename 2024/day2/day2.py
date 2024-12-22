test_file_path = "C:/Users/peter/Documents/GitHub/advent-of-code/2024/day2/test2.txt"
input_file_path = "C:/Users/peter/Documents/GitHub/advent-of-code/2024/day2/input.txt"

lists = [[int(char) for char in line.split()] for line in open(input_file_path).read().splitlines()]
# Part 1 
def check_valid_p1(seq):
    change = seq[1]-seq[0]
    prev = seq[0]
    for i in range(1,len(seq)):
        if change*(seq[i]-prev) < 0 or abs(seq[i]-prev) > 3 or abs(seq[i]-prev) < 1:
            return False
        else:
            prev = seq[i]
    return True


#print(check_list())

# Part 2 
def check_valid_p2(seq):
    if len(seq) < 2:  
        return False
    for i in range(len(seq)):
        new_seq = seq[:i] + seq[i + 1:]
        if check_valid_p1(new_seq):
            return True
    return False


def check_list():
    num_of_safe=0
    for subseq in lists:
        if check_valid_p2(subseq):
            num_of_safe+=1
    return num_of_safe

print(check_list())