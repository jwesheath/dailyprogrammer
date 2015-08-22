import itertools
import time


def check(mark_combo):
    diffs = set()
    for pair in itertools.combinations(mark_combo, 2):
        diff = abs(pair[0] - pair[1])
        if diff in diffs:
            return False
        diffs.add(diff)
    return True


def find(order):
    found = False
    for max_mark in itertools.count(order):
            marks = range(0, max_mark)
            for mark_combo in [x for x in itertools.combinations(marks, order)]:
                if check(mark_combo):
                    found = True
                    print(str(order) + '   ' + str(max(mark_combo)) + '   ' +
                          ' '.join(str(mark) for mark in mark_combo))
            if found:
                return


def main():
    for order in [3, 4, 5, 6, 7, 8]:
        start = time.clock()
        find(order)
        elapsed = time.clock() - start
        print(elapsed)


if __name__ == '__main__':
    main()
