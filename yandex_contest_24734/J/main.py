def bubble_sort(array_len, array):
    n = 0

    swap_count = 0
    while n <= array_len:
        swapped = False
        for i in range(0, array_len):
            j = i + 1
            if j == array_len:
                continue

            if array[i] > array[j]:
                item_to_swap = array[j]
                array[j] = array[i]
                array[i] = item_to_swap
                swapped = True
                swap_count += 1

        n += 1

        if swapped:
            print(' '.join(str(elem) for elem in array))

    if swap_count == 0:
        print(' '.join(str(elem) for elem in array))


if __name__ == '__main__':
    bubble_sort(
        int(input()), [int(x) for x in input().split()])
