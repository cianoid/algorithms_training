def get_bigest_number(el1, el2):
    if len(el1) == len(el2):
        return int(el1) >= int(el2)

    if el1[0] > el2[0]:
        return True

    if el1[0] < el2[0]:
        return False

    return int(el1 + el2) > int(el2 + el1)


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
