def binary_search(arr, price, left, right, other_left=None, other_right=None):
    other_boundaries = other_left is not None and other_right is not None

    if arr[right - 1] < price and other_boundaries:
        return binary_search(arr, price, other_left, other_right)

    if right - left == 1:
        if arr[left] >= price:
            return left + 1

        if arr[left] != price:
            return -1

    mid_idx = (right + left) // 2

    if arr[mid_idx] < price:
        boundaries = [mid_idx, right, left, mid_idx]
    else:
        boundaries = [left, mid_idx, mid_idx, right]

    return binary_search(arr, price, *boundaries)


if __name__ == '__main__':
    days_count = int(input())
    numbers = [int(x) for x in input().split()]
    bike_price = int(input())

    leftb = 0
    rightb = len(numbers)

    print('{} {}'.format(
        binary_search(numbers, bike_price, leftb, rightb),
        binary_search(numbers, bike_price * 2, leftb, rightb)))


