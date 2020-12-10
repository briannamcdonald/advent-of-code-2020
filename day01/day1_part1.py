def main():
    data = open("day1/input.txt", "r")
    int_data = [int(num) for num in data]
    for num in int_data:
        if (2020 - num) in int_data:
            num2 = 2020 - num
            print(num * num2)
            break


if __name__ == "__main__":
    main()