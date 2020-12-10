def run_program(data):
    visited_indices = []
    index = 0
    accumulator = 0
    length = len(data)
    while True:
        # if the index is in visited indices list, we have an infinite loop
        if index in visited_indices:
            return (False, accumulator)
        visited_indices.append(index)
        # if we reach the end of the file, the program has completed
        if index >= length:
            return (True, accumulator)
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


def main():
    data = open("day8/input.txt", "r")
    data = [line.strip() for line in data]

    index = 0
    done = False
    while not done:
        # parse the instruction
        line = data[index].split()
        instruction = line[0]
        number = line[1]

        if instruction == "acc":
            index += 1
            continue
        # replace jmp with nop or nop with jmp and try running the program
        new_data = list(data)
        new_data[index] = "nop " + number if (instruction == "jmp") else "jmp " + number
        done, accumulator = run_program(new_data)
        index += 1
    print(accumulator)


if __name__ == "__main__":
    main()