def main():
    data = open("day1/input.txt", "r")
    int_data = [int(num) for num in data]
    found = False
    for n in int_data:
        for m in int_data:
            if (2020 - n - m) in int_data:
                l = 2020 - n - m
                print(n * m * l)
                found = True
                break
        if found:
            break


if __name__ == "__main__":
    main()