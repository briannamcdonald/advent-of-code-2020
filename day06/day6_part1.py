def main():
    data = open("day6/input.txt", "r")
    data = [line.strip() for line in data]

    total_sum = 0
    index = 0
    while index <= len(data):
        new_set = set()
        line = data[index]
        # until we reach a blank line separating the groups
        while line != "":
            # turn each line in the group into a set
            line_set = set(line)
            # combine each line set into a total set for the group
            new_set = new_set.union(line_set)
            index += 1
            if index >= len(data):
                break
            line = data[index]
        # add the length of the group's set to the total sum
        total_sum += len(new_set)
        index += 1
    print(total_sum)


if __name__ == "__main__":
    main()