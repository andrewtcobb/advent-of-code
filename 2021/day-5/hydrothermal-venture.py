from os import umask


def part_1(lines):
    ocean_floor = [[0 for col in range(10)] for row in range(10)]

    for line in lines:
        start, end = line.split(' -> ')
        add_line_to_ocean_floor(start, end, ocean_floor)

    for line in ocean_floor:
        print(line)

    return count_overlaps(ocean_floor)


def add_line_to_ocean_floor(start, end, ocean_floor):
    x1, y1 = start.split(',')
    x2, y2 = end.split(',')

    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)

    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2)+1):
            ocean_floor[y][x1] += 1
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2)+1):
            ocean_floor[y1][x] += 1
    elif is_line_45_degrees(x1, x2, y1, y2):
        if x1 > x2 and y1 > y2 or x2 > x1 and y2 > y1:  # 1,1 -> 0,0  or 0,0 -> 1,1
            x = min(x1, x2)
            y = min(y1, y2)

            for i in range(abs(x2-x1)+1):
                ocean_floor[x+i][y+i] += 1

        # if x1 > x2 and y2 > y1: # 4,4 -> 3,5
        #     x = x2
        #     y = y1
        # if x2 > x1 and y1 > y2: # 3,3 -> 4,2
        #     x = x1
        #     y = y2


def is_line_45_degrees(x1, x2, y1, y2):
    return (abs(x2 - x1) == abs(y2 - y1))


def count_overlaps(ocean_floor):
    count = 0
    for line in ocean_floor:
        for vent in line:
            if vent >= 2:
                count += 1

    return count


input = open('2021/day-5/example-input.txt', 'r').read().splitlines()

print(part_1(input))


'''
--- Part Two ---
Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need to also consider diagonal lines.

Because of the limits of the hydrothermal vent mapping system, the lines in your list will only ever be horizontal, vertical, or a diagonal line at exactly 45 degrees. In other words:

An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.
Considering all lines from the above example would now produce the following diagram:

1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111....
You still need to determine the number of points where at least two lines overlap. In the above example, this is still anywhere in the diagram with a 2 or larger - now a total of 12 points.

Consider all of the lines. At how many points do at least two lines overlap?
'''
