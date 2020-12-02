def main():
    input = open("day1/input.txt", "r")
    int_input = [int(num) for num in input]
    found = False
    for n in int_input:
        for m in int_input:
            if (2020 - n - m) in int_input:
                l = 2020 - n - m
                print(n * m * l)
                found = True
                break
        if found:
            break

main()