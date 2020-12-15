def main():
    nums = [0, 13, 16, 17, 1, 10, 6]
    last_said = {}
    counter = 1

    for num in nums:
        last_said[num] = counter
        counter += 1

    next_num = 0
    while counter <= 30000000:
        current_num = next_num
        if not current_num in last_said:
            next_num = 0
        else:
            next_num = counter - last_said[current_num]
        last_said[current_num] = counter
        counter += 1
    print(current_num)


if __name__ == "__main__":
    main()