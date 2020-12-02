def main():
    input = open("day2/input.txt", "r")

    valid_counter = 0
    for line in input:
        # split by spaces and organize info into variables
        info = line.split()
        letter = info[1][0]
        password = info[2]
        # split first part of info by - to get positions
        positions = info[0].split("-")
        # organize info into variables
        first_position = int(positions[0])
        second_position = int(positions[1])

        position_counter = 0
        for i in range(len(password)):
            if password[i] == letter and (i == (first_position - 1) or i == (second_position - 1)):
                position_counter += 1
            if position_counter > 1:
                break

        if position_counter == 1:
            valid_counter += 1
            
    print(valid_counter)

main()