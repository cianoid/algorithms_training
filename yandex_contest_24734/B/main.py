def get_subsequence(numbers, prefix, iteration, result):
    keyboard = {
        2: 'abc',
        3: 'def',
        4: 'ghi',
        5: 'jkl',
        6: 'mno',
        7: 'pqrs',
        8: 'tuv',
        9: 'wxyz'
    }

    if len(numbers) == iteration:
        result.append(prefix)
    else:
        for letter in keyboard[int(numbers[iteration])]:
            get_subsequence(numbers, prefix + letter, iteration + 1, result)

    if iteration == 0:
        return ' '.join(result)


if __name__ == '__main__':
    print(get_subsequence(input(), '', 0, []))
