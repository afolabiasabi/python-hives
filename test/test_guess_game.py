import pytest
from collections import namedtuple
from src.deckGuess import DeckCards, Card, main


# --- Unit tests for DeckCards ---

def test_deck_has_52_cards():
    deck = DeckCards()
    assert len(deck._cards) == 52
	

def test_deck_contains_expected_card():
    deck = DeckCards()
    card = Card("A", "spades")
    assert card in deck._cards

def test_get_clues_returns_card():
    deck = DeckCards()
    clue = deck.getClues()
    assert isinstance(clue, Card)
    assert clue.rank in DeckCards.ranks
    assert clue.suit in DeckCards.suits


# --- Integration tests for the game loop ---

def test_correct_guess(monkeypatch, capsys):
    """Simulate a user guessing the correct card immediately."""
    deck = DeckCards()
    chosen = deck.getClues()

    # simulate user input: first guess correct, then quit
    inputs = iter([f"{chosen.rank} {chosen.suit}", "no"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    monkeypatch.setattr("src.guess_game.DeckCards.getClues", lambda self: chosen)

    main()

    captured = capsys.readouterr()
    assert "Correct!" in captured.out
    assert f"{chosen.rank} of {chosen.suit}" in captured.out


def test_incorrect_then_out_of_guesses(monkeypatch, capsys):
    """Simulate a user guessing wrong 3 times."""
    chosen = Card("A", "spades")

    # simulate 3 wrong guesses, then quit
    inputs = iter(["2 hearts", "3 clubs", "4 diamonds", "no"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    monkeypatch.setattr("src.guess_game.DeckCards.getClues", lambda self: chosen)

    main()

    captured = capsys.readouterr()
    assert "Out of guesses!" in captured.out
    assert "A of spades" in captured.out