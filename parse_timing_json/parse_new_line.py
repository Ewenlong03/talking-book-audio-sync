# -*- coding: utf-8 -*-

import sys
import json
import array

# Load json file
def load_json_file(file_path):
    with open(file_path) as timing_json_file:
        return json.load(timing_json_file)


JSON_FILE_PATH = sys.argv[1]
json_array = load_json_file(JSON_FILE_PATH)
json_words_array = json_array["words"]
result_array = []

# json_words_array 是一个二维数组，它的每一个元素：
# json_word 是一个数组，["\nIf", 2.035]
for json_word in json_words_array:
    # 如果包含换行符，则拆分这个字符串，换行符单独处理。
    string = json_word[0]
    timing = json_word[1]
    if "\n" in string:
        print string + "  " +str(json_word[1])
        cLastIndex = 0
        for cIndex, c in enumerate(string, 0):
            if c=="\n" or cIndex == len(string)-1:
                if cIndex == 0 or cIndex == len(string)-1:
                    json_word_temp = []
                    json_word_temp.append(string[cLastIndex:cIndex+1])
                    json_word_temp.append(json_word[1])
                    result_array.append(json_word_temp)
                    cLastIndex = cIndex + 1
                else:
                    json_word_temp = []
                    json_word_temp.append(string[cLastIndex:cIndex])
                    json_word_temp.append(json_word[1])
                    result_array.append(json_word_temp)
                    cLastIndex = cIndex
                    json_word_temp = []
                    json_word_temp.append(string[cLastIndex:cIndex+1])
                    json_word_temp.append(json_word[1])
                    result_array.append(json_word_temp)
                    cLastIndex = cIndex+1
    else:
        result_array.append(json_word)
        
# creat a dictionary
result_dict = {
    "words" : result_array
}

# Create json file
output_json_file = JSON_FILE_PATH + ".out.json"
with open(output_json_file, "w") as outfile:
    json.dump(result_dict, outfile, indent=4)



# 如果一个字符串包含超过5个字

json_array = load_json_file(output_json_file)
json_words_array = json_array["words"]
result_array = []

# json_words_array 是一个二维数组，它的每一个元素：
# json_word 是一个数组，["\nIf", 2.035]
for json_word in json_words_array:
    # 如果包含换行符，则拆分这个字符串，换行符单独处理。
    string = json_word[0]
    timing = json_word[1]
    splited_string_array = string.split(" ")
    if len(splited_string_array) > 5:
        print splited_string_array
        count = 0
        splited_string = ""
        for idx, word in enumerate(splited_string_array, 0):
            splited_string += word + " "
            count = count + 1
            if count >= 3 or idx == len(splited_string_array)-1:
                json_word_temp = []
                json_word_temp.append(splited_string)
                json_word_temp.append(timing)
                result_array.append(json_word_temp)
                print splited_string
                count = 0
                splited_string = ""
    else:
        result_array.append(json_word)

# creat a dictionary
result_dict = {
    "words" : result_array
}

# Create json file
output_json_file = JSON_FILE_PATH + ".out.json"
with open(output_json_file, "w") as outfile:
    json.dump(result_dict, outfile, indent=4)

