
import collections
import counter
import unittest


class TestCounter(unittest.TestCase):

    def setUp(self) -> None:
        self.url_counter = counter.UrlWordCounter('', False)
        self.url_counter.excluded_words = {'the', 'is', 'a', 'this'}

    def test_get_words_per_line(self):
        test_line = 'Hello test this is a test!!'
        self.url_counter._get_words_per_line(test_line)

        expected_result = collections.Counter({'hello': 1, 'test': 2})
        self.assertEqual(expected_result, self.url_counter.word_counter)

    def test_get_words_per_line_hyphen(self):
        test_line = 'Hello re-use this re-use a!!'
        self.url_counter._get_words_per_line(test_line)

        expected_result = collections.Counter({'hello': 1, 're-use': 2})
        self.assertEqual(expected_result, self.url_counter.word_counter)

    def test_get_words_per_line_newlines(self):
        test_line = 'Hello re-use this re-use a!!\n\r'
        self.url_counter._get_words_per_line(test_line)

        expected_result = collections.Counter({'hello': 1, 're-use': 2})
        self.assertEqual(expected_result, self.url_counter.word_counter)

    def test_sort_counter_words(self):
        self.url_counter.word_counter = {
            'hello': 1, 're-use': 2, 'a': 1, 'this': 4
        }
        sorted_list = self.url_counter._sort_word_counter()

        expected_result = [('this', 4), ('re-use', 2), ('hello', 1), ('a', 1)]
        self.assertEqual(expected_result, sorted_list)
