import unittest

from cards import Deck


class UnitTests(unittest.TestCase):

    def test_draw_all_cards(self):
        deck = Deck()

        # Assert there are 52 cards initially
        self.assertEqual(len(deck.reveal()), 52)
        self.assertEqual(deck.get_num_cards(), 52)

        # Assert that all 52 cards can be drawn one at a time.
        hand = set()
        while deck.get_num_cards() != 0:
            one_card = deck.draw()
            hand.add(str(one_card))

        # Assert that another draw will return None
        self.assertTrue(deck.draw() is None)

        # Assert 52 unique cards were drawn
        self.assertEqual(len(hand), 52)

    def test_shuffle_single_deck(self):
        # Note that this test assumes we'll never get the same order after a
        # shuffle.  Assumming a perfectly random shuffle for a full deck, the
        # probability of that happening is 1 in 52! (52 factorial, or
        # approximately 8e23). I ran 1 million iterations and didn't see any
        # failures.
        NUM_TIMES = 100
        deck = Deck()
        before = deck.reveal()
        for num in range(NUM_TIMES):
            deck.shuffle()
            after = deck.reveal()
            # Assert that there are 52 cards before and after
            self.assertTrue(len(before) == len(after) == 52)
            # Assert that the deck is different after the shuffle
            self.assertNotEqual(before, after)
            before = after

    def test_shuffle_multiple_decks(self):
        # Note that the assumption in test_shuffle_single_deck() also applies
        # here.
        NUM_TIMES = 100
        deck1 = Deck()
        for num in range(NUM_TIMES):
            deck2 = Deck()
            # Assert that each new deck has a different order than the previous
            self.assertNotEqual(deck1.reveal(), deck2.reveal())
            deck1 = deck2

    def test_unshuffled_decks_are_identical(self):
        deck1 = Deck(shuffle=False)
        deck2 = Deck(shuffle=False)
        # Assert that two new unshuffled decks are identical
        self.assertEqual(deck1.reveal(), deck2.reveal())
        # Assert that drawing one card at a time from each deck yields the
        # same card.
        while deck1.get_num_cards() != 0:
            self.assertTrue(deck1.draw() == deck2.draw())

unittest.main()
