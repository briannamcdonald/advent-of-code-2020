def find_invalid(data):
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
    return answer


def find_weakness(data, invalid_num):
    g_index = 0
    while True:
        new_sum = 0
        new_list = []
        l_index = g_index
        while new_sum < invalid_num:
            new_sum += data[l_index]
            new_list.append(data[l_index])
            l_index += 1
        if new_sum == invalid_num:
            return min(new_list) + max(new_list)
        g_index += 1


def main():
    data = open("day9/input.txt", "r")
    data = [int(line.strip()) for line in data]

    invalid_num = find_invalid(data)
    weakness = find_weakness(data, invalid_num)
    print(weakness)


if __name__ == "__main__":
    main()