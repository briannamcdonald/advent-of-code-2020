# finds the last opening bracket in a given expression
def find_last_opening_bracket(expression):
    for i in range(len(expression) - 1, -1, -1):
        if expression[i] == "(":
            return i


# finds the first closing bracket after a given opening bracket in a given expression
def find_first_closing_bracket(expression, opening_index):
    for i in range(opening_index, len(expression)):
        if expression[i] == ")":
            return i


# performs operations, performing addition before multiplication
def evaluate_helper(expression):
    while "+" in expression and "*" in expression:
        add_index = expression.index("+")
        # evaluate addition expression
        value = evaluate_helper(expression[add_index - 1 : add_index + 2])
        # update expression with the evaluated value
        expression = (
            expression[: add_index - 1] + [str(value)] + expression[add_index + 2 :]
        )
    answer = int(expression[0])
    op_list = []
    for char in expression[1:]:
        if char.isdigit():
            char = int(char)
            op = op_list.pop()
            if op == "+":
                answer += char
            elif op == "*":
                answer *= char
        else:
            op_list.append(char)
    return answer


def evaluate(expression):
    while "(" in expression:
        open_bracket = find_last_opening_bracket(expression)
        close_bracket = find_first_closing_bracket(expression, open_bracket)
        # evaluate the expression between the brackets
        value = evaluate_helper(expression[open_bracket + 1 : close_bracket])
        # update the expression with the evaluted value
        expression = (
            expression[:open_bracket] + [str(value)] + expression[close_bracket + 1 :]
        )
    return evaluate_helper(expression)


def main():
    data = open("day18/input.txt", "r")
    data = [line.strip() for line in data]

    answer = 0
    for line in data:
        line = [char for char in line if char != " "]
        answer += evaluate(line)
    print(answer)


if __name__ == "__main__":
    main()