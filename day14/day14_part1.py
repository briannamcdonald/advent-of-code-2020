def main():
    data = open("day14/input.txt", "r")
    data = [line.strip() for line in data]

    memory = {}
    for line in data:
        line = line.split()
        if line[0] == "mask":
            mask_list = list(line[2])
            or_list = len(mask_list) * ["0"]
            and_list = len(mask_list) * ["1"]
            for i, char in enumerate(mask_list):
                if char == "1":
                    or_list[i] = "1"
                elif char == "0":
                    and_list[i] = "0"
            or_mask = int("".join(or_list), 2)
            and_mask = int("".join(and_list), 2)
        else:
            value = (int(line[2]) & and_mask) | or_mask
            location = line[0].split("[")
            location = int(location[1].strip("]"))
            memory[location] = value
    total_sum = 0
    for value in memory.values():
        total_sum += value
    print(total_sum)


if __name__ == "__main__":
    main()