def main():
    data = open("day5/input.txt", "r")
    data = [line.strip() for line in data]

    highest_id = -1
    for line in data:
        seat_id = int(
            line.replace("F", "0")
            .replace("B", "1")
            .replace("L", "0")
            .replace("R", "1"),
            2,
        )
        if seat_id > highest_id:
            highest_id = seat_id
    print(highest_id)


if __name__ == "__main__":
    main()