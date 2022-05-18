def get_total_gardenbeds(gardenbeds):
    pass


if __name__ == '__main__':
    inp_gardener_count = int(input())

    inp_gardenbeds = []

    for i in range(inp_gardener_count):
        inp_gardenbeds.append([int(x) for x in input().split()])

    for rb in get_total_gardenbeds(inp_gardenbeds):
        print(rb)
