def sort_by_number(len_array, array):
    for i in range(1, len_array):
        item_to_insert = array[i]
        j = i

        while j > 0 and item_to_insert < array[j - 1]:
            array[j] = array[j - 1]
            j -= 1

        array[j] = item_to_insert

    return array


def bubble_sort(array_len, array):
    n = 0

    swap_count = 0
    while n <= array_len:
        for i in range(0, array_len):
            j = i + 1
            if j == array_len:
                continue

            if array[i] > array[j]:
                item_to_swap = array[j]
                array[j] = array[i]
                array[i] = item_to_swap
                swap_count += 1

        n += 1

    return array


def merge_sort(array):
    if len(array) == 1:
        return array

    mid = len(array) // 2
    left = merge_sort(array[0:mid])
    right = merge_sort(array[mid:len(array)])

    result = [None] * len(array)

    counter1, counter2, counter3 = 0, 0, 0
    while counter1 < len(left) and counter2 < len(right):
        if left[counter1] <= right[counter2]:
            result[counter3] = left[counter1]
            counter1 += 1
        else:
            result[counter3] = right[counter2]
            counter2 += 1
        counter3 += 1

    while counter1 < len(left):
        result[counter3] = left[counter1]
        counter1 += 1
        counter3 += 1

    while counter2 < len(right):
        result[counter3] = right[counter2]
        counter2 += 1
        counter3 += 1

    return result


def get_total_gardenbeds(gardenbeds, gardener_count):
    # gardenbeds = merge_sort(gardenbeds)
    gardenbeds = sorted(gardenbeds)

    garden = []

    for start1, end1 in gardenbeds:
        if len(garden) == 0:
            garden.append([start1, end1])
            continue

        index2 = -1
        add = False

        for start2, end2 in garden:
            # print(f'{start2}-{end2}')
            index2 += 1
            if start1 <= end2:
                if end1 > end2:
                    garden[index2][1] = end1
                add = False
                break
            else:
                add = True

        if add:
            garden.append([start1, end1])

    return garden


if __name__ == '__main__':
    inp_gardener_count = int(input())
    inp_gardenbeds = []

    for _no_i in range(inp_gardener_count):
        inp_gardenbeds.append([int(x) for x in input().split()])

    gd = get_total_gardenbeds(inp_gardenbeds, inp_gardener_count)

    for g in gd:
        print(*g)

