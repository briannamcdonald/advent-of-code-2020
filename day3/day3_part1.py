def main():
    input = open("day3/input.txt", "r")
    input = [line.strip() for line in input.readlines()]

    tree_counter = 0
    x = 0
    for line in input:
        if x >= len(line):
            x = x % (len(line))
        if line[x] == "#":
            tree_counter += 1
        x += 3
    print(tree_counter)


main()