def main():
    data = open("day10/input.txt", "r")
    data = [int(line.strip()) for line in data]
    data.sort()

    current_num = 0
    one_diffs = 0
    three_diffs = 1
    highest_val = max(data)
    while True:
        index = 0
        while True:
            val = data[index]
            if val > current_num + 3:
                index += 1
                continue
            elif val - 1 == current_num:
                current_num = val
                one_diffs += 1
                break
            elif val - 2 == current_num:
                current_num = val
                break
            elif val - 3 == current_num:
                current_num = val
                three_diffs += 1
                break
            index += 1
        if current_num == highest_val:
            break
    print(one_diffs * three_diffs)


if __name__ == "__main__":
    main()