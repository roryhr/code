from functools import reduce

class Card:
    def __init__(self, value, faceup=True, suit=None):
        self.value = value
        self.faceup = faceup
        self.suit = suit


class Deck:
    def __init__(self, nb_decks=-1):
        self.nb_decks = nb_decks


class PokerPlayer:
    def __init__(self, hand=[], deck=Deck()):
        self.hand = hand

    def hit(self):
        self.hand.append(self.deck.draw_card())

    def stay(self):
        pass

    @property
    def total(self):
        total_count = 0
        for card in self.hand:
            total_count += card.value

        return total_count


class PokerDealer(PokerPlayer):
    def __init__(self, hand=[], deck=Deck()):
        self.deck = deck

    def draw_card(self):
        return Card(4)


card = Deck().draw_card()
print(card.value)

p = PokerPlayer()
p.hit()
p.hit()
print(p.total)
