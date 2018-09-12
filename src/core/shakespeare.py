#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import os


class Shakespeare(object):
    ''' Shakespeare translator class '''
    def __init__(self, dictionary=None):
        self.dictionary = dictionary or os.path.abspath(
                          os.path.join(os.path.dirname(__file__), 'dict.db'))
        self.connection = sqlite3.connect(self.dictionary)
        self.connection.execute('PRAGMA case_sensitive_like = OFF;')
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def search(self, word, searchtype=0, exact=False, reverse=False):
        """
        English to spanish
        word = word to search
        searchtype = [startswith, endswith, contains]
        exact = exact search
        reverse = translate from spanish to english
        The query is limited to 200 for performance reasons
        """
        if not word:
            return
        if exact:
            sql_search = u'{}'
        else:
            if searchtype is 0:
                sql_search = u'{}%%' # starts with
            elif searchtype is 1:
                sql_search = u'%%{}' # ends with
            else:
                sql_search = u'%%{}%%' # contains
        sql_search = sql_search.format(word)
        word_a, word_b = ('sword', 'eword') if reverse else ('eword', 'sword')
        search_string = '''select {a}, {b} from dict where {a} like\
        ? order by {a} limit 200'''.format(a=word_a, b=word_b)
        self.cursor.execute(search_string, (sql_search,))
        result = self.cursor.fetchall()
        return result


if __name__ == '__main__':
    s = Shakespeare()
    # first, search for some love :)
    print(s.search('love'))
