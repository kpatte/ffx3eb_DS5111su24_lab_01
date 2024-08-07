"""
This module runs tests on the 'clean_text()' function contained in text_processor.py

def clean_text(input_text: str) -> str:
    lowercase_text = input_text.lower()
    cleaned_text = re.sub(r"[^\w\s]", "", lowercase_text)
    return cleaned_text
"""
import pytest
import subprocess
import sys
import re
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from text_processing import clean_text


def test_clean_raven_snippet():
    # Given a string _text_
    # When I pass _text_ to the 'clean_text()' function
    # I should get a string returned with lower case and no punctuation based on regex match
    text = 'But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.'
    result = clean_text(text)
    assert isinstance(result, str), f"clean_text failed on sample text: {text}"
    assert result.islower(), f"clean_text failed to convert all to lower in: {text}"
    assert not re.search (r'[^\w\s]', clean_text(text)), f"clean_text failed to remove all punctuation in: {text}"


def test_clean_french():
    # Given a string _text_ in french
    # When I pass _text_ to the 'clean_text()' function
    # I should get a string returned with lower case and no punctuation based on regex match
    text = """Mais le Corbeau, perché solitairement sur ce buste placide, parla
    ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je ne
    proférai donc rien de plus: il n'agita donc pas de plume--jusqu'à ce
    que je fis à peine davantage que marmotter «D'autres amis déjà ont
    pris leur vol--demain il me laissera comme mes Espérances déjà ont
    pris leur vol.» Alors l'oiseau dit: «Jamais plus.»"""
    result = clean_text(text)
    assert isinstance(result, str), f"clean_text failed on french text"
    assert not re.search (r'[^\w\s]', result), f"clean_text failed to remove all punctuation in french text"

@pytest.mark.parametrize("filename", [
        "pg17192.txt"
])
def test_clean_full_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    result = clean_text(content)
    assert isinstance(result, str), f"clean_text failed on file: {filename}"
    assert not re.search (r'[^\w\s]', result), f"clean_text returned empty list for file: {filename}"

def test_clean_all_english_files():
    # Given a string _text_ of all english files
    # When I pass _text_ to the 'clean_text()' function
    # I should get a string returned with that is longer than length 0
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
    result = clean_text(full_text)
    assert isinstance(result, str), "clean_text failed on all English files"
    assert len(result) > 0, "clean_text returned empty string for all English files"


@pytest.mark.skip(reason="Japanese test not implemented yet")
def test_clean_japanese():
    # This test will be skipped
    pass

@pytest.mark.skipif(sys.platform != "linux", reason="Test only runs on Linux")
def test_clean_linux_specific():
    # This test will only run on Linux
    pass

@pytest.mark.skipif(sys.version_info < (3, 7), reason="Requires Python 3.7 or higher")
def test_clean_python_version_specific():
    # This test will only run on Python 3.7 or higher
    pass

def test_clean_text_compare_with_bash():
    # Given a _text_ input
    # When I pass _text_ through python clean_text() function and bash cleaning
    # I should get the same output for the two processes 
    text = "The Quick Brown Fox Jumps Over the Lazy Dog!"
    python_result = clean_text(text)

    bash_command = f"echo '{text}' | tr '[:upper:]' '[:lower:]' | tr -d '[:punct:]'"
    bash_result = subprocess.check_output(bash_command, shell=True).decode().strip()
    
    assert python_result == bash_result, "different results from python clean_text and bash cleaning"


@pytest.mark.xfail(reason="clean_text function doesn't take non-string input")
def test_clean_text_fail_not_string_input():
    # Given a non-string list input
    # When I pass a list to the clean_text() function
    # I should get a failure since clean_text() requires string input
    non_string_input = ["hello","world"]
    
    with pytest.raises(TypeError):
        clean_text(non_string_input)
