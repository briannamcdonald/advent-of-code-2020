def check_slope(right, down, data):
    x = 0
    tree_counter = 0
    for line in data[::down]:
        if x >= len(line):
            x = x % (len(line))
        if line[x] == "#":
            tree_counter += 1
        x += right
    return tree_counter


def main():
    data = open("day3/input.txt", "r")
    data = [line.strip() for line in data.readlines()]

    tree_counter1 = check_slope(1, 1, data)
    tree_counter2 = check_slope(3, 1, data)
    tree_counter3 = check_slope(5, 1, data)
    tree_counter4 = check_slope(7, 1, data)
    tree_counter5 = check_slope(1, 2, data)
    print(tree_counter1 * tree_counter2 * tree_counter3 * tree_counter4 * tree_counter5)


if __name__ == "__main__":
    main()
