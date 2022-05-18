def is_subsubsequence(s, t):
    if s == '':
        return True

    if t == '':
        return False

    last_index = -1
    for letter in s:
        try:
            last_index = t.index(letter, last_index + 1)
        except ValueError:
            return False

    return True


if __name__ == '__main__':
    inp_s = input()
    inp_t = input()

    print(is_subsubsequence(inp_s, inp_t))
