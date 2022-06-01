import os

import counter

TXT_FILE_URL = os.environ.get('TXT_FILE_URL')

# Constant of words to exclude from count
EXCLUDED_WORDS = {'the', 'of', 'to', 'and', 'a', 'in', 'is', 'it', 'you',
                  'that', 'he', 'was', 'for', 'on', 'are', 'with', 'as', 'i',
                  'his', 'they', 'be', 'at', 'one', 'have', 'this', 'from',
                  'or', 'had', 'by', 'not', 'word', 'but', 'what', 'some', 'we',
                  'can', 'out', 'other', 'were', 'all', 'there', 'when', 'up',
                  'use', 'your', 'how', 'said', 'an', 'each', 'she'}


def main():
    # Use context so url file object will be cleaned up
    with counter.UrlWordCounter(TXT_FILE_URL) as word_counter:
        word_counter.excluded_words = EXCLUDED_WORDS
        top_words = word_counter.get_top_occurring_words()
        print(f'Count of top words: {len(top_words)}')
        print(top_words)


if __name__ == '__main__':
    main()
