#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """a method that determines if a given data set
    represents a valid UTF-8 encoding
    """
    numb_bytes = 0

    num_1 = 1 << 7
    num_2 = 1 << 6

    for i in data:

        num_byte = 1 << 7

        if numb_bytes == 0:

            while num_byte & i:
                numb_bytes += 1
                num_byte = num_byte >> 1

            if numb_bytes == 0:
                continue

            if numb_bytes == 1 or numb_bytes > 4:
                return False

        else:
            if not (i & num_1 and not (i & num_2)):
                return False

        numb_bytes -= 1

    if numb_bytes == 0:
        return True

    return False
