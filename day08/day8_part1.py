def main():
    data = open("day8/input.txt", "r")
    data = [line.strip() for line in data]

    visited_indices = []
    index = 0
    accumulator = 0
    while True:
        # if the index is in visited indices list, we are done
        if index in visited_indices:
            break
        visited_indices.append(index)
        # parse the instruction
        line = data[index].split()
        instruction = line[0]
        number = int(line[1])
        # execute the instruction
        if instruction == "acc":
            accumulator += number
            index += 1
        elif instruction == "jmp":
            index += number
        else:
            index += 1
    print(accumulator)


if __name__ == "__main__":
    main()