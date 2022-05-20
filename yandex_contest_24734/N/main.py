def get_total_gardenbeds(gardenbeds):
    gardenbeds = sorted(gardenbeds)

    garden = []

    for start1, end1 in gardenbeds:
        if len(garden) == 0:
            garden.append([start1, end1])
            continue

        index2 = -1
        add = False

        for start2, end2 in garden:
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

    for i in range(inp_gardener_count):
        inp_gardenbeds.append([int(x) for x in input().split()])

    gd = get_total_gardenbeds(inp_gardenbeds)

    for g in gd:
        print(*g)

