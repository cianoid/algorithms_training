if __name__ == '__main__':
    gardener = int(input())

    gardenbed = []

    for i in range(gardener):
        gardenbed.append([int(x) for x in input().split()])

    print(gardenbed)