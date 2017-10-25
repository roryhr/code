from functools import reduce
import numpy as np

class Card:
    def __init__(self, value, faceup=True, suit=None):
        self.value = value
        self.faceup = faceup
        self.suit = suit


class Deck:
    def __init__(self, nb_decks=-1):
        self.nb_decks = nb_decks
        self.card_values = [2,3,4,5,6,7,8,9,10,10,10,10,10]

    def draw_card(self):
        value = np.random.choice(self.card_values, 1)[0]
        return(Card(value=value))

class PokerPlayer:
    def __init__(self, dealer, hand=[], stay=False):
        self.dealer = dealer
        self.hand = hand
        self.stay = stay

    def hit(self):
        self.hand.append(self.dealer.draw_card())

    def stay(self):
        self.stay = True

    @property
    def sum(self):
        total_count = 0
        for card in self.hand:
            total_count += card.value

        return total_count
    
    @property
    def isbusted(self):
        if self.sum > 21:
            return True
        else:
            return False


class PokerDealer:
    def __init__(self, deck, hand=[]):
        self.deck = deck
        self.hand = hand

    def draw_card(self):
        return self.deck.draw_card()

    def deal_in(self):
        return self.deck.draw_card().draw_card()

dealer = PokerDealer(Deck())

p = PokerPlayer(dealer=dealer)
p.deal_in()
print(p.sum)
p.hit()
print(p.sum)
