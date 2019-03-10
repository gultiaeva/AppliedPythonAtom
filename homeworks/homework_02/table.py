from reading import *
from printing import *
import sys
import json
import re
from collections import OrderedDict


def main(filename):
    match = re.fullmatch(r'^.+-(.+)\..+$', filename)
    encoding= match[1]
    data = read_file(filename, encoding)
    if data:
        pretty_print(data)


if __name__ == "__main__":
    filename = sys.argv[1]
    main(filename)