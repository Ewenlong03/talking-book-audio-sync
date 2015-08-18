# -*- coding: utf-8 -*- 

# Refer
# [1 Search for string in txt file](http://stackoverflow.com/questions/4940032/search-for-string-in-txt-file-python)
# [2 Parsing values from a JSON file](http://stackoverflow.com/questions/2835559/parsing-values-from-a-json-file-in-python)
# [3 How to read next word from file](http://stackoverflow.com/questions/24753866/how-to-read-next-word-or-words-till-next-line-from-file-in-python)
# [4 Start index for iterating Python list](http://stackoverflow.com/a/6148636/2722270)
# [5 Write JSON data to file in python](http://stackoverflow.com/a/12309296/2722270)
# [6 How to remove an element from a list by index in Python?](http://stackoverflow.com/a/627441/2722270)
# [7 15 Python Array Examples – Declare, Append, Index, Remove, Count](http://www.thegeekstuff.com/2013/08/python-array/)
# [8 Two dimensional array in python](http://stackoverflow.com/a/8183168/2722270)
# [9 Python中用json.loads解码字符串出错：ValueError: No JSON object could be decoded](http://www.crifan.com/python_json_loads_valueerror_no_json_object_could_be_decoded/)
# [10 Saving and loading data in Python with JSON](http://kaira.sgo.fi/2014/05/saving-and-loading-data-in-python-with.html)

import sys
import json
import mmap
import re
import array
from pprint import  pprint


# this parameter maybe make a difference in building timing-json-file.
MAX_MATCHING_TIME = 80


# [Splitting a string into words and punctuation](http://stackoverflow.com/a/367292/2722270)
def split_str_into_words_and_punc(string):
    return re.findall(r"[\w']+|[.,!?;-]", string)


# [Compare two string ignore case](http://stackoverflow.com/a/11993250/2722270)
def is_equal(a, b):
    try:
        return a.upper() == b.upper()
    except AttributeError:
        return a == b

#
def is_punctuation(c):
    return is_equal(c,'.') or is_equal(c,',') or is_equal(c,'!') or is_equal(c,'?') or is_equal(c,';') or is_equal(c, '-')


#
def join_array_to_string(array):
    if len(array) <= 0:
        return ""
    result = array[0]
    if (len(array) >= 1):
        for element in array[1:]:
            if is_punctuation(element):
                result += element
            else:
                result += " " + element
    return result
        

# Split file into words, with all seperators include punctuation and line break.
def split_file_into_words_with_all_seperators(file_path):
    words_in_file = []
    with open(file_path) as raw_file:
        # raw_data = mmap.mmap(raw_file.fileno(), 0, access=mmap.ACCESS_READ)
        lines = raw_file.readlines() # split file by lines
        for line in lines:
            words_in_file += split_str_into_words_and_punc(line) + ['\n']
        return words_in_file        


# Load json file
def load_json_file(file_path):
    with open(file_path) as timing_json_file:
        return json.load(timing_json_file)


# Search the given word in the give array start from specific index,
# If found within given time, then return the index, else return -1.
def search_word_in_array(word_to_search, array, start_idx):
    for idx, word in enumerate(array[start_idx:], start_idx):
        # print "<search_word_in_array> " + str(idx) + "  " + word_to_search + " --vs-- " + word
        if (idx - start_idx) > MAX_MATCHING_TIME:
            return -1
        if is_equal(word_to_search, word):
            return idx
    return -1
'''
print "test search_word_in_array function:"
print search_word_in_array('1', txt_array, 0)
print search_word_in_array('grippe', txt_array, 1111)
print search_word_in_array('to da', txt_array, 0)
'''


# Search some words in the given array start from specific index,
# If these given words are matched sequentially within 30 words in the array,
# We can assume that the 1st word is in same context, then return the index of array.
def search_words_in_array(words_to_search, array, start_idx):
    #print "<search_words_in_array>"
    # print words_to_search
    found_idx_array = []
    for word_to_search in words_to_search:
        found_idx = search_word_in_array(word_to_search, array, start_idx)
        if (found_idx == -1):
            # print word_to_search + " not exist."
            return -1
        elif (found_idx - start_idx) > MAX_MATCHING_TIME:
            # print word_to_search + " beyond range " + str(found_idx) + " - " + str(start_idx)
            return -1
        else:
            found_idx_array.append(found_idx)
            start_idx = found_idx + 1
            # print word_to_search + " " + str(found_idx)
    return found_idx_array[0]


# Search a given word in the given file, if the word exists in the file, return True.
# print search_word_in_file("da", 'chapter1.txt')

'''
# cannot work, since if find a sub-string of a word, it will also return true.
    with open(file_path) as file:
        data = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
    found = data.find(word_to_search)
    return (found != -1)
'''
def search_word_in_file(word_to_search, file_path):
    array = split_file_into_words_with_all_seperators(file_path)
    for word in array:
        if is_equal(word_to_search, word):
            return True
    return False
'''
print "test search_word_in_file function:" 
print search_word_in_file("probabl", 'chapter1.txt')
print search_word_in_file("probably", 'chapter1.txt')
'''


# main
# 
# 从json文件中取出5个words，与给定的array（从指定的下标开始计数，30个以内）做匹配,
# 如果可以顺序匹配到这5个words，则认为第1个word是处于同样上下文中的同一个单词，
# 那么把json文件中的时间戳写入到txt文件对应的单词后.

# long-audio-align生成的json文件，存在省略标点的错误：isnt, 

# 1个单词, 在txt文件中查找与之匹配的单词,
# 若找到, 则从json文件中顺序取出第2个单词，从上一个匹配的txt单词之后开始查找,
# 若找到, 则取出第3个单词, ...
# 当第5次匹配，并且查找的txt单词不超过30个时,
# 则认为第1次匹配的单词是处于同样上下文中的同一个单词, 
# 
# json key is "words", word[0] represent the word, word[1] represent start timestamp of the word.

# donot check sys.argv
JSON_FILE_PATH = sys.argv[1]
TXT_FILE_PATH = sys.argv[2]

json_array = load_json_file(JSON_FILE_PATH)
json_words_array = json_array["words"]
txt_array = split_file_into_words_with_all_seperators(TXT_FILE_PATH)

# delete word in json file but not exists in txt file
for idx, json_word in enumerate(json_words_array, 0):
    if search_word_in_file(json_word[0], TXT_FILE_PATH)==False:
        # print "remove " + json_word[0] + str(idx)
        json_words_array.pop(idx)

# start to match
last_json_idx = 0
start_find_idx = 0
found_idx = 0
last_found_idx = 0
result_array = []
for json_idx, json_word in enumerate(json_words_array, 0):
    if (json_idx <= len(json_words_array) - 5):
        to_search_array = [json_words_array[json_idx][0], json_words_array[json_idx+1][0], json_words_array[json_idx+2][0], json_words_array[json_idx+3][0], json_words_array[json_idx+4][0]]
        found_idx = search_words_in_array(to_search_array, txt_array, start_find_idx)
        if (found_idx == -1):
            continue
        else:
            found_word_array = []
            # print "result range [" + str(last_found_idx+1) + ", " + str(found_idx) + "]"
            for txt_idx, word in enumerate(txt_array[last_found_idx+1:], last_found_idx+1):
                if (txt_idx > found_idx):
                    break
                found_word_array.append(word)
            # print "%.3f" %json_words_array[last_json_idx+1][1], join_array_to_string(found_word_array)
            #  
            found_timing = json_words_array[last_json_idx+1][1]
            found_string = join_array_to_string(found_word_array)
            found_group = []
            found_group.append(found_string)
            found_group.append(found_timing)
            result_array.append(found_group)
            #
            start_find_idx = found_idx + 1
            last_found_idx = found_idx
            last_json_idx = json_idx


# process the end of the txt array
found_word_array = []
for idx, word in enumerate(txt_array[last_found_idx+1:], last_found_idx+1):
    found_word_array.append(word)
found_string = join_array_to_string(found_word_array)
result_array[len(result_array)-1][0] =  result_array[len(result_array)-1][0] + " " + found_string

# creat a dictionary
result_dict = {
    "words" : result_array
}

# Create json file
output_json_file = JSON_FILE_PATH + ".out.json"
with open(output_json_file, "w") as outfile:
    json.dump(result_dict, outfile, indent=4)
