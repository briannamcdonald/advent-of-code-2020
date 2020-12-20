# returns a list of ending indicies that bound the substrings of the message that match the given rule for a given message and start index
def check_rule(rules, rule_num, message, start):
    rule = rules[rule_num]
    if rule == [['"a"']] or rule == [['"b"']]:
        if start < len(message) and rule[0][0][1] == message[start]:
            return {start + 1}
        else:
            return set()
    else:
        endings = set()
        for subrule in rule:
            buffer = {start}
            for num in subrule:
                temp = set()
                for start_index in buffer:
                    temp = temp.union(check_rule(rules, num, message, start_index))
                buffer = temp
            endings = endings.union(buffer)
        return endings


def main():
    data = open("day19/input.txt", "r")
    data = [line.strip() for line in data]

    # parse rules and store them in a dictionary
    rules = {}
    index = 0
    line = data[index]
    while line != "":
        rule_num, rule_text = line.split(": ")
        content = [rule_seq.split() for rule_seq in rule_text.split(" | ")]
        rules[rule_num] = content
        index += 1
        line = data[index]
    # get message strings
    messages = [line for line in data[index + 1 :]]
    # check if each string matches rule 0
    true_counter = 0
    for message in messages:
        result = len(message) in check_rule(rules, "0", message, 0)
        if result == True:
            true_counter += 1
    print(true_counter)


if __name__ == "__main__":
    main()