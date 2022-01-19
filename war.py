# This class represents a card in the game, with a card object having a suit and a value instance variables
class Card:
    # Arranged by strength of suit, the strongest suit is last
    suits = ("spades",
             "hearts",
             "diamonds",
             "clubs")

    # First two values are none so their values match their index
    values = (None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10",
              "Jack", "Queen", "King", "Ace")

    def __init__(self, v, s):
        """suit + value are ints"""
        self.value = v
        self.suit = s

    # Compare with less than symbol
    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    # Compare with greater than symbol
    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    # Print card objects by displaying value and suit
    def __repr__(self):
        v = self.values[self.value] + " of " \
         + self.suits[self.suit]
        return v
