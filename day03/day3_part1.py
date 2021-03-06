def main():
    data = open("day3/input.txt", "r")
    data = [line.strip() for line in data.readlines()]

    tree_counter = 0
    x = 0
    for line in data:
        if x >= len(line):
            x = x % (len(line))
        if line[x] == "#":
            tree_counter += 1
        x += 3
    print(tree_counter)


if __name__ == "__main__":
    main()