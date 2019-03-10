import json


def read_file(filename, enc):
    try:
        return read_json(filename, enc)
    except FileNotFoundError:
        print("Файл не валиден")
    except json.JSONDecodeError:
        try:
            return read_tsv(filename, enc)
        except IndexError:
            print("Формат не валиден")
    return None


def read_tsv(filename, enc):
    with open(filename, 'r', encoding=enc) as tsv:
        data = [[], [], [], []]
        tsv.readline()
        for line in tsv:
            tmp = line.strip().split('\t')
            data[0].append(tmp[0])
            data[1].append(tmp[1])
            data[2].append(tmp[2])
            data[3].append(tmp[3])
    return data


def read_json(filename, enc):
    with open(filename, 'r', encoding=enc) as f:
        raw_data = json.load(f, object_pairs_hook=list, parse_int=str)
    data = [[], [], [], []]
    for item in raw_data:
        data[0].append(item[0][1])
        data[1].append(item[1][1])
        data[2].append(item[2][1])
        data[3].append(item[3][1])
    return data
