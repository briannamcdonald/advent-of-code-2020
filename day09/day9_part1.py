def main():
    data = open("day9/input.txt", "r")
    data = [int(line.strip()) for line in data]

    answer = 0
    for i in range(25, len(data)):
        value = data[i]
        found = False
        spliced_data = data[i - 25 : i]
        for num in spliced_data:
            num2 = value - num
            if num2 in spliced_data and num2 != num and num + num2 == value:
                found = True
        if found == False:
            answer = value
            break
    print(answer)


if __name__ == "__main__":
    main()