def get_bigest_number(el1, el2):
    len_el1 = len(el1)
    len_el2 = len(el2)

    if len_el1 == len_el2:
        return int(el1) >= int(el2)
    if el1[0] > el2[0]:
        return True
    if el1[0] < el2[0]:
        return False

    oel1 = el1
    oel2 = el2

    len_delta = abs(len_el1 - len_el2)

    if len_el1 > len_el2:
        for i in range(len_delta):
            el2 += el2[0]
    elif len_el2 > len_el1:
        for i in range(len_delta):
            el1 += el1[0]

    if el1 == el2:
        return int(oel1 + oel2) > int(oel2 + oel1)

    return int(el1) >= int(el2)


def sort_by_number(len_array, array, func):
    for i in range(1, len_array):
        item_to_insert = array[i]
        j = i

        while j > 0 and func(item_to_insert, array[j - 1]):
            array[j] = array[j - 1]
            j -= 1

        array[j] = item_to_insert

    return array


if __name__ == '__main__':
    n = int(input())
    data = input().split()

    print(''.join(sort_by_number(n, data, get_bigest_number)))
