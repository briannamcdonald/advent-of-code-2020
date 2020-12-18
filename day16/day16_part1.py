def main():
    data = open("day16/input.txt", "r")
    data = [line.strip() for line in data]

    # create a list of all valid ranges
    list_of_ranges = []
    for line in data:
        if line == "":
            break
        line = line.split()
        lower, upper = line[-1].split("-")
        list_of_ranges.append((int(lower), int(upper)))
        lower, upper = line[-3].split("-")
        list_of_ranges.append((int(lower), int(upper)))
    # check if all values on each ticket are in a valid range
    index = 25
    invalid_vals = []
    while index < len(data):
        ticket = [int(val) for val in data[index].split(",")]
        for val in ticket:
            valid = False
            for r in list_of_ranges:
                if r[0] <= val and r[1] >= val:
                    valid = True
                    break
            if valid == False:
                invalid_vals.append(val)
        index += 1
    print(sum(invalid_vals))


if __name__ == "__main__":
    main()