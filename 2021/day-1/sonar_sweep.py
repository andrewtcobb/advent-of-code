def part1(report):
    last_depth = -1
    num_increases = 0

    for depth in report:
        if last_depth < depth and last_depth >= 0:
            num_increases += 1
        last_depth = depth

    return num_increases


def part2(report):
    sums = []

    for i, depth in enumerate(report):
        if i + 2 < len(report):
            sums.append(depth + report[i+1] + report[i+2])

    return part1(sums)


input = open('input.txt', 'r').read().splitlines()
report = [int(i) for i in input]


print(part1(report))
print(part2(report))
