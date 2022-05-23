# ID посылки:

def get_element_index(element):
    return tuple([-element[1], element[2], element[0]])


def partition(participants, pivot):
    left = [None] * len(participants)
    center = left.copy()
    right = left.copy()

    len_left = 0
    len_center = 0
    len_right = 0

    pivot_index = get_element_index(pivot)

    for element in participants:
        element_index = get_element_index(element)

        if element_index < pivot_index:
            left[len_left] = element
            len_left += 1
        elif element_index > pivot_index:
            right[len_right] = element
            len_right += 1
        else:
            center[len_center] = element
            len_center += 1

    return left[:len_left], center[:len_center], right[:len_right]


def effective_quick_sort(participants):
    if len(participants) < 2:
        return participants

    pivot = participants[len(participants) // 2]
    left, center, right = partition(participants, pivot)

    return effective_quick_sort(left) + center + effective_quick_sort(right)


if __name__ == '__main__':
    inp_participant_count = int(input())
    inp_participants = []

    for i in range(inp_participant_count):
        inp_participants.append(
            tuple([
                int(param) if param.isdigit() else param
                for param in input().split()]))

    for participant in effective_quick_sort(inp_participants):
        print(participant[0])
