"""
This module runs tests on the 'count_words()' function contained in text_processor.py
"""

import sys
import os
import subprocess
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
try:
    from ffx3eb.text_processing import count_words
except ImportError:
    from src.ffx3eb.text_processing import count_words

def test_count_raven_snippet():
    """
    # Given a string _text_
    # When I pass _text_ to the 'count_words()' function
    # I should get a appropriate word counts
    """
    text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."
    result = count_words(text)
    assert len(result) == 21, f"failure: expected 21 unique words in f{text}"
    assert (
        result["outpour"] == 1
    ), "failure: expected 'outpour' to appear once in f{text}"
    assert result["the"] == 2, "failure: expected 'the' to appear twice in f{text}"


def test_count_french():
    """
    # Given a string _text_ in French
    # When I pass _text_ to the 'count_words()' function
    # I should get a dictionary with 'ont' wordcount == 2
    """
    text = """Mais le Corbeau, perché solitairement sur ce buste placide, parla
    ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je ne
    proférai donc rien de plus: il n'agita donc pas de plume--jusqu'à ce
    que je fis à peine davantage que marmotter «D'autres amis déjà ont
    pris leur vol--demain il me laissera comme mes Espérances déjà ont
    pris leur vol.» Alors l'oiseau dit: «Jamais plus.»"""
    result = count_words(text)
    assert isinstance(result, dict), f"count_words failed to return dictionary"
    assert result["ont"] == 2, "failure: expected 'ont' to appear once in french text"


@pytest.mark.parametrize("filename", ["pg17192.txt"])
def test_clean_full_file(filename):
    """
    # Given a string _text_ for one file
    # When I pass _text_ to the 'count_words()' function
    # I should get a dictionary with 'ont' wordcount == 2
    """
    with open(filename, "r") as file:
        content = file.read()
    result = count_words(content)
    assert isinstance(result, dict), f"count_words failed on file: {filename}"
    assert all(
        isinstance(k, str) and isinstance(v, int) for k, v in result.items()
    ), "count_words failed on k,v types for The Raven file"


def test_clean_all_english_files():
    """
    # given a list of file names
    # When i iterate through each file
    # I should get a dictionary with k,v str,int back
    """
    filenames = ["pg17192.txt", "pg932.txt", "pg1063.txt", "pg10031.txt"]
    full_text = ""
    for filename in filenames:
        with open(filename, "r") as file:
            full_text += file.read() + "\n"
    result = count_words(full_text)
    assert isinstance(result, dict), "count_words failed on all English files"
    assert all(
        isinstance(k, str) and isinstance(v, int) for k, v in result.items()
    ), "count_words failed on k,v types for all English files"


@pytest.mark.skip(reason="Japanese test not implemented yet")
def test_count_japanese():
    """ This test will be skipped"""

@pytest.mark.skipif(sys.platform != "linux", reason="Test only runs on Linux")
def test_count_linux_specific():
    """This test will only run on Linux"""


@pytest.mark.skipif(sys.version_info < (3, 7), reason="Requires Python 3.7 or higher")
def test_count_python_version_specific():
    """This test will only run on Python 3.7 or higher"""


def test_count_words_compare_with_bash():
    """
    # Given a _text_ input
    # When I pass _text_ through python count_words() function and bash counting
    # I should get the same output for the two processes
    """
    text = "The quick brown fox jumps over the lazy dog. The dog is lazy."
    python_result = count_words(text)
    bash_command = f"echo '{text}' | tr '[:upper:]' '[:lower:]' | tr -d '[:punct:]' | tr ' ' '\\n' | sort | uniq -c | awk '{{print $2 \" \" $1}}'"
    bash_output = subprocess.check_output(bash_command, shell=True).decode().strip()
    bash_result = dict(line.split() for line in bash_output.split("\n"))
    bash_result = {k: int(v) for k, v in bash_result.items()}

    assert (
        python_result == bash_result
    ), "different results from python count_words and bash counting"


@pytest.mark.xfail(reason="count_words function doesn't take non-string input")
def test_count_words_fail_not_string_input():
    """
    # Given a non-string list input
    # When I pass a list to the count_words() function
    # I should get a failure since count_words() requires string input
    """
    non_string_input = ["hello", "world"]

    with pytest.raises(TypeError):
        count_words(non_string_input)
