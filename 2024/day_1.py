#test input
test_input = '''3   4
4   3
2   5
1   3
3   9
3   3'''

# arrayInput = str_input.split("\n")
arrayTest = test_input.split("\n")

current_input = arrayTest

left = []
right = []

# spilt and put each value into diff list
for i in current_input:
    print(i)
    left.append(int(i.split()[0]))
    right.append(int(i.split()[1]))

print(left)

left.sort()
right.sort()

# part 1
# print(left)

# sum = 0

# for i in range(len(left)):
#     sum += abs(left[i] - right[i])

# print(sum)

# part 2
score = 0
for i in range(len(left)):
    score += left[i] * right.count(left[i])

print(score)