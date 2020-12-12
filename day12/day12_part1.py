def main():
    data = open("day12/input.txt", "r")
    data = [line.strip() for line in data]

    east_west_pos = 0
    north_south_pos = 0
    # ship starts facing east
    current_dir = "E"
    current_dir_index = 1
    dirs = ["N", "E", "S", "W"]
    for line in data:
        direction, value = line[:1], int(line[1 : len(line)])
        if direction == "R":
            current_dir_index = (current_dir_index + (value / 90)) % 4
            current_dir = dirs[current_dir_index]
        elif direction == "L":
            current_dir_index = (current_dir_index - (value / 90)) % 4
            current_dir = dirs[current_dir_index]
        else:
            if direction == "F":
                direction = current_dir
            if direction == "N":
                north_south_pos += value
            elif direction == "S":
                north_south_pos -= value
            elif direction == "E":
                east_west_pos += value
            elif direction == "W":
                east_west_pos -= value
    print(abs(north_south_pos) + abs(east_west_pos))


if __name__ == "__main__":
    main()