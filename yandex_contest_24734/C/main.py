def is_subsubsequence(s, t):
    if s == '':
        return True

    if t == '':
        return False

    last_index = -1
    len_s = len(s)
    len_t = len(t)
    counter = 0

    for letter in s:
        counter += 1

        prev_index = last_index
        for index in range(last_index + 1, len_t):
            if t[index] == letter:
                if len_s == counter:
                    return True

                last_index = index
                break

        if prev_index == last_index:
            return False

    return False


if __name__ == '__main__':
    inp_s = input()
    inp_t = input()

    print(is_subsubsequence(inp_s, inp_t))
