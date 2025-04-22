import random

class Card:
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["♦", "♣", "♥", "♠"]

    def __init__(self, suit, rank):
        """
        Initializes a Card object with a suit and rank.
        Raises a ValueError if the rank or suit is invalid.
        """
        if rank not in self.RANKS:
            raise ValueError("Invalid Rank")
        if suit not in self.SUITS:
            raise ValueError("Invalid Suit")
        self._suit = suit
        self._rank = rank

    def __eq__(self, other):
        """
        Checks if two cards have the same rank.
        :param other: Another Card object
        :return: True if ranks match, False otherwise
        """
        return self.rank == other.rank

    def __gt__(self, other):
        """
        Compares two cards based on rank strength.
        :param other: Another Card object
        :return: True if this card's rank is greater than the other
        """
        return self.RANKS.index(self.rank) > self.RANKS.index(other.rank)

    def __str__(self):
        """
        Returns a human-readable string of the card, like "Q♠".
        """
        return f"{self._rank}{self._suit}"

    def __repr__(self):
        """
        Returns the string representation of the card, used for debugging.
        """
        return self.__str__()

    @property
    def suit(self):
        """Returns the suit of the card."""
        return self._suit

    @property
    def rank(self):
        """Returns the rank of the card."""
        return self._rank

class Deck:
    def __init__(self):
        """
        Initializes a standard 52-card deck using all suits and ranks.
        """
        self._deck = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self._deck.append(Card(suit, rank))

    def __str__(self):
        """
        Returns a string showing all the cards in the deck.
        """
        return str(self._deck)

    def shuffle(self):
        """
        Randomly shuffles the deck of cards.
        """
        random.shuffle(self._deck)

    def deal(self):
        """
        Deals (removes and returns) the top card from the deck.
        :return: Card object
        """
        return self._deck.pop(0)

if __name__ == "__main__":
    deck = Deck()
    print(deck)
    deck.shuffle()
    print(deck)
    print(deck.deal())
