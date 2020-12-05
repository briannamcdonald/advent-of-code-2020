def main():
    data = open("day5/input.txt", "r")
    data = [line.strip() for line in data]

    # put all seat ids into a sorted list
    id_list = []
    for line in data:
        seat_id = int(
            line.replace("F", "0")
            .replace("B", "1")
            .replace("L", "0")
            .replace("R", "1"),
            2,
        )
        id_list.append(seat_id)
    id_list.sort()
    # find my seat id by finding the one that is missing
    found = False
    index = 1
    my_id = 0
    while not found:
        if index - 1 < 0 or index + 1 >= len(id_list):
            continue
        if id_list[index] != id_list[index - 1] + 1:
            my_id = id_list[index - 1] + 1
            found = True
        index += 1

    print(my_id)


if __name__ == "__main__":
    main()