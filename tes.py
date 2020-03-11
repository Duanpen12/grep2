import re


def text_file_to_list(text_file):
    f = open(text_file, 'r')
    content = f.readlines()
    f.close()
    return content


text_of_file = 'my_text.txt'
regex_line = text_file_to_list(text_of_file)

# matching one character
print("Matching one character:")
regex_one_q_character = 'q'
for line in regex_line:
    line = line.strip()
    line_match = re.search(regex_one_q_character, line)
    if line_match:
        # print("\t   this line match regex '%s':      " % regex_one_q_character, line)
        print("\t      first match for regex '%s' is:        " % regex_one_q_character, line_match.group(0))
    # else:
    #     print("\tline doesn't match regex '%s':   " % regex_one_q_character, line)


# matching whole line
print("Matching whole line:")
regex_whole_line_having_q = '.*q.*'
for line in regex_line:
    line = line.strip()
    line_match = re.search(regex_whole_line_having_q, line)
    if line_match:
        # print("\t   this line match regex '%s':      " % regex_whole_line_having_q, line)
        print("\t      first match for regex '%s' is:        " % regex_whole_line_having_q, line_match.group(0))
    # else:
    #     print("\tline doesn't match regex '%s':   " % regex_one_q_character, line)


# matching one word starting with q
print("Matching one word starting with q:")
regex_one_word_having_q = 'q\w+'  # '\w' means word character, it's the same what '[a-zA-Z0-9_]'.
# '+' means one or more occurences, so '\w+' is one or more occurences of word character
for line in regex_line:
    line = line.strip()
    line_match = re.search(regex_one_word_having_q, line)
    if line_match:
        # print("\t   this line match regex '%s':      " % regex_one_word_having_q, line)
        print("\t      first match for regex '%s' is:        " % regex_one_word_having_q, line_match.group(0))
    # else:
    #     print("\tline doesn't match regex '%s':   " % regex_one_word_having_q, line)

# matching one word ending with o
print("Matching one word ending with o:")
regex_one_word_ending_with_o = '(\w+o)\W'  # '\w' means word character, it's the same what '[a-zA-Z0-9_]'.
# '+' means one or more occurences, so '\w+' is one or more occurences of word character. '\W' is non word character -
# - can be space, coma, new line. In order to don't include this non word character in result, i used brackets '(\w+o)'
# to get results only for brackets. line_match.group(0) is whole match, line_match.group(1) is match from brackets
for line in regex_line:
    line = line.strip()
    line_match = re.search(regex_one_word_ending_with_o, line)
    if line_match:
        # print("\t   this line match regex '%s':      " % regex_one_word_ending_with_o, line)
        print("\t      first match for regex '%s' is:        " % regex_one_word_ending_with_o, line_match.group(1))
    # else:
    #     print("\tline doesn't match regex '%s':   " % regex_one_word_ending_with_o, line)


# matching one word containing s in the middle (not at the beginning, nor at the end)
print("Matching one word containing s in the middle:")
regex_one_word_containing_s_in_the_middle = '\w+s\w+'  # '\w' means word character, it's the same what '[a-zA-Z0-9_]'.
# '+' means one or more occurences, so '\w+' is one or more occurences of word character
for line in regex_line:
    line = line.strip()
    line_match = re.search(regex_one_word_containing_s_in_the_middle, line)
    if line_match:
        # print("\t   this line match regex '%s':      " % regex_one_word_containing_s_in_the_middle, line)
        print("\t      first match for regex '%s' is:        " % regex_one_word_containing_s_in_the_middle, line_match.group(0))
    # else:
    #     print("\tline doesn't match regex '%s':   " % regex_one_word_containing_s_in_the_middle, line)

