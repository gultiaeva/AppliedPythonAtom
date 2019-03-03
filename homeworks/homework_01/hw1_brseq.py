#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    '''
    Метод проверяющий является ли поданная скобочная
     последовательность правильной (скобки открываются и закрываются)
     не пересекаются
    :param input_string: строка, содержащая 6 типов скобок (,),[,],{,}
    :return: True or False
    '''

    tmp_stack = []
    OPEN_BRACKETS = "[{("
    CLOSE_BRACKETS = "]})"
    for bracket in input_string:
        if bracket in OPEN_BRACKETS:
            tmp_stack.append(bracket)
        elif bracket in CLOSE_BRACKETS:
            try:
                tmp = tmp_stack.pop()
            except IndexError:
                return False
            else:
                if ((tmp, bracket) != ('[', ']') and
                    (tmp, bracket) != ('{', '}') and
                        (tmp, bracket) != ('(', ')')):
                    return False
        else:
            return False

    if len(tmp_stack) == 0:
        return True
    else:
        return False
