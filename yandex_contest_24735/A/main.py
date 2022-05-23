# ID посылки:

def broken_search(nums, target, start=None, end=None) -> int:
    if start is None or end is None:
        start, end = 0, len(nums)

    if end - start == 1:
        return 0 if target == nums[start] else -1

    if end - start == 2:
        if nums[start] == target:
            return start
        elif nums[end - 1] == target:
            return end - 1

    mid_index = (start + end) // 2
    mid_element = nums[mid_index]

    if target == mid_element:
        return mid_index

    # print('Checking')
    # print(
    #     f'nums[{start}] = {nums[start]}\n'
    #     f'nums[{mid_index}] = {mid_element}\n'
    #     f'nums[{end - 1}] = {nums[end - 1]}')

    # 9620 <= 25 < 16 or 16 < 25 < 423

    # print(target < mid_element, target < nums[end - 1])

    if mid_element <= target < nums[end - 1]:
        start = mid_index
    elif nums[0] <= target < mid_element:
        end = mid_index
    elif target < mid_element and target < nums[end - 1]:
        if mid_element - target < nums[end - 1] - target:
            end = mid_index
        else:
            start = mid_index
    elif target > nums[0] and target > mid_element:
        if mid_element - nums[0] < target - mid_element:
            end = mid_index
        else:
            start = mid_index
    elif target < mid_element:
        end = mid_index
    else:
        start = mid_index

    # print(f'interval is - {start}:{end}\n')

    return broken_search(nums, target, start, end)


def test():
    # arr = [
    #     3271, 3298, 3331, 3397, 3407, 3524, 3584, 3632, 3734, 3797, 3942, 4000,
    #     4180, 4437, 4464, 4481, 4525, 4608, 4645, 4803, 4804, 4884, 4931, 4965,
    #     5017, 5391, 5453, 5472, 5671, 5681, 5959, 6045, 6058, 6301, 6529, 6621,
    #     6961, 7219, 7291, 7372, 7425, 7517, 7600, 7731, 7827, 7844, 7987, 8158,
    #     8169, 8265, 8353, 8519, 8551, 8588, 8635, 9209, 9301, 9308, 9336, 9375,
    #     9422, 9586, 9620, 9752, 9776, 9845, 9906, 9918, 16, 25, 45, 152, 199,
    #     309, 423, 614, 644, 678, 681, 725, 825, 830, 936, 1110, 1333, 1413,
    #     1617, 1895, 1938, 2107, 2144, 2184, 2490, 2517, 2769, 2897, 2970, 3023,
    #     3112, 3156
    # ]
    arr = [
        8158, 8164, 8228, 8296, 8394, 8426, 8719, 8728, 9182, 9220, 9388, 9453,
        9512, 9544,
        9962, 37, 265, 392, 444, 519, 549, 649, 910, 999, 1056, 1090, 1211,
        1429, 1526, 1628,
        1688, 1694, 1733, 1816, 1994, 2039, 2290, 2335, 2389, 2667, 2690, 2748,
        2799, 2831,
        2905, 2927, 2993, 3033, 3048, 3132, 3166, 3330, 3346, 3417, 3457, 3505,
        3573, 3599,
        3679, 3691, 3839, 4009, 4013, 4151, 4192, 4219, 4305, 4548, 4799, 4862,
        4866, 4869,
        4976, 5190, 5401, 5452, 5477, 5553, 5938, 5945, 6041, 6099, 6132, 6163,
        6437, 6524,
        6780, 6801, 6888, 7101, 7187, 7220, 7228, 7346, 7387, 7546, 7762, 7981,
        7983, 8120,

    ]
    # print(9220)
    print(broken_search(arr, 9220), 9)
    # arr = [
    #     2472, 2473, 2486, 2534, 2628, 2977, 3016, 3155, 3215, 3383, 3522, 3533,
    #     3572, 3599, 3754, 3856, 3888, 3890, 4082, 4130, 4155, 4207, 4555, 4556,
    #     4594, 4597, 4854, 4861, 4948, 5085, 5107, 5251, 5257, 5378, 5408, 5452,
    #     5484, 5584, 5626, 5701, 5760, 5781, 5851, 5855, 6025, 6047, 6133, 6243,
    #     6296, 6314, 6409, 6516, 6521, 6659, 6735, 6813, 6917, 7059, 7120, 7296,
    #     7310, 7345, 7360, 7379, 7425, 7498, 7693, 7925, 7993, 8035, 8165, 8277,
    #     8310, 8363, 8544, 8562, 8774, 8827, 8860, 8952, 9163, 9177, 9255, 9793,
    #     9894, 199, 213, 227, 429, 465, 498, 728, 939, 1502, 1744, 1768, 1821,
    #     2317, 2428, 2471]
    # assert broken_search(arr, 227) == 87
    arr = [12, 41, 122, 411, 412, 1222, 3000, 12222, 122222]
    print(broken_search(arr, 3000), 6)
    # arr = [1]
    # assert broken_search(arr, 1) == 0
    # arr = [1, 2, 3, 5, 6, 7, 9, 0]
    # print(broken_search(arr, 3))
    # arr = [3, 6, 7]
    # print(broken_search(arr, 8))
    # assert broken_search(arr, 2) == 1
    # arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    # assert broken_search(arr, 5) == 6
    # arr = [1, 2, 3, 5, 6, 7, 9, 0]
    # assert broken_search(arr, 3) == 2
    # arr = [1, 5]
    # print(broken_search(arr, 1), 0)


if __name__ == '__main__':
    test()
