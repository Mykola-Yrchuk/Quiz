import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from quiz import is_correct


def test_is_correct():
    assert is_correct(5, 5) == True


def test_wrong_answer():
    assert is_correct("7", "8") == False
