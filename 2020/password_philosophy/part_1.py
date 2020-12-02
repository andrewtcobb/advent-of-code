def format_input(input):
    formatted_input = []
    for line in input:
        rule = line[0: line.index(':')]
        password = line[line.index(':')+2: -1]
        formatted_input.append((rule, password))

    return formatted_input


def is_valid(rule, password):
    char_frequency = {}
    for char in password:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

    rule_char = rule[-1]
    min_frequency = int(rule[0:rule.index('-')])
    max_frequency = int(rule[rule.index('-')+1:rule.index(' ')])

    if rule_char not in char_frequency:
        return False

    if char_frequency[rule_char] >= min_frequency and char_frequency[rule_char] <= max_frequency:
        return True
    else:
        return False


input = []
file = open("input.txt")

for line in file:
    input.append(line)

formatted_input = format_input(input)

valid_count = 0
for entry in formatted_input:
    if(is_valid(entry[0], entry[1])):
        valid_count += 1

print(valid_count)
