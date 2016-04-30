#!/usr/bin/env pythonw
# -*- coding: utf-8 -*-

from __future__ import (print_function, unicode_literals,
                        with_statement)


"""Latin Search program"""

import os
import sys
try:
    import cPickle as pickle
except ImportError:
    import pickle
import string
import collections
from difflib import SequenceMatcher
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

__version__ = "v0.1.0"
__author__ = 'Jin'


_history = []


DATA_FILE = os.path.abspath('data/latin_without_sougou.csv')
PICKLE_KEYS_FILE = os.path.abspath('data/latin_60000.keys.pickle')
PICKLE_DICT_FILE = os.path.abspath('data/latin_60000.dict.pickle')

# 中国植物志网站链接
FRPS_BASE_URL = 'http://frps.eflora.cn/frps/'
# 拉丁名中的特殊字符
SPECIAL_CHARS = ['×', '〔', '）', '【', '】', '', '', '<', '>',
                 '*', '[', '@', ']', '［', '|']

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
            [word[0:i]+word[i+1:] for i in range(n)] +  # deletion
            # transposition
            [word[0:i]+word[i+1]+word[i]+word[i+2:] for i in range(n-1)] +
            # alteration
            [word[0:i]+c+word[i+1:] for i in range(n) for c in self.alphabet] +
            # insertion
            [word[0:i]+c+word[i:] for i in range(n+1) for c in self.alphabet])

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


class QueryWord(object):
    """Four query strategy.

    [Strategies]

        1. Starts with              'abcde'.startswith('abc')
        2. Contains                 'bcd' in 'abcde'
        3. Rank by Similarity
        4. Spell check

    [Usage]

        lines = get_lines(file_name)
        query_object = QueryWord(lines)

        # Startswith
        query_object.get_starts_with_candidates(query)
        # Contains
        query_object.get_contains_candidates(query)
        # Similarity
        query_object.get_similar_candidates(query, limit=30)
        # Spell Check
        query_object.get_spell_check_candidate(query)
        # All Four
        query_object.query_all_four(query)



    """
    def __init__(self, all_candidate_list):
        self.all_candidate_list = [x.strip() for x in all_candidate_list]
        self.trained_object = SpellCheck(all_candidate_list)

    # --------------------------------------------------------
    # 1:  Startswith or Endswith Check
    # --------------------------------------------------------
    def get_starts_with_candidates(self, query):
        """Check startswith & endswith"""
        _tmp_list = []
        for i, candidate in enumerate(self.all_candidate_list):
            if candidate.lower().startswith(query.strip().lower()) or\
                    candidate.lower().endswith(query.strip().lower()):
                _tmp_list.append(candidate)
        return _tmp_list

    # --------------------------------------------------------
    # 2:  Contains Check
    # --------------------------------------------------------
    def get_contains_candidates(self, query):
        """Check contains"""
        _tmp_list = []
        for i, candidate in enumerate(self.all_candidate_list):
            if query.strip().lower() in candidate.lower():
                _tmp_list.append(candidate)
        return _tmp_list

    # --------------------------------------------------------
    # 3:  Similarity Check
    # --------------------------------------------------------
    def get_similar_candidates(self, query, limit=30):
        """Rank candidates by similarity"""
        _tmp_list = []
        for i, candidate in enumerate(self.all_candidate_list):
            _similarity = get_similarity(candidate.lower(),
                                         query.strip().lower())
            _tmp_list.append((_similarity, candidate))
        _tmp_list.sort(key=lambda x: x[0], reverse=True)
        _tmp_list = _tmp_list[:limit]
        _similar_hits = [_[1] for _ in _tmp_list]
        # _similar_hits = ['%.4f  %s' % _ for _ in _tmp_list]

        return _similar_hits

    # --------------------------------------------------------
    # 4:  Advanced Spell Check
    # --------------------------------------------------------
    def get_spell_check_candidate(self, query):
        """Get spell check candicates"""
        return self.trained_object.correct(query)

    def query_all_four(self, query):
        """Get four results"""
        result_one = self.get_starts_with_candidates(query)
        result_two = self.get_contains_candidates(query)
        result_three = self.get_similar_candidates(query, limit=30)
        result_four = self.get_spell_check_candidate(query)

        return result_one, result_two, result_three, result_four


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
            menu.add_command(label="Cut", state='disable')
            menu.add_command(label="Copy", state='disable')
        else:
            # use Tkinter's virtual events for brevity.  These could
            # be hardcoded with our own functions to immitate the same
            # actions but there's no point except as a novice exercise
            # (which I recommend if you're a novice).
            menu.add_command(label="Cut", command=self._cut)
            menu.add_command(label="Copy", command=self._copy)
        # if there's string data in the clipboard then make the normal
        # Paste command.  otherwise disable it.
        if self.paste_string_state():
            menu.add_command(label="Paste", command=self._paste)
        else:
            menu.add_command(label="Paste", state='disable')
        # again, if there's no marked text then the Delete option is disabled.
        if not self.parent.selection_present():
            menu.add_command(label="Delete", state='disable')
        else:
            menu.add_command(label="Delete", command=self._clear)
        # make things pretty with a horizontal separator
        menu.add_separator()
        # I don't know of if there's a virtual event for select all though
        # I did look in vain for documentation on -any- of Tkinter's
        # virtual events.  Regardless, the method itself is trivial.
        menu.add_command(label="Select All", command=self._select_all)
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
        menu.add_command(label="Copy", command=self._copy)
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
        menu.add_command(label="Cut", command=self._cut)
        menu.add_command(label="Copy", command=self._copy)
        # if there's string data in the clipboard then make the normal
        # Paste command.  otherwise disable it.
        if self._paste_string_state():
            menu.add_command(label="Paste",
                             command=self._paste_if_string_in_clipboard)
        else:
            menu.add_command(label="Paste", state='disable')
        # again, if there's no marked text then the Delete option is disabled.
        menu.add_command(label="Delete", command=self._delete)
        # make things pretty with a horizontal separator
        menu.add_separator()
        # I don't know of if there's a virtual event for select all though
        # I did look in vain for documentation on -any- of Tkinter's
        # virtual events.  Regardless, the method itself is trivial.
        menu.add_command(label="Select All", command=self._select_all)
        menu.add_command(label="Clear All", command=self._clear_all)
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
        self.query_object = QueryWord(keys_for_all)
        self.dict_for_all = dict_for_all
        self.history = []
        self.master.grid()
        self.set_style()
        self.create_menu()
        self.create_widgets()
        self.grid_configure()
        self.create_right_menu()
        self.master.geometry('1400x800')
        self.master.title('Latin Finder %s' % __version__)

    def set_style(self):
        """Set style for widgets in the main window."""
        s = ttk.Style()
        s.configure('TCombobox', padding=(11))
        s.configure('auto.TCombobox', foreground='red')
        s.configure('TButton', padding=(10))
        s.configure('open.TButton', foreground='blue')

    def create_menu(self):
        """Create menubar for the main window."""
        self.menubar = tk.Menu(self.master)

        self.file_menu = tk.Menu(self.menubar, tearoff=0)
        self.file_menu.add_command(
            label='Open',
            # command=reload_GUI_with_new_list
            )
        self.file_menu.add_command(
            label='Exit',
            command=self.master.quit)
        self.menubar.add_cascade(label='File', menu=self.file_menu)

        self.help_menu = tk.Menu(self.menubar, tearoff=0)
        self.help_menu.add_command(
            label='Help',
            command=lambda: self.print_help)
        self.menubar.add_cascade(label='Help', menu=self.help_menu)

        self.master.config(menu=self.menubar)

    def create_widgets(self):
        """Create widgets for the main GUI window."""
        self.content = ttk.Frame(self.master, padding=(8))
        self.content.grid(row=0, column=0, sticky=(tk.W+tk.E+tk.N+tk.S))

        self.label_1 = ttk.Label(self.content,
                                 text='Candidates (Startswith / Endswith)')
        self.listbox1 = tk.Listbox(self.content, font=('Monospace', 10))
        self.scrollbar1 = ttk.Scrollbar(self.content)

        self.label_2 = ttk.Label(
            self.content, text='Candidates (Contains)')
        self.listbox2 = tk.Listbox(self.content, font=('Monospace', 10))
        self.scrollbar2 = ttk.Scrollbar(self.content)

        self.label_3 = ttk.Label(
            self.content, text='Candidates (Rank by similarity)')
        self.listbox3 = tk.Listbox(self.content, font=('Monospace', 10))
        self.scrollbar3 = ttk.Scrollbar(self.content)

        self.label_4 = ttk.Label(
            self.content,
            text='Candidates (Spell check, single edit distance)')
        self.listbox4 = tk.Listbox(self.content, font=('Monospace', 10))
        self.scrollbar4 = ttk.Scrollbar(self.content)

        self.label_5 = ttk.Label(
            self.content,
            text=('Click "Do Query" button and see results. '
                  '** Double Click ** candidate to see detailed result.'))
        self.scrolled_text_5 = st.ScrolledText(self.content,
                                               font=('Monospace', 10))

        self.input_box = ttk.Combobox(
            self.content,
            style='auto.TCombobox')

        self.input_box.grid(row=0, column=0, columnspan=6, sticky=(tk.W+tk.E))
        self.input_box.focus()

        # self.open_file_button = ttk.Button(
        #     self.content,
        #     text='Open Tree File',
        #     # command=reload_GUI_with_new_list,
        #     style='open.TButton')
        # self.open_file_button.grid(
        #     row=0,
        #     column=0,
        #     columnspan=2,
        #     sticky=(tk.W+tk.E))

        self.do_query_button = ttk.Button(
            self.content,
            text='Do Query',
            command=self.show_candidates,
            style='copy.TButton')
        self.do_query_button.grid(
            row=0,
            column=6,
            columnspan=2,
            sticky=(tk.W))

        self.label_1.grid(row=1, column=0, columnspan=2, sticky=(tk.W))
        self.listbox1.grid(row=2, column=0, sticky=(tk.W+tk.E+tk.N+tk.S))
        self.scrollbar1.grid(row=2, column=1, sticky=(tk.N+tk.S))
        self.listbox1.config(yscrollcommand=self.scrollbar1.set)
        self.scrollbar1.config(command=self.listbox1.yview)

        self.label_2.grid(row=1, column=2, columnspan=2, sticky=(tk.W))
        self.listbox2.grid(row=2, column=2, sticky=(tk.W+tk.E+tk.N+tk.S))
        self.scrollbar2.grid(row=2, column=3, sticky=(tk.N+tk.S))
        self.listbox2.config(yscrollcommand=self.scrollbar2.set)
        self.scrollbar2.config(command=self.listbox2.yview)

        self.label_3.grid(row=1, column=4, columnspan=2, sticky=(tk.W))
        self.listbox3.grid(row=2, column=4, sticky=(tk.W+tk.E+tk.N+tk.S))
        self.scrollbar3.grid(row=2, column=5, sticky=(tk.N+tk.S))
        self.listbox3.config(yscrollcommand=self.scrollbar3.set)
        self.scrollbar3.config(command=self.listbox3.yview)

        self.label_4.grid(row=1, column=6, columnspan=2, sticky=(tk.W))
        self.listbox4.grid(row=2, column=6, sticky=(tk.W+tk.E+tk.N+tk.S))
        self.scrollbar4.grid(row=2, column=7, sticky=(tk.N+tk.S))
        self.listbox4.config(yscrollcommand=self.scrollbar4.set)
        self.scrollbar4.config(command=self.listbox4.yview)

        self.label_5.grid(row=3, column=0, columnspan=7, sticky=(tk.W))
        self.scrolled_text_5.grid(row=4, column=0, columnspan=7,
                                  sticky=(tk.N+tk.S+tk.W+tk.E))
        self.scrolled_text_5.delete("0.1", "end-1c")
        self.scrolled_text_5.insert('end', USAGE_INFO)

        def bind_command_to_listbox(widget):
            """Bind command to listbox.

            Double click on candidates from any column from the four,
            then the result will be on the output area.
            """
            # Single click left mouse
            # widget.bind('<Button-1>',
            #             lambda e: self.clean_and_insert_value(widget))

            # Double click left mouse
            widget.bind('<Double-Button-1>',
                        lambda e: self.clean_and_insert_value(widget))

            right_menu_widget = RightClickMenuForListBox(widget)
            widget.bind("<Button-3>", right_menu_widget)

        for listbox in [self.listbox1, self.listbox2,
                        self.listbox3, self.listbox4]:
            bind_command_to_listbox(listbox)

    def clean_and_insert_value(self, widget, is_clean_word=True):
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
            else:
                self.scrolled_text_5.insert(
                    'end',
                    ('请安装 prettytable 以获得更清晰的结果视图。\n'
                     '安装方法： pip install prettytable\n\n'
                     '+--------------+-------------+---------'
                     '+-------+-------+-------------+---------+\n'
                     '| Short Pinyin | Long Pinyin | Chinese '
                     '| Latin | Namer | Data Source | Web URL |\n'
                     '+--------------+-------------+---------+'
                     '-------+-------+-------------+---------+\n'
                     '\n%s\n' % ('='*100)))
                for each_result in result:
                    elements = '  |  '.join(each_result)
                    self.scrolled_text_5.insert('end', elements)
                    self.scrolled_text_5.insert('end', ('\n%s\n' % ('-' * 100)))

    def do_query(self):
        """Command of Do Query button. Get Search result.
        Then display the result @show_candidates().
        """
        final_name = self.input_box.get().strip()
        if final_name:
            # Latin name, there is white space in name
            if ' ' in final_name:
                # If latin name match keys in dictionary, it will be quick
                # and easy.
                if final_name in self.dict_for_all:
                    all_candidate_list = \
                        self.dict_for_all[final_name][0]
                    _tmp_list = []
                    _tmp_list.append([all_candidate_list[0]])
                    _tmp_list.append([all_candidate_list[1]])
                    _tmp_list.append([all_candidate_list[3]])
                    _tmp_list.append(all_candidate_list[3])
                    return _tmp_list
                else:
                    # If no exact key match in dictionary, try fuzzy match
                    _tmp_list = []
                    candidate_3 = self.query_object.get_similar_candidates(
                        final_name)
                    candidate_4 = self.query_object.get_spell_check_candidate(
                        final_name)

                return ([], [], candidate_3,
                        candidate_4 if candidate_4 else '')

            # query starts with English letters, not Chinese
            # We can apply similarity search and spell check for only English
            if final_name[0] in string.printable:
                if final_name in self.dict_for_all:
                    all_candidate_list = \
                        self.dict_for_all[final_name][0]
                    _tmp_list = []
                    # Get result for Startswith / Endswith column
                    _tmp_list.append(
                        [all_candidate_list[0]] +
                        self.query_object.get_starts_with_candidates(
                            final_name))
                    # Get result for Contains column
                    _tmp_list.append([all_candidate_list[1]])
                    # Get result for Similarity column
                    _tmp_list.append([all_candidate_list[3]])
                    # Get result for Spell Check column
                    _tmp_list.append(all_candidate_list[3])
                    return _tmp_list
                else:
                    all_candidate_list = self.query_object.\
                        query_all_four(final_name)
                    return all_candidate_list
            else:
                # Query is Chinese word
                # No similarity check and spell check
                try:
                    # If query is in dictionary
                    # Chinese name may encounter Unicode related errors
                    # For Chinese, fuzzy search does not work.
                    # Just try to search in dictionary
                    all_candidate_list = \
                        self.dict_for_all[final_name][0]
                    _tmp_list = []
                    _tmp_list.append(
                        # Exactly match
                        [all_candidate_list[0]] +
                        # Startswith or Endswith
                        self.query_object.get_starts_with_candidates(
                            final_name))
                    _tmp_list.append([all_candidate_list[1]])
                    _tmp_list.append([all_candidate_list[3]])
                    _tmp_list.append(all_candidate_list[3])
                    return _tmp_list
                except KeyError as e:
                    _tmp_list = []
                    _tmp_list.append(
                        self.query_object.get_starts_with_candidates(
                            final_name))
                    _tmp_list.append(
                        self.query_object.get_contains_candidates(
                            final_name))
                    _tmp_list.append([])
                    _tmp_list.append('')
                    return _tmp_list
        else:
            return ([], [], [], '')

    def show_candidates(self):
        # ---------------------------
        # Do query and get candidates
        # ---------------------------
        all_candidate_list = self.do_query()
        # Get all candidates
        result_one, result_two, result_three, result_four = all_candidate_list

        # ------------------------------------------------
        # Start show candidates in four candidate columns
        # ------------------------------------------------
        # listbox1
        self.listbox1.delete('0', 'end')
        for item in result_one:
            self.listbox1.insert('end', item)

        # listbox2
        self.listbox2.delete('0', 'end')
        for item in result_two:
            self.listbox2.insert('end', item)

        # listbox3
        self.listbox3.delete('0', 'end')
        for item in result_three:
            self.listbox3.insert('end', item)

        # listbox4
        self.listbox4.delete('0', 'end')
        self.listbox4.insert('end', result_four)

    def grid_configure(self):
        """Grid configuration of window and widgets."""
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)

        self.content.rowconfigure(0, weight=0)
        self.content.rowconfigure(1, weight=0)
        self.content.rowconfigure(2, weight=1)
        self.content.rowconfigure(3, weight=0)
        self.content.rowconfigure(4, weight=1)
        self.content.columnconfigure(0, weight=1)
        self.content.columnconfigure(1, weight=0)
        self.content.columnconfigure(2, weight=1)
        self.content.columnconfigure(3, weight=0)
        self.content.columnconfigure(4, weight=1)
        self.content.columnconfigure(5, weight=0)
        self.content.columnconfigure(6, weight=1)
        self.content.columnconfigure(7, weight=0)

    def create_right_menu(self):
        # Right menu for input combobox
        right_menu_input_box = RightClickMenu(self.input_box)
        self.input_box.bind('<Button-3>', right_menu_input_box)

        # Right menu for output area
        right_menu_scrolled_text_5 = RightClickMenuForScrolledText(
            self.scrolled_text_5)
        self.scrolled_text_5.bind('<Button-3>', right_menu_scrolled_text_5)

    def print_help(self):
        self.scrolled_text_5.delete("0.1", "end-1c")
        self.scrolled_text_5.insert('end', USAGE_INFO)


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
    app = AutocompleteGUI(keys_for_all=keys_for_all,
                          dict_for_all=dict_for_all)
    app.mainloop()


def main():
    """Main func"""
    get_dict_for_all_columns()


if __name__ == '__main__':
    gui_main()
    # main()
