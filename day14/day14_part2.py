def handle_floats(memory, location, value):
    if location.count("X") == 0:
        memory[location] = value
        return
    handle_floats(memory, location.replace("X", "0", 1), value)
    handle_floats(memory, location.replace("X", "1", 1), value)


def apply_mask(mask, location):
    new_location = ""
    index = 0
    while index < len(location):
        if mask[index] == "0":
            new_location += location[index]
        else:
            new_location += mask[index]
        index += 1
    return new_location


def main():
    data = open("day14/input.txt", "r")
    data = [line.strip() for line in data]

    memory = {}
    for line in data:
        line = line.split()
        if line[0] == "mask":
            mask = line[2]
        else:
            value = int(line[2])
            location = line[0].split("[")[1].strip("]")
            location = "{0:036b}".format(int(location))
            location = apply_mask(mask, location)
            handle_floats(memory, location, value)
    total_sum = 0
    for value in memory.values():
        total_sum += value
    print(total_sum)


if __name__ == "__main__":
    main()