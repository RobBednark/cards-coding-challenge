import random


class Card(object):

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return '{rank}{suit}'.format(rank=self.rank, suit=self.suit)

    def __eq__(self, other):
        return (self.rank == other.rank) and (self.suit == other.suit)


class Deck(object):

    def __init__(self, shuffle=True):
        """Start with a new deck of 52 cards.

        If {shuffle}, then randomize the order of the deck.
        """
        SUITS = ['c', 's', 'd', 'h']  # clubs, spades, diamonds, hearts
        RANKS = [str(rank) for rank in range(2, 11)]  # ['2', '3', ..., '10']
        RANKS += ['J', 'Q', 'K', 'A']  # Jack, Queen, King, Ace

        self.cards = [Card(rank, suit)
                      for rank in RANKS
                      for suit in SUITS]
        if shuffle:
            self.shuffle()

    def shuffle(self):
        """Shuffle the cards remaining in the deck."""
        random.shuffle(self.cards)

    def draw(self):
        """Draw a card from the deck.

        Return a string indicating the card, e.g., "10s" == 10 of spades.
        Return None if there are no cards left in the deck.
        """
        if self.cards:
            return self.cards.pop()
        else:
            return None

    def get_num_cards(self):
        """Return the number of cards remaining in the deck."""
        return len(self.cards)

    def reveal(self):
        """Show all the remaining cards in the deck.

        Do not draw them, but leave them in the deck.
        Returns a list of strings, where each string is a card.
        """
        return [str(card) for card in self.cards]
