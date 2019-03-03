#!/usr/bin/env python
# coding: utf-8


UNHASHABLE = (list, set)


def unpack(iterable):
    unpacked = []
    for item in iterable:
        if isinstance(item, UNHASHABLE):
            for element in unpack(item):
                unpacked.append(element)
        else:
            unpacked.append(item)
    return unpacked


def invert_dict(input_dict):
    output_dict = {}
    if not input_dict:
        return output_dict
    for k, v in input_dict.items():
        if isinstance(v, UNHASHABLE):
            input_dict[k] = unpack(input_dict[k])
            for item in input_dict[k]:
                if item in output_dict:
                    tmp = [output_dict[item]] if not isinstance(
                        output_dict[item], list) else output_dict[item]
                    tmp.append(k)
                    output_dict[item] = tmp
                else:
                    output_dict[item] = k
        else:
            if v in output_dict:
                tmp = [output_dict[v]] if not isinstance(
                    output_dict[v], list) else output_dict[v]
                tmp.append(k)
                output_dict[v] = tmp
            else:
                output_dict[v] = k

    return output_dict
