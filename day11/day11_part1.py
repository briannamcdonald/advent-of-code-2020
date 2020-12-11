def update_seats(current_data):
    new_data = list(current_data)

    for i in range(0, len(current_data)):
        for j in range(0, len(current_data[i])):
            occupied = 0
            n = len(current_data)
            m = len(current_data[i])

            for k in range(-1, 2):
                for l in range(-1, 2):
                    row = 0
                    col = 0

                    if (i == 0 and k == -1) or (i == n - 1 and k == 1):
                        continue
                    row = i + k

                    if (j == 0 and l == -1) or (j == m - 1 and l == 1):
                        continue
                    col = j + l

                    if current_data[row][col] == "#":
                        occupied += 1

            if current_data[i][j] == "#":
                occupied -= 1
            if current_data[i][j] == "L" and occupied == 0:
                new_data[i] = new_data[i][:j] + "#" + new_data[i][j + 1 :]
            if current_data[i][j] == "#" and occupied >= 4:
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