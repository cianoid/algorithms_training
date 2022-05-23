# ID посылки:

def effective_quick_sort(participants):
    pass


if __name__ == '__main__':
    inp_participant_count = int(input())
    inp_participants = []

    for i in range(inp_participant_count):
        inp_participants.append(
            tuple([
                int(param) if param.isdigit() else param
                for param in input().split()]))

    effective_quick_sort(inp_participants)
