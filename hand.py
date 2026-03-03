from deck import Deck
from evaluator import evaluate

class Hand():
    def __init__(self):
        self.table = []
        self.players_hand = []
    
    def draw(self, deck):
        deck.shuffle()
        for _ in range(0, 5):
            self.table.append(deck.deal())

        for _ in range(0, 2):
            self.players_hand.append(deck.deal())

        return evaluate(self.table, self.players_hand)
    

