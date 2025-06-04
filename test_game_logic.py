import pytest
from game_logic import get_random_word, display_game_state

def test_get_random_word_returns_valid_word():
    words = get_random_word()
    valid_words = ["python", "git", "github", "snowman", "meltdown"]
    assert words in valid_words

def test_display_game_state_print_correct_structure(capsys):
    secret_word = "git"
    guessed_letters = ["g", "t"]
    mistakes = 1

    display_game_state(mistakes, secret_word, guessed_letters)
    captured = capsys.readouterr()

    assert "Word: g_ t" in captured.out
    assert "Mistakes: 1" in captured.out
    assert "Guessed letters: g t" in captured.out
