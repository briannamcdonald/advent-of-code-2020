def main():
    input = open("day1/input.txt", "r")
    int_input = [int(num) for num in input]
    for num in int_input:
        if (2020 - num) in int_input:
            num2 = 2020 - num
            print(num * num2)
            break

main()