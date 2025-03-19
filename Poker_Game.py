from deck import Deck, Card

class PokerHand:
    def __init__(self, deck):
        self._cards = [deck.deal() for _ in range(5)]  # Draw 5 cards from the deck

    @property
    def cards(self):
        return self._cards

    def __str__(self):
        return str(self._cards)

    @property
    def is_flush(self):
        """Returns True if all cards in the hand have the same suit, otherwise False."""
        first_suit = self.cards[0].suit  # Get the suit of the first card
        return all(card.suit == first_suit for card in self.cards)  # Check all cards

# Simulation to estimate the probability of a flush
count = 0
flushes = 0

while flushes < 100:  # Run until 100 flush hands are found
    deck = Deck()
    deck.shuffle()
    hand = PokerHand(deck)
    if hand.is_flush:
        flushes += 1
    count += 1

print(f"Probability of a flush is {100 * flushes / count:.2f}%")
