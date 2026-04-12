real_input = ''''''
test_input = '''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47'''

current_input = test_input

arrayInput = current_input.split()

rules = []
manuals = []

# input formatting
for line in arrayInput:
    if '|' in line:
        rule_list = line.split('|')
        rules.append([int(rule_list[0]), int(rule_list[1])])
    if ',' in line:
        page_numbers = line.split(',')
        new_manual = []
        for page in page_numbers:
            new_manual.append(int(page))
        manuals.append(new_manual)
# print(rules)
# print(manuals)

# rule check function
def rule_check(manual, rules):
    for rule in rules:
        if rule[0] not in manual or rule[1] not in manual:
            return 0
        # print(manual.index(rule[0]))
        print(f'first num {} index: {manual.index(rule[0])}')
        if manual.index(rule[0]) > manual.index(rule[1]):
            return 0
        
    print(manual[len(manual) // 2] + 1)
    return manual[len(manual) / 2]

middle_sum = 0

for manual in manuals:
    print(manual)
    middle_sum += rule_check(manual, rules)

print(middle_sum)