
import collections
import urllib.request
import re
import typing


class UrlWordCounter:
    # Class variable to hold excluded words
    excluded_words = {}

    @staticmethod
    def _open_file(file_url: str) -> typing.BinaryIO:
        """
        Url open the file as binary IO.

        :param file_url: File url.
        :return: Binary file like object.
        """
        file_data = urllib.request.urlopen(file_url)
        return file_data

    def __init__(self, file_url: str, open_file=True):
        # Simple way to prevent network call during testing (could also mock)
        if open_file:
            self.data = self._open_file(file_url)

        # Counter object that behaves like a default dict
        self.word_counter = collections.Counter()

    def __enter__(self):
        return self

    def __exit__(self,
                 exc_type: typing.Any,
                 exc_val: typing.Any,
                 exc_tb: typing.Any):
        self.close()

    def close(self):
        """
        Close file handler if needed.
        """
        if not self.data.closed:
            self.data.close()

    def _get_words_per_line(self, line: str):
        """
        Given a specific line, strip line and count the number of words
        using word_counter.

        :param line: File line to count.
        """
        # Replace all special characters with blanks
        line = re.sub('[^a-zA-Z\\s\\-]', '', line)

        # Strip line and iterate over each word
        for word in line.strip().split(' '):
            word = word.lower()

            # Do not count word if it's excluded or empty
            if word and word not in self.excluded_words:
                self.word_counter[word] += 1

    def _sort_word_counter(self):
        """
        Sort word counter from most to least occurrences.
        """
        return sorted([(word, value)
                       for word, value in self.word_counter.items()],
                      key=lambda x: x[1], reverse=True)

    def get_top_occurring_words(self) -> typing.List[typing.Tuple[str, int]]:
        """
        Get the top 50 occurring words in file.

        :return: List of tuples (word, count) in sorted order.
        """
        # Parse line by line and count words per line
        for line in self.data:
            self._get_words_per_line(line.decode())

        # Sort words from counter map
        top = self._sort_word_counter()
        return top[:50]
