def main():
    data = open("day7/input.txt", "r")
    data = [line.strip() for line in data]

    total_set = {"shiny gold"}
    length = len(total_set)
    done = False
    while not done:
        # find all the bags that can hold a bag in the set
        for line in data:
            if any(bag in line for bag in total_set):
                # get the first two words of the line and store it in the set
                line = line.split()
                bag = line[0] + " " + line[1]
                if bag in total_set:
                    continue
                total_set.add(bag)
        # if no more bags were added this iteration, we are done
        if len(total_set) == length:
            done = True
        else:
            length = len(total_set)
    # subtract 1 since the shiny gold bag is included in the set
    print(len(total_set) - 1)


if __name__ == "__main__":
    main()