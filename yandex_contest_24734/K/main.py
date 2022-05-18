def merge(arr: list, left: int, mid: int, right: int) -> list:
    arr_left = arr[left:mid]
    arr_right = arr[mid:right]

    result = [None] * len(arr)
    counter1, counter2, counter3 = 0, 0, 0

    while counter1 < len(arr_left) and counter2 < len(arr_right):
        if arr_left[counter1] <= arr_right[counter2]:
            result[counter3] = arr_left[counter1]
            counter1 += 1
        else:
            result[counter3] = arr_right[counter2]
            counter2 += 1

        counter3 += 1

    while counter1 < len(arr_left):
        result[counter3] = arr_left[counter1]
        counter1 += 1
        counter3 += 1

    while counter2 < len(arr_right):
        result[counter3] = arr_right[counter2]
        counter2 += 1
        counter3 += 1

    return result


def merge_sort(arr: list, left: int, right: int) -> None:
    pass


def test():
    a = [1, 4, 9, 13, 2, 10, 11]
    b = merge(a, 0, 4, 7)
    expected = [1, 2, 4, 9, 10, 11, 13]
    assert b == expected

    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected


if __name__ == '__main__':
    test()
