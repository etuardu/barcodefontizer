#!/usr/bin/env python3
"""Utility to translate a EAN-13 code to a printable barcode.

Input: 13 decimal digits string (e.g. '1234567890123')
Output: string (e.g. '*23f5hj#iopqwe*')
    The resulting string can be rendered as a bar code using the barcode font.
Usage (cli):
$ ./barcodefontizer.py 1234567890123
*23f5hj#iopqwe*
Usage (python interpreter):
>>> print(barcodefontizer.code2text('1234567890123'))
*23f5hj#iopqwe*
"""

import sys

sets = {
    "A": "0123456789",
    "B": ";asdfghjkl",
    "C": "pqwertyuio"
}

swing = [
    "AAAAAA",
    "AABABB",
    "AABBAB",
    "AABBBA",
    "ABAABB",
    "ABBAAB",
    "ABBBAA",
    "ABABAB",
    "ABABBA",
    "ABBABA"
]

def code2text(code):
    """EAN-13 to barcode translation.
    
    Input: an EAN-13 code
    output: a string which displays as the bar code when using
    the bar code font.
    """

    myswing = swing[int(code[0])]

    part1 = ""
    for i in range(1, 7):
        part1 += sets[myswing[i-1]][int(code[i])]

    part2 = ""
    for i in range(7, 13):
        part2 += sets["C"][int(code[i])]

    txt = "*" + part1 + "#" + part2 + "*"

    return txt

if __name__ == '__main__':
    print(code2text(sys.argv[1]))
