from reading import *
from printing import *
import sys
import json
import re


def main(filename):
    match = re.fullmatch(r'^.+-(.+)\..+$', filename)
    if not match:
        print("Файл не валиден")
    else:
        encoding = match[1]
        data = read_file(filename, encoding)
        if data:
            pretty_print(data)


if __name__ == "__main__":
    try:
        filename = sys.argv[1]
        main(filename)
    except IndexError:
        print('Файл не валиден')
