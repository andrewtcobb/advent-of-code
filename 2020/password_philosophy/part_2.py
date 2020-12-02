def format_input(input):
    formatted_input = []
    for line in input:
        rule = line[0: line.index(':')]
        password = line[line.index(':')+2: -1]
        formatted_input.append((rule, password))

    return formatted_input


def is_valid(rule, password):
    rule_char = rule[-1]
    position1 = int(rule[0:rule.index('-')]) - 1
    position2 = int(rule[rule.index('-')+1:rule.index(' ')]) - 1

    is_valid = False

    if password[position1] is rule_char:
        is_valid = True
    if password[position2] is rule_char:
        is_valid = not is_valid

    return is_valid


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
