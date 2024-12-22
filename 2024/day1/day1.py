

# Part 1
test_file_path = "C:/Users/peter/Documents/GitHub/advent-of-code/2024/day1/test.txt"
input_file_path = "C:/Users/peter/Documents/GitHub/advent-of-code/2024/day1/input.txt"
lists = list(map(list,zip(*[list(map(int,line.split())) for line in open(input_file_path).read().splitlines()])))


for sublist in lists:
    sublist.sort()
length=0
for index in range(len(lists[0])):
    length+=abs(lists[0][index]-lists[1][index])
print(length)

# Part 2
sim_score = 0
for num in lists[0]:
    sim_score+= num*(lists[1].count(num))
print(sim_score)
