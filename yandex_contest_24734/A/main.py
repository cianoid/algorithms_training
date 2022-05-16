def gen_binary(n, prefix, max_open_br_count, open_br):
    if n == 0:
        print(prefix)
    else:
        if open_br < max_open_br_count and n > open_br:
            gen_binary(n - 1, prefix + '(', max_open_br_count, open_br + 1)
        if open_br > 0:
            gen_binary(n - 1, prefix + ')', max_open_br_count, open_br - 1)


if __name__ == '__main__':
    variant_count = int(input())

    gen_binary(variant_count * 2, '', variant_count, 0)
