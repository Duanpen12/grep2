import unittest
import regex_function
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


class RegexFunctionElementQTest(unittest.TestCase):
    def test_word_element_had_q_last(self):
        self.assertEqual(
            element_had_a_q("Iraq is a country located in the Middle East leopard"), ["Iraq"])

    def test_word_element_had_q_middle(self):
        self.assertEqual(
            element_had_a_q("in the Middle East leopard Mosque"), ["Mosque"])

    def test_word_element_had_q_start(self):
        self.assertEqual(
            element_had_a_q("banana pie qaids banana pie"), ["qaids"])

    def test_element_had_not_q_in_the_word(self):
        self.assertEqual(
            element_had_a_q("banana pie and banana pie"), [])


class RegexFunctionStartWithQTest(unittest.TestCase):
    def the_word_start_with_q_in_the_line(self):
        self.assertEqual(
            regex_function.starts_with_a_q("quality needs to have prere ekamai"), ["quality"])

    def the_word_start_with_q_in_the_middle_line(self):
        self.assertEqual(
            regex_function.starts_with_a_q("banana pie qaids banana pie"), ["qaids"])

    def the_word_start_with_a_q_in_the_end_line(self):
        self.assertEqual(
            regex_function.starts_with_a_q("Do you have any question"), ["question"])

    def no_the_word_start_with_q_in_the_line(self):
        self.assertEqual(
            regex_function.starts_with_a_q("in the Middle East leopard"), [])


class RegexFunctionHadThTest(unittest.TestCase):
    def the_word_has_th_in_it(self):
        self.assertEqual(
            regex_function.has_th_in_it("first alerted the world in 1985 that a deep thinning was occurring"), ["the", "that", "thinning"])

    def the_word_has_th_in_the_middle(self):
        self.assertEqual(
            regex_function.has_th_in_it("although we know it's a greenhouse gas "), ["although"])

    def the_word_has_th_in_the_end(self):
        self.assertEqual(
            regex_function.has_th_in_it("along with Joe Farman and Brian Gardiner"), ["with"])


class RegexFunctionHadQOrUpperQ(unittest.TestCase):
    def the_word_had_q_or_upper_q(self):
        self.assertEqual(
            regex_function.has_an_q_or_upper_q("Teaching experience is a necessary qualification for a tutor"), ["qualification"])

    def the_word_had_q_or_upper_q_in_the_middle(self):
        self.assertEqual(
            regex_function.has_an_q_or_upper_q("Permission is not required to link directly"), ["required"])

    def the_word_had_q_or_upper_q_start_with_upper_q(self):
        self.assertEqual(
            regex_function.has_an_q_or_upper_q("Questions for the ESL Classroom"), ["Questions"])

    def the_word_has_q_or_upper_q_in_the_end_word(self):
        self.assertEqual(
            regex_function.has_an_q_or_upper_q("He goes into its Cambridge HQ"), ["HQ"])

    def the_word_had_no_q_or_upper_q(self):
        self.assertEqual(
            regex_function.has_an_q_or_upper_q("along with Joe Farman and Brian Gardiner"), [])


class RegexFunctionHadAsteriskInIt(unittest.TestCase):
    def the_word_has_asterisk_in_it(self):
        self.assertEqual(
            regex_function.had_asterisk_in_it("**Dr **Thomas* bar*ningham"), ["bar*ningham"])

    def the_word_has_no_asterisk_in_it(self):
        self.assertEqual(
            regex_function.had_asterisk_in_it("the* although we know it's a greenhouse gas"), [])


class RegexFunctionStartWithOrUpperQ(unittest.TestCase):
    def the_word_start_with_q_or_upper_q(self):
        self.assertEqual(
            regex_function.start_with_q_or_upper_q("Questions for the ESL Classroom"), ["Questions"])

    def the_word_start_with_q_or_upper_q_in_middle_line(self):
        self.assertEqual(
            regex_function.start_with_q_or_upper_q("Ning is the most qualified candidate for this job"), ["qualified"])

    def the_word_start_with_q_or_upper_q_in_the_end_line(self):
        self.assertEqual(
            regex_function.start_with_q_or_upper_q("Do you have any question"), ["question"])

    def the_word_not_start_with_q_or_upper_q(self):
        self.assertEqual(
            regex_function.start_with_q_or_upper_q("i love python"), [])


class RegexFunctionHadBothAAndEInIt(unittest.TestCase):
    def the_word_had_both_a_and_e_start_a_or_e_last_e_or_a(self):
        self.assertEqual(
            regex_function.had_both_a_and_e_in_it("the ozone above Antarctica "), ["above"])

    def the_word_had_both_a_and_e_in_middle_word(self):
        self.assertEqual(
            regex_function.had_both_a_and_e_in_it("We're very pleased to have reached this milestone"), ["pleased", "have", "reached", "milestone"])

    def the_word_had_both_a_and_e_in_the_first_word(self):
        self.assertEqual(
            regex_function.had_both_a_and_e_in_it("the each spring in the winter"), ["each"])


class RegexFunctionHasAnAAndSomeWhereLaterE(unittest.TestCase):
    def the_word_has_a_some_where_later_e(self):
        self.assertEqual(
            regex_function.has_an_a_and_somewhere_later_an_e("Dr Shanklin's computer back in the UK via satellite"), ["satellite"])

    def the_word_has_a_some_where_later_e_start_with_a_in_the_word(self):
        self.assertEqual(
            regex_function.has_an_a_and_somewhere_later_an_e("absolute and apple"), ["absolute", "apple"])

    def the_word_has_a_some_where_later_e_in_the_fist_line(self):
        self.assertEqual(
            regex_function.has_an_a_and_somewhere_later_an_e("threadbare and banana"), ["threadbare"]
        )

    def the_word_has_not_a_some_where_later_e(self):
        self.assertEqual(
            regex_function.has_an_a_and_somewhere_later_an_e("my laptop is fixing"), [])


class RegexFunctionDoesNotHaveA(unittest.TestCase):
    def the_word_does_not_have_an_a(self):
        self.assertEqual(
            regex_function.does_not_have_an_a("banana pie Dr Shanklin and his colleagues at the British "), ['pie', 'Dr', 'his', 'the', 'British'])

    def the_word_does_not_have_an_a_in_the_line(self):
        self.assertEqual(
            regex_function.word_does_not_have_a("As time progresses, probably later in October "), ['As', 'time', 'progresses', 'in', 'October'])

    def the_word_have_an_a(self):
        self.assertEqual(
            regex_function.does_not_have_an_a("host of computer-controlled experiments"), [])


class RegexFunctionDoesNotHaveAOrE(unittest.TestCase):
    def the_word_does_not_have_a_or_e_in_the_line(self):
        self.assertEqual(
            regex_function.does_not_have_an_a_nor_e("The team discovery confirming the theoretical predictions of others"), ['confirming', 'of'])


class RegexFunctionHaveAButNotE(unittest.TestCase):
    def the_word_has_a_but_not_e(self):
        self.assertEqual(
            regex_function.has_an_a_but_not_e("It's very clear that the ozone data coming back"), ["that", "data", "back"])


class RegexFunctionHasAtLeastTwoConsecutive(unittest.TestCase):
    def the_word_had_at_least_two_consecutive_in_the_first_word(self):
        self.assertEqual(
            regex_function.has_at_least_two_consecutive("Ozone filters out harmful"), ["out"])

    def the_word_had_at_least_two_consecutive_in_the_middle_word(self):
        self.assertEqual(
            regex_function.has_at_least_two_consecutive("The team's discovery "), ["team's"])

    def the_word_had_not_at_least_two_consecutive(self):
        self.assertEqual(
            regex_function.has_at_least_two_consecutive("i love her"), [])


class RegexFunctionHasAtLeastThreeVowels(unittest.TestCase):
    def the_word_has_at_least_three_vowels(self):
        self.assertEqual(
            regex_function.has_at_least_three_vowels("We're very pleased to have reached this milestone"), ['pleased', 'reached', 'milestone'])


class RegexFunctionHadAtLeastSixCharacters(unittest.TestCase):
    def the_word_had_least_six_characters(self):
        self.assertEqual(
            regex_function.had_at_least_six_characters("Dr.Shanklin worries that SF6 is being treated in the same way"), ["Shanklin", "worries", "treated"])


class RegexFunctionHadAtExactlySixCharacters(unittest.TestCase):
    def the_word_had_at_exactly_six_characters(self):
        self.assertEqual(
            regex_function.had_at_exactly_six_characters("When the first personnel arrive back on station to begin our summer season"), ['arrive', 'summer', 'season'])


class RegexFunctionAllTheWordWithEitherBarBaz(unittest.TestCase):
    def the_word_all_the_word_with_either_bar_baz_in_the_middle_word(self):
        self.assertEqual(
            regex_function.all_the_word_with_either_bar_baz("banana pie hyperbaric"), ["hyperbaric"])

    def the_word_all_the_word_with_either_bar_baz_in_the_first_word(self):
        self.assertEqual(
            regex_function.all_the_word_with_either_bar_baz("A Drink at the bazar"), ["bazar"])

    def the_word_all_the_word_with_either_bar_baz(self):
        self.assertEqual(
            regex_function.all_the_word_with_either_bar_baz("Dr Thomas barningham and bazar"), ["barningham", "bazar"])


class RegexFunctionHaveBananaAndApple(unittest.TestCase):
    def the_line_have_have_banana_pie_or_apple_pie(self):
        self.assertEqual(
            regex_function.have_banana_pie_or_apple_pie("i want to eat banana pie and apple pie in the morning"), ["banana pie", "apple pie"])


if __name__ == '__main__':
    unittest.main()


















