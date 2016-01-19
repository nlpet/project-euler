from __future__ import division


def increasing(n):
    strn = str(n)
    for i in range(len(strn) - 1):
        if not strn[i] <= strn[i + 1]:
            return False
    return True


def decreasing(n):
    strn = str(n)
    for i in range(len(strn) - 1):
        if not strn[i] >= strn[i + 1]:
            return False
    return True


def find_bouncy(n, step, goal):
    bouncy = [0] * (n + 1)
    bouncy_so_far = 0
    for i in range(100, n + 1):
        if not (increasing(i) or decreasing(i)):
            bouncy[i] = 1
            bouncy_so_far += 1
        percentage = bouncy_so_far / i
        if i % step == 0:
            print 'Up to %d, bouncy at %.5f' % (i, percentage)
        if percentage == goal:
            print 'Done! Number is %d at %.5f' % (i, percentage)
            break


if __name__ == '__main__':
    n = 2000000
    step = 1000
    find_bouncy(n, step, 0.99)
