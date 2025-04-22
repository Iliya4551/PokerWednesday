from deck import Deck, Card

class PokerHand:
    def __init__(self, deck):
        """
        Initializes a PokerHand by drawing 5 cards from the given deck.
        :param deck: A Deck object to deal cards from
        """
        self._cards = [deck.deal() for _ in range(5)]

    @property
    def cards(self):
        """
        Returns the list of 5 cards in the hand.
        """
        return self._cards

    def __str__(self):
        """
        Returns a string representation of the poker hand.
        """
        return str(self._cards)

    @property
    def is_flush(self):
        """
        Checks if all 5 cards in the hand have the same suit.
        :return: True if all suits match, False otherwise.
        """
        first_suit = self.cards[0].suit
        return all(card.suit == first_suit for card in self.cards)

    @property
    def is_full_house(self):
        """
        Checks if the hand is a full house (3 of a kind + a pair).
        :return: True if number_matches == 8 (pattern logic), else False.
        """
        return self.number_matches == 8

    @property
    def number_matches(self):
        """
        Calculates the total number of rank matches in the hand.
        For example: full house = 3 matching + 2 matching = 8 comparisons.
        :return: The total number of matching rank pairs.
        """
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
        """
        Checks if the hand contains a single pair.
        :return: True if exactly 1 pair (2 matches), else False.
        """
        return self.number_matches == 2

    @property
    def is_two_pair(self):
        """
        Checks if the hand contains two different pairs.
        :return: True if 4 rank matches (2 pairs), else False.
        """
        return self.number_matches == 4

    @property
    def is_trips(self):
        """
        Checks if the hand contains three of a kind.
        :return: True if 3 cards of the same rank (6 matches), else False.
        """
        return self.number_matches == 6

    @property
    def is_quads(self):
        """
        Checks if the hand contains four of a kind.
        :return: True if 12 rank matches (4 matching cards), else False.
        """
        return self.number_matches == 12

    @property
    def is_straight(self):
        """
        Checks if the hand contains a straight (consecutive ranks).
        NOTE: Sorting must work and ranks must be consecutive.
        :return: True if straight, False otherwise.
        """
        self.cards.sort()  # Make sure the hand is sorted
        distance = Card.RANKS.index(self.cards[4].rank) - Card.RANKS.index(self.cards[0].rank)
        return self.number_matches == 0 and distance == 4

# Simulation
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

print(f"Probability of a straight is {100 * matches / count}%")
