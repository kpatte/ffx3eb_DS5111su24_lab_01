import pytest
import subprocess
import sys
import re
import os
import requests

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from text_processing import clean_text, tokenize, count_words


@pytest.mark.integration
def test_clean_and_count_the_raven():
    filename = "pg17192.txt"
    with open(filename, 'r') as file:
        content = file.read()
    cleaned_text = clean_text(content)
    cleaned_counted_text = count_words(cleaned_text)
    assert cleaned_counted_text['the'] > 100
    assert len(cleaned_counted_text) > 1000

@pytest.mark.integration
def test_download_and_tokenize_text():
    url = "https://www.gutenberg.org/cache/epub/932/pg932.txt"
    response = requests.get(url)
    raw_text = response.text
    
    cleaned_text = clean_text(raw_text)
    tokened_cleaned_text = tokenize(cleaned_text)
    cleaned_counted_text = count_words(cleaned_text)

    assert isinstance(tokened_cleaned_text, list), "tokened_cleaned_text failed on pg932.txt"
    assert isinstance(cleaned_counted_text, dict), "cleaned_counted_text failed on pg932.txt"


