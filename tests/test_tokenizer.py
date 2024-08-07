"""
This module runs tests on the 'tokenize()' function contained in text_processor.py

def tokenize(input_text: str) -> List[str]:
    cleaned_text = clean_text(text)
    tokens = cleaned_text.split()
    return tokens
"""

import pytest
import subprocess
import sys
import re
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from text_processing import tokenize


def test_tokenize_raven_snippet():
    # Given a string _text_
    # When I pass _text_ to the tokenize() function
    # I should get a list returned of lower case strings without punctuation
    text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."
    result = tokenize(text)
    assert len(result) == 25, f"Tokenizer expected 25 tokens in: f{text}"
    assert all(isinstance(token, str) for token in result), f"Tokenizer failed to return strings list elements for: f{text}"
    assert "raven" in result, f"Expected 'raven' in tokens for: f{text}"


def test_tokenize_french():
    # Given a string _text_ in French
    # When I pass _text_ to the tokenize() function
    # I should get a list returned of lower case strings without punctuation
    text = """Mais le Corbeau, perché solitairement sur ce buste placide, parla
    ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je ne
    proférai donc rien de plus: il n'agita donc pas de plume--jusqu'à ce
    que je fis à peine davantage que marmotter «D'autres amis déjà ont
    pris leur vol--demain il me laissera comme mes Espérances déjà ont
    pris leur vol.» Alors l'oiseau dit: «Jamais plus.»"""
    result = tokenize(text)
    assert isinstance(result, list), "Tokenizer failed on French text"
    assert len(result) > 0, "Tokenizer returned empty list for French text"
    assert "peine" in result, "Expected 'peine' in tokens"

@pytest.mark.parametrize("filename", [
    "pg17192.txt"
])
# Given a string _text_ for The Raven
# When I pass _text_ to the tokenize() function
# I should get a list returned of lower case strings without punctuation
def test_tokenize_full_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    result = tokenize(content)
    assert isinstance(result, list), f"Tokenizer failed on file: {filename}"
    assert len(result) > 0, f"Tokenizer returned empty list for file: {filename}"


def test_tokenize_all_english_files():
    # Given a string _text_ for all english files
    # When I pass _text_ to the tokenize() function
    # I should get a list returned of lower case strings without punctuation
    filenames = [
        "pg17192.txt",
        "pg932.txt",
        "pg1063.txt",
        "pg10031.txt"
    ]
    full_text = ""
    for filename in filenames:
        with open(filename, 'r') as file:
            full_text += file.read() + "\n"
    result = tokenize(full_text)
    assert isinstance(result, list), "Tokenizer failed on all English files"
    assert len(result) > 0, "Tokenizer returned empty list for all English files"


@pytest.mark.skip(reason="Japanese test not implemented yet")
def test_tokenize_japanese():
    # This test will be skipped
    pass

@pytest.mark.skipif(sys.platform != "linux", reason="Test only runs on Linux")
def test_tokenize_linux_specific():
    # This test will only run on Linux
    pass

@pytest.mark.skipif(sys.version_info < (3, 7), reason="Requires Python 3.7 or higher")
def test_tokenize_python_version_specific():
    # This test will only run on Python 3.7 or higher
    pass

def test_tokenize_compare_with_bash():
    # Given a _text_ input
    # When I pass _text_ through python tokenize() function and bash tokenization
    # I should get the same output for the two processes
    text = "The Quick Brown Fox Jumps Over the Lazy Dog!"
    python_result = len(tokenize(text))
    bash_result = int(subprocess.check_output(f"echo '{text}' | wc -w", shell=True).decode().strip())
    assert python_result == bash_result, "different results from python tokenizer and bash "

@pytest.mark.xfail(reason="Tokenize function doesn't take non-string input")
def test_tokenize_fail_not_string_input():
    # Given a non-string list input
    # When I pass a list to the tokenize() function
    # I should get a failure since tokenize() requires string input
    non_string_input = ["hello","world"]
    
    with pytest.raises(TypeError):
        tokenize(non_string_input)
