#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Latin Search program"""

from __future__ import (print_function, unicode_literals,
                        with_statement)

import os
import sys
# Local zipped libraries
sys.path.insert(0, os.path.join('data', 'lib.zip'))

import re
import time
import urllib
import platform
import requests
from threading import Thread
from bs4 import BeautifulSoup

try:
    import cPickle as pickle
except ImportError:
    import pickle
import string
import collections
from difflib import SequenceMatcher
from multiprocessing import Process

try:
    from prettytable import PrettyTable
except ImportError:
    PrettyTable = None
if sys.version[0] == '2':
    import Tkinter as tk
    import ttk
    import tkFileDialog
    import ScrolledText as st
elif sys.version[0] == '3':
    import tkinter as tk
    from tkinter import ttk
    import tkinter.scrolledtext as st
    from tkinter import filedialog as tkFileDialog

__version__ = "v0.3.1"
__author__ = 'Jin'

_history = []

CURRENT_PLATFORM = platform.system()
WINDOWS_PLATFORM = 'Windows'
LINUX_PLATFORM = 'Linux'
MAC_PLATFORM = 'Darwin'

DATA_FILE = os.path.abspath('data/latin_without_sougou.csv')
PICKLE_KEYS_FILE = os.path.abspath('data/latin_60000.keys.pickle')
PICKLE_DICT_FILE = os.path.abspath('data/latin_60000.dict.pickle')

# 中国植物志网站链接
FRPS_BASE_URL = 'http://frps.eflora.cn/frps/'

# Limit of results for similarity candidate area
SIMILAR_RESULT_NUM_LIMIT = 30

# Similarity threshold for similarity search
SIMILARITY_THRESHOLD = 0.3

# 拉丁名中的特殊字符
SPECIAL_CHARS = ['×', '〔', '）', '【', '】', '', '', '<', '>',
                 '*', '[', '@', ']', '［', '|']

# Two blanks in list are different!!
SPECIAL_CHARS_IN_BAIDU_RESULT = [' ', ' ', '\t']

TRAINED_OBJECT = object()

BAIDU_BAIKE_BASE_URL = 'http://www.baidu.com/s?wd='
WIKIPEDIA_BASE_URL = 'https://zh.wikipedia.org/wiki/'

HEADER = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/44.0.2403.125 Safari/537.36',
          }

TEXT_DICT_EN = {
    'main_window': {
        'geometry': '1400x800',
        'main_title': 'Latin Finder',
    },
    'menu_bar': {
        # File cascade
        'file_cascade': 'File',
        'save': 'Save result to file...',
        'exit': 'Exit',

        # Edit cascade
        'edit_cascade': 'Edit',
        'copy': 'Copy',
        'cut': 'Cut',
        'paste': 'Paste',
        'no_str_in_clipboard_warning': 'No string in clipboard!',
        'delete': 'Delete',

        # Helo cascade
        'help_cascade': 'Help',
        'help': 'Help',
        'about': 'About',
    },
    'config': {
        'config_label': 'Configurations',
        'similarity_search_switch': 'Turn off similarity search',
        'spell_check_switch': 'Turn off spell check',
        'match_whole_word': 'Match whole word',
    },
    'buttons': {
        'search_offline_button': 'Search Offline',
        'search_internet_button': 'Search Internet',
    },
    'labels': {
        # Candidate listbox labels
        'startswith_endswith_label': 'Candidates (Startswith / Endswith)',
        'contains_label': 'Candidates (Contains)',
        'similarity_label': 'Candidates (Rank by similarity)',
        'spell_check_label': 'Candidates (Spell check, single edit distance)',

        # Status label
        'default_status_label': (
            'Click "Do Query" button and see results. '
            '** Double Click ** candidate to see detailed result.'),
    },
    'info_text': {
        'blank_query_label': 'Blank query !!',
        'searching_baidu_baike': 'Searching Baidu Baike! Please wait...',
        'searching_wikipedia': 'Searching Wikipedia! Please wait...',

        'start_searching': 'Start searching! Please wait...',
        'search_complete': 'Search complete!',
        'start_offline_search': (
            'Start searching offline data. Please wait...'),
        'offline_search_complete_1': (
            'Baidu Baike searching complete! Time used:'),
        'offline_search_complete_2': (
            '. Double click candidate words to see detailed information'),

        # Baidu baike
        'baike_result_info': 'Baidu Baike:',
        'baike_search_complete': 'Baidu Baike searching complete! Time used:',
        'baike_no_result': 'No result from Baidu Baike!',

        # Wikipedia
        'wikipedia_result_info': 'Wikipedia:',
        'wikipedia_search_complete': 'Wikipedia searching complete! Time used:',
        'wikipedia_no_result': 'No result from Wikipedia!',

        'pretty_table_install_info': (
            'Please install "prettytable" to get nicer result.'
            '\nHow to install: '),

        # Baidu Baike result (prettytable header line)
        'baidu_result_attr': 'Attribute',
        'baidu_result_value': 'Value',
    },
    'right_click_menu': {
        'copy': 'Copy',
        'cut': 'Cut',
        'paste': 'Paste',
        'delete': 'Delete',
        'select_all': 'Select All',
    },
    'right_click_menu_listbox': {
        'copy': 'Copy',
    },
    'right_click_menu_st': {
        'copy': 'Copy',
        'cut': 'Cut',
        'paste': 'Paste',
        'delete': 'Delete',
        'select_all': 'Select All',
        'clear_all': 'Clear All',
    }
}

TEXT_DICT_CN = {
    'main_window': {
        'geometry': '1400x800',
        'main_title': '拉丁名搜索（Latin Finder）',
    },
    'menu_bar': {
        # File cascade
        'file_cascade': '文件',
        'save': '结果另存为...',
        'exit': '退出',

        # Edit cascade
        'edit_cascade': '编辑',
        'copy': '复制',
        'cut': '剪切',
        'paste': '粘贴',
        'no_str_in_clipboard_warning': '剪切板中无可粘贴的内容！',
        'delete': '删除',

        # Helo cascade
        'help_cascade': '帮助',
        'help': '帮助信息',
        'about': '关于',
    },
    'config': {
        'config_label': '配置区域',
        'similarity_search_switch': '关闭相似值搜索',
        'spell_check_switch': '关闭拼写检查',
        'match_whole_word': '全字匹配',
    },
    'buttons': {
        'search_offline_button': '搜索离线数据',
        'search_internet_button': '网络搜索',
    },
    'labels': {
        # Candidate listbox labels
        'startswith_endswith_label': '候选词（起始/结尾）',
        'contains_label': '候选词（包括）',
        'similarity_label': '候选词（相似度搜索）',
        'spell_check_label': '候选词（拼写检查）',

        # Status label
        'default_status_label': (
            '提示：1. 搜索离线数据后，双击上方的某个候选词，以查看对应的离线信息。  '
            '2. 离线搜索 / 网络搜索默认均开启模糊搜索。  '
            '3. 使用精确的搜索词可大幅提升搜索速度。'
        ),
    },
    'info_text': {
        'blank_query_label': '空的查询',
        'searching_baidu_baike': '正在搜索百度百科，请稍候...',
        'searching_wikipedia': '正在搜索维基百科，请稍候...',

        'start_searching': '开始搜索，请耐性等待...',
        'search_complete': '搜索完成！',
        'start_offline_search': '开始搜索离线数据，请稍候...',
        'offline_search_complete_1': '离线数据搜索完成！用时：',
        'offline_search_complete_2': '。双击候选词以查看详细信息',

        # Baidu baike
        'baike_result_info': '百度百科：',
        'baike_search_complete': '百度百科搜索完成！用时：',
        'baike_no_result': '查询百度百科未找到结果！',

        # Wikipedia
        'wikipedia_result_info': '维基百科：',
        'wikipedia_search_complete': '维基百科搜索完成！用时：',
        'wikipedia_no_result': '查询维基百科未找到结果！',

        'pretty_table_install_info': (
            '请安装 prettytable 以获得更清晰的结果视图。\n安装方法：'),

        # Baidu Baike result (prettytable header line)
        'baidu_result_attr': '属性',
        'baidu_result_value': '搜索结果',
    },
    'right_click_menu': {
        'copy': '复制',
        'cut': '剪切',
        'paste': '粘贴',
        'delete': '删除',
        'select_all': '全部选择',
    },
    'right_click_menu_listbox': {
        'copy': '复制',
    },
    'right_click_menu_st': {
        'copy': '复制',
        'cut': '剪切',
        'paste': '粘贴',
        'delete': '删除',
        'select_all': '全部选择',
        'clear_all': '清空',
    }
}

CURRENT_TEXT_DICT = TEXT_DICT_CN

USAGE_INFO = """
植物拉丁名搜索（Latin Namer Finer）

[介绍]

    根据植物拼音缩写、拼音、中文名称或者拉丁名搜索植物其他信息。

    得到候选词后，*双击* 候选词，将得到详细信息。如果没有匹配，将会使用糢糊搜索。

[版本]

    %s

[使用方法]

    1. 使用拼音首字母搜索。例如搜索 “eqxlm”，将会得到 “二球悬铃木”
       及其他悬铃木相关的结果。
    2. 使用拼音全称搜索。例如搜索 “erqiuxuanlingmu”，将会得到 “二球悬铃木”
       及其他悬铃木相关的结果。
    3. 使用中文搜索。例如搜索 “悬铃木”，将会得到 “二球悬铃木”， “三球悬铃木”
       等相关搜索结果。
    4. 使用拉丁名搜索。例如搜索 “Platanus × acerifolia”，将会得到 “二球悬铃木”
       相关的结果。

[候选词介绍]

    +---+------------------------+
    | 1 | 候选词以查询词开始或结尾
    |---+------------------------+
    | 2 | 候选词包含查询词
    |---+------------------------+
    | 3 | 根据相似性进行糢糊搜索
    |---+------------------------+
    | 4 | 拼写检查（编辑距离为 1)
    +---+------------------------+

""" % __version__

ABOUT_INFO = """
============================================================
软件名称：植物拉丁名搜索（Latin Namer Finer）
软件版本：%s
软件作者：%s
使用方法：请点击菜单栏中 "Help" - "Help" 以查看使用方式。
============================================================
""" % (__version__, __author__)


def get_lines(file_name):
    """Read file and return a list of lines."""
    with open(file_name, 'r') as f_in:
        return f_in.readlines()


def get_key_value_pairs_from_file(file_name):
    """
    File:
        +-----+-------+------+----------------------+-------+
        | mg  | mugua | 木瓜 | Chaenomeles sinensis | Lynn. |
        +-----+-------+--- --+----------------------+-------+

    Processing:

        dict_1: {'mg': ('mg', 'mugua', '木瓜', 'Chaenomeles sinensis', '')}
        dict_2: {'mugua': ('mg', 'mugua', '木瓜', 'Chaenomeles sinensis', '')}
        dict_3: {'木瓜': ('mg', 'mugua', '木瓜', 'Chaenomeles sinensis', '')}
        dict_4: {'Chaenomeles sinensis': ('mg', 'mugua',
                                          '木瓜', 'Chaenomeles sinensis', '')}

    Returns:
        (dict_1, dict_2, dict_3, dict_4)
    """
    column_list_1, column_list_2, column_list_3, column_list_4 = [], [], [], []
    detailed_info_tuple_list = []
    with open(file_name, 'r') as f_in:
        for line in f_in:
            if sys.version[0] == '2':
                line = line.decode('utf-8')
            elements = [x.strip() for x in line.split(',')]
            column_list_1.append(elements[0])
            column_list_2.append(elements[1])
            column_list_3.append(elements[2])
            column_list_4.append(elements[3])
            detailed_info_tuple_list.append(tuple(elements))

    return (column_list_1, column_list_2, column_list_3,
            column_list_4, detailed_info_tuple_list)


def get_one_to_more_dict(key_list, value_list):
    """
    Generate a dictionary from two lists. keys may be duplicated.

    >>> get_one_to_more_dict(['a', 'b', 'a', 'a'], [1, 2, 3, 4])
    {'a': [1, 3, 4], 'b': [2]}
    """
    _out_dict = {}
    for i, (key, value) in enumerate(zip(key_list, value_list)):
        if key not in _out_dict:
            _out_dict[key] = []
            _out_dict[key].append(value)
        else:
            _out_dict[key].append(value)

    return _out_dict


def get_dict_for_all_columns():
    """Combine dicts, each with one column as key and whole line as value."""
    (column_list_1, column_list_2, column_list_3,
     column_list_4, detailed_info_tuple_list) = \
        get_key_value_pairs_from_file(DATA_FILE)
    dict_1 = get_one_to_more_dict(column_list_1, detailed_info_tuple_list)
    dict_2 = get_one_to_more_dict(column_list_2, detailed_info_tuple_list)
    dict_3 = get_one_to_more_dict(column_list_3, detailed_info_tuple_list)
    dict_4 = get_one_to_more_dict(column_list_4, detailed_info_tuple_list)

    # Merge all dicts to a single dict
    for each_dict in (dict_2, dict_3, dict_4):
        if each_dict:
            dict_1.update(each_dict)

    keys_for_all = list(set(column_list_1 + column_list_2 +
                            column_list_3 + column_list_4))

    return keys_for_all, dict_1


# ============================================================================
# Utils Part
# ============================================================================

def get_similarity(str_a, str_b):
    """Return similarity of two strings.

    [Example]
        >>> get_similarity('abcde', 'bcdef')
        0.8
    """
    return SequenceMatcher(None, str_a, str_b).ratio()


# ============================================================================
# Query Part
# ============================================================================

class SpellCheck(object):
    """Train data set with given data then do spell check for given word.

    [Example]
        >>> s = SpellCheck(['abcd', 'fghi'])
        >>> s.correct('abci')
        'abcd'

    [Reference]
        [1]: Title:   How to Write a Spelling Corrector
             Author:  Peter Norvig
             Webpage: http://norvig.com/spell-correct.html
    """

    def __init__(self, candidate_list):
        self.candidate_list = candidate_list
        self.NWORDS = self.train()
        self.NWORDS_lower = self.train(lower=True)
        self.alphabet = ('abcdefghijklmnopqrstuvwxyz'
                         'ABCDEFGHIJKLMNOPQRSTUVWXYZ_-.:1234567890')

    def train(self, lower=False):
        """Train model with data set."""
        if not self.candidate_list:
            raise ValueError('Blank training list (Choosed blank file?).')
        model = collections.defaultdict(lambda: 1)
        if not lower:
            for f in self.candidate_list:
                model[f] += 1
        else:
            tmp_list = self.candidate_list[:]
            for f in map(lambda _: _.lower(), tmp_list):
                model[f] += 1
        return model

    def edits1(self, word):
        """Words that has one edit distance.

        1. deletion
        2. transposition
        3. alteration
        4. insertion
        """
        n = len(word)
        return set(
            [word[0:i] + word[i + 1:] for i in range(n)] +  # deletion
            # transposition
            [word[0:i] + word[i + 1] + word[i] + word[i + 2:] for i in range(n - 1)] +
            # alteration
            [word[0:i] + c + word[i + 1:] for i in range(n) for c in self.alphabet] +
            # insertion
            [word[0:i] + c + word[i:] for i in range(n + 1) for c in self.alphabet])

    def known_edits2(self, word):
        """Words that has two edit distance."""
        return set(e2 for e1 in self.edits1(word) for e2 in self.edits1(e1)
                   if e2.lower() in self.NWORDS_lower)

    def known(self, words):
        """Known words."""
        return set(w for w in words if w.lower() in self.NWORDS_lower)

    def correct(self, word):
        """Do spell check and correct word if word was wrong spelled"""
        # Edit 1 and Edit 2 (Low performance, but better accuracy)
        # candidates = (self.known([word]) or self.known(self.edits1(word))
        #               or self.known_edits2(word) or [word])

        # Only Edit 1 (For better performance)
        candidates = (self.known([word]) or self.known(self.edits1(word))
                      or [word])

        return max(candidates, key=lambda w: self.NWORDS_lower[w])


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Query class for easy organizing
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class QueryWord(object):
    """Query with 4 strategy with multi-processing.

    [Strategies]

        1. Starts with              'abcde'.startswith('abc')
        2. Contains                 'bcd' in 'abcde'
        3. Rank by Similarity
        4. Spell check

    [turn_on_mode]

        Default: (True, True, True, True)
            Return all 4 results.

        (True, True, False, False)
            Return results of strategy_1 and strategy_2, and blank result
            of strategy_3 and strategy_4

    [Usage]

        query_object = QueryWord(keys_for_all, dict_for_all)

        # Startswith
        # query_object.get_starts_with_candidates(query)
        # Contains
        # query_object.get_contains_candidates(query)
        # Similarity
        # query_object.get_similar_candidates(query, limit=30)
        # Spell Check
        # query_object.get_spell_check_candidate(query)
        # All Four

        query_object.query_all_four(
            query,
            turn_on_mode=(True, True, True, True))
    """

    def __init__(self, keys_for_all, dict_for_all):
        self.keys_for_all = [x.strip() for x in keys_for_all
                             if x.strip()]
        self.dict_for_all = dict_for_all
        self.trained_object = SpellCheck(keys_for_all)
        self.query = ''
        self.result_dict = {}

    # --------------------------------------------------------
    # 1:  Startswith or Endswith Check
    # --------------------------------------------------------
    @staticmethod
    def get_starts_with_candidates(query, keys_for_all, dict_for_all,
                                   result_dict, match_whole_word=False,
                                   turn_on=True):
        """Check startswith & endswith"""
        _tmp_list = []
        if turn_on:
            # Check totally match. Totally matched result should be on top
            if query in keys_for_all:
                _tmp_list.append(query)
                if match_whole_word:
                    result_dict.update({'0': _tmp_list})
                    return
                result_elements = dict_for_all.get(query)[0]
                for each in result_elements[:4]:
                    if each.strip() and each != query:
                        _tmp_list.append(each)
            # Check partially match
            for i, candidate in enumerate(keys_for_all):
                if candidate.startswith(query) or \
                        candidate.endswith(query):
                    if candidate != query:
                        _tmp_list.append(candidate)

        result_dict.update({'0': _tmp_list})

    # --------------------------------------------------------
    # 2:  Contains Check
    # --------------------------------------------------------
    @staticmethod
    def get_contains_candidates(query, keys_for_all, dict_for_all,
                                result_dict, match_whole_word=False,
                                turn_on=True):
        """Check contains"""
        _tmp_list = []
        if turn_on:
            # Check totally match. Totally matched result should be on top
            if query in keys_for_all:
                _tmp_list.append(query)
                if match_whole_word:
                    result_dict.update({'1': _tmp_list})
                    return
                result_elements = dict_for_all.get(query)[0]
                for each in result_elements[:4]:
                    if each.strip() and each != query:
                        _tmp_list.append(each)
            # Check partially match
            for i, candidate in enumerate(keys_for_all):
                if query in candidate:
                    if candidate != query:
                        _tmp_list.append(candidate)

        result_dict.update({'1': _tmp_list})

    # --------------------------------------------------------
    # 3:  Similarity Check
    # --------------------------------------------------------
    @staticmethod
    def get_similar_candidates(query, keys_for_all, dict_for_all,
                               result_dict, match_whole_word=False,
                               turn_on=True):
        """Rank candidates by similarity"""
        _tmp_list = []
        _similar_hits = []
        # If strategy 2 (contains search) got a result, similarity search
        # will skip for performance reason
        if match_whole_word:
            result_dict.update({'2': []})
            return
        if turn_on and len(result_dict.get('1')) == 0:
            for i, candidate in enumerate(keys_for_all):
                _similarity = get_similarity(candidate, query)
                if _similarity > SIMILARITY_THRESHOLD:
                    _tmp_list.append((_similarity, candidate))
            _tmp_list.sort(key=lambda x: x[0], reverse=True)
            _tmp_list = _tmp_list[:SIMILAR_RESULT_NUM_LIMIT]
            _similar_hits = [_[1] for _ in _tmp_list] if _tmp_list else []
            # _similar_hits = ['%.4f  %s' % _ for _ in _tmp_list]

        result_dict.update({'2': _similar_hits})

    # --------------------------------------------------------
    # 4:  Advanced Spell Check
    # --------------------------------------------------------
    @staticmethod
    def get_spell_check_candidate(query, keys_for_all, dict_for_all,
                                  result_dict, match_whole_word=False,
                                  turn_on=True):
        """Get spell check candicates"""
        candidate = ''
        if match_whole_word:
            result_dict.update({'3': ''})
            return
        if turn_on and len(result_dict.get('1')) == 0:
            candidate = TRAINED_OBJECT.correct(query)

        result_dict.update({'3': candidate})

    def query_all_four(self, query, match_whole_word, turn_on_mode):
        """Get four results"""
        # Reset self.query to the value of parameter query
        self.query = query
        result_dict = {}

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # Single process
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # for i, each_func in enumerate(func_list):
        #     each_func(turn_on_mode[i])

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # Multi-processing
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # startswith/endswith and contains
        func_list_1 = [QueryWord.get_starts_with_candidates,
                       QueryWord.get_contains_candidates]
        # similarity and spell check
        func_list_2 = [QueryWord.get_similar_candidates,
                       QueryWord.get_spell_check_candidate]

        for i, each_func in enumerate(func_list_1):
            p = Process(target=each_func(self.query, self.keys_for_all,
                                         self.dict_for_all, result_dict,
                                         match_whole_word, turn_on_mode[i]))
            p.start()

        # If "contains search" got results, similarity search & spell check
        # will not be performed for performance reason
        for i, each_func in enumerate(func_list_2):
            p = Process(target=each_func(self.query, self.keys_for_all,
                                         self.dict_for_all, result_dict,
                                         match_whole_word, turn_on_mode[i + 2]))
            p.start()

        return result_dict


class InternetQuery(object):
    @staticmethod
    def search_baidu_baike(keyword):
        """Search baidu and retrive content from first baike URL"""
        url = BAIDU_BAIKE_BASE_URL + urllib.quote(keyword.encode('GBK'))
        session = requests.session()
        req = session.get(url, headers=HEADER)
        req.encoding = 'utf-8'
        soup = BeautifulSoup(req.text, "html.parser")
        outcomes = soup.findAll('h3', {'class': 'c-gap-bottom-small'})
        first_baike_url = outcomes[0].find(href=True).get('href')

        req = session.get(first_baike_url, headers=HEADER)
        req.encoding = 'utf-8'
        soup = BeautifulSoup(req.text, "html.parser")
        main_content = soup.find('div', {'class': 'basic-info cmn-clearfix'})
        re_newline = re.compile(r'[^\n]+')
        if main_content:
            out_list = re_newline.findall(main_content.text)
            return '\n'.join(out_list)
        return ''

    @staticmethod
    def prettify_baike_result(baike_result):
        out_list = []
        lines = [x.strip() for x in baike_result.splitlines() if x.strip()]
        if PrettyTable:
            table = PrettyTable([
                CURRENT_TEXT_DICT.get('info_text').get('baidu_result_attr'),
                CURRENT_TEXT_DICT.get('info_text').get('baidu_result_value')])
            for column in (
                CURRENT_TEXT_DICT.get('info_text').get('baidu_result_attr'),
                CURRENT_TEXT_DICT.get('info_text').get('baidu_result_value')
            ):
                table.align[column] = "l"
            table.padding_width = 1
            list_for_each_line = []
            for i, line in enumerate(lines):
                if i % 2 == 0:
                    for each_char in SPECIAL_CHARS_IN_BAIDU_RESULT:
                        line = line.replace(each_char, '')
                    list_for_each_line.append(line)
                else:
                    list_for_each_line.append(line)
                    table.add_row(list_for_each_line)
                    list_for_each_line = []
            return table.get_string()
        else:
            temp_str = ''
            for i, line in enumerate(lines):
                if i % 2 == 0:
                    temp_str = line.replace(' ', '')
                else:
                    temp_str = temp_str + '\t\t| ' + line
                    out_list.append(temp_str)
            return '\n'.join(out_list)

    @staticmethod
    def search_wikipedia(keyword):
        """Search glossary from Wikipedia."""
        out_list = []
        url = WIKIPEDIA_BASE_URL + \
              urllib.quote(keyword.replace(' ', '_').encode('GBK'))
        session = requests.session()
        req = session.get(url, headers=HEADER)
        soup = BeautifulSoup(req.text, 'html.parser')
        out = soup.find('table', {'class': 'infobox biota'})
        if not out:
            return ''
        td_out = out.find_all('td')
        for each in td_out:
            if each:
                out_list.append(each.text.strip().replace('\n', ' '))
        return '\n'.join(out_list)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Right Menu
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class RightClickMenu(object):
    """
    Simple widget to add basic right click menus to entry widgets.

    usage:

    rclickmenu = RightClickMenu(some_entry_widget)
    some_entry_widget.bind("<3>", rclickmenu)

    If you prefer to import Tkinter over Tix, just replace all Tix
    references with Tkinter and this will still work fine.
    """

    def __init__(self, parent):
        self.parent = parent
        # bind Control-A to select_all() to the widget.  All other
        # accelerators seem to work fine without binding such as
        # Ctrl-V, Ctrl-X, Ctrl-C etc.  Ctrl-A was the only one I had
        # issue with.
        self.parent.bind("<Control-a>", lambda e: self._select_all(), add='+')
        self.parent.bind("<Control-A>", lambda e: self._select_all(), add='+')

    def __call__(self, event):
        # if the entry widget is disabled do nothing.
        if self.parent.cget('state') == 'disable':
            return
        # grab focus of the entry widget.  this way you can see
        # the cursor and any marking selections
        self.parent.focus_force()
        self.build_menu(event)

    def build_menu(self, event):
        """Build right click menu"""
        menu = tk.Menu(self.parent, tearoff=0)
        # check to see if there is any marked text in the entry widget.
        # if not then Cut and Copy are disabled.
        if not self.parent.selection_present():
            menu.add_command(
                label=CURRENT_TEXT_DICT.get('right_click_menu').get('copy'),
                state='disable')
            menu.add_command(
                label=CURRENT_TEXT_DICT.get('right_click_menu').get('cut'),
                state='disable')
        else:
            # use Tkinter's virtual events for brevity.  These could
            # be hardcoded with our own functions to immitate the same
            # actions but there's no point except as a novice exercise
            # (which I recommend if you're a novice).
            menu.add_command(
                label=CURRENT_TEXT_DICT.get('right_click_menu').get('copy'),
                command=self._copy)
            menu.add_command(
                label=CURRENT_TEXT_DICT.get('right_click_menu').get('cut'),
                command=self._cut)
        # if there's string data in the clipboard then make the normal
        # Paste command.  otherwise disable it.
        if self.paste_string_state():
            menu.add_command(
                label=CURRENT_TEXT_DICT.get('right_click_menu').get('paste'),
                command=self._paste)
        else:
            menu.add_command(
                label=CURRENT_TEXT_DICT.get('right_click_menu').get('paste'),
                state='disable')
        # again, if there's no marked text then the Delete option is disabled.
        if not self.parent.selection_present():
            menu.add_command(
                label=CURRENT_TEXT_DICT.get('right_click_menu').get('delete'),
                state='disable')
        else:
            menu.add_command(
                label=CURRENT_TEXT_DICT.get('right_click_menu').get('delete'),
                command=self._clear)
        # make things pretty with a horizontal separator
        menu.add_separator()
        # I don't know of if there's a virtual event for select all though
        # I did look in vain for documentation on -any- of Tkinter's
        # virtual events.  Regardless, the method itself is trivial.
        menu.add_command(
            label=CURRENT_TEXT_DICT.get('right_click_menu').get('select_all'),
            command=self._select_all)
        menu.post(event.x_root, event.y_root)

    def _cut(self):
        self.parent.event_generate("<<Cut>>")

    def _copy(self):
        self.parent.event_generate("<<Copy>>")

    def _paste(self):
        self.parent.event_generate("<<Paste>>")

    def _clear(self):
        self.parent.event_generate("<<Clear>>")

    def _select_all(self):
        self.parent.selection_range(0, 'end')
        self.parent.icursor('end')
        # return 'break' because, for some reason, Control-a (little 'a')
        # doesn't work otherwise.  There's some natural binding that
        # Tkinter entry widgets want to do that send the cursor to Home
        # and deselects.
        return 'break'

    def paste_string_state(self):
        """Returns true if a string is in the clipboard"""
        try:
            # this assignment will raise an exception if the data
            # in the clipboard isn't a string (such as a picture).
            # in which case we want to know about it so that the Paste
            # option can be appropriately set normal or disabled.
            clipboard = self.parent.selection_get(selection='CLIPBOARD')
        except:
            return False
        return True


class RightClickMenuForListBox(object):
    """
    Simple widget to add basic right click menus to entry widgets.

    usage:

    rclickmenu = RightClickMenuForListBox(listbox_widget)
    listbox_widget.bind("<3>", rclickmenu)

    If you prefer to import Tkinter over Tix, just replace all Tix
    references with Tkinter and this will still work fine.
    """

    def __init__(self, parent):
        self.parent = parent

    def __call__(self, event):
        # if the entry widget is disabled do nothing.
        if self.parent.cget('state') == 'disable':
            return
        # grab focus of the entry widget.  this way you can see
        # the cursor and any marking selections
        self.parent.focus_force()
        self.build_menu(event)

    def build_menu(self, event):
        """Build right click menu"""
        menu = tk.Menu(self.parent, tearoff=0)
        menu.add_command(
            label=CURRENT_TEXT_DICT.get(
                'right_click_menu_listbox').get('copy'),
            command=self._copy)
        menu.post(event.x_root, event.y_root)

    def _copy(self):
        self.parent.event_generate("<<Copy>>")


class RightClickMenuForScrolledText(object):
    """Simple widget to add basic right click menus to entry widgets."""

    def __init__(self, parent):
        self.parent = parent
        # bind Control-A to select_all() to the widget.  All other
        # accelerators seem to work fine without binding such as
        # Ctrl-V, Ctrl-X, Ctrl-C etc.  Ctrl-A was the only one I had
        # issue with.
        self.parent.bind("<Control-a>", lambda e: self._select_all(), add='+')
        self.parent.bind("<Control-A>", lambda e: self._select_all(), add='+')

    def __call__(self, event):
        # if the entry widget is disabled do nothing.
        if self.parent.cget('state') == tk.DISABLED:
            return
        # grab focus of the entry widget.  this way you can see
        # the cursor and any marking selections
        self.parent.focus_force()
        self.build_menu(event)

    def build_menu(self, event):
        """build menu"""
        menu = tk.Menu(self.parent, tearoff=0)
        # check to see if there is any marked text in the entry widget.
        # if not then Cut and Copy are disabled.
        # if not self.parent.selection_get():
        #     menu.add_command(label="Cut", state=tk.DISABLED)
        #     menu.add_command(label="Copy", state=tk.DISABLED)
        # else:
        # use Tkinter's virtual events for brevity.  These could
        # be hardcoded with our own functions to immitate the same
        # actions but there's no point except as a novice exercise
        # (which I recommend if you're a novice).
        menu.add_command(
            label=CURRENT_TEXT_DICT.get('right_click_menu_st').get('copy'),
            command=self._copy)
        menu.add_command(
            label=CURRENT_TEXT_DICT.get('right_click_menu_st').get('cut'),
            command=self._cut)
        # if there's string data in the clipboard then make the normal
        # Paste command.  otherwise disable it.
        if self._paste_string_state():
            menu.add_command(
                label=CURRENT_TEXT_DICT.get(
                    'right_click_menu_st').get('paste'),
                command=self._paste_if_string_in_clipboard)
        else:
            menu.add_command(
                label=CURRENT_TEXT_DICT.get(
                    'right_click_menu_st').get('paste'),
                state='disable')
        # again, if there's no marked text then the Delete option is disabled.
        menu.add_command(
            label=CURRENT_TEXT_DICT.get('right_click_menu_st').get('delete'),
            command=self._delete)
        # make things pretty with a horizontal separator
        menu.add_separator()
        # I don't know of if there's a virtual event for select all though
        # I did look in vain for documentation on -any- of Tkinter's
        # virtual events.  Regardless, the method itself is trivial.
        menu.add_command(
            label=CURRENT_TEXT_DICT.get(
                'right_click_menu_st').get('select_all'),
            command=self._select_all)
        menu.add_command(
            label=CURRENT_TEXT_DICT.get(
                'right_click_menu_st').get('clear_all'),
            command=self._clear_all)
        menu.post(event.x_root, event.y_root)

    def _cut(self):
        self.parent.event_generate("<<Cut>>")

    def _copy(self):
        self.parent.event_generate("<<Copy>>")

    def _delete(self):
        self.parent.event_generate("<<Clear>>")

    def _paste_if_string_in_clipboard(self):
        self.parent.event_generate("<<Paste>>")

    def _select_all(self, ):
        """select all"""
        self.parent.tag_add('sel', "1.0", "end-1c")
        self.parent.mark_set('insert', "1.0")
        self.parent.see('insert')
        return 'break'

    def _paste_string_state(self):
        """Returns true if a string is in the clipboard"""
        try:
            # this assignment will raise an exception if the data
            # in the clipboard isn't a string (such as a picture).
            # in which case we want to know about it so that the Paste
            # option can be appropriately set normal or disabled.
            clipboard = self.parent.selection_get(selection='CLIPBOARD')
        except:
            return False
        return True

    def _clear_all(self):
        """Clear all"""
        self.parent.delete('1.0', 'end')


class AutocompleteGUI(tk.Frame):
    """The main GUI for autocomplete program."""

    def __init__(self, master=None, keys_for_all=[], dict_for_all={}):
        tk.Frame.__init__(self, master)
        # Data
        self.keys_for_all = keys_for_all
        self.dict_for_all = dict_for_all
        self.history = []

        # GUI
        self.master.geometry(
            CURRENT_TEXT_DICT.get('main_window').get('geometry'))
        self.master.title(
            '%s %s' % (CURRENT_TEXT_DICT.get('main_window').get("main_title"),
                       __version__))
        self.set_style()
        self.create_menu_bar()
        self.create_widgets()
        self.grid_configure()
        self.row_and_column_configure()
        self.create_right_menu()

        # Func
        self.bind_func()

    def set_style(self):
        """Set style for widgets in the main window."""
        s = ttk.Style()
        s.configure('TCombobox', padding=(11))
        s.configure('auto.TCombobox', foreground='red')
        s.configure('TButton', padding=(10))
        s.configure('open.TButton', foreground='blue')

        # Configure Title Frame
        s.configure(
            'config.TLabel',
            padding=10,
            font=('helvetica', 11, 'bold'),
        )
        s.configure(
            'listbox.TLabel',
            padding=2,
        )
        s.configure(
            'status.TLabel',
            padding=5,
            foreground='blue',
        )

    def create_menu_bar(self):
        """Create menu_bar for the main window."""
        menu_bar = tk.Menu(self.master)

        # ~~~~~~~~~~~~~~~~~~~~~~
        # File Menu
        # ~~~~~~~~~~~~~~~~~~~~~~
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(
            label=CURRENT_TEXT_DICT.get('menu_bar').get('save'),
            command=self._ask_save_file
        )
        file_menu.add_separator()
        file_menu.add_command(
            label=CURRENT_TEXT_DICT.get('menu_bar').get('exit'),
            command=self.master.quit)
        menu_bar.add_cascade(
            label=CURRENT_TEXT_DICT.get('menu_bar').get('file_cascade'),
            menu=file_menu)

        # ~~~~~~~~~~~~~~~~~~~~~~
        # Edit Menu
        # ~~~~~~~~~~~~~~~~~~~~~~
        edit_menu = tk.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(
            label=CURRENT_TEXT_DICT.get('menu_bar').get('copy'),
            command=self._copy)
        edit_menu.add_command(
            label=CURRENT_TEXT_DICT.get('menu_bar').get('cut'),
            command=self._cut)
        # try:
        #     edit_menu.add_command(label="Paste", command=self._paste)
        # except Exception:
        #     pass
        if self._paste_string_state():
            edit_menu.add_command(
                label=CURRENT_TEXT_DICT.get('menu_bar').get('paste'),
                command=self._paste)
        else:
            edit_menu.add_command(
                label=CURRENT_TEXT_DICT.get('menu_bar').get('paste'),
                command=lambda: print(
                    CURRENT_TEXT_DICT.get('menu_bar').get(
                        'no_str_in_clipboard_warning')))
        edit_menu.add_separator()
        edit_menu.add_command(
            label=CURRENT_TEXT_DICT.get('menu_bar').get('delete'),
            command=self._delete)
        menu_bar.add_cascade(
            label=CURRENT_TEXT_DICT.get('menu_bar').get('edit_cascade'),
            menu=edit_menu)

        # ~~~~~~~~~~~~~~~~~~~~~~
        # About Menu
        # ~~~~~~~~~~~~~~~~~~~~~~
        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(
            label=CURRENT_TEXT_DICT.get('menu_bar').get('help'),
            command=self._display_help)
        help_menu.add_command(
            label=CURRENT_TEXT_DICT.get('menu_bar').get('about'),
            command=self._display_about)
        menu_bar.add_cascade(
            label=CURRENT_TEXT_DICT.get('menu_bar').get('help_cascade'),
            menu=help_menu)

        self.master.config(menu=menu_bar)

    def create_widgets(self):
        """Create widgets for the main GUI window."""
        self.content = ttk.Frame(self.master, padding=(8))
        self.content.grid(row=0, column=0, sticky=(tk.W + tk.E + tk.N + tk.S))

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # Sidebar configuration area
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.config_label = ttk.Label(
            self.content,
            text=CURRENT_TEXT_DICT.get('config').get('config_label'),
            style='config.TLabel')

        self.turn_off_similarity_search_var = tk.IntVar()
        self.similarity_search_checkbutton = ttk.Checkbutton(
            self.content,
            text=CURRENT_TEXT_DICT.get(
                'config').get('similarity_search_switch'),
            variable=self.turn_off_similarity_search_var,
            onvalue=1, offvalue=0
        )
        self.turn_off_similarity_search_var.set(0)

        self.turn_off_spell_check_var = tk.IntVar()
        self.spell_check_checkbutton = ttk.Checkbutton(
            self.content,
            text=CURRENT_TEXT_DICT.get('config').get('spell_check_switch'),
            variable=self.turn_off_spell_check_var,
            onvalue=1, offvalue=0
        )
        self.turn_off_spell_check_var.set(0)

        self.totally_match_var = tk.IntVar()
        self.totally_match_checkbutton = ttk.Checkbutton(
            self.content,
            text=CURRENT_TEXT_DICT.get('config').get('match_whole_word'),
            variable=self.totally_match_var,
            onvalue=1, offvalue=0
        )
        self.totally_match_var.set(0)

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # Search bar & Search offline button & Search internet button
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.input_box = ttk.Combobox(
            self.content,
            style='auto.TCombobox')
        self.input_box.focus()

        self.search_offline_button = ttk.Button(
            self.content,
            text=CURRENT_TEXT_DICT.get('buttons').get('search_offline_button'),
            style='copy.TButton')

        self.search_internet_button = ttk.Button(
            self.content,
            text=CURRENT_TEXT_DICT.get('buttons').get('search_internet_button'),
            style='copy.TButton')

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # Four labels & Four candidate listboxes
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.label_1 = ttk.Label(
            self.content,
            text=CURRENT_TEXT_DICT.get('labels').get('startswith_endswith_label'),
            style='listbox.TLabel')
        if CURRENT_PLATFORM in (MAC_PLATFORM, ):
            self.listbox1 = tk.Listbox(self.content, font=('Monaco', 12))
        else:
            self.listbox1 = tk.Listbox(self.content, font=('Monospace', 10))
        self.scrollbar1 = ttk.Scrollbar(self.content)

        self.label_2 = ttk.Label(
            self.content,
            text=CURRENT_TEXT_DICT.get('labels').get('contains_label'),
            style='listbox.TLabel')
        if CURRENT_PLATFORM in (MAC_PLATFORM, ):
            self.listbox2 = tk.Listbox(self.content, font=('Monaco', 12))
        else:
            self.listbox2 = tk.Listbox(self.content, font=('Monospace', 10))
        self.scrollbar2 = ttk.Scrollbar(self.content)

        self.label_3 = ttk.Label(
            self.content,
            text=CURRENT_TEXT_DICT.get('labels').get('similarity_label'),
            style='listbox.TLabel')
        if CURRENT_PLATFORM in (MAC_PLATFORM, ):
            self.listbox3 = tk.Listbox(self.content, font=('Monaco', 12))
        else:
            self.listbox3 = tk.Listbox(self.content, font=('Monospace', 10))
        self.scrollbar3 = ttk.Scrollbar(self.content)

        self.label_4 = ttk.Label(
            self.content,
            text=CURRENT_TEXT_DICT.get('labels').get('spell_check_label'),
            style='listbox.TLabel')
        if CURRENT_PLATFORM in (MAC_PLATFORM, ):
            self.listbox4 = tk.Listbox(self.content, font=('Monaco', 12))
        else:
            self.listbox4 = tk.Listbox(self.content, font=('Monospace', 10))
        self.scrollbar4 = ttk.Scrollbar(self.content)

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # Result label & Result ScrolledText area
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.status_label_value = tk.StringVar()
        self.label_5 = ttk.Label(
            self.content,
            textvariable=self.status_label_value,
            style='status.TLabel')
        self.status_label_value.set(
            CURRENT_TEXT_DICT.get('labels').get('default_status_label'))
        if CURRENT_PLATFORM in (MAC_PLATFORM, ):
            self.scrolled_text_5 = st.ScrolledText(self.content,
                                                   font=('Monaco', 12))
        else:
            self.scrolled_text_5 = st.ScrolledText(self.content,
                                                   font=('Monospace', 10))

        self._display_help()

    def grid_configure(self):
        """Grid configuration of window and widgets."""
        self.master.grid()

        # 110 110 110 110
        # |->         <-|
        self.input_box.grid(row=0, column=0, columnspan=9, sticky='wens')
        self.search_offline_button.grid(row=0, column=9, sticky='wens')
        self.search_internet_button.grid(row=0, column=10, sticky='wens')

        # Config lines
        # 110 110 110 110
        # |-|
        self.config_label.grid(row=1, rowspan=2, column=0, columnspan=2,
                               sticky='wens')
        self.similarity_search_checkbutton.grid(row=1, column=3, sticky='we')
        self.spell_check_checkbutton.grid(row=2, column=3, sticky='we')
        self.totally_match_checkbutton.grid(row=1, column=4, sticky='we')

        # 110 110 110 110
        # |-|
        self.label_1.grid(row=3, column=0, columnspan=3, sticky='ws')
        self.listbox1.grid(row=4, column=0, columnspan=2, sticky='wens')
        self.scrollbar1.grid(row=4, column=2, sticky='ns')
        self.listbox1.config(yscrollcommand=self.scrollbar1.set)
        self.scrollbar1.config(command=self.listbox1.yview)

        # 110 110 110 110
        #     |-|
        self.label_2.grid(row=3, column=3, columnspan=3, sticky='w')
        self.listbox2.grid(row=4, column=3, columnspan=2, sticky='wens')
        self.scrollbar2.grid(row=4, column=5, sticky='ns')
        self.listbox2.config(yscrollcommand=self.scrollbar2.set)
        self.scrollbar2.config(command=self.listbox2.yview)

        # 110 110 110 110
        #         |-|
        self.label_3.grid(row=3, column=6, columnspan=3, sticky='w')
        self.listbox3.grid(row=4, column=6, columnspan=2, sticky='wens')
        self.scrollbar3.grid(row=4, column=8, sticky='ns')
        self.listbox3.config(yscrollcommand=self.scrollbar3.set)
        self.scrollbar3.config(command=self.listbox3.yview)

        # 110 110 110 110
        #             |-|
        self.label_4.grid(row=3, column=9, columnspan=3, sticky='w')
        self.listbox4.grid(row=4, column=9, columnspan=2, sticky='wens')
        self.scrollbar4.grid(row=4, column=11, sticky='ns')
        self.listbox4.config(yscrollcommand=self.scrollbar4.set)
        self.scrollbar4.config(command=self.listbox4.yview)

        # 110 110 110 110
        # |->         <-|
        self.label_5.grid(row=5, column=0, columnspan=12, sticky='w')
        self.scrolled_text_5.grid(row=6, column=0, columnspan=12,
                                  sticky='wens')

    def row_and_column_configure(self):
        """Rows and columns configuration"""
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)

        # Search bar
        self.content.rowconfigure(0, weight=0)
        # Config lines
        self.content.rowconfigure(1, weight=0)
        self.content.rowconfigure(2, weight=0)
        # listboxes
        self.content.rowconfigure(3, weight=0)
        self.content.rowconfigure(4, weight=1)
        # Result ScrolledText area
        self.content.rowconfigure(5, weight=0)
        self.content.rowconfigure(6, weight=1)

        # listbox1  listbox2  listbox3  listbox4
        #   110        110      110       110
        self.content.columnconfigure(0, weight=1, uniform="fred")
        self.content.columnconfigure(1, weight=1, uniform="fred")
        self.content.columnconfigure(2, weight=0)
        self.content.columnconfigure(3, weight=1, uniform="fred")
        self.content.columnconfigure(4, weight=1, uniform="fred")
        self.content.columnconfigure(5, weight=0)
        self.content.columnconfigure(6, weight=1, uniform="fred")
        self.content.columnconfigure(7, weight=1, uniform="fred")
        self.content.columnconfigure(8, weight=0)
        self.content.columnconfigure(9, weight=1, uniform="fred")
        self.content.columnconfigure(10, weight=1, uniform="fred")
        self.content.columnconfigure(11, weight=0)

    def create_right_menu(self):
        # Right menu for input combobox
        right_menu_input_box = RightClickMenu(self.input_box)
        # Fix right click menu on Mac OSX
        if CURRENT_PLATFORM in (MAC_PLATFORM, ):
            self.input_box.bind('<Button-2>', right_menu_input_box)
        else:
            self.input_box.bind('<Button-3>', right_menu_input_box)

        # Right menu for output area
        right_menu_scrolled_text_5 = RightClickMenuForScrolledText(
            self.scrolled_text_5)
        # Fix right click menu on Mac OSX
        if CURRENT_PLATFORM in (MAC_PLATFORM, ):
            self.scrolled_text_5.bind('<Button-2>', right_menu_scrolled_text_5)
        else:
            self.scrolled_text_5.bind('<Button-3>', right_menu_scrolled_text_5)

    def bind_func(self):
        self.search_offline_button['command'] = self._display_candidates
        self.search_internet_button['command'] = self._query_baidu_baike

        def bind_command_to_listbox(widget):
            """Bind command to listbox.

            Double click on candidates from any column from the four,
            then the result will be on the output area.
            """
            # Single click left mouse
            # widget.bind('<Button-1>',
            #             lambda e: self._display_search_result(widget))

            # Double click left mouse
            widget.bind('<Double-Button-1>',
                        lambda e: self._display_search_result(widget))

            right_menu_widget = RightClickMenuForListBox(widget)
            # Fix right click menu on Mac OSX
            if CURRENT_PLATFORM in (MAC_PLATFORM, ):
                widget.bind("<Button-2>", right_menu_widget)
            else:
                widget.bind("<Button-3>", right_menu_widget)

        for listbox in [self.listbox1, self.listbox2,
                        self.listbox3, self.listbox4]:
            bind_command_to_listbox(listbox)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Functional methods
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def _query_offline_data(self):
        """Command of Do Query button with multi-processing"""
        query = self.input_box.get().strip()
        if not query:
            self.status_label_value.set(
                CURRENT_TEXT_DICT.get('info_text').get('blank_query_label'))
            return ''
        query_word_object = QueryWord(
            self.keys_for_all, self.dict_for_all)
        result_dict = {'0': [], '1': [], '2': [], '3': ''}
        match_whole_word = self.totally_match_var.get()
        if query:
            # If name match keys in dictionary, just do strategy 1 & 2
            if query in self.dict_for_all:
                turn_on_mode = [True, True, False, False]
                result_dict = query_word_object.query_all_four(
                    query, match_whole_word, turn_on_mode)
            # No exactly match
            else:
                # Latin
                # Dirty trick to check if query is Latin name (space between words)
                if ' ' in query:
                    turn_on_mode = [True, True, True, False]
                    if self.turn_off_similarity_search_var.get():
                        turn_on_mode[2] = False
                    result_dict = query_word_object.query_all_four(
                        query, match_whole_word, turn_on_mode)
                # English
                # query starts with English letters, not Chinese
                # We can apply similarity search and spell check for only English
                elif query[0] in string.printable:
                    turn_on_mode = [True, True, True, True]
                    if self.turn_off_similarity_search_var.get():
                        turn_on_mode[2] = False
                    if self.turn_off_spell_check_var.get():
                        turn_on_mode[3] = False
                    result_dict = query_word_object.query_all_four(
                        query, match_whole_word, turn_on_mode)
                else:
                    # For Chinese, fuzzy search does not work.
                    # No similarity check and spell check.
                    # Chinese name may encounter Unicode related errors
                    turn_on_mode = [True, True, True, False]
                    if self.turn_off_similarity_search_var.get():
                        turn_on_mode[2] = False
                    result_dict = query_word_object.query_all_four(
                        query, match_whole_word, turn_on_mode)
        return result_dict

    def _query_baidu_baike(self):
        keyword = self.input_box.get().strip()
        if not keyword:
            self.status_label_value.set(
                CURRENT_TEXT_DICT.get('info_text').get('blank_query_label'))
            return ''
        self.status_label_value.set(
            CURRENT_TEXT_DICT.get('info_text').get('searching_baidu_baike'))
        start_time = time.time()
        baike_result = InternetQuery.prettify_baike_result(
            InternetQuery.search_baidu_baike(keyword))
        if baike_result:
            baike_result = '%s\n\n%s\n\n\n\n' % (
                CURRENT_TEXT_DICT.get('info_text').get('baike_result_info'),
                baike_result)
            end_time = time.time()
            self._insert_to_text_area(self.scrolled_text_5, baike_result)
            self.status_label_value.set(
                '%s%fs' % (
                    CURRENT_TEXT_DICT.get(
                        'info_text').get('baike_search_complete'),
                    end_time - start_time))
        else:
            self._insert_to_text_area(self.scrolled_text_5, baike_result)
            self.status_label_value.set(
                CURRENT_TEXT_DICT.get('info_text').get('baike_no_result'))

    def _query_wikipedia(self):
        keyword = self.input_box.get().strip()
        if not keyword:
            self.status_label_value.set(
                CURRENT_TEXT_DICT.get('info_text').get('blank_query_label')
            )
            return ''
        self.status_label_value.set(
            CURRENT_TEXT_DICT.get('info_text').get('searching_wikipedia'))
        start_time = time.time()
        wikipedia_result = InternetQuery.search_wikipedia(keyword)
        if wikipedia_result:
            wikipedia_result = '%s\n\n%s\n\n\n\n' % (
                CURRENT_TEXT_DICT.get(
                    'info_text').get('wikipedia_result_info'),
                wikipedia_result)
            end_time = time.time()
            self._insert_to_text_area(self.scrolled_text_5, wikipedia_result)
            self.status_label_value.set(
                '%s%fs' % (
                    CURRENT_TEXT_DICT.get(
                        'info_text').get('wikipedia_search_complete'),
                    end_time - start_time))
        else:
            self._insert_to_text_area(self.scrolled_text_5, wikipedia_result)
            self.status_label_value.set(
                CURRENT_TEXT_DICT.get('info_text').get('wikipedia_no_result'))

    def _query_internet_multithreading(self):
        func_list = [self._query_baidu_baike,
                     self._query_wikipedia]

        self.status_label_value.set(
            CURRENT_TEXT_DICT.get('info_text').get('start_searching'))
        self.scrolled_text_5.delete('1.0', 'end-1c')
        self.scrolled_text_5.update_idletasks()
        for i, each_func in enumerate(func_list):
            thread = Thread(target=each_func)
            thread.setDaemon(True)
            thread.start()
            # thread.join()
            time.sleep(0.1)
        self.status_label_value.set(
            CURRENT_TEXT_DICT.get('info_text').get('search_complete'))

    def _display_candidates(self):
        self.status_label_value.set(
            CURRENT_TEXT_DICT.get('info_text').get('start_offline_search'))
        start_time = time.time()
        result_dict = self._query_offline_data()
        end_time = time.time()
        if not result_dict:
            return
        # Display outcome to candidate widget 1
        self.listbox1.delete('0', 'end')
        for item in result_dict['0']:
            self.listbox1.insert('end', item)

        # Display outcome to candidate widget 2
        self.listbox2.delete('0', 'end')
        for item in result_dict['1']:
            self.listbox2.insert('end', item)

        # Display outcome to candidate widget 3
        self.listbox3.delete('0', 'end')
        for item in result_dict['2']:
            self.listbox3.insert('end', item)

        # Display outcome to candidate widget 4
        self.listbox4.delete('0', 'end')
        self.listbox4.insert('end', result_dict['3'])

        self.status_label_value.set(
            '%s%fs%s' % (
                CURRENT_TEXT_DICT.get(
                    'info_text').get('offline_search_complete_1'),
                end_time - start_time,
                CURRENT_TEXT_DICT.get(
                    'info_text').get('offline_search_complete_2')))

    def _display_search_result(self, widget, is_clean_word=True):
        """Clean content in Output Area and insert new value."""
        # Listbox index must be: active, anchor, end, @x,y, or a number
        selection_value = widget.get('active')
        # if not is_clean_word:
        #     if selection_value:
        #         selection_value = selection_value.split()[1]
        self.input_box.delete(0, tk.END)
        self.input_box.insert(tk.END, selection_value)

        self.scrolled_text_5.delete("0.1", "end-1c")
        result = self.dict_for_all.get(selection_value)
        if result:
            if PrettyTable:
                table = PrettyTable(
                    ["Short Pinyin", "Long Pinyin", 'Chinese',
                     'Latin', 'Namer', 'Data Source', 'Web URL'])
                for column in ('Short Pinyin', 'Long Pinyin', 'Chinese',
                               'Latin', 'Namer', 'Data Source', 'Web URL'):
                    table.align[column] = "l"
                table.padding_width = 1
                for each_result in result:
                    normal_word_list = [x for x in each_result[3].split()
                                        if x not in SPECIAL_CHARS]
                    url = (FRPS_BASE_URL + '%20'.join(normal_word_list))
                    tmp_list = [_ for _ in each_result]
                    tmp_list.append(url)
                    table.add_row(tmp_list)

                self.scrolled_text_5.insert('end', table.get_string())
                self.scrolled_text_5.see(tk.END)
                self.scrolled_text_5.update_idletasks()
            else:
                self.scrolled_text_5.insert(
                    'end',
                    ('%s pip install prettytable\n\n'
                     '+--------------+-------------+---------'
                     '+-------+-------+-------------+---------+\n'
                     '| Short Pinyin | Long Pinyin | Chinese '
                     '| Latin | Namer | Data Source | Web URL |\n'
                     '+--------------+-------------+---------+'
                     '-------+-------+-------------+---------+\n'
                     '\n%s\n' % (
                         CURRENT_TEXT_DICT.get(
                             'info_text').get('pretty_table_install_info'),
                         '=' * 100)))
                for each_result in result:
                    elements = '  |  '.join(each_result)
                    self.scrolled_text_5.insert('end', elements)
                    self.scrolled_text_5.insert('end', ('\n%s\n' % ('-' * 100)))
                    # self.scrolled_text_5.see(tk.END)
                    # self.scrolled_text_5.update_idletasks()

    @staticmethod
    def _insert_to_text_area(st_widget, content):
        """Clear original content from ScrolledText area and insert new"""
        st_widget.delete('1.0', 'end')
        st_widget.insert('end', content)
        # st_widget.see(tk.END)
        st_widget.update_idletasks()

    def _copy(self):
        # self.master.clipboard_clear()
        # self.master.clipboard_append(self.master.focus_get().selection_get())
        self.master.focus_get().event_generate("<<Copy>>")

    def _cut(self):
        # self.master.clipboard_clear()
        # self.master.clipboard_append(self.master.focus_get().selection_get())
        # # self.master.focus_get().selection_clear()
        self.master.focus_get().event_generate("<<Cut>>")

    def _paste(self):
        # print(self.master.selection_get(selection='CLIPBOARD'))
        self.master.focus_get().event_generate("<<Paste>>")

    def _delete(self):
        self.master.focus_get().event_generate("<<Clear>>")

    def _paste_string_state(self):
        """Returns true if a string is in the clipboard"""
        try:
            # this assignment will raise an exception if the data
            # in the clipboard isn't a string (such as a picture).
            # in which case we want to know about it so that the Paste
            # option can be appropriately set normal or disabled.
            clipboard = self.master.selection_get(selection='CLIPBOARD')
        except:
            return False
        return True

    def _ask_save_file(self):
        """Dialog to open file."""
        f = tkFileDialog.asksaveasfile(mode='w', defaultextension=".txt")
        if f is None:
            return
        text_to_save = self.scrolled_text_5.get('1.0', 'end-1c').encode('GBK')
        f.write(text_to_save.decode('GBK').encode('utf-8'))
        f.close()

    def _display_help(self):
        self.scrolled_text_5.delete("0.1", "end-1c")
        self.scrolled_text_5.insert('end', USAGE_INFO)

    def _display_about(self):
        self.scrolled_text_5.delete('0.1', 'end-1c')
        self.scrolled_text_5.insert('end', ABOUT_INFO)


def dump_with_pickle(keys_for_all, dict_for_all):
    """Dump generated dictinary to pickle raw file.

    Generally, this function need only do once.
    """
    keys_for_all, dict_for_all = get_dict_for_all_columns()
    pickle_keys = pickle.dumps(keys_for_all)
    pickle_dict = pickle.dumps(dict_for_all)
    with open(PICKLE_KEYS_FILE, 'wb') as f_out:
        f_out.write(pickle_keys)
    with open(PICKLE_DICT_FILE, 'wb') as f_out:
        f_out.write(pickle_dict)


def load_with_pickle(pickle_keys_file, pickle_dict_file):
    """Load keys and dict from pickle raw file"""
    with open(pickle_keys_file, 'rb') as f_in:
        pickle_keys = f_in.read()
        keys_for_all = pickle.loads(pickle_keys)

    with open(pickle_dict_file, 'rb') as f_in:
        pickle_dict = f_in.read()
        dict_for_all = pickle.loads(pickle_dict)

    return keys_for_all, dict_for_all


def gui_main():
    """The main GUI program."""
    # Read from plain text file
    # keys_for_all, dict_for_all = get_dict_for_all_columns()

    # Read from pickle file
    keys_for_all, dict_for_all = load_with_pickle(PICKLE_KEYS_FILE,
                                                  PICKLE_DICT_FILE)
    global TRAINED_OBJECT
    TRAINED_OBJECT = SpellCheck(keys_for_all)
    app = AutocompleteGUI(keys_for_all=keys_for_all,
                          dict_for_all=dict_for_all)
    app.mainloop()


def main():
    """Main func"""
    get_dict_for_all_columns()


if __name__ == '__main__':
    gui_main()
    # main()
