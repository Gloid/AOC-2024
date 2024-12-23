test_file_path = "C:/Users/peter/Documents/GitHub/advent-of-code/2024/day5/test.txt"
input_file_path = "C:/Users/peter/Documents/GitHub/advent-of-code/2024/day5/input.txt"
input = [line for line in open(test_file_path).read().splitlines()]
rules = []
while input and input[0] != "": 
    rule = input.pop(0)
    rules.append([int(rule[:2]), int(rule[3:])])
updates = []
while len(input)>1:
    temp_updates = []
    update_string = input.pop(1)
    for update in update_string.split(","):
        temp_updates.append(int(update))
    updates.append(temp_updates)

def check_valid():
    total = 0
    for update in updates:
        invalid = False
        for index, page in enumerate(update):
            rule_before = [rules[i][0] for i in range(len(rules)) if rules[i][1] == page]
            rule_after = [rules[i][1] for i in range(len(rules)) if rules[i][0] == page]
            new_list = update[:update.index(page)] + update[update.index(page)+1:]
            for new_index, new_page in enumerate(update):
                if page == new_page: continue
                if new_page in rule_before and new_index > index:
                    invalid = True
                    break
                if new_page in rule_after and new_index < index:
                    invalid = True
                    break
        if not invalid:
            total += update[int(len(update)/2)]
    return total                   
print(check_valid())

