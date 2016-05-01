�
��%Wc           @� s�  d  Z  d d l m Z m Z m Z d d l Z d d l Z d d l Z d d l Z d d l	 m
 Z
 d d l Z d d l Z d d l m Z y d d l Z Wn e k
 r� d d l Z n Xd d l Z d d l Z d d l m Z d d l m Z y d d l m Z Wn e k
 re Z n Xe j d	 d
 k rfd d l Z d d l Z d d l Z d d l  Z! nQ e j d	 d k r�d d l" Z d d l" m Z d d l# j$ Z! d d l" m% Z n  d Z& d Z' g  Z( e j) j* d � Z+ e j) j* d � Z, e j) j* d � Z- d Z. d Z/ d Z0 d d d d d d d d d d d  d! d" d# d$ g Z1 e2 �  a3 d% Z4 d& Z5 i d' d( 6Z6 d) e& Z7 d* e& e' f Z8 d+ �  Z9 d, �  Z: d- �  Z; d. �  Z< d/ �  Z= d0 e2 f d1 �  �  YZ> d2 e2 f d3 �  �  YZ? d4 e2 f d5 �  �  YZ@ d6 e2 f d7 �  �  YZA d8 e2 f d9 �  �  YZB d: e2 f d; �  �  YZC d< e jD f d= �  �  YZE d> �  ZF d? �  ZG d@ �  ZH dA �  ZI eJ dB k r�eH �  n  d S(C   u   Latin Search programi����(   t   print_functiont   unicode_literalst   with_statementN(   t   Thread(   t   BeautifulSoup(   t   SequenceMatcher(   t   Process(   t   PrettyTablei    u   2u   3(   t   ttk(   t
   filedialogu   v0.2.0u   Jinu   data/latin_without_sougou.csvu   data/latin_60000.keys.pickleu   data/latin_60000.dict.pickleu   http://frps.eflora.cn/frps/i   g333333�?u   ×u   〔u   ）u   【u   】u   u   u   <u   >u   *u   [u   @u   ]u   ［u   |u   http://www.baidu.com/s?wd=u   https://zh.wikipedia.org/wiki/us   Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36u
   User-Agentu�  
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

u)  
============================================================
软件名称：植物拉丁名搜索（Latin Namer Finer）
软件版本：%s
软件作者：%s
使用方法：请点击菜单栏中 "Help" - "Help" 以查看使用方式。
============================================================
c         C� s&   t  |  d � � } | j �  SWd QXd S(   u%   Read file and return a list of lines.u   rN(   t   opent	   readlines(   t	   file_namet   f_in(    (    s   latinsearch.pywt	   get_lines{   s    c   
      C� s  g  g  g  g  f \ } } } } g  } t  |  d � �� } x� | D]� } t j d d k rh | j d � } n  g  | j d � D] } | j �  ^ qx }	 | j |	 d � | j |	 d � | j |	 d � | j |	 d � | j t |	 � � q= WWd	 QX| | | | | f S(
   u�  
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
    u   ri    u   2u   utf-8u   ,i   i   i   N(   R
   t   syst   versiont   decodet   splitt   stript   appendt   tuple(
   R   t   column_list_1t   column_list_2t   column_list_3t   column_list_4t   detailed_info_tuple_listR   t   linet   xt   elements(    (    s   latinsearch.pywt   get_key_value_pairs_from_file�   s    (	c         C� sq   i  } xd t  t |  | � � D]M \ } \ } } | | k rX g  | | <| | j | � q | | j | � q W| S(   u�   
    Generate a dictionary from two lists. keys may be duplicated.

    >>> get_one_to_more_dict(['a', 'b', 'a', 'a'], [1, 2, 3, 4])
    {'a': [1, 3, 4], 'b': [2]}
    (   t	   enumeratet   zipR   (   t   key_listt
   value_listt	   _out_dictt   it   keyt   value(    (    s   latinsearch.pywt   get_one_to_more_dict�   s    (
c          C� s�   t  t � \ }  } } } } t |  | � } t | | � } t | | � } t | | � } x- | | | f D] }	 |	 rg | j |	 � qg qg Wt t |  | | | � � }
 |
 | f S(   uC   Combine dicts, each with one column as key and whole line as value.(   R   t	   DATA_FILER'   t   updatet   listt   set(   R   R   R   R   R   t   dict_1t   dict_2t   dict_3t   dict_4t	   each_dictt   keys_for_all(    (    s   latinsearch.pywt   get_dict_for_all_columns�   s    c         C� s   t  d |  | � j �  S(   un   Return similarity of two strings.

    [Example]
        >>> get_similarity('abcde', 'bcdef')
        0.8
    N(   R   t   Nonet   ratio(   t   str_at   str_b(    (    s   latinsearch.pywt   get_similarity�   s    t
   SpellCheckc           B� sG   e  Z d  Z d �  Z e d � Z d �  Z d �  Z d �  Z d �  Z	 RS(   uW  Train data set with given data then do spell check for given word.

    [Example]
        >>> s = SpellCheck(['abcd', 'fghi'])
        >>> s.correct('abci')
        'abcd'

    [Reference]
        [1]: Title:   How to Write a Spelling Corrector
             Author:  Peter Norvig
             Webpage: http://norvig.com/spell-correct.html
    c         C� s:   | |  _  |  j �  |  _ |  j d t � |  _ d |  _ d  S(   Nt   loweruB   abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-.:1234567890(   t   candidate_listt   traint   NWORDSt   Truet   NWORDS_lowert   alphabet(   t   selfR:   (    (    s   latinsearch.pywt   __init__�   s    	c         C� s�   |  j  s t d � � n  t j d �  � } | sW x[ |  j  D] } | | c d 7<q: Wn7 |  j  } x* t d �  | � D] } | | c d 7<qt W| S(   u   Train model with data set.u*   Blank training list (Choosed blank file?).c           S� s   d S(   Ni   (    (    (    (    s   latinsearch.pywt   <lambda>�   s    i   c         S� s
   |  j  �  S(   N(   R9   (   t   _(    (    s   latinsearch.pywRB   �   s    (   R:   t
   ValueErrort   collectionst   defaultdictt   map(   R@   R9   t   modelt   ft   tmp_list(    (    s   latinsearch.pywR;   �   s    	
c      	   C� s  t  | � } t g  t | � D] } | d | !| | d ^ q g  t | d � D]3 } | d | !| | d | | | | d ^ qO g  t | � D]3 } |  j D]# } | d | !| | | d ^ q� q� g  t | d � D]/ } |  j D] } | d | !| | | ^ q� q� � S(   u�   Words that has one edit distance.

        1. deletion
        2. transposition
        3. alteration
        4. insertion
        i    i   i   (   t   lenR+   t   rangeR?   (   R@   t   wordt   nR$   t   c(    (    s   latinsearch.pywt   edits1   s    �c         � s#   t  �  f d �  �  j | � D� � S(   u!   Words that has two edit distance.c         3� s@   |  ]6 } �  j  | � D]  } | j �  �  j k r | Vq q d  S(   N(   RP   R9   R>   (   t   .0t   e1t   e2(   R@   (    s   latinsearch.pyws	   <genexpr>  s    (   R+   RP   (   R@   RM   (    (   R@   s   latinsearch.pywt   known_edits2  s    c         � s   t  �  f d �  | D� � S(   u   Known words.c         3� s*   |  ]  } | j  �  �  j k r | Vq d  S(   N(   R9   R>   (   RQ   t   w(   R@   (    s   latinsearch.pyws	   <genexpr>  s    (   R+   (   R@   t   words(    (   R@   s   latinsearch.pywt   known  s    c         � sL   �  j  | g � p0 �  j  �  j | � � p0 | g } t | d �  f d �  �S(   u9   Do spell check and correct word if word was wrong spelledR%   c         � s   �  j  |  S(   N(   R>   (   RU   (   R@   (    s   latinsearch.pywRB   %  s    (   RW   RP   t   max(   R@   RM   t
   candidates(    (   R@   s   latinsearch.pywt   correct  s    *	(
   t   __name__t
   __module__t   __doc__RA   t   FalseR;   RP   RT   RW   RZ   (    (    (    s   latinsearch.pywR8   �   s   				t	   QueryWordc           B� sw   e  Z d  Z d �  Z e e d � � Z e e d � � Z e e d � � Z e e d � � Z	 e e e e f d � Z
 RS(   u�  Query with 4 strategy with multi-processing.

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
    c         C� s\   g  | D] } | j  �  r | j  �  ^ q |  _ | |  _ t | � |  _ d |  _ i  |  _ d  S(   Nu    (   R   R1   t   dict_for_allR8   t   trained_objectt   queryt   result_dict(   R@   R1   R`   R   (    (    s   latinsearch.pywRA   Q  s    !		c   
      C� s�   g  } | r� |  | k rx | j  |  � | j |  � d } x= | d  D]. } | j �  rC | |  k rC | j  | � qC qC Wn  xZ t | � D]I \ } }	 |	 j |  � s� |	 j |  � r� |	 |  k r� | j  |	 � q� q� q� Wn  | j i | d 6� d S(   u   Check startswith & endswithi    i   u   0N(   R   t   getR   R   t
   startswitht   endswithR)   (
   Rb   R1   R`   Rc   t   turn_ont	   _tmp_listt   result_elementst   eachR$   t	   candidate(    (    s   latinsearch.pywt   get_starts_with_candidates\  s    c   
      C� s�   g  } | r� |  | k rx | j  |  � | j |  � d } x= | d  D]. } | j �  rC | |  k rC | j  | � qC qC Wn  xH t | � D]7 \ } }	 |  |	 k r� |	 |  k r� | j  |	 � q� q� q� Wn  | j i | d 6� d S(   u   Check containsi    i   u   1N(   R   Rd   R   R   R)   (
   Rb   R1   R`   Rc   Rg   Rh   Ri   Rj   R$   Rk   (    (    s   latinsearch.pywt   get_contains_candidatesu  s    c         C� s�   g  } g  } | r� t  | j d � � d k r� xK t | � D]= \ } } t | |  � }	 |	 t k r: | j |	 | f � q: q: W| j d d �  d t � | t  } | r� g  | D] }
 |
 d ^ q� n g  } n  | j	 i | d 6� d S(	   u   Rank candidates by similarityu   1i    R%   c         S� s   |  d S(   Ni    (    (   R   (    (    s   latinsearch.pywRB   �  s    t   reversei   u   2N(
   RK   Rd   R   R7   t   SIMILARITY_THRESHOLDR   t   sortR=   t   SIMILAR_RESULT_NUM_LIMITR)   (   Rb   R1   R`   Rc   Rg   Rh   t   _similar_hitsR$   Rk   t   _similarityRC   (    (    s   latinsearch.pywt   get_similar_candidates�  s    !
,c         C� sQ   d } | r9 t  | j d � � d k r9 t j |  � } n  | j i | d 6� d S(   u   Get spell check candicatesu    u   1i    u   3N(   RK   Rd   t   TRAINED_OBJECTRZ   R)   (   Rb   R1   R`   Rc   Rg   Rk   (    (    s   latinsearch.pywt   get_spell_check_candidate�  s    !c   	   
   C� s�   | |  _  i  } t j t j g } t j t j g } xR t | � D]D \ } } t d | |  j  |  j |  j	 | | | � � } | j
 �  q@ WxR t | � D]D \ } } t d | |  j  |  j |  j	 | | | � � } | j
 �  q� W| S(   u   Get four resultst   target(   Rb   R_   Rl   Rm   Rt   Rv   R   R   R1   R`   t   start(	   R@   Rb   t   turn_on_modeRc   t   func_list_1t   func_list_2R$   t	   each_funct   p(    (    s   latinsearch.pywt   query_all_four�  s"    	(   R[   R\   R]   RA   t   staticmethodR=   Rl   Rm   Rt   Rv   R~   (    (    (    s   latinsearch.pywR_   +  s   $		t   InternetQueryc           B� s5   e  Z e d  �  � Z e d �  � Z e d �  � Z RS(   c   
      C� s  t  t j |  j d � � } t j �  } | j | d t �} d | _ t	 | j
 d � } | j d i d d 6� } | d j d	 t � j d
 � } | j | d t �} d | _ t	 | j
 d � } | j d i d d 6� } t j d � } | r| j | j
 � }	 d j |	 � Sd S(   u5   Search baidu and retrive content from first baike URLu   GBKt   headersu   utf-8u   html.parseru   h3u   c-gap-bottom-smallu   classi    t   hrefu   hrefu   divu   basic-info cmn-clearfixu   [^\n]+u   
u    (   t   BAIDU_BAIKE_BASE_URLt   urllibt   quotet   encodet   requestst   sessionRd   t   HEADERt   encodingR   t   textt   findAllt   findR=   t   ret   compilet   findallt   join(
   t   keywordt   urlR�   t   reqt   soupt   outcomest   first_baike_urlt   main_contentt
   re_newlinet   out_list(    (    s   latinsearch.pywt   search_baidu_baike�  s     		c         C� s�   g  } g  |  j  �  D] } | j �  r | j �  ^ q } d } xN t | � D]@ \ } } | d d k ro | } qJ | d | } | j | � qJ Wd j | � S(   Nu    i   i    u   		| u   
(   t
   splitlinesR   R   R   R�   (   t   baike_resultR�   R   t   linest   temp_strR$   R   (    (    s   latinsearch.pywt   prettify_baike_result�  s    1	c   	      C� s�   g  } t  t j |  j d d � j d � � } t j �  } | j | d t �} t	 | j
 d � } | j d i d d 6� } | s� d	 S| j d
 � } x9 | D]1 } | r� | j | j
 j �  j d d � � q� q� Wd j | � S(   u   Search glossary from Wikipedia.u    u   _u   GBKR�   u   html.parseru   tableu   infobox biotau   classu    u   tdu   
(   t   WIKIPEDIA_BASE_URLR�   R�   t   replaceR�   R�   R�   Rd   R�   R   R�   R�   t   find_allR   R   R�   (	   R�   R�   R�   R�   R�   R�   t   outt   td_outRj   (    (    s   latinsearch.pywt   search_wikipedia�  s    %)(   R[   R\   R   R�   R�   R�   (    (    (    s   latinsearch.pywR�   �  s   t   RightClickMenuc           B� s_   e  Z d  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z	 d �  Z
 d	 �  Z RS(
   u5  
    Simple widget to add basic right click menus to entry widgets.

    usage:

    rclickmenu = RightClickMenu(some_entry_widget)
    some_entry_widget.bind("<3>", rclickmenu)

    If you prefer to import Tkinter over Tix, just replace all Tix
    references with Tkinter and this will still work fine.
    c         � sQ   | �  _  �  j  j d �  f d �  d d ��  j  j d �  f d �  d d �d  S(   Nu   <Control-a>c         � s
   �  j  �  S(   N(   t   _select_all(   t   e(   R@   (    s   latinsearch.pywRB   $  s    t   addu   +u   <Control-A>c         � s
   �  j  �  S(   N(   R�   (   R�   (   R@   (    s   latinsearch.pywRB   %  s    (   t   parentt   bind(   R@   R�   (    (   R@   s   latinsearch.pywRA     s    	"c         C� s:   |  j  j d � d k r d  S|  j  j �  |  j | � d  S(   Nu   stateu   disable(   R�   t   cgett   focus_forcet
   build_menu(   R@   t   event(    (    s   latinsearch.pywt   __call__'  s    c         C� sD  t  j |  j d d �} |  j j �  sV | j d d d d � | j d d d d � n2 | j d d d |  j � | j d d d |  j � |  j �  r� | j d d	 d |  j � n | j d d	 d d � |  j j �  s� | j d d
 d d � n | j d d
 d |  j	 � | j
 �  | j d d d |  j � | j | j | j � d S(   u   Build right click menut   tearoffi    t   labelu   Copyt   stateu   disableu   Cutt   commandu   Pasteu   Deleteu
   Select AllN(   t   tkt   MenuR�   t   selection_presentt   add_commandt   _copyt   _cutt   paste_string_statet   _pastet   _cleart   add_separatorR�   t   postt   x_roott   y_root(   R@   R�   t   menu(    (    s   latinsearch.pywR�   0  s    
c         C� s   |  j  j d � d  S(   Nu   <<Cut>>(   R�   t   event_generate(   R@   (    (    s   latinsearch.pywR�   R  s    c         C� s   |  j  j d � d  S(   Nu   <<Copy>>(   R�   R�   (   R@   (    (    s   latinsearch.pywR�   U  s    c         C� s   |  j  j d � d  S(   Nu	   <<Paste>>(   R�   R�   (   R@   (    (    s   latinsearch.pywR�   X  s    c         C� s   |  j  j d � d  S(   Nu	   <<Clear>>(   R�   R�   (   R@   (    (    s   latinsearch.pywR�   [  s    c         C� s'   |  j  j d d � |  j  j d � d S(   Ni    u   endu   break(   R�   t   selection_ranget   icursor(   R@   (    (    s   latinsearch.pywR�   ^  s    c         C� s(   y |  j  j d d � } Wn t SXt S(   u,   Returns true if a string is in the clipboardt	   selectionu	   CLIPBOARD(   R�   t   selection_getR^   R=   (   R@   t	   clipboard(    (    s   latinsearch.pywR�   g  s
    (   R[   R\   R]   RA   R�   R�   R�   R�   R�   R�   R�   R�   (    (    (    s   latinsearch.pywR�     s   					"						t   RightClickMenuForListBoxc           B� s2   e  Z d  Z d �  Z d �  Z d �  Z d �  Z RS(   u9  
    Simple widget to add basic right click menus to entry widgets.

    usage:

    rclickmenu = RightClickMenuForListBox(listbox_widget)
    listbox_widget.bind("<3>", rclickmenu)

    If you prefer to import Tkinter over Tix, just replace all Tix
    references with Tkinter and this will still work fine.
    c         C� s   | |  _  d  S(   N(   R�   (   R@   R�   (    (    s   latinsearch.pywRA   �  s    c         C� s:   |  j  j d � d k r d  S|  j  j �  |  j | � d  S(   Nu   stateu   disable(   R�   R�   R�   R�   (   R@   R�   (    (    s   latinsearch.pywR�   �  s    c         C� sK   t  j |  j d d �} | j d d d |  j � | j | j | j � d S(   u   Build right click menuR�   i    R�   u   CopyR�   N(   R�   R�   R�   R�   R�   R�   R�   R�   (   R@   R�   R�   (    (    s   latinsearch.pywR�   �  s    c         C� s   |  j  j d � d  S(   Nu   <<Copy>>(   R�   R�   (   R@   (    (    s   latinsearch.pywR�   �  s    (   R[   R\   R]   RA   R�   R�   R�   (    (    (    s   latinsearch.pywR�   t  s
   				t   RightClickMenuForScrolledTextc           B� sh   e  Z d  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z	 d �  Z
 d	 �  Z d
 �  Z RS(   u>   Simple widget to add basic right click menus to entry widgets.c         � sQ   | �  _  �  j  j d �  f d �  d d ��  j  j d �  f d �  d d �d  S(   Nu   <Control-a>c         � s
   �  j  �  S(   N(   R�   (   R�   (   R@   (    s   latinsearch.pywRB   �  s    R�   u   +u   <Control-A>c         � s
   �  j  �  S(   N(   R�   (   R�   (   R@   (    s   latinsearch.pywRB   �  s    (   R�   R�   (   R@   R�   (    (   R@   s   latinsearch.pywRA   �  s    	"c         C� s=   |  j  j d � t j k r d  S|  j  j �  |  j | � d  S(   Nu   state(   R�   R�   R�   t   DISABLEDR�   R�   (   R@   R�   (    (    s   latinsearch.pywR�   �  s    c         C� s�   t  j |  j d d �} | j d d d |  j � | j d d d |  j � |  j �  rr | j d d d |  j � n | j d d d d	 � | j d d
 d |  j � | j	 �  | j d d d |  j
 � | j d d d |  j � | j | j | j � d S(   u
   build menuR�   i    R�   u   CopyR�   u   Cutu   PasteR�   u   disableu   Deleteu
   Select Allu	   Clear AllN(   R�   R�   R�   R�   R�   R�   t   _paste_string_statet   _paste_if_string_in_clipboardt   _deleteR�   R�   t
   _clear_allR�   R�   R�   (   R@   R�   R�   (    (    s   latinsearch.pywR�   �  s    
c         C� s   |  j  j d � d  S(   Nu   <<Cut>>(   R�   R�   (   R@   (    (    s   latinsearch.pywR�   �  s    c         C� s   |  j  j d � d  S(   Nu   <<Copy>>(   R�   R�   (   R@   (    (    s   latinsearch.pywR�   �  s    c         C� s   |  j  j d � d  S(   Nu	   <<Clear>>(   R�   R�   (   R@   (    (    s   latinsearch.pywR�   �  s    c         C� s   |  j  j d � d  S(   Nu	   <<Paste>>(   R�   R�   (   R@   (    (    s   latinsearch.pywR�   �  s    c         C� s=   |  j  j d d d � |  j  j d d � |  j  j d � d S(   u
   select allu   selu   1.0u   end-1cu   insertu   break(   R�   t   tag_addt   mark_sett   see(   R@   (    (    s   latinsearch.pywR�   �  s    c         C� s(   y |  j  j d d � } Wn t SXt S(   u,   Returns true if a string is in the clipboardR�   u	   CLIPBOARD(   R�   R�   R^   R=   (   R@   R�   (    (    s   latinsearch.pywR�   �  s
    c         C� s   |  j  j d d � d S(   u	   Clear allu   1.0u   endN(   R�   t   delete(   R@   (    (    s   latinsearch.pywR�   �  s    (   R[   R\   R]   RA   R�   R�   R�   R�   R�   R�   R�   R�   R�   (    (    (    s   latinsearch.pywR�   �  s   					!						t   AutocompleteGUIc           B� s�   e  Z d  Z d g  i  d � Z d �  Z d �  Z d �  Z d �  Z d �  Z	 d �  Z
 d �  Z d	 �  Z d
 �  Z d �  Z d �  Z d �  Z e d � Z e d �  � Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z RS(   u&   The main GUI for autocomplete program.c         C� s�   t  j j |  | � | |  _ | |  _ g  |  _ |  j j d � |  j j d t	 � |  j
 �  |  j �  |  j �  |  j �  |  j �  |  j �  |  j �  d  S(   Nu   1400x800u   Latin Finder %s(   R�   t   FrameRA   R1   R`   t   historyt   mastert   geometryt   titlet   __version__t	   set_stylet   create_menu_bart   create_widgetst   grid_configuret   row_and_column_configuret   create_right_menut	   bind_func(   R@   R�   R1   R`   (    (    s   latinsearch.pywRA   �  s    			





c         C� s\   t  j �  } | j d d d �| j d d d �| j d d d �| j d	 d d
 �d S(   u)   Set style for widgets in the main window.u	   TComboboxt   paddingi   u   auto.TComboboxt
   foregroundu   redu   TButtoni
   u   open.TButtonu   blueN(   R   t   Stylet	   configure(   R@   t   s(    (    s   latinsearch.pywR�     s
    c         C� s�  t  j |  j � |  _ t  j |  j d d �|  _ |  j j d d d |  j � |  j j �  |  j j d d d |  j j � |  j j	 d d d |  j � t  j |  j d d �} | j d d	 d |  j
 � | j d d
 d |  j � |  j �  r| j d d d |  j � n | j d d d d �  � | j d d d |  j � |  j j	 d d d | � t  j |  j d d �|  _ |  j j d d d |  j � |  j j d d d |  j � |  j j	 d d d |  j � |  j j d |  j � d S(   u#   Create menubar for the main window.R�   i    R�   u   Save result to file...R�   u   Exitu   FileR�   u   Copyu   Cutu   Pastec           S� s
   t  d � S(   Nu   No string in clipboard!(   t   print(    (    (    s   latinsearch.pywRB   1  s    u   Deleteu   Editu   Helpu   AboutN(   R�   R�   R�   t   menubart	   file_menuR�   t   _ask_save_fileR�   t   quitt   add_cascadeR�   R�   R�   R�   R�   t	   help_menut   _display_helpt   _display_aboutt   config(   R@   t	   edit_menu(    (    s   latinsearch.pywR�     s6    
	

c         C� s,  t  j |  j d d �|  _ |  j j d d d d d t j t j t j t j	 � t  j
 |  j d d �|  _ |  j j �  t  j |  j d	 d
 d d �|  _ t  j |  j d	 d d d �|  _ t  j |  j d	 d �|  _ t j |  j d d �|  _ t  j |  j � |  _ t  j |  j d	 d �|  _ t j |  j d d �|  _ t  j |  j � |  _ t  j |  j d	 d �|  _ t j |  j d d �|  _ t  j |  j � |  _ t  j |  j d	 d �|  _ t j |  j d d �|  _ t  j |  j � |  _ t  j |  j d	 d �|  _ t  j! |  j d d �|  _" |  j# �  d S(   u'   Create widgets for the main GUI window.R�   i   t   rowi    t   columnt   stickyt   styleu   auto.TComboboxR�   u   Search Offlineu   copy.TButtonu   Search Internetu"   Candidates (Startswith / Endswith)t   fontu	   Monospacei
   u   Candidates (Contains)u   Candidates (Rank by similarity)u.   Candidates (Spell check, single edit distance)u]   Click "Do Query" button and see results. ** Double Click ** candidate to see detailed result.N(   u	   Monospacei
   (   u	   Monospacei
   (   u	   Monospacei
   (   u	   Monospacei
   (   u	   Monospacei
   ($   R   R�   R�   t   contentt   gridR�   t   Wt   Et   Nt   St   Comboboxt	   input_boxt   focust   Buttont   search_offline_buttont   search_internet_buttont   Labelt   label_1t   Listboxt   listbox1t	   Scrollbart
   scrollbar1t   label_2t   listbox2t
   scrollbar2t   label_3t   listbox3t
   scrollbar3t   label_4t   listbox4t
   scrollbar4t   label_5t   stt   ScrolledTextt   scrolled_text_5R�   (   R@   (    (    s   latinsearch.pywR�   A  sJ    7					c      	   C� s*  |  j  j �  |  j j d d d d d d d d � |  j j d d d d	 d d � |  j j d d d d
 d d � |  j j d d d d d d d d � |  j j d d d d d d d d � |  j j d d d d d d � |  j j d |  j j	 � |  j j d |  j j
 � |  j j d d d d d d d d � |  j j d d d d d d d d � |  j j d d d d d d � |  j j d |  j j	 � |  j j d |  j j
 � |  j j d d d d d d d d � |  j j d d d d d d d d � |  j j d d d d d d � |  j j d |  j j	 � |  j j d |  j j
 � |  j j d d d d	 d d d d � |  j j d d d d	 d d d d � |  j j d d d d d d � |  j j d |  j j	 � |  j j d |  j j
 � |  j j d d d d d d d d � |  j j d d d d d d d d � d S(   u)   Grid configuration of window and widgets.R�   i    R�   i   t
   columnspani	   R�   u   wensi
   i   i   u   wsi   u   nst   yscrollcommandR�   i   u   wi   i   i   N(   R�   R�   R�   R  R  R  R  R	  R�   R+   t   yviewR
  R  R  R  R  R  R  R  R  R  R  (   R@   (    (    s   latinsearch.pywR�   |  s6    %%%%%%%%%%c         C� s�  |  j  j d d d �|  j  j d d d �|  j j d d d �|  j j d d d �|  j j d d d �|  j j d d d �|  j j d d d �|  j j d d d �|  j j d d d �|  j j d d d �|  j j d d d �|  j j d d d �|  j j d d d �|  j j d d d �|  j j d	 d d �|  j j d
 d d �|  j j d d d �|  j j d d d �|  j j d d d �|  j j d d d �d S(   u   Rows and columns configurationi    t   weighti   i   i   i   i   i   i   i   i	   i
   i   i   N(   R�   t   rowconfiguret   columnconfigureR�   (   R@   (    (    s   latinsearch.pywR�   �  s(    c         C� sH   t  |  j � } |  j j d | � t |  j � } |  j j d | � d  S(   Nu
   <Button-3>(   R�   R�   R�   R�   R  (   R@   t   right_menu_input_boxt   right_menu_scrolled_text_5(    (    s   latinsearch.pywR�   �  s
    c         � sf   �  j  �  j d <�  j �  j d <�  f d �  } x0 �  j �  j �  j �  j g D] } | | � qN Wd  S(   Nu   commandc         � s<   �  j  d � �  f d �  � t �  � } �  j  d | � d S(   u�   Bind command to listbox.

            Double click on candidates from any column from the four,
            then the result will be on the output area.
            u   <Double-Button-1>c         � s   �  j  � � S(   N(   t   _display_search_result(   R�   (   R@   t   widget(    s   latinsearch.pywRB   �  s    u
   <Button-3>N(   R�   R�   (   R   t   right_menu_widget(   R@   (   R   s   latinsearch.pywt   bind_command_to_listbox�  s    	(   t   _display_candidatesR  t   _query_baidu_baikeR  R  R  R  R  (   R@   R"  t   listbox(    (   R@   s   latinsearch.pywR�   �  s    c         C� s  |  j  j �  j �  } t |  j |  j � } i g  d 6g  d 6g  d 6d d 6} | r| |  j k r� | j | d t t t t f �} qd | k r� | j | d t t t t f �} q| d t	 j
 k r� | j | d t t t t f �} q| j | d t t t t f �} n  | S(	   u0   Command of Do Query button with multi-processingu   0u   1u   2u    u   3Ry   u    i    (   R�   Rd   R   R_   R1   R`   R~   R=   R^   t   stringt	   printable(   R@   Rb   t   query_word_objectRc   (    (    s   latinsearch.pywt   _query_offline_data�  s*    "c         C� sX   |  j  j �  j �  } | s d St j t j | � � } d | } |  j |  j | � d  S(   Nu    u   百度百科：

%s



(   R�   Rd   R   R�   R�   R�   t   _insert_to_text_areaR  (   R@   R�   R�   (    (    s   latinsearch.pywR$    s    
c         C� sO   |  j  j �  j �  } | s d St j | � } d | } |  j |  j | � d  S(   Nu    u   维基百科：

%s



(   R�   Rd   R   R�   R�   R*  R  (   R@   R�   t   wikipedia_result(    (    s   latinsearch.pywt   _query_wikipedia!  s    
c         C� s�   |  j  |  j g } t d � |  j j d d � |  j j �  xZ t | � D]L \ } } t d | � t d | � } | j t	 � | j
 �  t j d � qI Wd  S(   Nu!   开始搜索，请耐性等待...u   1.0u   end-1cu   start: Rw   g�������?(   R$  R,  R�   R  R�   t   update_idletasksR   R   t	   setDaemonR=   Rx   t   timet   sleep(   R@   t	   func_listR$   R|   t   thread(    (    s   latinsearch.pywt   _query_internet_multithreading+  s    

c         C� s�   |  j  �  } |  j j d d � x% | d D] } |  j j d | � q* W|  j j d d � x% | d D] } |  j j d | � qe W|  j j d d � x% | d D] } |  j j d | � q� W|  j j d d � |  j j d | d � d  S(   Nu   0u   endu   1u   2u   3(   R)  R  R�   t   insertR  R  R  (   R@   Rc   t   item(    (    s   latinsearch.pywR#  <  s    c         C� s�  | j  d � } |  j j d t j � |  j j t j | � |  j j d d � |  j j  | � } | r�t rvt d d d d d	 d
 d g � } x d D] } d | j	 | <q� Wd | _
 x� | D]{ } g  | d j �  D] } | t k r� | ^ q� }	 t d j |	 � }
 g  | D] } | ^ q
} | j |
 � | j | � q� W|  j j d | j �  � |  j j t j � |  j j �  q�|  j j d d d d � xN | D]C } d j | � } |  j j d | � |  j j d d d d � q�Wn  d S(   u2   Clean content in Output Area and insert new value.u   activei    u   0.1u   end-1cu   Short Pinyinu   Long Pinyinu   Chineseu   Latinu   Nameru   Data Sourceu   Web URLu   li   i   u   %20u   endu[  请安装 prettytable 以获得更清晰的结果视图。
安装方法： pip install prettytable

+--------------+-------------+---------+-------+-------+-------------+---------+
| Short Pinyin | Long Pinyin | Chinese | Latin | Namer | Data Source | Web URL |
+--------------+-------------+---------+-------+-------+-------------+---------+

%s
u   =id   u     |  u   
%s
u   -N(   u   Short Pinyinu   Long Pinyinu   Chineseu   Latinu   Nameru   Data Sourceu   Web URL(   Rd   R�   R�   R�   t   ENDR4  R  R`   R   t   alignt   padding_widthR   t   SPECIAL_CHARSt   FRPS_BASE_URLR�   R   t   add_rowt
   get_stringR�   R-  (   R@   R   t   is_clean_wordt   selection_valuet   resultt   tableR�   t   each_resultR   t   normal_word_listR�   RC   RJ   R   (    (    s   latinsearch.pywR  Q  s@    	
		c         C� s.   |  j  d d � |  j d | � |  j �  d S(   u<   Clear original content from ScrolledText area and insert newu   1.0u   endN(   R�   R4  R-  (   t	   st_widgetR�   (    (    s   latinsearch.pywR*  �  s    c         C� s   |  j  j �  j d � d  S(   Nu   <<Copy>>(   R�   t	   focus_getR�   (   R@   (    (    s   latinsearch.pywR�   �  s    c         C� s   |  j  j �  j d � d  S(   Nu   <<Cut>>(   R�   RD  R�   (   R@   (    (    s   latinsearch.pywR�   �  s    c         C� s   |  j  j �  j d � d  S(   Nu	   <<Paste>>(   R�   RD  R�   (   R@   (    (    s   latinsearch.pywR�   �  s    c         C� s   |  j  j �  j d � d  S(   Nu	   <<Clear>>(   R�   RD  R�   (   R@   (    (    s   latinsearch.pywR�   �  s    c         C� s(   y |  j  j d d � } Wn t SXt S(   u,   Returns true if a string is in the clipboardR�   u	   CLIPBOARD(   R�   R�   R^   R=   (   R@   R�   (    (    s   latinsearch.pywR�   �  s
    c         C� ss   t  j d d d d � } | d k r( d S|  j j d d � j d � } | j | j d � j d	 � � | j �  d S(
   u   Dialog to open file.t   modeu   wt   defaultextensionu   .txtNu   1.0u   end-1cu   GBKu   utf-8(	   t   tkFileDialogt   asksaveasfileR3   R  Rd   R�   t   writeR   t   close(   R@   RI   t   text_to_save(    (    s   latinsearch.pywR�   �  s    c         C� s*   |  j  j d d � |  j  j d t � d  S(   Nu   0.1u   end-1cu   end(   R  R�   R4  t
   USAGE_INFO(   R@   (    (    s   latinsearch.pywR�   �  s    c         C� s*   |  j  j d d � |  j  j d t � d  S(   Nu   0.1u   end-1cu   end(   R  R�   R4  t
   ABOUT_INFO(   R@   (    (    s   latinsearch.pywR�   �  s    N(   R[   R\   R]   R3   RA   R�   R�   R�   R�   R�   R�   R�   R)  R$  R,  R3  R#  R=   R  R   R*  R�   R�   R�   R�   R�   R�   R�   R�   (    (    (    s   latinsearch.pywR�   �  s0   		1	;	0		
		(		
		3								c         C� s{   t  �  \ }  } t j |  � } t j | � } t t d � � } | j | � Wd QXt t d � � } | j | � Wd QXd S(   ub   Dump generated dictinary to pickle raw file.

    Generally, this function need only do once.
    u   wbN(   R2   t   picklet   dumpsR
   t   PICKLE_KEYS_FILERI  t   PICKLE_DICT_FILE(   R1   R`   t   pickle_keyst   pickle_dictt   f_out(    (    s   latinsearch.pywt   dump_with_pickle�  s    c         C� sp   t  |  d � �" } | j �  } t j | � } Wd QXt  | d � �" } | j �  } t j | � } Wd QX| | f S(   u'   Load keys and dict from pickle raw fileu   rbN(   R
   t   readRN  t   loads(   t   pickle_keys_filet   pickle_dict_fileR   RR  R1   RS  R`   (    (    s   latinsearch.pywt   load_with_pickle�  s    c          C� sD   t  t t � \ }  } t |  � a t d |  d | � } | j �  d S(   u   The main GUI program.R1   R`   N(   RZ  RP  RQ  R8   Ru   R�   t   mainloop(   R1   R`   t   app(    (    s   latinsearch.pywt   gui_main�  s    	c           C� s   t  �  d S(   u	   Main funcN(   R2   (    (    (    s   latinsearch.pywt   main�  s    u   __main__(K   R]   t
   __future__R    R   R   t   osR�   R   R�   t	   threadingR   R�   R/  t   bs4R   t   cPickleRN  t   ImportErrorR&  RE   t   difflibR   t   multiprocessingR   t   prettytableR   R3   R   t   TkinterR�   R   RG  R  R  t   tkintert   tkinter.scrolledtextt   scrolledtextR	   R�   t
   __author__t   _historyt   patht   abspathR(   RP  RQ  R:  Rq   Ro   R9  t   objectRu   R�   R�   R�   RL  RM  R   R   R'   R2   R7   R8   R_   R�   R�   R�   R�   R�   R�   RU  RZ  R]  R^  R[   (    (    (    s   latinsearch.pywt   <module>   s�   
	)
			#			N�9c#Z� �				