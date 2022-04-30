def is_correct_bracket_seq(data):
    brackets_dict = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    brackets = []

    if data == '':
        return True

    for bracket in data:
        if bracket in brackets_dict.keys():
            brackets.append(bracket)

        elif bracket in brackets_dict.values():
            try:
                popped_bracket = brackets.pop()
            except IndexError:
                return False

            if brackets_dict[popped_bracket] != bracket:
                return False

    return len(brackets) == 0


if __name__ == '__main__':
    print(is_correct_bracket_seq(input()))
