import pytest
from text_processing import clean_text, tokenize, count_words


def test_clean_text():
    assert clean_text("This is a Test Script!") == "this is a test script"


def test_tokenize():
    assert tokenize("Hello World!") == ["hello", "world"]


def test_count_words():
    assert count_words("Test Hello World Test!") == {"test": 2, "hello": 1, "world": 1}
    assert count_words("a A a b c B C") == {"a": 3, "b": 2, "c": 2}


def test_input_validation():
    with pytest.raises(AssertionError):
        clean_text(10)
    with pytest.raises(AssertionError):
        tokenize(None)
    with pytest.raises(AssertionError):
        count_words(["list", "of", "words"])
