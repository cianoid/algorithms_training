def combinations(count, arr, memo, results):
    for i in range(0, count):
        cur = [arr.pop(i)]

        if len(arr) == 0:
            results.append(int(''.join(memo + cur)))

        combinations(count-1, arr, memo + cur, results)
        arr.insert(i, cur[0])

    return results


def big_number(number_count, numbers):
    big_numbers = combinations(number_count, numbers, [], [])

    return max(big_numbers)


if __name__ == '__main__':
    print(big_number(int(input()), input().split()))
