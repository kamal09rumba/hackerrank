#!/usr/bin/python
import sys


def plusMinus(arr):
    p = 0
    n = 0
    z = 0
    arr_len = float(len(arr))
    for i in arr:
        if i > 0:
            p += 1
        elif i < 0:
            n += 1
        else:
            z += 1
    fp = float(p) / arr_len
    fn = float(n) / arr_len
    fz = float(z) / arr_len
    print fp, fn, fz
    # print round(fn, 6)


if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    plusMinus(arr)
