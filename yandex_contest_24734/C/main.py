def is_subsubsequence(s, t):
    if len(s) == 0:
        return True

    if len(t) == 0:
        return False

    counter = 0

    for letter_2 in t:
        if letter_2 == s[counter]:
            counter += 1

            if counter == len(s):
                return True

    return False


if __name__ == '__main__':
    inp_s = input()
    inp_t = input()

    print(is_subsubsequence(inp_s, inp_t))
