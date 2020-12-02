def main():
    input = open("day2/input.txt", "r")

    valid_counter = 0
    for line in input:
        # split by spaces and organize info into variables
        info = line.split()
        letter = info[1][0]
        password = info[2]
        # split first part of info by - to get bounds
        bounds = info[0].split("-")
        # organize info into variables
        lower_bound = int(bounds[0])
        upper_bound = int(bounds[1])

        letter_counter = 0
        for i in password:
            if i == letter:
                letter_counter += 1
            if letter_counter > upper_bound:
                break

        if letter_counter >= lower_bound and letter_counter <= upper_bound:
            valid_counter += 1

    print(valid_counter)            

main()