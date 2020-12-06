def main():
    data = open("day6/input.txt", "r")
    data = [line.strip() for line in data]

    total_sum = 0
    index = 0
    set_list = []
    while index <= len(data):
        line = data[index]
        # until we reach a blank line separating the groups
        while line != "":
            # turn each line in the group into a set
            line_set = set(line)
            # add each set to a list of sets
            set_list.append(line_set)
            index += 1
            if index >= len(data):
                break
            line = data[index]
        # take the intersection of all the sets for the group to find the questions that everyone said yes to
        total_set = set.intersection(*set_list)
        # add the length of the group's total set to the total sum
        total_sum += len(total_set)
        index += 1
        set_list = []
    print(total_sum)


if __name__ == "__main__":
    main()