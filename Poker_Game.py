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

    @property
    def is_full_house(self):
        return self.number_matches == 8

    @property
    def number_matches(self):
        matches = 0
        for i in range(len(self.cards)):
            for j in range(len(self.cards)):
                if i == j:
                    continue
                if self.cards[i].rank == self.cards[j].rank:
                    matches += 1
        return matches

    @property
    def is_pair(self):
        if self.number_matches == 2: #simple way
            return True
        return False


    @property
    def is_two_pair(self):
        return self.number_matches == 4 #more advanced!

    @property
    def is_trips(self):
        if self.number_matches == 6:
            return True
        return False

    @property
    def is_quads(self):
        if self.number_matches == 12:
            return True
        return False

    @property
    def is_straight(self):
        self.cards.sort()
        distance = Card.RANKS.index(self.cards[4].rank) - \
                   Card.RANKS.indeex(self.cards[0])
        return self.number_matches == 0 and distance == 4

count = 0
matches = 0
while matches < 10:
    deck = Deck()
    deck.shuffle()
    hand = PokerHand(deck)
    if hand.is_full_house:
        matches += 1
        print(hand)
    count += 1

print(f"Probability of a straight is {100*matches/count}%")
