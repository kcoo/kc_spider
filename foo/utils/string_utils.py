# -*- coding: utf-8 -*-


class StrList(object):
    _str_char = ""

    def __init__(self, str_char):
        self._str_char = str_char

    def get_string(self, n=2):
        if n == 1:
            for tmp_i in self._str_char:
                yield tmp_i
        else:
            for tmp_j in self._str_char:
                for tmp_k in self.get_string(n - 1):
                    yield tmp_j + tmp_k

