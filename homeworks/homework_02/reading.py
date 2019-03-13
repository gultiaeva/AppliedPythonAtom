import json
import csv


DEFAULT_ENCODINGS = ['utf8', 'utf16', 'cp1251']


def define_encoding(filename, enclist=DEFAULT_ENCODINGS):
    for enc in enclist:
        try:
            with open(filename, 'r', encoding=enc) as f:
                # Костыль
                f.readline()
                return enc
        except UnicodeError:
            continue
    return None


def read_file(filename):
    try:
        with open(filename) as f:
            pass
    except FileNotFoundError:
        print("Файл не валиден")
        return None
    if filename:
        enc = define_encoding(filename)
        if not enc:
            print("Формат не валиден")
            return None
        format = get_format(filename, enc)

        if format == 'json':
            data = read_json(filename, enc)
        elif format == 'tsv':
            data = read_tsv(filename, enc)
        else:
            print("Формат не валиден")
            return None

        if any(len(row) != len(data[0]) for row in data):
            print("Формат не валиден")
            return None
    else:
        print("Файл не валиден")
        return None
    return data


def read_tsv(filename, enc):
    with open(filename, 'r', encoding=enc) as tsv:
        head = tsv.readline()
        headers = head.strip().split('\t')
        n_cols = len(headers)
        data = [[header] for header in headers]
        for line in tsv:
            tmp = line.strip().split('\t')
            for i in range(n_cols):
                data[i].append(tmp[i])
    return data


def read_json(filename, enc):
    try:
        with open(filename, 'r', encoding=enc) as f:
            raw_data = json.load(f, object_pairs_hook=dict, parse_int=str)
    except ValueError:
        print("Формат не валиден")
        return None
    except UnicodeDecodeError:
        print("Формат не валиден")
        return None
    head = raw_data[0]
    headers = head.keys()
    data = [[header] for header in headers]
    n_cols = len(head)
    for item in raw_data:
        for i, val in enumerate(item.values()):
            data[i].append(val)

    return data


def is_json(filename, enc):
    try:
        with open(filename, encoding=enc) as f_obj:
            json.load(f_obj)
            return True
    except json.JSONDecodeError:
        return False


def is_tsv(filename, enc):
    try:
        with open(filename, encoding=enc) as f_obj:
            csv.reader(f_obj, delimiter="\t")
            return True
    except csv.Error:
        return False


def get_format(filename, enc):
    if is_json(filename, enc):
        return 'json'
    elif is_tsv(filename, enc):
        return "tsv"
