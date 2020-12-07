def find_num_bags(color, rules):
    if not rules[color]:
        return 0
    else:
        return sum(
            int(num) + int(num) * find_num_bags(clr, rules) for num, clr in rules[color]
        )


def main():
    data = open("day7/input.txt", "r")
    data = [line.strip() for line in data]

    # create a dictionary that stores the rules for each bag
    rules = {}
    for line in data:
        outer, contents = line.split(" bags contain ")
        inner_list = []
        for bag in contents.split(","):
            if not "no other bags." in bag:
                inner_list.append(bag.strip("bags.").strip().split(" ", 1))
        rules[outer] = inner_list

    total_sum = find_num_bags("shiny gold", rules)
    print(total_sum)


if __name__ == "__main__":
    main()