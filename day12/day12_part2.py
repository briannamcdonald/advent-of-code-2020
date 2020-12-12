def main():
    data = open("day12/input.txt", "r")
    data = [line.strip() for line in data]

    waypoint_east_west_pos = 10
    waypoint_north_south_pos = 1
    ship_east_west_pos = 0
    ship_north_south_pos = 0
    for line in data:
        direction, value = line[:1], int(line[1 : len(line)])
        if direction == "R":
            if value == 90:
                temp = waypoint_east_west_pos
                waypoint_east_west_pos = waypoint_north_south_pos
                waypoint_north_south_pos = -temp
            elif value == 180:
                waypoint_east_west_pos = -waypoint_east_west_pos
                waypoint_north_south_pos = -waypoint_north_south_pos
            elif value == 270:
                temp = waypoint_east_west_pos
                waypoint_east_west_pos = -waypoint_north_south_pos
                waypoint_north_south_pos = temp
        elif direction == "L":
            if value == 90:
                temp = waypoint_east_west_pos
                waypoint_east_west_pos = -waypoint_north_south_pos
                waypoint_north_south_pos = temp
            elif value == 180:
                waypoint_east_west_pos = -waypoint_east_west_pos
                waypoint_north_south_pos = -waypoint_north_south_pos
            elif value == 270:
                temp = waypoint_east_west_pos
                waypoint_east_west_pos = waypoint_north_south_pos
                waypoint_north_south_pos = -temp
        elif direction == "F":
            ship_east_west_pos += value * waypoint_east_west_pos
            ship_north_south_pos += value * waypoint_north_south_pos
        elif direction == "N":
            waypoint_north_south_pos += value
        elif direction == "S":
            waypoint_north_south_pos -= value
        elif direction == "E":
            waypoint_east_west_pos += value
        elif direction == "W":
            waypoint_east_west_pos -= value
    print(abs(ship_north_south_pos) + abs(ship_east_west_pos))


if __name__ == "__main__":
    main()