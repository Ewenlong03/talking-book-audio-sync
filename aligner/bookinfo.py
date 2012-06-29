#!/usr/bin/env python
"""
Basic metadata for books of the Bible
"""

class BookInfo:
    def __init__(self, chapters, osis, nasb, name, index):
        self.chapters = chapters
        self.osis = osis
        self.nasb = nasb
        self.name = name
        self.index = index

# @todo This might work better as an OrderedDict, keyed by osisBook
books = (
    BookInfo(range(1,50+1),  'Gen',    'Gen',    'Genesis', 		1),
    BookInfo(range(1,40+1),  'Exod',   'Exo',   'Exodus', 		2),
    BookInfo(range(1,27+1),  'Lev',    'Lev',    'Leviticus', 	3),
    BookInfo(range(1,36+1),  'Num',    'Num',    'Numbers', 		4),
    BookInfo(range(1,34+1),  'Deut',   'Deu',   'Deuteronomy', 	5),
    BookInfo(range(1,24+1),  'Josh',   'Jos',   'Joshua', 		6),
    BookInfo(range(1,21+1),  'Judg',   'Jdg',   'Judges', 		7),
    BookInfo(range(1,4+1),   'Ruth',   'Rth',   'Ruth', 			8),
    BookInfo(range(1,31+1),  '1Sam',   '1Sa',   '1 Samuel', 		9),
    BookInfo(range(1,24+1),  '2Sam',   '2Sa',   '2 Samuel', 		10),
    BookInfo(range(1,22+1),  '1Kgs',   '1Ki',   '1 Kings', 		11),
    BookInfo(range(1,25+1),  '2Kgs',   '2Ki',   '2 Kings', 		12),
    BookInfo(range(1,29+1),  '1Chr',   '1Ch',   '1 Chronicles', 	13),
    BookInfo(range(1,36+1),  '2Chr',   '2Ch',   '2 Chronicles', 	14),
    BookInfo(range(1,10+1),  'Ezra',   'Ezr',   'Ezra', 			15),
    BookInfo(range(1,13+1),  'Neh',    'Neh',    'Nehemiah', 		16),
    BookInfo(range(1,10+1),  'Esth',   'Est',   'Esther', 		17),
    BookInfo(range(1,42+1),  'Job',    'Job',    'Job', 			18),
    BookInfo(range(1,150+1), 'Ps',     'Psa',     'Psalms', 		19),
    BookInfo(range(1,31+1),  'Prov',   'Pro',   'Proverbs', 		20),
    BookInfo(range(1,12+1),  'Eccl',   'Ecc',   'Ecclesiastes', 	21),
    BookInfo(range(1,8+1),   'Song',   'Son',   'Song of Solomon', 22),
    BookInfo(range(1,66+1),  'Isa',    'Isa',    'Isaiah', 		23),
    BookInfo(range(1,52+1),  'Jer',    'Jer',    'Jeremiah', 		24),
    BookInfo(range(1,5+1),   'Lam',    'Lam',    'Lamentations', 	25),
    BookInfo(range(1,48+1),  'Ezek',   'Eze',   'Ezekiel', 		26),
    BookInfo(range(1,12+1),  'Dan',    'Dan',    'Daniel', 		27),
    BookInfo(range(1,14+1),  'Hos',    'Hos',    'Hosea', 		28),
    BookInfo(range(1,3+1),   'Joel',   'Joe',   'Joel', 			29),
    BookInfo(range(1,9+1),   'Amos',   'Amo',   'Amos', 			30),
    BookInfo(range(1,1+1),   'Obad',   'Oba',   'Obadiah', 		31),
    BookInfo(range(1,4+1),   'Jonah',  'Jon',  'Jonah', 		32),
    BookInfo(range(1,7+1),   'Mic',    'Mic',    'Micah', 		33),
    BookInfo(range(1,3+1),   'Nah',    'Nah',    'Nahum', 		34),
    BookInfo(range(1,3+1),   'Hab',    'Hab',    'Habakkuk', 		35),
    BookInfo(range(1,3+1),   'Zeph',   'Zep',   'Zephaniah', 	36),
    BookInfo(range(1,2+1),   'Hag',    'Hag',    'Haggai', 		37),
    BookInfo(range(1,14+1),  'Zech',   'Zec',   'Zechariah', 	38),
    BookInfo(range(1,4+1),   'Mal',    'Mal',    'Malachi', 		39),
    BookInfo(range(1,28+1),  'Matt',   'Mat',   'Matthew', 		40),
    BookInfo(range(1,16+1),  'Mark',   'Mar',   'Mark', 			41),
    BookInfo(range(1,24+1),  'Luke',   'Luk',   'Luke', 			42),
    BookInfo(range(1,21+1),  'John',   'Joh',   'John', 			43),
    BookInfo(range(1,28+1),  'Acts',   'Act',   'Acts', 			44),
    BookInfo(range(1,16+1),  'Rom',    'Rom',    'Romans', 		45),
    BookInfo(range(1,16+1),  '1Cor',   '1Co',   '1 Corinthians', 46),
    BookInfo(range(1,13+1),  '2Cor',   '2Co',   '2 Corinthians', 47),
    BookInfo(range(1,6+1),   'Gal',    'Gal',    'Galatians', 	48),
    BookInfo(range(1,6+1),   'Eph',    'Eph',    'Ephesians', 	49),
    BookInfo(range(1,4+1),   'Phil',   'Phi',   'Philippians', 	50),
    BookInfo(range(1,4+1),   'Col',    'Col',    'Colossians', 	51),
    BookInfo(range(1,5+1),   '1Thess', '1Th', '1 Thessalonians', 52),
    BookInfo(range(1,3+1),   '2Thess', '2Th', '2 Thessalonians', 53),
    BookInfo(range(1,6+1),   '1Tim',   '1Ti',   '1 Timothy', 	54),
    BookInfo(range(1,4+1),   '2Tim',   '2Ti',   '2 Timothy', 	55),
    BookInfo(range(1,3+1),   'Titus',  'Tts',  'Titus', 		56),
    BookInfo(range(1,1+1),   'Phlm',   'Phi',   'Philemon', 		57),
    BookInfo(range(1,13+1),  'Heb',    'Heb',    'Hebrews', 		58),
    BookInfo(range(1,5+1),   'Jas',    'Jam',    'James', 		59),
    BookInfo(range(1,5+1),   '1Pet',   '1Pe',   '1 Peter', 		60),
    BookInfo(range(1,3+1),   '2Pet',   '2Pe',   '2 Peter', 		61),
    BookInfo(range(1,5+1),   '1John',  '1Jo',  '1 John', 		62),
    BookInfo(range(1,1+1),   '2John',  '2Jo',  '2 John', 		63),
    BookInfo(range(1,1+1),   '3John',  '3Jo',  '3 John', 		64),
    BookInfo(range(1,1+1),   'Jude',   'Jud',   'Jude', 			65),
    BookInfo(range(1,22+1),  'Rev',    'Rev',    'Revelation', 	66),
)


def get_book_subset(args):
    """
    Get a subset of BookInfo books; if args is empty, returns all books
    
    args -- a list of osisBooks and chapter numbers; the chapter numbers are associated
    
    with their immediately-preceding osisBook. If an osisBook appears without any
    subsequent chapters, then all chapters in the book will be returned.
    
    >>> subset_books = get_book_subset('John', '1')
    >>> len(subset_books)
    1
    >>> subset_books[0].osis
    'John'
    >>> len(subset_books[0].chapters)
    1
    >>> subset_books[0].chapters[0]
    1
    >>> subset_books = get_book_subset('Mark', '1', '3', '6', 'Jude')
    >>> subset_books[0].chapters
    [1, 3, 6]
    >>> len(subset_books)
    2
    >>> subset_books[1].osis
    'Jude'
    >>> subset_books[1].chapters
    [1]
    >>> len(get_book_subset())
    66
    >>> subset_books = get_book_subset('Mark', '1', 'Mark')
    Traceback (most recent call last):
    ...
    ValueError: You already provided the osisBook 'Mark'
    >>> subset_books = get_book_subset('1', 'Mark')
    Traceback (most recent call last):
    ...
    ValueError: Expected osisBook. A chapter must be preceded by an osisBook
    >>> subset_books = get_book_subset('Jude', 2)
    Traceback (most recent call last):
    ...
    ValueError: Chapter '2' does not exist in Jude
    >>> subset_books = get_book_subset('Matt', 1, 2, 3, 'FOO')
    Traceback (most recent call last):
    ...
    ValueError: Invalid arg 'FOO'. Expected valid osisBook or chapter.
    >>> subset_books = get_book_subset('Matt', 1, 2, 1)
    Traceback (most recent call last):
    ...
    ValueError: You already provided chapter '1' for Matt
    
    """
    
    import re
    from copy import deepcopy
    from collections import OrderedDict
    
    osis_books = [book.osis for book in books]
    current_osis_book = None
    subset_book_dict = OrderedDict()
    for arg in args:
        # osisBook
        if arg in osis_books:
            if arg in subset_book_dict:
                raise ValueError("You already provided the osisBook '%s'" % arg)
            current_osis_book = arg
            subset_book_dict[current_osis_book] = []
        # chapter
        elif re.match('^\d+$', str(arg)):
            if current_osis_book is None:
                raise ValueError("Expected osisBook. A chapter must be preceded by an osisBook")
            
            chapter = int(arg)
            if chapter not in books[osis_books.index(current_osis_book)].chapters:
                raise ValueError("Chapter '%d' does not exist in %s" % (chapter, current_osis_book))
            
            if chapter in subset_book_dict[current_osis_book]:
                raise ValueError("You already provided chapter '%d' for %s" % (chapter, current_osis_book))
            subset_book_dict[current_osis_book].append(chapter)
        else:
            raise ValueError("Invalid arg '%s'. Expected valid osisBook or chapter." % arg)
    
    if len(subset_book_dict.keys()) == 0:
        return books
    else:
        subset_books = []
        for osis_book, chapters in subset_book_dict.iteritems():
            if len(chapters) == 0:
                subset_books.append(books[osis_books.index(osis_book)])
            else:
                book_info = deepcopy(books[osis_books.index(osis_book)])
                book_info.chapters = chapters
                subset_books.append(book_info)
        return subset_books


# Run tests
if __name__ == '__main__':
    import sys
    if '--json' in sys.argv:
        import json
        print json.dumps([book.__dict__ for book in books], indent=4)
    elif '--js' in sys.argv:
        import json
        import re
        bookinfo_json = json.dumps([book.__dict__ for book in books], indent=4)
        bookinfo_js = re.sub(r'\[\s+(\d+)[^\]]+?(\d+)\s+\]', '_.range(\g<1>, \g<2>+1)', bookinfo_json, 0, re.S)
        bookinfo_js = re.sub(r'\[\s+(\d+)\s+\]', '_.range(\g<1>, \g<1>+1)', bookinfo_js, 0, re.S)
        print bookinfo_js
    else:
        print "Running tests wthout without any args"
        import doctest
        doctest.testmod()
