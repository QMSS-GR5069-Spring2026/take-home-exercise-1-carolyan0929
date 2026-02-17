"""
Test file for Wordle functions - Template

This is a template showing the structure your test_wordle.py file should have.
Students should write their own test implementations.
"""

import pytest
from wordle import (
    validate_guess,
    check_guess,
    is_valid_word,
)
print("This is Zhijie speaking")
# Word list for testing
WORD_LIST = [
    "crane", "apple", "hello", "world", "python", 
    "house", "water", "light", "music", "dream",
    "happy", "smile", "peace", "heart", "brain",
    "table", "chair", "phone", "paper", "green"
]


# =============================================================================
# PART 1: BASIC TESTING
# =============================================================================
# Note: Each test function can contain multiple related assertions.
# This is standard practice - you're testing the same function with different
# inputs to verify it handles various scenarios correctly.

def test_validate_guess():
    """
    Test the validate_guess function with various inputs.
    
    TODO: Students should implement this test function with:
    - Valid guesses (correct length, lowercase, alphabetic)
    - Invalid guesses (wrong length, uppercase, non-alphabetic)
    - Edge cases (empty string, None, non-string inputs)
    """
    # The word must be 5 character
    assert validate_guess("apple") == True # correct length
    assert validate_guess("app") == False # wrong length, too short
    assert validate_guess("apples") == False # wrong length, too long

    # The word must be lowercase
    assert validate_guess("apple") == True # lowercase
    assert validate_guess("APPLE") == False # uppercase
    assert validate_guess("Apple") == False # mixed

    # The word must be alphabetic
    assert validate_guess("APP1E") == False # non-alphabetic
    assert validate_guess("Apple!") == False # non-alphabetic

    assert validate_guess("") == False # empty string
    assert validate_guess(None) == False # None
    assert validate_guess(1234) == False # non-string inputs


def test_check_guess_basic():
    """
    Test basic check_guess functionality.
    
    TODO: Students should implement this test function with:
    - Perfect match (all green)
    - No matches (all gray)
    - Mixed results (green, yellow, gray combinations)
    - Edge cases (different lengths)
    
    Remember: Run check_guess() with different inputs first to see what it returns!
    """
    # TODO: Implement your test cases here
    pass


def test_is_valid_word():
    """
    Test the is_valid_word function.
    
    TODO: Students should implement this test function with:
    - Valid words (case insensitive)
    - Invalid words (not in list)
    - Edge cases (empty string, empty word list)
    """
    # TODO: Implement your test cases here
    pass


# =============================================================================
# PART 2: ADVANCED TESTING
# =============================================================================

@pytest.mark.parametrize("secret_word,guess,expected", [
    # TODO: Students should add 5-6 test cases here
    # Remember to run check_guess() first to see what the actual output is!
    # 
    # Include test cases for:
    # - Perfect match (all green)
    # - No matches (all gray)
    # - Mixed results (combination of green, yellow, gray)
    # - Duplicate letters in guess
    # - Additional scenarios of your choice
])
def test_check_guess_comprehensive(secret_word, guess, expected):
    """
    Test check_guess with multiple scenarios using parametrize.
    
    This test will run once for each set of parameters you provide above.
    """
    result = check_guess(secret_word, guess)
    assert result == expected, f"Failed for {secret_word} vs {guess}. Expected {expected}, got {result}"


@pytest.fixture
def common_word_list():
    """
    Fixture providing a list of common 5-letter words.
    
    TODO: Students should implement this fixture by returning a word list.
    You can use the WORD_LIST defined above, or create your own.
    """
    # TODO: Return your word list
    pass


def test_word_list_fixture(common_word_list):
    """
    Test function demonstrating fixture usage.
    
    TODO: Students should implement this test to demonstrate using the fixture.
    Test that the fixture works and use it with one of the Wordle functions.
    """
    # TODO: Implement your test using the common_word_list fixture
    pass
