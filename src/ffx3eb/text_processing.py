"""
This module defines functions for text processing, including cleaning, tokenizing,
and word counting.
"""

import re
import logging
from typing import List, Dict

# logging setup
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def clean_text(input_text: str) -> str:
    """
    converts text to lowercase and removes punctuation
    """
    assert isinstance(input_text, str), "input must be a string"

    logging.info("cleaning text")

    lowercase_text = input_text.lower()

    cleaned_text = re.sub(r"[^\w\s]", "", lowercase_text)

    assert isinstance(cleaned_text, str), "output must be a string"
    logging.info("text cleaning complete")
    return cleaned_text


def tokenize(input_text: str) -> List[str]:
    """
    tokenize the input string into a list of words.
    """
    assert isinstance(input_text, str), "input must be a string"

    logging.info("tokenizing text")

    cleaned_text = clean_text(input_text)

    tokens = cleaned_text.split()
    assert isinstance(tokens, list), "output must be a list"
    assert all(isinstance(token, str) for token in tokens), "all tokens must be strings"
    logging.info("Tokenization completed. {} tokens generated".format(len(tokens)))
    return tokens


def count_words(input_text: str) -> Dict[str, int]:
    """
    takes a string as input and returns a dictionary with each word as the key and the wordcount as value
    """
    assert isinstance(input_text, str), "input must be a string"

    logging.info("counting words")

    cleaned_text = clean_text(input_text)

    tokens = cleaned_text.split()

    word_counts = {}

    for word in tokens:
        word_counts[word] = word_counts.get(word, 0) + 1

    assert isinstance(word_counts, dict), "output must be a dictionary"
    assert all(
        isinstance(k, str) and isinstance(v, int) for k, v in word_counts.items()
    ), "dictionary must contain string keys and integer values"
    logging.info(
        "Word counting completed. {} unique words found".format(len(word_counts))
    )
    return word_counts
