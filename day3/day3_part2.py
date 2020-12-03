def check_slope(right, down, input):
    x = 0
    tree_counter = 0
    for line in input[::down]:
        if x >= len(line):
            x = x % (len(line))
        if line[x] == "#":
            tree_counter += 1
        x += right
    return tree_counter


def main():
    input = open("day3/input.txt", "r")
    input = [line.strip() for line in input.readlines()]

    tree_counter1 = check_slope(1, 1, input)
    tree_counter2 = check_slope(3, 1, input)
    tree_counter3 = check_slope(5, 1, input)
    tree_counter4 = check_slope(7, 1, input)
    tree_counter5 = check_slope(1, 2, input)
    print(tree_counter1 * tree_counter2 * tree_counter3 * tree_counter4 * tree_counter5)


main()