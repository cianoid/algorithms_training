# ID успешной посылки xxx

def get_points(max_button_count, play_field):
    similar_buttons = dict()
    digits = []
    points = 0

    # вытащить все кнопки в список
    for line in play_field:
        digits += [int(ln) for ln in line if ln != '.']

    # посчитать количество одинаковых кнопок
    for number in digits:
        similar_buttons[number] = similar_buttons.get(number, 0) + 1

    # если оба игрока могут нажать все кнопки, то +1 бал
    for count in similar_buttons.values():
        if count <= max_button_count:
            points += 1

    return points


if __name__ == '__main__':
    input_max_button_count = int(input()) * 2
    input_play_field = []

    for i in range(0, 4):
        input_play_field.append(input())

    print(get_points(input_max_button_count, input_play_field))
