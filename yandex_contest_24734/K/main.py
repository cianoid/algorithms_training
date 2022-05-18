def merge(arr: list, left: int, mid: int, right: int) -> list:
    result = [None] * (right - left)
    counter1, counter2, counter3 = left, mid, 0

    while counter1 < mid and counter2 < right:
        if arr[counter1] <= arr[counter2]:
            result[counter3] = arr[counter1]
            counter1 += 1
        else:
            result[counter3] = arr[counter2]
            counter2 += 1

        counter3 += 1

    while counter1 < mid:
        result[counter3] = arr[counter1]
        counter1 += 1
        counter3 += 1

    while counter2 < right:
        result[counter3] = arr[counter2]
        counter2 += 1
        counter3 += 1

    return result


def merge_sort(arr: list, left: int, right: int) -> None:
    if len(arr[left:right]) == 1:
        return None

    mid = (left + right) // 2

    merge_sort(arr, left, mid)
    merge_sort(arr, mid, right)

    x = merge(arr, left, mid, right)
    j = 0
    for i in range(left, right):
        arr[i] = x[j]
        j += 1


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
