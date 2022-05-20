def sort_clothes(clothes_colors):
    elements = {0: 0, 1: 0, 2: 0}

    for element in clothes_colors:
        elements[element] += 1

    return [0] * elements[0] + [1] * elements[1] + [2] * elements[2]


if __name__ == '__main__':
    inp_clothes_count = int(input())
    inp_clothes_colors = [int(x) for x in input().split()]

    print(*sort_clothes(inp_clothes_colors))
