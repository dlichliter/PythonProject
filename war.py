# This program allows two players to compete in the classic card game of war
from random import shuffle


# This class represents a card in the game, with a card object having a suit and a value instance variables
class Card:
    # Arranged by strength of suit, the strongest suit is last
    suits = ("Spades",
             "Hearts",
             "Diamonds",
             "Clubs")

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


# This class represents a standard deck of cards
class Deck:
    # Create a deck of 52 cards in the standard suits and append to a cards list, then shuffle
    def __init__(self):
        self.cards = []
        for v in range(2, 15):
            for s in range(4):
                self.cards.append(Card(v, s))
        shuffle(self.cards)

    # If there is still at least one card in the deck, remove a card
    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()


# This class keeps track of a players cards and number of rounds won
class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name


# This class runs the game of war between two players
class Game:
    # Create the players off of user input and create a deck for the game
    def __init__(self):
        player1 = input("Player 1 name: ")
        player2 = input("Player 2 name: ")
        self.deck = Deck()
        self.p1 = Player(player1)
        self.p2 = Player(player2)

    def wins(self, winner):
        w = "{} wins this round"
        w = w.format(winner)
        print(w)

    # Simulate the draw of a card for both players
    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} drew {} {} drew {}"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    # Run the game as long as there are at least two cards left or the player does not quit the program
    def play_game(self):
        cards = self.deck.cards
        print("Start of War!")
        while len(cards) >= 2:
            m = "q to quit. Any " + "key to play:"
            response = input(m)
            if response == "q":
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)

        print("War is over. {} wins".format(win))

    # Determine the winner when the deck is empty
    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "It was a tie!"


game = Game()
game.play_game()
