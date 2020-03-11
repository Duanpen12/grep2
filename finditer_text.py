import re


def text_file_to_list(text_file):
    list_of_line = open(text_file, 'r')
    content = list_of_line.readlines()
    list_of_line.close()
    return content

text_of_file = 'my_text.txt'
my_all_file = text_file_to_list(text_of_file)
print(my_all_file)


def element_had_a_q(text):
    result_list = []
    match_list = re.finditer(r'.*q.*', text)
    if match_list:
        for match in match_list:
            result_list.append(match.group(0))
        return result_list

print("1. element had a 'q'")
for line in my_all_file:
    line = line.strip()
    print(element_had_a_q(line))


def starts_with_a_q(text):
    result_list = []
    match_list = re.finditer(r'^[q]\w+', text)
    if match_list:
        for match in match_list:
            result_list.append(match.group(0))
        return result_list

print("2. starts with a 'q'")
for line in my_all_file:
    line = line.strip()
    print(starts_with_a_q(line))


def has_th(text):
    result_list = []
    match_list = re.finditer(r'\w*th\w*', text)
    if match_list:
        for match in match_list:
            result_list.append(match.group(0))
        return result_list

print("3. has 'th'")
for line in my_all_file:
    line = line.strip()
    print(has_th(line))


def had_an_q_or_upper_q(text):
    result_list = []
    match_list = re.finditer(r'\w*[q|Q]\w*', text)
    if match_list:
        for match in match_list:
            result_list.append(match.group(0))
        return result_list

print("4. has an 'q' or a 'Q'")
for line in my_all_file:
    line = line.strip()
    print(had_an_q_or_upper_q(line))


def had_asterisk_in_it(text):
    result_list = []
    match_list = re.finditer(r'\w*[*]\w*', text)
    if match_list:
        for match in match_list:
            result_list.append(match.group(0))
        return result_list

print("5. has a '*' in it")
for line in my_all_file:
    line = line.strip()
    print(had_asterisk_in_it(line))


def start_with_an_q_or_q(text):
    result_list = []
    match_list = re.finditer(r'^[q|Q]\w+', text)
    if match_list:
        for match in match_list:
            result_list.append(match.group(0))
        return result_list

print("6. starts with an 'q' or an 'Q'")
for line in my_all_file:
    line = line.strip()
    print(start_with_an_q_or_q(line))


# def had_both_a_and_e_in_it(text):
#     result_list = []
#     match_list = re.finditer(r'(\w*a\w*e\w*)|(\w*e\w*a\w*)', text)
#     if match_list:
#         for match in match_list:
#             result_list.append(match.group(0))
#         return result_list
#
# print("7. has both 'a' and 'e' in it")
# for line in my_all_file:
#     line = line.strip()
#     print(had_both_a_and_e_in_it(line))


def has_an_a_and_somewhere_later_an_e(text):
    result_list = []
    match_list = re.finditer(r'(\w*a\w*e)\b', text)
    if match_list:
        for match in match_list:
            result_list.append(match.group(1))
        return result_list

print("8. has an 'a' and somewhere later an 'e'")
for line in my_all_file:
    line = line.strip()
    print(has_an_a_and_somewhere_later_an_e(line))


def does_not_have_an_a(text):
    result_list = []
    match_list = re.finditer(r'\b([^a]*)\b', text)
    if match_list:
        for match in match_list:
            result_list.append(match.group(1))
        return result_list

print("9. does not have an 'a'")
for line in my_all_file:
    line = line.strip()
    print(does_not_have_an_a(line))


# def does_not_have_an_a_nor_e(text):
#     result_list = []
#     match_list = re.finditer(r'\b([^a|e]*)\b', text)
#     if match_list:
#         for match in match_list:
#             result_list.append(match.group(0))
#         return result_list
#
# print("10. does not have an 'a' nor 'e'")
# for line in my_all_file:
#     line = line.strip()
#     print(does_not_have_an_a_nor_e(line))
#
# #
def has_an_a_but_not_e(text):
    result_list = []
    match_list = re.finditer(r'(\w*[a]\w(\b([^e]*)\b))\W', text) #(\w*[a]\w*[e])\W
    if match_list:
        for match in match_list:
            result_list.append(match.group(0))
        return result_list

print("11. has an 'a' but not 'e'")
for line in my_all_file:
    line = line.strip()
    print(has_an_a_but_not_e(line))


def has_at_least_two_consecutive(text):
    result_list = []
    match_list = re.finditer(r'(\w*[aeiou]{2,})\w*', text)
    if match_list:
        for match in match_list:
            result_list.append(match.group(0))
        return result_list

print("12. has at least 2 consecutive vowels (a,e,i,o,u) like in the word bear")
for line in my_all_file:
    line = line.strip()
    print(has_at_least_two_consecutive(line))


def has_at_least_three_vowels(text):
    result_list = []
    match_list = re.finditer(r'(\w*[aeiou]){3,}\b', text)
    if match_list:
        for match in match_list:
            result_list.append(match.group(0))
        return result_list

print("13. has at least 3 vowels")
for line in my_all_file:
    line = line.strip()
    print(has_at_least_three_vowels(line))


def had_at_least_six_characters(text):
    result_list = []
    match_list = re.finditer(r'\b(\w{6,})\b', text)
    if match_list:
        for match in match_list:
            result_list.append(match.group(0))
        return result_list

print("14. has at least 6 characters")
for line in my_all_file:
    line = line.strip()
    print(had_at_least_six_characters(line))


def had_at_exactly_six_characters(text):
    result_list = []
    match_list = re.finditer(r'\b(\w{6})\b', text)
    if match_list:
        for match in match_list:
            result_list.append(match.group(0))
        return result_list

print("15. has at exactly 6 characters")
for line in my_all_file:
    line = line.strip()
    print(had_at_exactly_six_characters(line))


def all_the_word_with_either_bar_baz(text):
    result_list = []
    match_list = re.finditer(r'(\w*ba[rz]\w*)\b', text)
    if match_list:
        for match in match_list:
            result_list.append(match.group(0))
        return result_list

print("16. all the words with either 'Bar' or 'Baz' in them")
for line in my_all_file:
    line = line.strip()
    print(all_the_word_with_either_bar_baz(line))


def have_banana_pie_or_apple_pie(text):
    result_list = []
    match_list = re.finditer(r'\b(.*banana pie.*|.*apple pie.*)\b', text)
    if match_list:
        for match in match_list:
            result_list.append(match.group())
        return result_list

print("17. all the rows with either 'apple pie' or 'banana pie' in them")
for line in my_all_file:
    line = line.strip()
    print(have_banana_pie_or_apple_pie(line))













