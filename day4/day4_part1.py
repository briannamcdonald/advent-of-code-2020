def create_dicts(data):
    line_index = 0
    dict_list = []
    new_dict = {}
    while line_index < len(data):
        # get line from the data
        line = data[line_index]
        # split line into a list by whitespace
        line_list = line.split()
        # separate each field from the list into key value pairs and add them to the new dictionary
        for field in line_list:
            (key, value) = field.split(":")
            new_dict[key] = value
        # if this is the blank line that separates passports
        if line_list == []:
            dict_list.append(new_dict)
            new_dict = {}
        line_index += 1
    return dict_list


def has_key(key, d):
    return key in d


def has_correct_keys(d):
    if len(d) == 8:
        return True
    elif len(d) < 7:
        return False
    elif (
        has_key("byr", d)
        and has_key("hgt", d)
        and has_key("ecl", d)
        and has_key("pid", d)
        and has_key("eyr", d)
        and has_key("iyr", d)
        and has_key("hcl", d)
    ):
        return True
    else:
        return False


def main():
    data = open("day4/input.txt", "r")
    data = data.readlines()

    dict_list = create_dicts(data)
    valid_counter = 0
    for d in dict_list:
        if has_correct_keys(d):
            valid_counter += 1
    print(valid_counter)


if __name__ == "__main__":
    main()