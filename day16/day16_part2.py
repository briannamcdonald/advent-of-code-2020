def get_ranges(data):
    # create a list of all valid ranges
    list_of_ranges = {}
    for line in data:
        if line == "":
            break
        l = []
        key = line.split(":")[0]
        line = line.split()
        lower, upper = line[-1].split("-")
        l.append((int(lower), int(upper)))
        lower, upper = line[-3].split("-")
        l.append((int(lower), int(upper)))
        list_of_ranges[key] = l
    return list_of_ranges


def get_valid_tickets(data, list_of_ranges):
    index = 25
    valid_tickets = []
    while index < len(data):
        ticket = [int(val) for val in data[index].split(",")]
        valid_val_counter = 0
        for val in ticket:
            for r in list_of_ranges.values():
                if (
                    r[0][0] <= val
                    and r[0][1] >= val
                    or r[1][0] <= val
                    and r[1][1] >= val
                ):
                    valid_val_counter += 1
                    break
        if valid_val_counter == len(ticket):
            valid_tickets.append(ticket)
        index += 1
    return valid_tickets


def main():
    data = open("day16/input.txt", "r")
    data = [line.strip() for line in data]

    list_of_ranges = get_ranges(data)
    valid_tickets = get_valid_tickets(data, list_of_ranges)
    my_ticket = [int(val) for val in data[22].split(",")]
    possible_fields = [set() for _ in my_ticket]

    for ticket in valid_tickets:
        for i, val in enumerate(ticket):
            fields = set()
            for item in list_of_ranges:
                r = list_of_ranges.get(item)
                if (
                    r[0][0] <= val
                    and r[0][1] >= val
                    or r[1][0] <= val
                    and r[1][1] >= val
                ):
                    fields.add(item)
            possible_fields[i] = (
                possible_fields[i].intersection(fields)
                if possible_fields[i]
                else fields
            )
    to_remove = []
    field_positions = {}
    while True:
        if len(field_positions) == 20:
            break
        for i, curr_set in enumerate(possible_fields):
            if len(curr_set) == 1:
                field_positions[i] = list(curr_set)[0]
                to_remove.append(list(curr_set)[0])
        for item in to_remove:
            for curr_set in possible_fields:
                if item in curr_set:
                    curr_set.remove(item)
    answer = 1
    for item in field_positions:
        if "departure" in field_positions.get(item):
            answer *= my_ticket[field_positions.keys().index(item)]
    print(answer)


if __name__ == "__main__":
    main()