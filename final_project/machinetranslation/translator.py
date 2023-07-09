"""
This module provides a simple functions that can translate english to french text and vice versa
"""

from deep_translator import MyMemoryTranslator


def english_to_french(english_text: str) -> str:
    """
    this function receives a string of english text and returns a string of it's french translation
    """
    french_text = MyMemoryTranslator(source="english", target="french").translate(english_text)
    return french_text


def french_to_english(french_text):
    """
    this function receives a string of french text and returns a string of it's english translation
    """
    english_text = MyMemoryTranslator(source="french", target="english").translate(french_text)
    return english_text
