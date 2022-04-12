def calculate_distances_to_zero_house(street_length, house_numbers):
    distances = []
    last_zero_house_key = -1

    # пройдем по улице слева направо
    for key, house_number in enumerate(house_numbers):
        if house_number > 0:
            # сохраним расстояние
            distances.append(
                key - last_zero_house_key
                if last_zero_house_key >= 0 else None)
            continue

        # если на участке нет дома, сохраним его местоположение
        # в last_zero_house_key и запишем дистанцию
        last_zero_house_key = key
        distances.append(house_number)

        # если предыдущие дом 0, 1, то идем к следующему дому
        if key - 1 >= 0 and distances[key - 1] in [1, 0]:
            continue

        # теперь надо пройти обратно
        for house_left_key in range(key - 1, -1, -1):
            # считаем расстояние от "нуля", оставшегося справа
            house_left_distance = distances[house_left_key]
            distance = key - house_left_key

            # условие, что дом находится уже слишком далеко от правого нуля
            # (левый ближе)
            house_is_toofar = (
                    house_left_distance is not None
                    and distance >= house_left_distance)
            # условие, что мы дошли до нуля
            zero_house_reached = (
                    house_left_distance is not None
                    and house_left_distance == 0)

            # дальше идти нет смысла
            if house_is_toofar or zero_house_reached:
                break

            # сохраним новое расстояние
            distances[house_left_key] = distance

    return distances


if __name__ == '__main__':
    input_street_length = int(input())
    input_house_numbers = list(map(int, input().split()))

    output_distances = calculate_distances_to_zero_house(
        input_street_length, input_house_numbers)

    print(' '.join(list(map(str, output_distances))))
