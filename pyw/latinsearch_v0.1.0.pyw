ó
î$Wc           @ s  d  d l  m Z m Z m Z d  d l Z d  d l Z y d  d l Z Wn e k
 rc d  d l Z n Xd  d l	 Z	 d  d l
 Z
 d  d l m Z y d  d l m Z Wn e k
 r¹ e Z n Xe j d d k r d  d l Z d  d l Z d  d l Z d  d l Z nQ e j d d k rQd  d l Z d  d l m Z d  d l j Z d  d	 l m Z n  d
 Z d Z g  Z e j j d  Z  e j j d  Z! e j j d  Z" d Z# d d d d d d d d d d d d d d d g Z$ d e Z% d    Z& d!   Z' d"   Z( d#   Z) d$   Z* d% e+ f d&     YZ, d' e+ f d(     YZ- d) e j. f d*     YZ/ d+   Z0 d,   Z1 d-   Z2 d.   Z3 e4 d/ k re2   n  d S(0   iÿÿÿÿ(   t   print_functiont   unicode_literalst   with_statementN(   t   SequenceMatcher(   t   PrettyTablei    u   2u   3(   t   ttk(   t
   filedialogu   v0.1.0u   Jinu   data/latin_without_sougou.csvu   data/latin_60000.keys.pickleu   data/latin_60000.dict.pickleu   http://frps.eflora.cn/frps/u   Ãu   ãu   ï¼u   ãu   ãu   îu   îu   <u   >u   *u   [u   @u   ]u   ï¼»u   |uå  
æ¤ç©æä¸åæç´¢ï¼Latin Namer Finerï¼

[ä»ç»]

    æ ¹æ®æ¤ç©æ¼é³ç¼©åãæ¼é³ãä¸­æåç§°æèæä¸åæç´¢æ¤ç©å¶ä»ä¿¡æ¯ã

    å¾å°åéè¯åï¼*åå»* åéè¯ï¼å°å¾å°è¯¦ç»ä¿¡æ¯ãå¦ææ²¡æå¹éï¼å°ä¼ä½¿ç¨ç³¢ç³æç´¢ã

[çæ¬]

    %s

[ä½¿ç¨æ¹æ³]

    1. ä½¿ç¨æ¼é³é¦å­æ¯æç´¢ãä¾å¦æç´¢ âeqxlmâï¼å°ä¼å¾å° âäºçæ¬éæ¨â
       åå¶ä»æ¬éæ¨ç¸å³çç»æã
    2. ä½¿ç¨æ¼é³å¨ç§°æç´¢ãä¾å¦æç´¢ âerqiuxuanlingmuâï¼å°ä¼å¾å° âäºçæ¬éæ¨â
       åå¶ä»æ¬éæ¨ç¸å³çç»æã
    3. ä½¿ç¨ä¸­ææç´¢ãä¾å¦æç´¢ âæ¬éæ¨âï¼å°ä¼å¾å° âäºçæ¬éæ¨âï¼ âä¸çæ¬éæ¨â
       ç­ç¸å³æç´¢ç»æã
    4. ä½¿ç¨æä¸åæç´¢ãä¾å¦æç´¢ âPlatanus Ã acerifoliaâï¼å°ä¼å¾å° âäºçæ¬éæ¨â
       ç¸å³çç»æã

[åéè¯ä»ç»]

    +---+------------------------+
    | 1 | åéè¯ä»¥æ¥è¯¢è¯å¼å§æç»å°¾
    |---+------------------------+
    | 2 | åéè¯åå«æ¥è¯¢è¯
    |---+------------------------+
    | 3 | æ ¹æ®ç¸ä¼¼æ§è¿è¡ç³¢ç³æç´¢
    |---+------------------------+
    | 4 | æ¼åæ£æ¥ï¼ç¼è¾è·ç¦»ä¸º 1)
    +---+------------------------+

c         C s&   t  |  d   } | j   SWd QXd S(   u%   Read file and return a list of lines.u   rN(   t   opent	   readlines(   t	   file_namet   f_in(    (    s   latinsearch.pyt	   get_linesY   s    c   
      C s  g  g  g  g  f \ } } } } g  } t  |  d  ¼ } x² | D]ª } t j d d k rh | j d  } n  g  | j d  D] } | j   ^ qx }	 | j |	 d  | j |	 d  | j |	 d  | j |	 d  | j t |	   q= WWd	 QX| | | | | f S(
   u  
    File:
        +-----+-------+------+----------------------+-------+
        | mg  | mugua | æ¨ç | Chaenomeles sinensis | Lynn. |
        +-----+-------+--- --+----------------------+-------+

    Processing:

        dict_1: {'mg': ('mg', 'mugua', 'æ¨ç', 'Chaenomeles sinensis', '')}
        dict_2: {'mugua': ('mg', 'mugua', 'æ¨ç', 'Chaenomeles sinensis', '')}
        dict_3: {'æ¨ç': ('mg', 'mugua', 'æ¨ç', 'Chaenomeles sinensis', '')}
        dict_4: {'Chaenomeles sinensis': ('mg', 'mugua',
                                          'æ¨ç', 'Chaenomeles sinensis', '')}

    Returns:
        (dict_1, dict_2, dict_3, dict_4)
    u   ri    u   2u   utf-8u   ,i   i   i   N(   R   t   syst   versiont   decodet   splitt   stript   appendt   tuple(
   R	   t   column_list_1t   column_list_2t   column_list_3t   column_list_4t   detailed_info_tuple_listR
   t   linet   xt   elements(    (    s   latinsearch.pyt   get_key_value_pairs_from_file_   s    (	c         C sq   i  } xd t  t |  |   D]M \ } \ } } | | k rX g  | | <| | j |  q | | j |  q W| S(   u¨   
    Generate a dictionary from two lists. keys may be duplicated.

    >>> get_one_to_more_dict(['a', 'b', 'a', 'a'], [1, 2, 3, 4])
    {'a': [1, 3, 4], 'b': [2]}
    (   t	   enumeratet   zipR   (   t   key_listt
   value_listt	   _out_dictt   it   keyt   value(    (    s   latinsearch.pyt   get_one_to_more_dict   s    (
c          C s¯   t  t  \ }  } } } } t |  |  } t | |  } t | |  } t | |  } x- | | | f D] }	 |	 rg | j |	  qg qg Wt t |  | | |   }
 |
 | f S(   uC   Combine dicts, each with one column as key and whole line as value.(   R   t	   DATA_FILER$   t   updatet   listt   set(   R   R   R   R   R   t   dict_1t   dict_2t   dict_3t   dict_4t	   each_dictt   keys_for_all(    (    s   latinsearch.pyt   get_dict_for_all_columns   s    c         C s   t  d |  |  j   S(   un   Return similarity of two strings.

    [Example]
        >>> get_similarity('abcde', 'bcdef')
        0.8
    N(   R   t   Nonet   ratio(   t   str_at   str_b(    (    s   latinsearch.pyt   get_similarity­   s    t
   SpellCheckc           B sG   e  Z d  Z d   Z e d  Z d   Z d   Z d   Z d   Z	 RS(   uW  Train data set with given data then do spell check for given word.

    [Example]
        >>> s = SpellCheck(['abcd', 'fghi'])
        >>> s.correct('abci')
        'abcd'

    [Reference]
        [1]: Title:   How to Write a Spelling Corrector
             Author:  Peter Norvig
             Webpage: http://norvig.com/spell-correct.html
    c         C s:   | |  _  |  j   |  _ |  j d t  |  _ d |  _ d  S(   Nt   loweruB   abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-.:1234567890(   t   candidate_listt   traint   NWORDSt   Truet   NWORDS_lowert   alphabet(   t   selfR7   (    (    s   latinsearch.pyt   __init__È   s    	c         C s   |  j  s t d   n  t j d    } | sW x[ |  j  D] } | | c d 7<q: Wn7 |  j  } x* t d   |  D] } | | c d 7<qt W| S(   u   Train model with data set.u*   Blank training list (Choosed blank file?).c           S s   d S(   Ni   (    (    (    (    s   latinsearch.pyt   <lambda>Ó   s    i   c         S s
   |  j    S(   N(   R6   (   t   _(    (    s   latinsearch.pyR?   Ù   s    (   R7   t
   ValueErrort   collectionst   defaultdictt   map(   R=   R6   t   modelt   ft   tmp_list(    (    s   latinsearch.pyR8   Ï   s    	
c      	   C s  t  |  } t g  t |  D] } | d | !| | d ^ q g  t | d  D]3 } | d | !| | d | | | | d ^ qO g  t |  D]3 } |  j D]# } | d | !| | | d ^ q  q g  t | d  D]/ } |  j D] } | d | !| | | ^ qè qÛ  S(   u   Words that has one edit distance.

        1. deletion
        2. transposition
        3. alteration
        4. insertion
        i    i   i   (   t   lenR(   t   rangeR<   (   R=   t   wordt   nR!   t   c(    (    s   latinsearch.pyt   edits1Ý   s    »c          s#   t    f d     j |  D  S(   u!   Words that has two edit distance.c         3 s@   |  ]6 }   j  |  D]  } | j     j k r | Vq q d  S(   N(   RM   R6   R;   (   t   .0t   e1t   e2(   R=   (    s   latinsearch.pys	   <genexpr>ñ   s    (   R(   RM   (   R=   RJ   (    (   R=   s   latinsearch.pyt   known_edits2ï   s    c          s   t    f d   | D  S(   u   Known words.c         3 s*   |  ]  } | j      j k r | Vq d  S(   N(   R6   R;   (   RN   t   w(   R=   (    s   latinsearch.pys	   <genexpr>ö   s    (   R(   (   R=   t   words(    (   R=   s   latinsearch.pyt   knownô   s    c          sL     j  | g  p0   j    j |   p0 | g } t | d   f d   S(   u9   Do spell check and correct word if word was wrong spelledR"   c          s     j  |  S(   N(   R;   (   RR   (   R=   (    s   latinsearch.pyR?     s    (   RT   RM   t   max(   R=   RJ   t
   candidates(    (   R=   s   latinsearch.pyt   correctø   s    *	(
   t   __name__t
   __module__t   __doc__R>   t   FalseR8   RM   RQ   RT   RW   (    (    (    s   latinsearch.pyR5   »   s   				t	   QueryWordc           B sG   e  Z d  Z d   Z d   Z d   Z d d  Z d   Z d   Z RS(   u¢  Four query strategy.

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



    c         C s5   g  | D] } | j    ^ q |  _ t |  |  _ d  S(   N(   R   t   all_candidate_listR5   t   trained_object(   R=   R]   R   (    (    s   latinsearch.pyR>   "  s    "c         C s|   g  } xo t  |  j  D]^ \ } } | j   j | j   j    sd | j   j | j   j    r | j |  q q W| S(   u   Check startswith & endswith(   R   R]   R6   t
   startswithR   t   endswithR   (   R=   t   queryt	   _tmp_listR!   t	   candidate(    (    s   latinsearch.pyt   get_starts_with_candidates)  s    !!c         C sX   g  } xK t  |  j  D]: \ } } | j   j   | j   k r | j |  q q W| S(   u   Check contains(   R   R]   R   R6   R   (   R=   Ra   Rb   R!   Rc   (    (    s   latinsearch.pyt   get_contains_candidates5  s
    i   c   	      C s   g  } xQ t  |  j  D]@ \ } } t | j   | j   j    } | j | | f  q W| j d d   d t  | |  } g  | D] } | d ^ q } | S(   u   Rank candidates by similarityR"   c         S s   |  d S(   Ni    (    (   R   (    (    s   latinsearch.pyR?   G  s    t   reversei   (   R   R]   R4   R6   R   R   t   sortR:   (	   R=   Ra   t   limitRb   R!   Rc   t   _similarityR@   t   _similar_hits(    (    s   latinsearch.pyt   get_similar_candidates@  s    
c         C s   |  j  j |  S(   u   Get spell check candicates(   R^   RW   (   R=   Ra   (    (    s   latinsearch.pyt   get_spell_check_candidateQ  s    c         C sR   |  j  |  } |  j |  } |  j | d d } |  j |  } | | | | f S(   u   Get four resultsRh   i   (   Rd   Re   Rk   Rl   (   R=   Ra   t
   result_onet
   result_twot   result_threet   result_four(    (    s   latinsearch.pyt   query_all_fourU  s
    (	   RX   RY   RZ   R>   Rd   Re   Rk   Rl   Rq   (    (    (    s   latinsearch.pyR\     s   				t   AutocompleteGUIc           B sk   e  Z d  Z d
 g  i  d  Z d   Z d   Z d   Z e d  Z	 d   Z
 d   Z d   Z d	   Z RS(   u&   The main GUI for autocomplete program.c         C s   t  j j |  |  t |  |  _ | |  _ g  |  _ |  j j   |  j	   |  j
   |  j   |  j   |  j j d  |  j j d t  d  S(   Nu   1400x800u   Latin Finder %s(   t   tkt   FrameR>   R\   t   query_objectt   dict_for_allt   historyt   mastert   gridt	   set_stylet   create_menut   create_widgetst   grid_configuret   geometryt   titlet   __version__(   R=   Rx   R.   Rv   (    (    s   latinsearch.pyR>   a  s    		



c         C s\   t  j   } | j d d d | j d d d | j d d d | j d	 d d
 d S(   u)   Set style for widgets in the main window.u	   TComboboxt   paddingi   u   auto.TComboboxt
   foregroundu   redu   TButtoni
   u   open.TButtonu   blueN(   R   t   Stylet	   configure(   R=   t   s(    (    s   latinsearch.pyRz   n  s
    c          sñ   t  j   j    _ t  j   j d d   _   j j d d    j j d d d   j j    j j d d d   j  t  j   j d d   _   j j d d	 d   f d
      j j d d	 d   j    j j	 d   j  d S(   u#   Create menubar for the main window.t   tearoffi    t   labelu   Openu   Exitt   commandu   Filet   menuu   Helpc            s     j  S(   N(   t
   print_help(    (   R=   (    s   latinsearch.pyR?     s    N(
   Rs   t   MenuRx   t   menubart	   file_menut   add_commandt   quitt   add_cascadet	   help_menut   config(   R=   (    (   R=   s   latinsearch.pyR{   v  s    c      
    s  t  j   j d d   _   j j d d d d d t j t j t j t j	  t  j
   j d d   _ t j   j d	 d#   _ t  j   j    _ t  j
   j d d   _ t j   j d	 d$   _ t  j   j    _ t  j
   j d d   _ t j   j d	 d%   _ t  j   j    _ t  j
   j d d   _ t j   j d	 d&   _ t  j   j    _ t  j
   j d d   _ t j   j d	 d'   _ t  j   j d d   _   j j d d d d d d d t j t j    j j   t  j    j d d d   j! d d   _"   j" j d d d d d d d t j    j j d d d d d d d t j    j j d d d d d t j t j t j t j	    j j d d d d d t j t j	    j j# d   j j$    j j# d   j j%    j j d d d d d d d t j    j j d d d d d t j t j t j t j	    j j d d d d d t j t j	    j j# d   j j$    j j# d   j j%    j j d d d d d d d t j    j j d d d d d t j t j t j t j	    j j d d d d d t j t j	    j j# d   j j$    j j# d   j j%    j j d d d d d d d t j    j j d d d d d t j t j t j t j	    j j d d d d d t j t j	    j j# d   j j$    j j# d   j j%    j j d d d d d d d t j    j j d d d d d d d t j t j	 t j t j    j j& d d    j j' d  t(    f d!   } x0   j   j   j   j g D] } | |  qþWd" S((   u'   Create widgets for the main GUI window.R   i   t   rowi    t   columnt   stickyt   textu"   Candidates (Startswith / Endswith)t   fontu	   Monospacei
   u   Candidates (Contains)u   Candidates (Rank by similarity)u.   Candidates (Spell check, single edit distance)u]   Click "Do Query" button and see results. ** Double Click ** candidate to see detailed result.t   styleu   auto.TComboboxt
   columnspani   u   Do QueryR   u   copy.TButtoni   i   t   yscrollcommandi   i   i   i   u   0.1u   end-1cu   endc          s      j  d    f d    d S(   u¤   Bind command to listbox.

            Double click on candidates from any column from the four,
            then the result will be on the output area.
            u   <Double-Button-1>c          s     j    S(   N(   t   clean_and_insert_value(   t   e(   R=   t   widget(    s   latinsearch.pyR?   ô  s    N(   t   bind(   R   (   R=   (   R   s   latinsearch.pyt   bind_command_to_listboxè  s    	N(   u	   Monospacei
   (   u	   Monospacei
   (   u	   Monospacei
   (   u	   Monospacei
   (   u	   Monospacei
   ()   R   Rt   Rx   t   contentRy   Rs   t   Wt   Et   Nt   St   Labelt   label_1t   Listboxt   listbox1t	   Scrollbart
   scrollbar1t   label_2t   listbox2t
   scrollbar2t   label_3t   listbox3t
   scrollbar3t   label_4t   listbox4t
   scrollbar4t   label_5t   stt   ScrolledTextt   scrolled_text_5t   Comboboxt	   input_boxt   focust   Buttont   show_candidatest   do_query_buttonR   R(   t   yviewt   deletet   insertt
   USAGE_INFO(   R=   R   t   listbox(    (   R=   s   latinsearch.pyR|     s    7			/		
(7)(7)(7)(7)(c         C s¸  | j  d  } |  j j d t j  |  j j t j |  |  j j d d  |  j | } t rKt d d d d d	 d
 d g  } x d D] } d | j	 | <q Wd | _
 x | D]{ } g  | d j   D] } | t k rÇ | ^ qÇ }	 t d j |	  }
 g  | D] } | ^ qÿ } | j |
  | j |  q° W|  j j d | j    ni |  j j d d d d  xK | D]C } d j |  } |  j j d |  |  j j d d d d  qmWd S(   u2   Clean content in Output Area and insert new value.u   activei    u   0.1u   end-1cu   Short Pinyinu   Long Pinyinu   Chineseu   Latinu   Nameru   Data Sourceu   Web URLu   li   i   u   %20u   endu[  è¯·å®è£ prettytable ä»¥è·å¾æ´æ¸æ°çç»æè§å¾ã
å®è£æ¹æ³ï¼ pip install prettytable

+--------------+-------------+---------+-------+-------+-------------+---------+
| Short Pinyin | Long Pinyin | Chinese | Latin | Namer | Data Source | Web URL |
+--------------+-------------+---------+-------+-------+-------------+---------+

%s
u   =id   u     |  u   
%s
u   -N(   u   Short Pinyinu   Long Pinyinu   Chineseu   Latinu   Nameru   Data Sourceu   Web URL(   t   getR¹   R¿   Rs   t   ENDRÀ   R·   Rv   R   t   alignt   padding_widthR   t   SPECIAL_CHARSt   FRPS_BASE_URLt   joinR   t   add_rowt
   get_string(   R=   R   t   is_clean_wordt   selection_valuet   resultt   tableR   t   each_resultR   t   normal_word_listt   urlR@   RG   R   (    (    s   latinsearch.pyR   ú  s:    	
		c         C s  |  j  j   j   } | rd | k rä | |  j k r |  j | d } g  } | j | d g  | j | d g  | j | d g  | j | d  | Sg  } |  j j |  } |  j j |  } g  g  | | rÝ | n d f S| d t j	 k r| |  j k r~|  j | d } g  } | j | d g |  j j
 |   | j | d g  | j | d g  | j | d  | S|  j j |  } | Sqy| |  j | d } g  } | j | d g |  j j
 |   | j | d g  | j | d g  | j | d  | SWqt k
 r{} g  } | j |  j j
 |   | j |  j j |   | j g   | j d  | SXn g  g  g  d f Sd S(   uk   Command of Do Query button. Get Search result.
        Then display the result @show_candidates().
        u    i    i   i   u    N(   R¹   RÃ   R   Rv   R   Ru   Rk   Rl   t   stringt	   printableRd   Rq   t   KeyErrorRe   (   R=   t
   final_nameR]   Rb   t   candidate_3t   candidate_4R   (    (    s   latinsearch.pyt   do_query(  sp    					
			
		
	
c         C sí   |  j    } | \ } } } } |  j j d d  x! | D] } |  j j d |  q8 W|  j j d d  x! | D] } |  j j d |  qo W|  j j d d  x! | D] } |  j j d |  q¦ W|  j j d d  |  j j d |  d  S(   Nu   0u   end(   RÙ   R¨   R¿   RÀ   R¬   R¯   R²   (   R=   R]   Rm   Rn   Ro   Rp   t   item(    (    s   latinsearch.pyR¼     s    c         C sN  |  j  j d d d |  j  j d d d |  j j d d d |  j j d d d |  j j d d d |  j j d d d |  j j d d d |  j j d d d |  j j d d d |  j j d d d |  j j d d d |  j j d d d |  j j d d d |  j j d d d |  j j d	 d d d
 S(   u)   Grid configuration of window and widgets.i    t   weighti   i   i   i   i   i   i   N(   Rx   t   rowconfiguret   columnconfigureR    (   R=   (    (    s   latinsearch.pyR}     s    c         C s*   |  j  j d d  |  j  j d t  d  S(   Nu   0.1u   end-1cu   end(   R·   R¿   RÀ   RÁ   (   R=   (    (    s   latinsearch.pyR   ±  s    N(   RX   RY   RZ   R0   R>   Rz   R{   R|   R:   R   RÙ   R¼   R}   R   (    (    (    s   latinsearch.pyRr   _  s   			n.	X		c         C s{   t    \ }  } t j |   } t j |  } t t d   } | j |  Wd QXt t d   } | j |  Wd QXd S(   ub   Dump generated dictinary to pickle raw file.

    Generally, this function need only do once.
    u   wbN(   R/   t   picklet   dumpsR   t   PICKLE_KEYS_FILEt   writet   PICKLE_DICT_FILE(   R.   Rv   t   pickle_keyst   pickle_dictt   f_out(    (    s   latinsearch.pyt   dump_with_pickle¶  s    c         C sp   t  |  d  " } | j   } t j |  } Wd QXt  | d  " } | j   } t j |  } Wd QX| | f S(   u'   Load keys and dict from pickle raw fileu   rbN(   R   t   readRÞ   t   loads(   t   pickle_keys_filet   pickle_dict_fileR
   Rã   R.   Rä   Rv   (    (    s   latinsearch.pyt   load_with_pickleÄ  s    c          C s8   t  t t  \ }  } t d |  d |  } | j   d S(   u   The main GUI program.R.   Rv   N(   Rë   Rà   Râ   Rr   t   mainloop(   R.   Rv   t   app(    (    s   latinsearch.pyt   gui_mainÑ  s
    	c           C s   t    d S(   u	   Main funcN(   R/   (    (    (    s   latinsearch.pyt   mainÞ  s    u   __main__(5   t
   __future__R    R   R   t   osR   t   cPickleRÞ   t   ImportErrorRÓ   RB   t   difflibR   t   prettytableR   R0   R   t   TkinterRs   R   t   tkFileDialogR¶   Rµ   t   tkintert   tkinter.scrolledtextt   scrolledtextR   R   t
   __author__t   _historyt   patht   abspathR%   Rà   Râ   RÈ   RÇ   RÁ   R   R   R$   R/   R4   t   objectR5   R\   Rt   Rr   Ræ   Rë   Rî   Rï   RX   (    (    (    s   latinsearch.pyt   <module>   s`   
&
		#			JZÿ X				