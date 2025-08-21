"""  
This is a simple card guessing game, where the user tries to guess a randomly chosen card.  
Users have three (3) chances to succeed.  
"""

# Package imports 
from collections import namedtuple
from random import choice

# Global variable of type namedtuple
Card = namedtuple('Card', ['rank', 'suit'])

class DeckCards:
    """A DeckCards class which simulates a French deck."""
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
    
    def __getitem__(self, position):
        return self._cards[position]

    def getClues(self):
        """Return a random Card object from the deck."""
        return choice(self._cards) 


def main():
    print("You are playing 'Guess the Rank and Suit of a French Deck Card'.")
    print("I will pick a card, and you have 3 chances to guess correctly.\n")
	
	# variable of type DeckCards
    deckcards = DeckCards()

    while True:  # starts outer loop continuous play
		
		#maximum allowed guesses set to 3
        max_guesses = 3
		
		#Counter to track number of guesses users make
        guessCount = 0
		
		#variable holding the dealt card they are trying to guess
        magicCard = deckcards.getClues()
        print(f"I have my card ready. You have {max_guesses} guesses!")
		
        while guessCount < max_guesses:
            guess = input("Enter your guess (e.g. 'A spades' or '10 hearts'): ").strip().split()
            
            if len(guess) != 2:
                print("⚠️ Please enter both rank and suit (example: 'Q hearts').")
                continue
			#receive  user input 
            rank, suit = guess
            getResponse = Card(rank, suit)
            
            if magicCard == getResponse:
                print(f" Correct! The secret card was {magicCard.rank} of {magicCard.suit}.")
                break
            else:
                if magicCard.rank == getResponse.rank:
                    print(f" You got the rank right ({getResponse.rank})")
                else:
                    print(f"Wrong rank ({getResponse.rank})")
                
                if magicCard.suit == getResponse.suit:
                    print(f"You got the suit right ({getResponse.suit})")
                else:
                    print(f"Wrong suit ({getResponse.suit})")

            guessCount += 1
            print(f"Guesses left: {max_guesses - guessCount}\n")
        
        else:  # runs if loop exits without a correct guess
            print(f"Out of guesses! The card was {magicCard.rank} of {magicCard.suit}.")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if not play_again.startswith('y'):
            print("Thanks for playing!")
            break


if __name__ == '__main__': 
    main()
