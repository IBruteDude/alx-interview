#!/usr/bin/python3
""" Module for defining the UTF-8 encoding validator
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """ Function for validating if a sequence of bytes is valid utf-8
    """
    i = 0
    ln = len(data)
    def utf8_tail(b: int) -> bool: return 0x80 <= b <= 0xBF
    while i < ln:
        if data[i] & 0b10000000 == 0:
            i += 1
        elif data[i] & 0b11100000 == 0b11000000:
            if i + 1 >= ln:
                return False
            if not utf8_tail(data[i + 1]):
                return False
            if not (0xC2 <= data[i] <= 0xDF):
                return False
            i += 2
        elif data[i] & 0b11110000 == 0b11100000:
            if i + 2 >= ln:
                return False
            if not utf8_tail(data[i + 2]):
                return False
            if data[i] == 0xE0:
                if not (0xA0 <= data[i + 1] <= 0xBF):
                    return False
            elif data[i] == 0xED:
                if not (0x80 <= data[i + 1] <= 0x9F):
                    return False
            elif 0xE1 <= data[i] <= 0xEF:
                if not utf8_tail(data[i + 1]):
                    return False
            else:
                return False
            i += 3
        elif data[i] & 0b11111000 == 0b11110000:
            if i + 3 >= ln:
                return False
            if not (utf8_tail(data[i + 2]) and utf8_tail(data[i + 3])):
                return False
            if data[i] == 0xF0:
                if not 0x90 <= data[i + 1] <= 0xBF:
                    return False
            elif data[i] == 0xF4:
                if not 0x80 <= data[i + 1] <= 0x8F:
                    return False
            elif 0xF1 <= data[i] <= 0xF3:
                if not utf8_tail(data[i + 1]):
                    return False
            else:
                return False
            i += 4
    return True


if __name__ == '__main__':
    data = [65]
    print(validUTF8(data))

    data = [80, 121, 116, 104, 111, 110, 32,
            105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data))

    data = [229, 65, 127, 256]
    print(validUTF8(data))
