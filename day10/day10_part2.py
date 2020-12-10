def main():
    data = open("day10/input.txt", "r")
    data = [0] + [int(line.strip()) for line in data]
    data.sort()
    data.append(max(data) + 3)
    length = len(data)

    ways = [0 for i in range(length)]
    ways[0] = 1

    for i in range(1, length):
        for j in range(i - 3, i):
            if data[i] - data[j] <= 3:
                ways[i] += ways[j]
    print(ways[length - 1])


if __name__ == "__main__":
    main()