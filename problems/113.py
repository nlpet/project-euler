from math import factorial as fc


def choose(n, k):
    return fc(n) / (fc(k) * fc(n - k))


if __name__ == '__main__':
    n = 100
    print "Result: {} non-bouncy nums before 10^{}".format(
        choose(n + 10, 10) + choose(n + 9, 9) - (10 * 100) - 2,
        n
    )
