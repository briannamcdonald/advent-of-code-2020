def create_neighbour_list(x, y, z, w):
    neighbour_list = []
    for x_val in range(x - 1, x + 2):
        for y_val in range(y - 1, y + 2):
            for z_val in range(z - 1, z + 2):
                for w_val in range(w - 1, w + 2):
                    if x_val == x and y_val == y and z_val == z and w_val == w:
                        continue
                    neighbour_list.append((x_val, y_val, z_val, w_val))
    return neighbour_list


def update_space(coord_dict):
    neighbour_dict = {}
    for coord in coord_dict:
        if coord_dict[coord] == "#":
            neighbour_list = create_neighbour_list(
                coord[0], coord[1], coord[2], coord[3]
            )
            for neighbour in neighbour_list:
                try:
                    neighbour_dict[neighbour] += 1
                except:
                    neighbour_dict[neighbour] = 1
    new_space = {}
    active_count = 0
    for coord in neighbour_dict:
        try:
            curr_state = coord_dict[coord]
        except:
            curr_state = "."
        if (
            curr_state == "#"
            and neighbour_dict[coord] != 2
            and neighbour_dict[coord] != 3
        ):
            new_space[coord] = "."
        elif curr_state == "." and neighbour_dict[coord] == 3:
            new_space[coord] = "#"
        else:
            new_space[coord] = curr_state
        if new_space[coord] == "#":
            active_count += 1
    return new_space, active_count


def main():
    data = open("day17/input.txt", "r")
    data = [line.strip() for line in data]

    # set up dictionary
    coord_dict = {}
    y = 0
    z = 0
    w = 0
    for line in data:
        for x, val in enumerate(line):
            coord_dict[(x, y, z, w)] = val
        y += 1
    for cycle in range(6):
        coord_dict, counter = update_space(coord_dict)
    print(counter)


if __name__ == "__main__":
    main()