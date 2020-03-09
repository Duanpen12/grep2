import re


def element_had_a_q(text):
    result_list = []
    match_list = re.finditer(r'\b(\w*q\w*)\b', text)
    if match_list:
        for match in match_list:
            result_list.append(match.group(1))
        return result_list

word_element_had_a_q = element_had_a_q("Iraq is a country located in the Middle East leopard"
                                       "In the Middle East leopard Mosque "
                                       "Banana pie qaids banana pie")

print(word_element_had_a_q)

# print(element_had_a_q("Iraq is a country located in the Middle East leopard qaids and Mosque"))
# assert element_had_a_q("Iraq is a country located in the Middle East leopard") == ["Iraq"]
# assert element_had_a_q("is a country") == []
# assert element_had_a_q("banana pie qaids banana pie Iraq and mosque") == ["qaids", "Iraq", "mosque"]


def starts_with_a_q(text):
    result_list = []
    match_list = re.finditer(r'\b(q\w*)\b', text)
    if match_list:
        for match in match_list:
            result_list.append(match.group(1))
    return result_list

word_start_with_a_q = starts_with_a_q("quality needs to have prere ekamai"
                                      "banana pie qaids banana pie"
                                      "Do you have any question"
                                      "in the Middle East leopard")

# print(word_start_with_a_q)

#
# print(starts_with_a_q("do you have any question"))
# assert starts_with_a_q("quality needs to have prere ekamai") == ["quality"]
# assert starts_with_a_q("need to have prere") == []
# assert starts_with_a_q("quick banana pie qaids question banana pie quality ") == ["quick", "qaids", "question", "quality"]


def has_th_in_it(text):
    result_list = []
    match_list = re.finditer(r'\b(\w*th\w*)\b', text)
    if match_list:
        for match in match_list:
            result_list.append(match.group(0))
    return result_list

word_had_th_in_it = has_th_in_it("first alerted the world in 1985 that a deep thinning was occurring "
                                 "although we know it's a greenhouse gas "
                                 "along with Joe Farman and Brian Gardiner")

# print(word_had_th_in_it)

#
# print(has_th_in_it("although emissions to the atmosphere are relatively small at the moment, they are increasing"))
# assert has_th_in_it("the dogs are open a door last night") == ["the"]
# assert has_th_in_it("open door") == []
# assert has_th_in_it("when the door open that girl call them come in") == ["the", "that", "them"]


def has_an_q_or_upper_q(text):
    result_list = []
    match_list = re.finditer(r'\b(\w*[q|Q]\w*)\b', text)
    if match_list:
        for match in match_list:
            result_list.append(match.group(0))
    return result_list

word_has_q_or_upper_q = has_an_q_or_upper_q("Teaching experience is a necessary qualification for a tutor"
                                            "Permission is not required to link directly"
                                            "Questions for the ESL Classroom"
                                            "He goes into its Cambridge HQ"
                                            )

# print(word_has_q_or_upper_q)

# print(has_an_q_or_upper_q("its cambridge HQ twice, quick up banana pie qaids banana pie"))
# assert has_an_q_or_upper_q("He goes into its Cambridge HQ twice a week interpret the Dobson data") == ["HQ"]
# assert has_an_q_or_upper_q("we go to into its") == []
# assert has_an_q_or_upper_q("its cambridge HQ twice, quick up banana pie qaids banana pie") == ["HQ", "quick", "qaids"]


def had_asterisk_in_it(text):
    result_list = []
    match_list = re.finditer(r'\b(\w*[*]\w*)\b', text)
    if match_list:
        for match in match_list:
            result_list.append(match.group(0))
    return result_list

word_had_asterisk_in_it = had_asterisk_in_it("**Dr **Thomas* bar*ningham"
                                             "he's still very plugged in*to the politics of ozone"
                                             "There was an assumption they would don*t harm* "
                                             "the* although we know it's a greenhouse gas")

# print(word_had_asterisk_in_it)

# print(had_asterisk_in_it("i shall go to the shopping mall tomorrow*night and i will have eaten lunch by the time i*get home"))
# assert had_asterisk_in_it("She is talking with her boyfriend i*love you") == ["i*love"]
# assert had_asterisk_in_it("she is talking") == []
# assert had_asterisk_in_it("i shall go to the shopping mall tomorrow*night and i will have eaten lunch by the time i*get home") == ["tomorrow*night", "i*get"]


def start_with_q_or_upper_q(text):
    result_list = []
    match_list = re.finditer(r'\b([q|Q]\w*)\b', text)
    if match_list:
        for match in match_list:
            result_list.append(match.group())
    return result_list

word_start_with_q_or_upper_q = start_with_q_or_upper_q("Questions for the ESL Classroom"
                                                       "Ning is the most qualified candidate for this job"
                                                       "Do you have any question")

# print(word_start_with_q_or_upper_q)

# print(start_with_q_or_upper_q("quick glance this year might lead you to think we've fixed the ozone hole Quality"))
# assert start_with_q_or_upper_q("quick glance this year might lead you to think we've fixed the ozone hole") == ["quick"]
# assert start_with_q_or_upper_q("glance this year") == []
# assert start_with_q_or_upper_q("Quality needs to have prere") == ["Quality"]


def had_both_a_and_e_in_it(text):
    result_list = []
    match_list = re.finditer(r'\b(\w*a\w*e\w*)\b|\b(\w*e\w*a\w*)\b', text)
    if match_list:
        for match in match_list:
            result_list.append(match.group(0))
    return result_list

word_had_both_a_and_e = had_both_a_and_e_in_it("the ozone above Antarctica "
                                               "We're very pleased to have reached this milestone "
                                               "the each spring in the winter ")

# print(word_had_both_a_and_e)

# print(had_both_a_and_e_in_it("It's delivering ozone measurements computer back in the UK via satellite"))
# assert had_both_a_and_e_in_it("Dr Shanklin worries that SF6 is being treated") == ["treated"]
# assert had_both_a_and_e_in_it("Dr Shanklin") == []
# assert had_both_a_and_e_in_it("It's delivering ozone measurements computer back in the UK via satellite") == ["measurements", "satellite"]


def has_an_a_and_somewhere_later_an_e(text):
    result_list = []
    match_list = re.finditer(r'\b(\w*a\w*e)\b', text)
    if match_list:
        for match in match_list:
            result_list.append(match.group(1))
    return result_list

word_has_a_somewhere_later_e = has_an_a_and_somewhere_later_an_e("Dr Shanklin's computer back in the UK via satellite "
                                                                 "absolute and apple "
                                                                 "threadbare and banana")

# print(word_has_a_somewhere_later_e)

# print(has_an_a_and_somewhere_later_an_e("Dr Shanklin's computer back in the UK via satellite"))
# assert has_an_a_and_somewhere_later_an_e("absolute and apple") == ["absolute", "apple"]
# assert has_an_a_and_somewhere_later_an_e("this a banana") == []
# assert has_an_a_and_somewhere_later_an_e("threadbare and climate and glance") == ["threadbare", "climate", "glance"]


def does_not_have_an_a(text):
    result_list = []
    match_list = re.finditer(r'\b[^a\W]+\b', text)
    if match_list:
        for match in match_list:
            result_list.append(match.group(0))
        return result_list

word_does_not_have_a = does_not_have_an_a("banana pie Dr Shanklin and his colleagues at the British "
                                          "As time progresses, probably later in October "
                                          "along with Joe Farman and Brian Gardiner")

# print(word_does_not_have_a)

# print(does_not_have_an_a("Ozone filters out harmful ultraviolet radiation from the Sun apple pie"))
# assert does_not_have_an_a("Ozone filters out harmful ultraviolet radiation from the Sun apple pie") == ["Ozone", "filters", "out", "from", "the", "Sun", "pie"]
# assert does_not_have_an_a("team what Montreal") == []
# assert does_not_have_an_a("Ozone filters out harmful ultraviolet radiation from the Sun") == ["Ozone", "filters", "out", "from", "the", "Sun"]


def does_not_have_an_a_nor_e(text):
    result_list = []
    match_list = re.finditer(r'\b([^a|e\W]+)\b', text)
    if match_list:
        for match in match_list:
            result_list.append(match.group(0))
        return result_list

word_does_not_have_a_or_e = does_not_have_an_a_nor_e("The team discovery confirming the theoretical predictions of others")

# print(word_does_not_have_a_or_e)

# print(does_not_have_an_a_nor_e("The team discovery confirming the theoretical predictions of others led to the Montreal Protocol"))
# assert does_not_have_an_a_nor_e("The team discovery confirming the theoretical predictions of others led to the Montreal Protocol") == ["confirming", "of", "to", "Protocol"]
# assert does_not_have_an_a_nor_e("team what Montreal") == []
# assert does_not_have_an_a_nor_e("The team discovery confirming the theoretical predictions of others led to") == ["confirming", "of", "to"]


def has_an_a_but_not_e(text):
    result_list = []
    match_list = re.finditer(r'\b(\w*[a]\w([^e\W]+))\b', text)
    if match_list:
        for match in match_list:
            result_list.append(match.group(1))
        return result_list

word_has_a_but_not_e = has_an_a_but_not_e("It's very clear that the ozone data coming back")

# print(word_has_a_but_not_e)

# print(has_an_a_but_not_e("The team discovery confirming the theoretical predictions of others led to the Montreal Protocol and"))
# assert has_an_a_but_not_e("The team discovery confirming the theoretical predictions of others led to the Montreal Protocol and") == ["and"]
# assert has_an_a_but_not_e("team they Montreal") == []
# assert has_an_a_but_not_e("Dr Shanklin, along with Joe Farman and") == ["Shanklin", "along", "Farman", "and"]


def has_at_least_two_consecutive(text):
    result_list = []
    match_list = re.finditer(r'\b(\w*[aoieu]{2,}\w*)\b', text)
    if match_list:
        for match in match_list:
            result_list.append(match.group(1))
        return result_list

word_has_at_two_conversation = has_at_least_two_consecutive("Ozone filters out harmful "
                                                            "The team's discovery "
                                                            "occurring in the ozone layer above Antarctica each spring "
                                                            "we should really only view it as an anomaly")

# print(word_has_at_two_conversation)

# print(has_at_least_two_consecutive("Ozone filters out harmful ultraviolet radiation from the Sun apple pie banana apple"))
# assert has_at_least_two_consecutive("Ozone filters out harmful ultraviolet radiation from the Sun apple pie banana apple") == ["out", "ultraviolet", "radiation", "pie"]
# assert has_at_least_two_consecutive("Ozone filters") == []
# assert has_at_least_two_consecutive("Ozone filters out harmful ultraviolet") == ["out", "ultraviolet"]


def has_at_least_three_vowels(text):
    result_list = []
    match_list = re.finditer(r'\b((\w*[aeiou]){3,}\w*)\b', text)
    if match_list:
        for match in match_list:
            result_list.append(match.group(0))
        return result_list

word_has_at_least_three_vowels = has_at_least_three_vowels("We're very pleased to have reached this milestone "
                                                           "these substances were being used widely as refrigerants "
                                                           "banana pie question")

# print(word_has_at_least_three_vowels)

# print(has_at_least_three_vowels("banana pie qaidsea banana pie"))
# assert has_at_least_three_vowels("There was an assumption they would do no harm banana") == ["assumption", "banana"]
# assert has_at_least_three_vowels("the globe so we can") == []
# assert has_at_least_three_vowels("There was an assumption they would do no harm banana It's an extremely potent") == ["assumption", "banana", "extremely"]


def had_at_least_six_characters(text):
    result_list = []
    match_list = re.finditer(r'\b(\w{6,})\b', text)
    if match_list:
        for match in match_list:
            result_list.append(match.group(0))
        return result_list

word_had_six_characters = had_at_least_six_characters("banana pie question "
                                                      "Dr Shanklin worries that SF6 is being treated in the same way  "
                                                      "help interpret the Dobson data. And, of course")

# print(word_had_six_characters)


# print(had_at_least_six_characters("It's delivering ozone measurements direct to Dr Shanklin's computer back in the UK via satellite"))
# assert had_at_least_six_characters("It's delivering ozone measurements direct to Dr Shanklin's computer back in the UK via satellite") == ["delivering", "measurements", "direct", "Shanklin", "computer", "satellite"]
# assert had_at_least_six_characters("say to the ") == []
# assert had_at_least_six_characters("banana pie qaids banana pie") == ["banana", "banana"]


def had_at_exactly_six_characters(text):
    result_list = []
    match_list = re.finditer(r'\b(\w{6})\b', text)
    if match_list:
        for match in match_list:
            result_list.append(match.group(0))
        return result_list

word_had_exactly_six_characters = had_at_exactly_six_characters("when the first personnel arrive back on station to begin our summer season "
                                                                "that's why we need the various monitoring sensors around the globe so we can "
                                                                "banana pie  and apple pie follow me on Twitter")

# print(word_had_exactly_six_characters)

# print(had_at_exactly_six_characters("Dr Thomas barningham, who's implemented the banana pie novel Halley set-up added"))
# assert had_at_exactly_six_characters("when the first personnel arrive back on station to begin") == ["arrive"]
# assert had_at_exactly_six_characters("We're very pleased to have reached this milestone.") == []
# assert had_at_exactly_six_characters("when the first personnel arrive back on station to begin banana nearby ice") == ["arrive", "banana", "nearby"]


def all_the_word_with_either_bar_baz(text):
    result_list = []
    match_list = re.finditer(r'(\w*ba[rz]\w*)\b', text)
    if match_list:
        for match in match_list:
            result_list.append(match.group(0))
        return result_list

word_all_either_bar_baz = all_the_word_with_either_bar_baz("banana pie hyperbaric "
                                                           "A Drink at the bazar "
                                                           "Dr Thomas barningham and bazar")

# print(word_all_either_bar_baz)

# print(all_the_word_with_either_bar_baz("banana pie hyperbaric"))
# assert all_the_word_with_either_bar_baz("including the Dobson photospectrometer stopbar apple pie") == ["stopbar"]
# assert all_the_word_with_either_bar_baz("The survey is now running a mini-jet engine non-stop at Halley") == []
# assert all_the_word_with_either_bar_baz("barbershop banana pie and banana pie hyperbaric stopbar apple pie") == ["barbershop", "hyperbaric", "stopbar"]


def have_banana_pie_or_apple_pie(text):
    result_list = []
    match_list = re.finditer(r'\b(\w*banana pie\w*|\w*apple pie\w*)\b', text)
    if match_list:
        for match in match_list:
            result_list.append(match.group())
        return result_list

word_have_banana_or_apple = have_banana_pie_or_apple_pie("i love apple pie "
                                                         "banana pie is delicious "
                                                         "i want to eat banana pie and apple pie in the morning")

# print(word_have_banana_or_apple)

# print(have_banana_pie_or_apple_pie("qaids banana pie"))
# assert have_banana_pie_or_apple_pie("Jonathan.Amos-INTERNET@bbc.co.uk and  banana pie ") == ["Jonathan Amos INTERNET@bbc co uk and banana pie"]
# assert have_banana_pie_or_apple_pie("Dr Shanklin is now an emeritus fellow at BAS.") == []
# assert have_banana_pie_or_apple_pie("mosque banana pie or apple pie") == ["mosque banana pie or apple pie"]
