# ID посылки: 68569931

def broken_search(
        nums: list, target: int, start: [int, None] = None,
        end: [int, None] = None) -> int:
    # задаем границы массива при первом запуске
    if start is None or end is None:
        start, end = 0, len(nums)

    if end - start <= 2:
        # базовый случай рекурсии, если длина массива <= 2
        for index in range(start, end):
            if nums[index] == target:
                return index

        return -1

    # определяем центральный элемент
    mid_index = (start + end) // 2
    mid_element = nums[mid_index]

    # базовые случай рекурсии
    if target == mid_element:
        return mid_index
    if target == nums[start]:
        return start
    if target == nums[end - 1]:
        return end - 1

    if mid_element <= target < nums[end - 1]:
        # если искомое число в правом отрезке
        start = mid_index
    elif nums[0] <= target < mid_element:
        # если искомое число в левом отрезке
        end = mid_index
    elif target < mid_element and target < nums[end - 1]:
        # если искомое число меньше последних элементов обоих отрезков, то
        # определим ближайщий последний элемент отрезка и выберем его
        if mid_element - target < nums[end - 1] - target:
            end = mid_index
        else:
            start = mid_index
    elif target > nums[0] and target > mid_element:
        # если искомое число меньше первых элементов обоих отрезков, то
        # определим ближайщий первый элемент отрезка и выберем его
        if target - nums[0] < target - mid_element:
            end = mid_index
        else:
            start = mid_index

    # запустим поиск значения на новом отрезке
    return broken_search(nums, target, start, end)


def test():
    arr = [8, 10, 0, 2, 4]
    assert broken_search(arr, 4) == 4


if __name__ == '__main__':
    test()
