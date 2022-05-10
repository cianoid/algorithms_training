import time


def combinations(count, arr, memo, lenarr, maximum):
    for i in range(0, count):
        if arr[i] is not None:

            cur = arr.pop(i)
            lenarr -= 1

            if lenarr == 0:
                x = int(memo + cur)
                if x > maximum:
                    maximum = x

            maximum = combinations(
                count - 1, arr, memo + cur, lenarr, maximum)
            arr.insert(i, cur)
            lenarr += 1

    return maximum


def big_number(number_count, numbers):
    t1 = time.time()
    big_numbers = combinations(number_count, numbers, '', number_count, 0)
    print('Elapsed {}ms'.format(round(1000 * (time.time() - t1))))

    return big_numbers


if __name__ == '__main__':
    print(big_number(int(input()), input().split()))
