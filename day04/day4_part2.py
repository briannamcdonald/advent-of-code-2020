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


def has_valid_data(d):
    # check birth year
    birth_year = int(d.get("byr"))
    if birth_year < 1920 or birth_year > 2002:
        return False
    # check issue year
    issue_year = int(d.get("iyr"))
    if issue_year < 2010 or issue_year > 2020:
        return False
    # check expiration year
    exp_year = int(d.get("eyr"))
    if exp_year < 2020 or exp_year > 2030:
        return False
    # check height
    height = d.get("hgt")
    height_unit = height[len(height) - 2 : len(height) :]
    height_val = height[0 : len(height) - 2 :]
    if height_val == "":
        return False
    height_val = int(height_val)
    if height_unit != "cm" and height_unit != "in":
        return False
    if height_unit == "cm":
        if height_val < 150 or height_val > 193:
            return False
    elif height_unit == "in":
        if height_val < 59 or height_val > 76:
            return False
    # check hair color
    hair_color = d.get("hcl")
    if hair_color[0] != "#" or len(hair_color) != 7:
        return False
    valid_chars = ["a", "b", "c", "d", "e", "f"]
    for i in range(1, len(hair_color)):
        if hair_color[i] not in valid_chars and not hair_color[i].isdigit():
            return False
    # check eye color
    eye_color = d.get("ecl")
    valid_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if eye_color not in valid_colors:
        return False
    # check passport id
    passport_id = d.get("pid")
    if len(passport_id) != 9 or not passport_id.isdigit():
        return False
    return True


def main():
    data = open("day4/input.txt", "r")
    data = data.readlines()

    dict_list = create_dicts(data)
    # get only passports with the correct keys
    correct_keys_list = []
    for d in dict_list:
        if has_correct_keys(d):
            correct_keys_list.append(d)
    # check how many of them also have valid data
    valid_counter = 0
    for d in correct_keys_list:
        if has_valid_data(d):
            valid_counter += 1
    print(valid_counter)


if __name__ == "__main__":
    main()