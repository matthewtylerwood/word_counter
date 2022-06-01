# Word Counter

Simple url word counter that outputs the top 50 words for a text file url.

## Usage

Before running, the environment variable `TXT_FILE_URL` must be set. This could
look like the following if running via command line:

```bash
export TXT_FILE_URL=http://www.gutenberg.org/files/2701/2701-0.txt
python main.py
```

## Python Version

Script was tested against Python 3.9.2