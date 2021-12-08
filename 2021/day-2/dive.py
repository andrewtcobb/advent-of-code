def part_1(course):
    horizontal = 0
    vertical = 0
    for directions in course:
        direction, units = directions.split(' ')
        units = int(units)

        if direction == 'forward':
            horizontal += units
        elif direction == 'down':
            vertical += units
        elif direction == 'up':
            vertical -= units

    return horizontal*vertical


def part_2(course):
    horizontal = 0
    vertical = 0
    aim = 0

    for directions in course:
        direction, units = directions.split(' ')
        units = int(units)

        if direction == 'forward':
            horizontal += units
            vertical += aim*units
        elif direction == 'down':
            aim += units
        elif direction == 'up':
            aim -= units

    return horizontal*vertical


input = open('input.txt', 'r').read().splitlines()

print(part_1(input))
print(part_2(input))
