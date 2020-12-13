# reference: https://crypto.stanford.edu/pbc/notes/numbertheory/crt.html


def main():
    data = open("day13/input.txt", "r")
    data = [line.strip() for line in data]
    bus_list = data[1].split(",")

    a_and_m = [
        (int(bus), int(bus) - index) for index, bus in enumerate(bus_list) if bus != "x"
    ]
    M = 1
    for m, a in a_and_m:
        M *= m
    total = 0
    for m, a in a_and_m:
        b = M // m
        b_inverse = b % m
        for x in range(1, m):
            if (b * x) % m == 1:
                b_inverse = x
        total += a * b * b_inverse
    print(total % M)


if __name__ == "__main__":
    main()