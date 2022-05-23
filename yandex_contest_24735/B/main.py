# ID посылки: 68565904

def get_element_index(element):
    return [-element[1], element[2], element[0]]


def effective_partition(participants, pivot, len_participants):
    if len_participants == 1:
        return participants

    index_pivot = get_element_index(pivot)

    pointer_left = 0
    pointer_right = len_participants - 1

    while True:
        index_left = get_element_index(participants[pointer_left])
        index_right = get_element_index(participants[pointer_right])

        if index_left < index_pivot:
            pointer_left += 1

        if index_right > index_pivot:
            pointer_right -= 1

        if index_right <= index_pivot <= index_left:
            swap = participants[pointer_right]
            participants[pointer_right] = participants[pointer_left]
            participants[pointer_left] = swap

        if pointer_left >= pointer_right:
            break

    return participants[0:pointer_left], participants[pointer_left:]


def effective_quick_sort(participants):
    len_participants = len(participants)

    if len_participants < 2:
        return participants

    pivot = participants[len_participants // 2]

    left, right = effective_partition(participants, pivot, len_participants)

    return effective_quick_sort(left) + effective_quick_sort(right)


if __name__ == '__main__':
    inp_participant_count = int(input())
    inp_participants = []

    for i in range(inp_participant_count):
        inp_participants.append(
            [int(param) if param.isdigit() else param
             for param in input().split()])

    for participant in effective_quick_sort(inp_participants):
        print(participant[0])
