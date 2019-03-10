def process_data(data):
    data[0].insert(0, 'Название')
    data[1].insert(0, 'Ссылка')
    data[2].insert(0, 'Теги')
    data[3].insert(0, 'Оценка')


def get_full_length(data):
    return (len(max(data[0], key=len)), len(max(data[1], key=len)),
            len(max(data[2], key=len)), len(max(data[3], key=len)))


def pretty_print(data):
    process_data(data)
    lens = get_full_length(data)
    print('-' * (sum(lens) + 21))
    col1, col2, col3, col4 = data
    print(f'|  {col1[0].center(lens[0])}  |  {col2[0].center(lens[1])}  ',
          f'|  {col3[0].center(lens[2])}  |  {col4[0].ljust(lens[3])}  |',
          sep='')

    for c1, c2, c3, c4 in zip(col1[1:], col2[1:], col3[1:], col4[1:]):
        print(f'|  {c1.ljust(lens[0])}  |  {c2.ljust(lens[1])}  |',
              f'  {c3.ljust(lens[2])}  |  {c4.rjust(lens[3])}  |',
              sep='')
    print('-' * (sum(lens) + 21))
