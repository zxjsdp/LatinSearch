�
��'Wc           @� s.  d  Z  d d l m Z m Z m Z d d l Z e j j d d � d d l Z d d l	 Z	 d d l
 Z
 d d l Z d d l Z d d l m Z d d l m Z y d d l Z Wn e k
 r� d d l Z n Xd d l Z d d l Z d d l m Z d d	 l m Z y d d
 l m Z Wn e k
 r2e Z n Xe j d d k ryd d l Z d d l  Z  d d l! Z! d d l" Z# nQ e j d d k r�d d l$ Z d d l$ m  Z  d d l% j& Z# d d l$ m' Z! n  d Z( d Z) g  Z* e j j+ d � Z, e j j+ d � Z- e j j+ d � Z. d Z/ d Z0 d Z1 d d d d d d d d d d  d! d" d# d$ d% g Z2 d& d' d( g Z3 e4 �  a5 d) Z6 d* Z7 i d+ d, 6Z8 i	 i d- d. 6d/ d0 6d1 6i d2 d3 6d4 d5 6d6 d7 6d8 d9 6d: d; 6d< d= 6d> d? 6d@ dA 6dB dC 6dD dE 6dD dF 6dG dH 6dI 6i dJ dK 6dL dM 6dN dO 6dP dQ 6dR 6i dS dT 6dU dV 6dW 6i dX dY 6dZ d[ 6d\ d] 6d^ d_ 6d` da 6db 6i dc dd 6de df 6dg dh 6di dj 6dk dl 6dm dn 6do dp 6dq dr 6ds dt 6do du 6dv dw 6dx dy 6dz d{ 6d| d} 6d~ d 6d� d� 6d� d� 6d� 6i d: d; 6d< d= 6d> d? 6dB dC 6d� d� 6d� 6i d: d; 6d� 6i d: d; 6d< d= 6d> d? 6dB dC 6d� d� 6d� d� 6d� 6Z9 i	 i d- d. 6d� d0 6d1 6i d� d3 6d� d5 6d� d7 6d� d9 6d� d; 6d� d= 6d� d? 6d� dA 6d� dC 6d� dE 6d� dF 6d� dH 6dI 6i d� dK 6d� dM 6d� dO 6d� dQ 6dR 6i d� dT 6d� dV 6dW 6i d� dY 6d� d[ 6d� d] 6d� d_ 6d� da 6db 6i d� dd 6d� df 6d� dh 6d� dj 6d� dl 6d� dn 6d� dp 6d� dr 6d� dt 6d� du 6d� dw 6d� dy 6d� d{ 6d� d} 6d� d 6d� d� 6d� d� 6d� 6i d� d; 6d� d= 6d� d? 6d� dC 6d� d� 6d� 6i d� d; 6d� 6i d� d; 6d� d= 6d� d? 6d� dC 6d� d� 6d� d� 6d� 6Z: e: Z; d� e( Z< d� e( e) f Z= d� �  Z> d� �  Z? d� �  Z@ d� �  ZA d� �  ZB d� e4 f d� �  �  YZC d� e4 f d� �  �  YZD d� e4 f d� �  �  YZE d� e4 f d� �  �  YZF d� e4 f d� �  �  YZG d� e4 f d� �  �  YZH d� e jI f d� �  �  YZJ d� �  ZK d� �  ZL d� �  ZM d� �  ZN eO d� k r*eM �  n  d S(�   u   Latin Search programi����(   t   print_functiont   unicode_literalst   with_statementNi    u   lib.zip(   t   Thread(   t   BeautifulSoup(   t   SequenceMatcher(   t   Process(   t   PrettyTableu   2u   3(   t   ttk(   t
   filedialogu   v0.3.0u   Jinu   data/latin_without_sougou.csvu   data/latin_60000.keys.pickleu   data/latin_60000.dict.pickleu   http://frps.eflora.cn/frps/i   g333333�?u   ×u   〔u   ）u   【u   】u   u   u   <u   >u   *u   [u   @u   ]u   ［u   |u    u    u   	u   http://www.baidu.com/s?wd=u   https://zh.wikipedia.org/wiki/us   Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36u
   User-Agentu   1400x800u   geometryu   Latin Finderu
   main_titleu   main_windowu   Fileu   file_cascadeu   Save result to file...u   saveu   Exitu   exitu   Editu   edit_cascadeu   Copyu   copyu   Cutu   cutu   Pasteu   pasteu   No string in clipboard!u   no_str_in_clipboard_warningu   Deleteu   deleteu   Helpu   help_cascadeu   helpu   Aboutu   aboutu   menu_baru   Configurationsu   config_labelu   Turn off similarity searchu   similarity_search_switchu   Turn off spell checku   spell_check_switchu   Match whole wordu   match_whole_wordu   configu   Search Offlineu   search_offline_buttonu   Search Internetu   search_internet_buttonu   buttonsu"   Candidates (Startswith / Endswith)u   startswith_endswith_labelu   Candidates (Contains)u   contains_labelu   Candidates (Rank by similarity)u   similarity_labelu.   Candidates (Spell check, single edit distance)u   spell_check_labelu]   Click "Do Query" button and see results. ** Double Click ** candidate to see detailed result.u   default_status_labelu   labelsu   Blank query !!u   blank_query_labelu%   Searching Baidu Baike! Please wait...u   searching_baidu_baikeu#   Searching Wikipedia! Please wait...u   searching_wikipediau   Start searching! Please wait...u   start_searchingu   Search complete!u   search_completeu,   Start searching offline data. Please wait...u   start_offline_searchu*   Baidu Baike searching complete! Time used:u   offline_search_complete_1u:   . Double click candidate words to see detailed informationu   offline_search_complete_2u   Baidu Baike:u   baike_result_infou   baike_search_completeu   No result from Baidu Baike!u   baike_no_resultu
   Wikipedia:u   wikipedia_result_infou(   Wikipedia searching complete! Time used:u   wikipedia_search_completeu   No result from Wikipedia!u   wikipedia_no_resultuB   Please install "prettytable" to get nicer result.
How to install: u   pretty_table_install_infou	   Attributeu   baidu_result_attru   Valueu   baidu_result_valueu	   info_textu
   Select Allu
   select_allu   right_click_menuu   right_click_menu_listboxu	   Clear Allu	   clear_allu   right_click_menu_stu!   拉丁名搜索（Latin Finder）u   文件u   结果另存为...u   退出u   编辑u   复制u   剪切u   粘贴u$   剪切板中无可粘贴的内容！u   删除u   帮助u   帮助信息u   关于u   配置区域u   关闭相似值搜索u   关闭拼写检查u   全字匹配u   搜索离线数据u   网络搜索u   候选词（起始/结尾）u   候选词（包括）u   候选词（相似度搜索）u   候选词（拼写检查）u�   提示：1. 搜索离线数据后，双击上方的某个候选词，以查看对应的离线信息。  2. 离线搜索 / 网络搜索默认均开启模糊搜索。  3. 使用精确的搜索词可大幅提升搜索速度。u   空的查询u'   正在搜索百度百科，请稍候...u'   正在搜索维基百科，请稍候...u!   开始搜索，请耐性等待...u   搜索完成！u'   开始搜索离线数据，请稍候...u$   离线数据搜索完成！用时：u'   。双击候选词以查看详细信息u   百度百科：u$   百度百科搜索完成！用时：u$   查询百度百科未找到结果！u   维基百科：u$   维基百科搜索完成！用时：u$   查询维基百科未找到结果！uJ   请安装 prettytable 以获得更清晰的结果视图。
安装方法：u   属性u   搜索结果u   全部选择u   清空u�  
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
c         C� s&   t  |  d � � } | j �  SWd QXd S(   u%   Read file and return a list of lines.u   rN(   t   opent	   readlines(   t	   file_namet   f_in(    (    s   latinsearch.pywt	   get_linesD  s    c   
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
   R   t   column_list_1t   column_list_2t   column_list_3t   column_list_4t   detailed_info_tuple_listR   t   linet   xt   elements(    (    s   latinsearch.pywt   get_key_value_pairs_from_fileJ  s    (	c         C� sq   i  } xd t  t |  | � � D]M \ } \ } } | | k rX g  | | <| | j | � q | | j | � q W| S(   u�   
    Generate a dictionary from two lists. keys may be duplicated.

    >>> get_one_to_more_dict(['a', 'b', 'a', 'a'], [1, 2, 3, 4])
    {'a': [1, 3, 4], 'b': [2]}
    (   t	   enumeratet   zipR   (   t   key_listt
   value_listt	   _out_dictt   it   keyt   value(    (    s   latinsearch.pywt   get_one_to_more_dictm  s    (
c          C� s�   t  t � \ }  } } } } t |  | � } t | | � } t | | � } t | | � } x- | | | f D] }	 |	 rg | j |	 � qg qg Wt t |  | | | � � }
 |
 | f S(   uC   Combine dicts, each with one column as key and whole line as value.(   R   t	   DATA_FILER'   t   updatet   listt   set(   R   R   R   R   R   t   dict_1t   dict_2t   dict_3t   dict_4t	   each_dictt   keys_for_all(    (    s   latinsearch.pywt   get_dict_for_all_columns  s    c         C� s   t  d |  | � j �  S(   un   Return similarity of two strings.

    [Example]
        >>> get_similarity('abcde', 'bcdef')
        0.8
    N(   R   t   Nonet   ratio(   t   str_at   str_b(    (    s   latinsearch.pywt   get_similarity�  s    t
   SpellCheckc           B� sG   e  Z d  Z d �  Z e d � Z d �  Z d �  Z d �  Z d �  Z	 RS(   uW  Train data set with given data then do spell check for given word.

    [Example]
        >>> s = SpellCheck(['abcd', 'fghi'])
        >>> s.correct('abci')
        'abcd'

    [Reference]
        [1]: Title:   How to Write a Spelling Corrector
             Author:  Peter Norvig
             Webpage: http://norvig.com/spell-correct.html
    c         C� s:   | |  _  |  j �  |  _ |  j d t � |  _ d |  _ d  S(   Nt   loweruB   abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-.:1234567890(   t   candidate_listt   traint   NWORDSt   Truet   NWORDS_lowert   alphabet(   t   selfR:   (    (    s   latinsearch.pywt   __init__�  s    	c         C� s�   |  j  s t d � � n  t j d �  � } | sW x[ |  j  D] } | | c d 7<q: Wn7 |  j  } x* t d �  | � D] } | | c d 7<qt W| S(   u   Train model with data set.u*   Blank training list (Choosed blank file?).c           S� s   d S(   Ni   (    (    (    (    s   latinsearch.pywt   <lambda>�  s    i   c         S� s
   |  j  �  S(   N(   R9   (   t   _(    (    s   latinsearch.pywRB   �  s    (   R:   t
   ValueErrort   collectionst   defaultdictt   map(   R@   R9   t   modelt   ft   tmp_list(    (    s   latinsearch.pywR;   �  s    	
c      	   C� s  t  | � } t g  t | � D] } | d | !| | d ^ q g  t | d � D]3 } | d | !| | d | | | | d ^ qO g  t | � D]3 } |  j D]# } | d | !| | | d ^ q� q� g  t | d � D]/ } |  j D] } | d | !| | | ^ q� q� � S(   u�   Words that has one edit distance.

        1. deletion
        2. transposition
        3. alteration
        4. insertion
        i    i   i   (   t   lenR+   t   rangeR?   (   R@   t   wordt   nR$   t   c(    (    s   latinsearch.pywt   edits1�  s    �c         � s#   t  �  f d �  �  j | � D� � S(   u!   Words that has two edit distance.c         3� s@   |  ]6 } �  j  | � D]  } | j �  �  j k r | Vq q d  S(   N(   RP   R9   R>   (   t   .0t   e1t   e2(   R@   (    s   latinsearch.pyws	   <genexpr>�  s    (   R+   RP   (   R@   RM   (    (   R@   s   latinsearch.pywt   known_edits2�  s    c         � s   t  �  f d �  | D� � S(   u   Known words.c         3� s*   |  ]  } | j  �  �  j k r | Vq d  S(   N(   R9   R>   (   RQ   t   w(   R@   (    s   latinsearch.pyws	   <genexpr>�  s    (   R+   (   R@   t   words(    (   R@   s   latinsearch.pywt   known�  s    c         � sL   �  j  | g � p0 �  j  �  j | � � p0 | g } t | d �  f d �  �S(   u9   Do spell check and correct word if word was wrong spelledR%   c         � s   �  j  |  S(   N(   R>   (   RU   (   R@   (    s   latinsearch.pywRB   �  s    (   RW   RP   t   max(   R@   RM   t
   candidates(    (   R@   s   latinsearch.pywt   correct�  s    *	(
   t   __name__t
   __module__t   __doc__RA   t   FalseR;   RP   RT   RW   RZ   (    (    (    s   latinsearch.pywR8   �  s   				t	   QueryWordc           B� st   e  Z d  Z d �  Z e e e d � � Z e e e d � � Z e e e d � � Z	 e e e d � � Z
 d �  Z RS(   u�  Query with 4 strategy with multi-processing.

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
    c         C� s\   g  | D] } | j  �  r | j  �  ^ q |  _ | |  _ t | � |  _ d |  _ i  |  _ d  S(   Nu    (   R   R1   t   dict_for_allR8   t   trained_objectt   queryt   result_dict(   R@   R1   R`   R   (    (    s   latinsearch.pywRA     s    !		c         C� s  g  } | r� |  | k r� | j  |  � | rC | j i | d 6� d S| j |  � d } x= | d  D]. } | j �  ra | |  k ra | j  | � qa qa Wn  xZ t | � D]I \ }	 }
 |
 j |  � s� |
 j |  � r� |
 |  k r� | j  |
 � q� q� q� Wn  | j i | d 6� d S(   u   Check startswith & endswithu   0Ni    i   (   R   R)   t   getR   R   t
   startswitht   endswith(   Rb   R1   R`   Rc   t   match_whole_wordt   turn_ont	   _tmp_listt   result_elementst   eachR$   t	   candidate(    (    s   latinsearch.pywt   get_starts_with_candidates%  s"    c         C� s�   g  } | r� |  | k r� | j  |  � | rC | j i | d 6� d S| j |  � d } x= | d  D]. } | j �  ra | |  k ra | j  | � qa qa Wn  xH t | � D]7 \ }	 }
 |  |
 k r� |
 |  k r� | j  |
 � q� q� q� Wn  | j i | d 6� d S(   u   Check containsu   1Ni    i   (   R   R)   Rd   R   R   (   Rb   R1   R`   Rc   Rg   Rh   Ri   Rj   Rk   R$   Rl   (    (    s   latinsearch.pywt   get_contains_candidatesB  s     c         C� s   g  } g  } | r* | j  i g  d 6� d S| r� t | j d � � d k r� xK t | � D]= \ } }	 t |	 |  � }
 |
 t k rX | j |
 |	 f � qX qX W| j d d �  d t � | t	  } | r� g  | D] } | d ^ q� n g  } n  | j  i | d 6� d S(	   u   Rank candidates by similarityu   2Nu   1i    R%   c         S� s   |  d S(   Ni    (    (   R   (    (    s   latinsearch.pywRB   o  s    t   reversei   (
   R)   RK   Rd   R   R7   t   SIMILARITY_THRESHOLDR   t   sortR=   t   SIMILAR_RESULT_NUM_LIMIT(   Rb   R1   R`   Rc   Rg   Rh   Ri   t   _similar_hitsR$   Rl   t   _similarityRC   (    (    s   latinsearch.pywt   get_similar_candidates^  s    !
,c         C� so   d } | r$ | j  i d d 6� d S| rW t | j d � � d k rW t j |  � } n  | j  i | d 6� d S(   u   Get spell check candicatesu    u   3Nu   1i    (   R)   RK   Rd   t   TRAINED_OBJECTRZ   (   Rb   R1   R`   Rc   Rg   Rh   Rl   (    (    s   latinsearch.pywt   get_spell_check_candidatey  s    !c   
      C� s�   | |  _  i  } t j t j g } t j t j g } xU t | � D]G \ } } t d | |  j  |  j |  j	 | | | | � � }	 |	 j
 �  q@ WxY t | � D]K \ } } t d | |  j  |  j |  j	 | | | | d � � }	 |	 j
 �  q� W| S(   u   Get four resultst   targeti   (   Rb   R_   Rm   Rn   Ru   Rw   R   R   R1   R`   t   start(
   R@   Rb   Rg   t   turn_on_modeRc   t   func_list_1t   func_list_2R$   t	   each_funct   p(    (    s   latinsearch.pywt   query_all_four�  s"    			(   R[   R\   R]   RA   t   staticmethodR^   R=   Rm   Rn   Ru   Rw   R   (    (    (    s   latinsearch.pywR_   �  s   $	t   InternetQueryc           B� s5   e  Z e d  �  � Z e d �  � Z e d �  � Z RS(   c   
      C� s  t  t j |  j d � � } t j �  } | j | d t �} d | _ t	 | j
 d � } | j d i d d 6� } | d j d	 t � j d
 � } | j | d t �} d | _ t	 | j
 d � } | j d i d d 6� } t j d � } | r| j | j
 � }	 d j |	 � Sd S(   u5   Search baidu and retrive content from first baike URLu   GBKt   headersu   utf-8u   html.parseru   h3u   c-gap-bottom-smallu   classi    t   hrefu   hrefu   divu   basic-info cmn-clearfixu   [^\n]+u   
u    (   t   BAIDU_BAIKE_BASE_URLt   urllibt   quotet   encodet   requestst   sessionRd   t   HEADERt   encodingR   t   textt   findAllt   findR=   t   ret   compilet   findallt   join(
   t   keywordt   urlR�   t   reqt   soupt   outcomest   first_baike_urlt   main_contentt
   re_newlinet   out_list(    (    s   latinsearch.pywt   search_baidu_baike�  s     		c         C� s�  g  } g  |  j  �  D] } | j �  r | j �  ^ q } t rTt t j d � j d � t j d � j d � g � } xE t j d � j d � t j d � j d � f D] } d | j | <q� Wd | _ g  } x} t | � D]o \ } } | d d k r&x  t D] }	 | j	 |	 d � } q� W| j
 | � q� | j
 | � | j | � g  } q� W| j �  Sd }
 xZ t | � D]L \ } } | d d k r�| j	 d	 d � }
 qg|
 d
 | }
 | j
 |
 � qgWd j | � Sd  S(   Nu	   info_textu   baidu_result_attru   baidu_result_valueu   li   i   i    u    u    u   		| u   
(   t
   splitlinesR   R   t   CURRENT_TEXT_DICTRd   t   alignt   padding_widthR   t   SPECIAL_CHARS_IN_BAIDU_RESULTt   replaceR   t   add_rowt
   get_stringR�   (   t   baike_resultR�   R   t   linest   tablet   columnt   list_for_each_lineR$   R   t	   each_chart   temp_str(    (    s   latinsearch.pywt   prettify_baike_result�  s8    1	

c   	      C� s�   g  } t  t j |  j d d � j d � � } t j �  } | j | d t �} t	 | j
 d � } | j d i d d 6� } | s� d	 S| j d
 � } x9 | D]1 } | r� | j | j
 j �  j d d � � q� q� Wd j | � S(   u   Search glossary from Wikipedia.u    u   _u   GBKR�   u   html.parseru   tableu   infobox biotau   classu    u   tdu   
(   t   WIKIPEDIA_BASE_URLR�   R�   R�   R�   R�   R�   Rd   R�   R   R�   R�   t   find_allR   R   R�   (	   R�   R�   R�   R�   R�   R�   t   outt   td_outRk   (    (    s   latinsearch.pywt   search_wikipedia�  s    %)(   R[   R\   R�   R�   R�   R�   (    (    (    s   latinsearch.pywR�   �  s   #t   RightClickMenuc           B� s_   e  Z d  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z	 d �  Z
 d	 �  Z RS(
   u5  
    Simple widget to add basic right click menus to entry widgets.

    usage:

    rclickmenu = RightClickMenu(some_entry_widget)
    some_entry_widget.bind("<3>", rclickmenu)

    If you prefer to import Tkinter over Tix, just replace all Tix
    references with Tkinter and this will still work fine.
    c         � sQ   | �  _  �  j  j d �  f d �  d d ��  j  j d �  f d �  d d �d  S(   Nu   <Control-a>c         � s
   �  j  �  S(   N(   t   _select_all(   t   e(   R@   (    s   latinsearch.pywRB     s    t   addu   +u   <Control-A>c         � s
   �  j  �  S(   N(   R�   (   R�   (   R@   (    s   latinsearch.pywRB     s    (   t   parentt   bind(   R@   R�   (    (   R@   s   latinsearch.pywRA   
  s    	"c         C� s:   |  j  j d � d k r d  S|  j  j �  |  j | � d  S(   Nu   stateu   disable(   R�   t   cgett   focus_forcet
   build_menu(   R@   t   event(    (    s   latinsearch.pywt   __call__  s    c         C� s�  t  j |  j d d �} |  j j �  sz | j d t j d � j d � d d � | j d t j d � j d � d d � nV | j d t j d � j d � d	 |  j � | j d t j d � j d � d	 |  j � |  j	 �  r
| j d t j d � j d
 � d	 |  j
 � n( | j d t j d � j d
 � d d � |  j j �  sl| j d t j d � j d � d d � n+ | j d t j d � j d � d	 |  j � | j �  | j d t j d � j d � d	 |  j � | j | j | j � d S(   u   Build right click menut   tearoffi    t   labelu   right_click_menuu   copyt   stateu   disableu   cutt   commandu   pasteu   deleteu
   select_allN(   t   tkt   MenuR�   t   selection_presentt   add_commandR�   Rd   t   _copyt   _cutt   paste_string_statet   _pastet   _cleart   add_separatorR�   t   postt   x_roott   y_root(   R@   R�   t   menu(    (    s   latinsearch.pywR�     sB    		
	
	
			
	

	
c         C� s   |  j  j d � d  S(   Nu   <<Cut>>(   R�   t   event_generate(   R@   (    (    s   latinsearch.pywR�   P  s    c         C� s   |  j  j d � d  S(   Nu   <<Copy>>(   R�   R�   (   R@   (    (    s   latinsearch.pywR�   S  s    c         C� s   |  j  j d � d  S(   Nu	   <<Paste>>(   R�   R�   (   R@   (    (    s   latinsearch.pywR�   V  s    c         C� s   |  j  j d � d  S(   Nu	   <<Clear>>(   R�   R�   (   R@   (    (    s   latinsearch.pywR�   Y  s    c         C� s'   |  j  j d d � |  j  j d � d S(   Ni    u   endu   break(   R�   t   selection_ranget   icursor(   R@   (    (    s   latinsearch.pywR�   \  s    c         C� s(   y |  j  j d d � } Wn t SXt S(   u,   Returns true if a string is in the clipboardt	   selectionu	   CLIPBOARD(   R�   t   selection_getR^   R=   (   R@   t	   clipboard(    (    s   latinsearch.pywR�   e  s
    (   R[   R\   R]   RA   R�   R�   R�   R�   R�   R�   R�   R�   (    (    (    s   latinsearch.pywR�   �  s   					4						t   RightClickMenuForListBoxc           B� s2   e  Z d  Z d �  Z d �  Z d �  Z d �  Z RS(   u9  
    Simple widget to add basic right click menus to entry widgets.

    usage:

    rclickmenu = RightClickMenuForListBox(listbox_widget)
    listbox_widget.bind("<3>", rclickmenu)

    If you prefer to import Tkinter over Tix, just replace all Tix
    references with Tkinter and this will still work fine.
    c         C� s   | |  _  d  S(   N(   R�   (   R@   R�   (    (    s   latinsearch.pywRA     s    c         C� s:   |  j  j d � d k r d  S|  j  j �  |  j | � d  S(   Nu   stateu   disable(   R�   R�   R�   R�   (   R@   R�   (    (    s   latinsearch.pywR�   �  s    c         C� s]   t  j |  j d d �} | j d t j d � j d � d |  j � | j | j | j	 � d S(   u   Build right click menuR�   i    R�   u   right_click_menu_listboxu   copyR�   N(
   R�   R�   R�   R�   R�   Rd   R�   R�   R�   R�   (   R@   R�   R�   (    (    s   latinsearch.pywR�   �  s    	
c         C� s   |  j  j d � d  S(   Nu   <<Copy>>(   R�   R�   (   R@   (    (    s   latinsearch.pywR�   �  s    (   R[   R\   R]   RA   R�   R�   R�   (    (    (    s   latinsearch.pywR�   r  s
   					t   RightClickMenuForScrolledTextc           B� sh   e  Z d  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z	 d �  Z
 d	 �  Z d
 �  Z RS(   u>   Simple widget to add basic right click menus to entry widgets.c         � sQ   | �  _  �  j  j d �  f d �  d d ��  j  j d �  f d �  d d �d  S(   Nu   <Control-a>c         � s
   �  j  �  S(   N(   R�   (   R�   (   R@   (    s   latinsearch.pywRB   �  s    R�   u   +u   <Control-A>c         � s
   �  j  �  S(   N(   R�   (   R�   (   R@   (    s   latinsearch.pywRB   �  s    (   R�   R�   (   R@   R�   (    (   R@   s   latinsearch.pywRA   �  s    	"c         C� s=   |  j  j d � t j k r d  S|  j  j �  |  j | � d  S(   Nu   state(   R�   R�   R�   t   DISABLEDR�   R�   (   R@   R�   (    (    s   latinsearch.pywR�   �  s    c         C� su  t  j |  j d d �} | j d t j d � j d � d |  j � | j d t j d � j d � d |  j � |  j �  r� | j d t j d � j d � d |  j	 � n( | j d t j d � j d � d	 d
 � | j d t j d � j d � d |  j
 � | j �  | j d t j d � j d � d |  j � | j d t j d � j d � d |  j � | j | j | j � d S(   u
   build menuR�   i    R�   u   right_click_menu_stu   copyR�   u   cutu   pasteR�   u   disableu   deleteu
   select_allu	   clear_allN(   R�   R�   R�   R�   R�   Rd   R�   R�   t   _paste_string_statet   _paste_if_string_in_clipboardt   _deleteR�   R�   t
   _clear_allR�   R�   R�   (   R@   R�   R�   (    (    s   latinsearch.pywR�   �  s:    	
	
			

	
	
c         C� s   |  j  j d � d  S(   Nu   <<Cut>>(   R�   R�   (   R@   (    (    s   latinsearch.pywR�   �  s    c         C� s   |  j  j d � d  S(   Nu   <<Copy>>(   R�   R�   (   R@   (    (    s   latinsearch.pywR�   �  s    c         C� s   |  j  j d � d  S(   Nu	   <<Clear>>(   R�   R�   (   R@   (    (    s   latinsearch.pywR�   �  s    c         C� s   |  j  j d � d  S(   Nu	   <<Paste>>(   R�   R�   (   R@   (    (    s   latinsearch.pywR�   �  s    c         C� s=   |  j  j d d d � |  j  j d d � |  j  j d � d S(   u
   select allu   selu   1.0u   end-1cu   insertu   break(   R�   t   tag_addt   mark_sett   see(   R@   (    (    s   latinsearch.pywR�   �  s    c         C� s(   y |  j  j d d � } Wn t SXt S(   u,   Returns true if a string is in the clipboardR�   u	   CLIPBOARD(   R�   R�   R^   R=   (   R@   R�   (    (    s   latinsearch.pywR�   �  s
    c         C� s   |  j  j d d � d S(   u	   Clear allu   1.0u   endN(   R�   t   delete(   R@   (    (    s   latinsearch.pywR�   �  s    (   R[   R\   R]   RA   R�   R�   R�   R�   R�   R�   R�   R�   R�   (    (    (    s   latinsearch.pywR�   �  s   					2						t   AutocompleteGUIc           B� s�   e  Z d  Z d g  i  d � Z d �  Z d �  Z d �  Z d �  Z d �  Z	 d �  Z
 d �  Z d	 �  Z d
 �  Z d �  Z d �  Z d �  Z e d � Z e d �  � Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z RS(   u&   The main GUI for autocomplete program.c         C� s�   t  j j |  | � | |  _ | |  _ g  |  _ |  j j t j	 d � j	 d � � |  j j
 d t j	 d � j	 d � t f � |  j �  |  j �  |  j �  |  j �  |  j �  |  j �  |  j �  d  S(   Nu   main_windowu   geometryu   %s %su
   main_title(   R�   t   FrameRA   R1   R`   t   historyt   mastert   geometryR�   Rd   t   titlet   __version__t	   set_stylet   create_menu_bart   create_widgetst   grid_configuret   row_and_column_configuret   create_right_menut	   bind_func(   R@   R�   R1   R`   (    (    s   latinsearch.pywRA     s     					





c         C� s�   t  j �  } | j d d d �| j d d d �| j d d d �| j d	 d d
 �| j d d d d d �| j d d d �| j d d d d d
 �d S(   u)   Set style for widgets in the main window.u	   TComboboxt   paddingi   u   auto.TComboboxt
   foregroundu   redu   TButtoni
   u   open.TButtonu   blueu   config.TLabelt   fontu	   helveticau   boldu   listbox.TLabeli   u   status.TLabeli   N(   u	   helveticai   u   bold(   R   t   Stylet	   configure(   R@   t   s(    (    s   latinsearch.pywR�     s     c         C� s�  t  j |  j � } t  j | d d �} | j d t j d � j d � d |  j � | j �  | j d t j d � j d � d |  j j � | j	 d t j d � j d � d	 | � t  j | d d �} | j d t j d � j d
 � d |  j
 � | j d t j d � j d � d |  j � |  j �  rW| j d t j d � j d � d |  j � n+ | j d t j d � j d � d d �  � | j �  | j d t j d � j d � d |  j � | j	 d t j d � j d � d	 | � t  j | d d �} | j d t j d � j d � d |  j � | j d t j d � j d � d |  j � | j	 d t j d � j d � d	 | � |  j j d	 | � d S(   u$   Create menu_bar for the main window.R�   i    R�   u   menu_baru   saveR�   u   exitu   file_cascadeR�   u   copyu   cutu   pastec           S� s   t  t j d � j d � � S(   Nu   menu_baru   no_str_in_clipboard_warning(   t   printR�   Rd   (    (    (    s   latinsearch.pywRB   ^  s   u   deleteu   edit_cascadeu   helpu   aboutu   help_cascadeN(   R�   R�   R�   R�   R�   Rd   t   _ask_save_fileR�   t   quitt   add_cascadeR�   R�   R�   R�   R�   t   _display_helpt   _display_aboutt   config(   R@   t   menu_bart	   file_menut	   edit_menut	   help_menu(    (    s   latinsearch.pywR�   5  sX    	

			
	
		

	
		
	
	c      
   C� s@  t  j |  j d d �|  _ |  j j d d d d d t j t j t j t j	 � t  j
 |  j d t j d � j d	 � d
 d �|  _ t j �  |  _ t  j |  j d t j d � j d � d |  j d d d d �|  _ |  j j d � t j �  |  _ t  j |  j d t j d � j d � d |  j d d d d �|  _ |  j j d � t j �  |  _ t  j |  j d t j d � j d � d |  j d d d d �|  _ |  j j d � t  j |  j d
 d �|  _ |  j j �  t  j |  j d t j d � j d � d
 d �|  _ t  j |  j d t j d � j d � d
 d �|  _ t  j
 |  j d t j d � j d � d
 d �|  _ t j |  j d d% �|  _ t  j  |  j � |  _! t  j
 |  j d t j d � j d � d
 d �|  _" t j |  j d d& �|  _# t  j  |  j � |  _$ t  j
 |  j d t j d � j d � d
 d �|  _% t j |  j d d' �|  _& t  j  |  j � |  _' t  j
 |  j d t j d � j d  � d
 d �|  _( t j |  j d d( �|  _) t  j  |  j � |  _* t j+ �  |  _, t  j
 |  j d! |  j, d
 d" �|  _- |  j, j t j d � j d# � � t. j/ |  j d d) �|  _0 |  j1 �  d$ S(*   u'   Create widgets for the main GUI window.R�   i   t   rowi    R�   t   stickyR�   u   configu   config_labelt   styleu   config.TLabelu   similarity_search_switcht   variablet   onvaluei   t   offvalueu   spell_check_switchu   match_whole_wordu   auto.TComboboxu   buttonsu   search_offline_buttonu   copy.TButtonu   search_internet_buttonu   labelsu   startswith_endswith_labelu   listbox.TLabelR�   u	   Monospacei
   u   contains_labelu   similarity_labelu   spell_check_labelt   textvariableu   status.TLabelu   default_status_labelN(   u	   Monospacei
   (   u	   Monospacei
   (   u	   Monospacei
   (   u	   Monospacei
   (   u	   Monospacei
   (2   R   R�   R�   t   contentt   gridR�   t   Wt   Et   Nt   St   LabelR�   Rd   t   config_labelt   IntVart   turn_off_similarity_search_vart   Checkbuttont   similarity_search_checkbuttonR+   t   turn_off_spell_check_vart   spell_check_checkbuttont   totally_match_vart   totally_match_checkbuttont   Comboboxt	   input_boxt   focust   Buttont   search_offline_buttont   search_internet_buttont   label_1t   Listboxt   listbox1t	   Scrollbart
   scrollbar1t   label_2t   listbox2t
   scrollbar2t   label_3t   listbox3t
   scrollbar3t   label_4t   listbox4t
   scrollbar4t	   StringVart   status_label_valuet   label_5t   stt   ScrolledTextt   scrolled_text_5R�   (   R@   (    (    s   latinsearch.pywR�   y  s�    7																	c         C� s�  |  j  j �  |  j j d d d d d d d d � |  j j d d d d d d � |  j j d d d d d d � |  j j d d	 d
 d d d d d d d � |  j j d d	 d d d d � |  j j d d d d d d � |  j j d d	 d d d d � |  j	 j d d d d d d d d � |  j
 j d d d d d d d d � |  j j d d d d d d � |  j
 j d |  j j � |  j j d |  j
 j � |  j j d d d d d d d d � |  j j d d d d d d d d � |  j j d d d d d d � |  j j d |  j j � |  j j d |  j j � |  j j d d d d d d d d � |  j j d d d d d d d d � |  j j d d d d d d � |  j j d |  j j � |  j j d |  j j � |  j j d d d d d d d d � |  j j d d d d d d d d � |  j j d d d d d d � |  j j d |  j j � |  j j d |  j j � |  j j d d d d d d d d � |  j j d d d d d d d d � d S(   u)   Grid configuration of window and widgets.R�   i    R�   t
   columnspani	   R   u   wensi
   i   t   rowspani   i   u   wei   u   wsu   nst   yscrollcommandR�   u   wi   i   i   i   i   N(   R�   R  R  R  R  R  R  R  R  R  R  R   R�   R+   t   yviewR!  R"  R#  R$  R%  R&  R'  R(  R)  R,  R/  (   R@   (    (    s   latinsearch.pywR�   �  s@    %$%%%%%%%%%c         C� s�  |  j  j d d d �|  j  j d d d �|  j j d d d �|  j j d d d �|  j j d d d �|  j j d d d �|  j j d d d �|  j j d d d �|  j j d d d �|  j j d d d �|  j j d d d �|  j j d d d �|  j j d d d �|  j j d d d �|  j j d d d �|  j j d d d �|  j j d	 d d �|  j j d
 d d �|  j j d d d �|  j j d d d �|  j j d d d �d S(   u   Rows and columns configurationi    t   weighti   i   i   i   i   i   i   i   i	   i
   i   N(   R�   t   rowconfiguret   columnconfigureR  (   R@   (    (    s   latinsearch.pywR�     s*    c         C� sH   t  |  j � } |  j j d | � t |  j � } |  j j d | � d  S(   Nu
   <Button-3>(   R�   R  R�   R�   R/  (   R@   t   right_menu_input_boxt   right_menu_scrolled_text_5(    (    s   latinsearch.pywR�   ;  s
    c         � sf   �  j  �  j d <�  j �  j d <�  f d �  } x0 �  j �  j �  j �  j g D] } | | � qN Wd  S(   Nu   commandc         � s<   �  j  d � �  f d �  � t �  � } �  j  d | � d S(   u�   Bind command to listbox.

            Double click on candidates from any column from the four,
            then the result will be on the output area.
            u   <Double-Button-1>c         � s   �  j  � � S(   N(   t   _display_search_result(   R�   (   R@   t   widget(    s   latinsearch.pywRB   U  s    u
   <Button-3>N(   R�   R�   (   R:  t   right_menu_widget(   R@   (   R:  s   latinsearch.pywt   bind_command_to_listboxI  s    	(   t   _display_candidatesR  t   _query_baidu_baikeR  R  R"  R%  R(  (   R@   R<  t   listbox(    (   R@   s   latinsearch.pywR�   E  s    c         C� s�  |  j  j �  j �  } | sA |  j j t j d � j d � � d St |  j |  j � } i g  d 6g  d 6g  d 6d d 6} |  j	 j �  } | r�| |  j k r� t
 t
 t t g } | j | | | � } q�d | k rt
 t
 t
 t g } |  j j �  r t | d	 <n  | j | | | � } q�| d
 t j k r�t
 t
 t
 t
 g } |  j j �  rYt | d	 <n  |  j j �  rut | d <n  | j | | | � } q�t
 t
 t
 t g } |  j j �  r�t | d	 <n  | j | | | � } n  | S(   u0   Command of Do Query button with multi-processingu	   info_textu   blank_query_labelu    u   0u   1u   2u   3u    i   i    i   (   R  Rd   R   R+  R+   R�   R_   R1   R`   R  R=   R^   R   R  t   stringt	   printableR  (   R@   Rb   t   query_word_objectRc   Rg   Rz   (    (    s   latinsearch.pywt   _query_offline_datab  sD    	"c         C� s:  |  j  j �  j �  } | sA |  j j t j d � j d � � d S|  j j t j d � j d � � t j �  } t j t j	 | � � } | rd t j d � j d � | f } t j �  } |  j
 |  j | � |  j j d t j d � j d � | | f � n5 |  j
 |  j | � |  j j t j d � j d	 � � d  S(
   Nu	   info_textu   blank_query_labelu    u   searching_baidu_baikeu
   %s

%s



u   baike_result_infou   %s%fsu   baike_search_completeu   baike_no_result(   R  Rd   R   R+  R+   R�   t   timeR�   R�   R�   t   _insert_to_text_areaR/  (   R@   R�   t
   start_timeR�   t   end_time(    (    s   latinsearch.pywR>  �  s0    		
		c         C� s1  |  j  j �  j �  } | sA |  j j t j d � j d � � d S|  j j t j d � j d � � t j �  } t j | � } | r� d t j d � j d � | f } t j �  } |  j	 |  j
 | � |  j j d t j d � j d � | | f � n5 |  j	 |  j
 | � |  j j t j d � j d	 � � d  S(
   Nu	   info_textu   blank_query_labelu    u   searching_wikipediau
   %s

%s



u   wikipedia_result_infou   %s%fsu   wikipedia_search_completeu   wikipedia_no_result(   R  Rd   R   R+  R+   R�   RD  R�   R�   RE  R/  (   R@   R�   RF  t   wikipedia_resultRG  (    (    s   latinsearch.pywt   _query_wikipedia�  s0    		
		c         C� s�   |  j  |  j g } |  j j t j d � j d � � |  j j d d � |  j j �  xM t	 | � D]? \ } } t
 d | � } | j t � | j �  t j d � qa W|  j j t j d � j d � � d  S(   Nu	   info_textu   start_searchingu   1.0u   end-1cRx   g�������?u   search_complete(   R>  RI  R+  R+   R�   Rd   R/  R�   t   update_idletasksR   R   t	   setDaemonR=   Ry   RD  t   sleep(   R@   t	   func_listR$   R}   t   thread(    (    s   latinsearch.pywt   _query_internet_multithreading�  s    	
	c         C� st  |  j  j t j d � j d � � t j �  } |  j �  } t j �  } | sP d  S|  j j d d � x% | d D] } |  j j d | � qn W|  j	 j d d � x% | d D] } |  j	 j d | � q� W|  j
 j d d � x% | d D] } |  j
 j d | � q� W|  j j d d � |  j j d | d � |  j  j d t j d � j d	 � | | t j d � j d
 � f � d  S(   Nu	   info_textu   start_offline_searchu   0u   endu   1u   2u   3u   %s%fs%su   offline_search_complete_1u   offline_search_complete_2(   R+  R+   R�   Rd   RD  RC  R  R�   t   insertR"  R%  R(  (   R@   RF  Rc   RG  t   item(    (    s   latinsearch.pywR=  �  s2    		c         C� s�  | j  d � } |  j j d t j � |  j j t j | � |  j j d d � |  j j  | � } | r�t rvt d d d d d	 d
 d g � } x d D] } d | j	 | <q� Wd | _
 x� | D]{ } g  | d j �  D] } | t k r� | ^ q� }	 t d j |	 � }
 g  | D] } | ^ q
} | j |
 � | j | � q� W|  j j d | j �  � |  j j t j � |  j j �  q�|  j j d d t j  d � j  d � d d f � xN | D]C } d j | � } |  j j d | � |  j j d d d d � q�Wn  d S(   u2   Clean content in Output Area and insert new value.u   activei    u   0.1u   end-1cu   Short Pinyinu   Long Pinyinu   Chineseu   Latinu   Nameru   Data Sourceu   Web URLu   li   i   u   %20u   endu  %s pip install prettytable

+--------------+-------------+---------+-------+-------+-------------+---------+
| Short Pinyin | Long Pinyin | Chinese | Latin | Namer | Data Source | Web URL |
+--------------+-------------+---------+-------+-------+-------------+---------+

%s
u	   info_textu   pretty_table_install_infou   =id   u     |  u   
%s
u   -N(   u   Short Pinyinu   Long Pinyinu   Chineseu   Latinu   Nameru   Data Sourceu   Web URL(   Rd   R  R�   R�   t   ENDRP  R/  R`   R   R�   R�   R   t   SPECIAL_CHARSt   FRPS_BASE_URLR�   R   R�   R�   R�   RJ  R�   (   R@   R:  t   is_clean_wordt   selection_valuet   resultR�   R�   t   each_resultR   t   normal_word_listR�   RC   RJ   R   (    (    s   latinsearch.pywR9  �  sD    	
		c         C� s.   |  j  d d � |  j d | � |  j �  d S(   u<   Clear original content from ScrolledText area and insert newu   1.0u   endN(   R�   RP  RJ  (   t	   st_widgetR  (    (    s   latinsearch.pywRE  3  s    c         C� s   |  j  j �  j d � d  S(   Nu   <<Copy>>(   R�   t	   focus_getR�   (   R@   (    (    s   latinsearch.pywR�   ;  s    c         C� s   |  j  j �  j d � d  S(   Nu   <<Cut>>(   R�   R[  R�   (   R@   (    (    s   latinsearch.pywR�   @  s    c         C� s   |  j  j �  j d � d  S(   Nu	   <<Paste>>(   R�   R[  R�   (   R@   (    (    s   latinsearch.pywR�   F  s    c         C� s   |  j  j �  j d � d  S(   Nu	   <<Clear>>(   R�   R[  R�   (   R@   (    (    s   latinsearch.pywR�   J  s    c         C� s(   y |  j  j d d � } Wn t SXt S(   u,   Returns true if a string is in the clipboardR�   u	   CLIPBOARD(   R�   R�   R^   R=   (   R@   R�   (    (    s   latinsearch.pywR�   M  s
    c         C� ss   t  j d d d d � } | d k r( d S|  j j d d � j d � } | j | j d � j d	 � � | j �  d S(
   u   Dialog to open file.t   modeu   wt   defaultextensionu   .txtNu   1.0u   end-1cu   GBKu   utf-8(	   t   tkFileDialogt   asksaveasfileR3   R/  Rd   R�   t   writeR   t   close(   R@   RI   t   text_to_save(    (    s   latinsearch.pywR�   Y  s    c         C� s*   |  j  j d d � |  j  j d t � d  S(   Nu   0.1u   end-1cu   end(   R/  R�   RP  t
   USAGE_INFO(   R@   (    (    s   latinsearch.pywR�   b  s    c         C� s*   |  j  j d d � |  j  j d t � d  S(   Nu   0.1u   end-1cu   end(   R/  R�   RP  t
   ABOUT_INFO(   R@   (    (    s   latinsearch.pywR�   f  s    N(   R[   R\   R]   R3   RA   R�   R�   R�   R�   R�   R�   R�   RC  R>  RI  RO  R=  R=   R9  R�   RE  R�   R�   R�   R�   R�   R�   R�   R�   (    (    (    s   latinsearch.pywR�     s0   		D	i	9	 	
		1				#5								c         C� s{   t  �  \ }  } t j |  � } t j | � } t t d � � } | j | � Wd QXt t d � � } | j | � Wd QXd S(   ub   Dump generated dictinary to pickle raw file.

    Generally, this function need only do once.
    u   wbN(   R2   t   picklet   dumpsR
   t   PICKLE_KEYS_FILER`  t   PICKLE_DICT_FILE(   R1   R`   t   pickle_keyst   pickle_dictt   f_out(    (    s   latinsearch.pywt   dump_with_picklek  s    c         C� sp   t  |  d � �" } | j �  } t j | � } Wd QXt  | d � �" } | j �  } t j | � } Wd QX| | f S(   u'   Load keys and dict from pickle raw fileu   rbN(   R
   t   readRe  t   loads(   t   pickle_keys_filet   pickle_dict_fileR   Ri  R1   Rj  R`   (    (    s   latinsearch.pywt   load_with_pickley  s    c          C� sD   t  t t � \ }  } t |  � a t d |  d | � } | j �  d S(   u   The main GUI program.R1   R`   N(   Rq  Rg  Rh  R8   Rv   R�   t   mainloop(   R1   R`   t   app(    (    s   latinsearch.pywt   gui_main�  s    	c           C� s   t  �  d S(   u	   Main funcN(   R2   (    (    (    s   latinsearch.pywt   main�  s    u   __main__(P   R]   t
   __future__R    R   R   R   t   pathRP  t   osR�   RD  R�   R�   t	   threadingR   t   bs4R   t   cPickleRe  t   ImportErrorR@  RE   t   difflibR   t   multiprocessingR   t   prettytableR   R3   R   t   TkinterR�   R   R^  R.  R-  t   tkintert   tkinter.scrolledtextt   scrolledtextR	   R�   t
   __author__t   _historyt   abspathR(   Rg  Rh  RT  Rr   Rp   RS  R�   t   objectRv   R�   R�   R�   t   TEXT_DICT_ENt   TEXT_DICT_CNR�   Rc  Rd  R   R   R'   R2   R7   R8   R_   R�   R�   R�   R�   R�   R�   Rl  Rq  Rt  Ru  R[   (    (    (    s   latinsearch.pywt   <module>   s�  
	&
			#			N�Ou&k� � j				