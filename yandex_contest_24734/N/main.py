def get_total_gardenbeds(gardenbeds):
    gardenbeds = sorted(gardenbeds)
    garden = []

    start2, end2 = -1, -1
    for start1, end1 in gardenbeds:
        if start2 == -1:
            start2, end2 = start1, end1
            continue

        if start1 > end2:
            garden.append(tuple([start2, end2]))
            start2, end2 = start1, end1
        elif end1 > end2:
            end2 = end1

    garden.append(tuple([start2, end2]))

    return garden


if __name__ == '__main__':
    inp_gardener_count = int(input())
    inp_gardenbeds = []

    for _no_i in range(inp_gardener_count):
        inp_gardenbeds.append(tuple(int(x) for x in input().split()))

    gd = get_total_gardenbeds(inp_gardenbeds)

    for g in gd:
        print(*g)

