def gen_binary(n, prefix):
    if n == 0:
        print(prefix)
    else:
        gen_binary(n - 1, prefix + '0')
        gen_binary(n - 1, prefix + '1')


if __name__ == '__main__':
    variant_count = int(input())

    print(gen_binary(variant_count, ''))

