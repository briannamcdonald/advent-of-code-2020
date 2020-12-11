def find_visible(dir, current_data, row, col):
    current_val = "."
    while current_val == ".":
        if dir == "up":
            row -= 1
        elif dir == "down":
            row += 1
        elif dir == "left":
            col -= 1
        elif dir == "right":
            col += 1
        elif dir == "up-left":
            row -= 1
            col -= 1
        elif dir == "up-right":
            row -= 1
            col += 1
        elif dir == "down-left":
            row += 1
            col -= 1
        elif dir == "down-right":
            row += 1
            col += 1
        if (
            row < 0
            or row >= len(current_data)
            or col < 0
            or col >= len(current_data[row])
        ):
            break
        current_val = current_data[row][col]
    if current_val == "#":
        return 1
    else:
        return 0


def update_seats(current_data):
    new_data = list(current_data)

    for i in range(0, len(current_data)):
        for j in range(0, len(current_data[i])):
            if current_data[i][j] == ".":
                continue
            occupied = 0
            occupied += find_visible("up", current_data, i, j)
            occupied += find_visible("down", current_data, i, j)
            occupied += find_visible("left", current_data, i, j)
            occupied += find_visible("right", current_data, i, j)
            occupied += find_visible("up-left", current_data, i, j)
            occupied += find_visible("up-right", current_data, i, j)
            occupied += find_visible("down-left", current_data, i, j)
            occupied += find_visible("down-right", current_data, i, j)

            if current_data[i][j] == "L" and occupied == 0:
                new_data[i] = new_data[i][:j] + "#" + new_data[i][j + 1 :]
            if current_data[i][j] == "#" and occupied >= 5:
                new_data[i] = new_data[i][:j] + "L" + new_data[i][j + 1 :]
    return new_data


def main():
    data = open("day11/input.txt", "r")
    data = [line.strip() for line in data]

    old_data = data
    new_data = update_seats(data)
    while not old_data == new_data:
        old_data = list(new_data)
        new_data = update_seats(new_data)
    occupied = 0
    for line in new_data:
        occupied += line.count("#")
    print(occupied)


if __name__ == "__main__":
    main()