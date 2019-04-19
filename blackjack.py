import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image(
    "http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image(
    "http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")

# initialize some useful global variables
inPlay = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
          '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10}


# define card class
class Card:

    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [
                          pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

    def draw_back(self, canvas, pos):
        card_loc = (CARD_BACK_CENTER[0], CARD_BACK_CENTER[1])
        canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, [pos[
                          0] + CARD_BACK_CENTER[0] + 1, pos[1] + CARD_BACK_CENTER[1] + 1], CARD_BACK_SIZE)


class Hand:

    def __init__(self):
        """Create Hand object."""
        self.cards = []

    def __str__(self):
        """Return a string representation of a hand."""
        handCards = ""
        for i in self.cards:
            handCards = handCards + str(i) + " "
        if len(handCards) == 0:
            return "Hand contains nothing."
        else:
            return "Hand contains " + handCards.strip() + "."

    def add_card(self, card):
        """Add a card object to a hand."""
        self.cards.append(card)

    def get_value(self):
        """
        Compute the value of the hand.
        Counts aces as 1, if the hand has an ace,
        then add 10 to hand value if it doesn't bust
        """
        value = 0
        isAce = False
        for card in self.cards:
            rank = card.get_rank()
            value = value + VALUES[rank]
            if rank == 'A':
                isAce = True
        if (isAce == True) and (value < 12):
            value = value + 10
        return value

    def draw(self, canvas, pos):
        """ Draws a hand on the canvas, uses the draw method for cards """
        for card in self.cards:
            pos[0] = pos[0] + CARD_SIZE[0] + 30
            card.draw(canvas, pos)


# define deck class
class Deck:

    def __init__(self):
        """ Creates a Deck object """
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        """Shuffles the deck, using random.shuffle() """
        random.shuffle(self.cards)

    def deal_card(self):
        """Deals a card object from the deck """
        return self.cards.pop()

    def __str__(self):
        """Returns a string representing the deck """
        deckstring = ""
        for card in self.cards:
            deckstring = deckstring + str(card) + " "
        if len(deckstring) == 0:
            return "Deck contains nothing."
        else:
            return "Deck contains " + deckstring.strip() + "."


# define event handlers for buttons
def deal():
    global score, inPlay
    if inPlay is True:
        inPlay = False
        score = score - 1
        deal()
    else:
        # start new deal
        restart_deal()


def restart_deal():
    global outcome, deck, inPlay, playerinput, dealerinput, result_of_match
    playerinput = Hand()
    dealerinput = Hand()
    deck = Deck()
    deck.shuffle()
    playerinput.add_card(deck.deal_card())
    playerinput.add_card(deck.deal_card())
    dealerinput.add_card(deck.deal_card())
    dealerinput.add_card(deck.deal_card())
    outcome = "Hit or Stand?"
    result_of_match = ""
    inPlay = True


def hit():
    global result_of_match, outcome, score, inPlay, deck, playerinput
    if inPlay is True:
        if playerinput.get_value() <= 21:
            playerinput.add_card(deck.deal_card())
            if playerinput.get_value() > 21:
                result_of_match = "You are BUSTED! You loose."
                score = score - 1
                outcome = "New Deal ?"
                inPlay = False


def stand():
    global result_of_match, playerinput, dealerinput, score, inPlay, deck, outcome
    if inPlay:
        while dealerinput.get_value() < 17:
            dealerinput.add_card(deck.deal_card())
        if dealerinput.get_value() > 21:
            result_of_match = "Dealer BUSTED! You win."
            score = score + 1
        elif playerinput.get_value() > dealerinput.get_value():
            result_of_match = "You win."
            score = score + 1
        else:
            result_of_match = "You loose."
            score = score - 1
        outcome = "New Deal?"
        inPlay = False


def draw(canvas):
    canvas.draw_text("~ BLACKJACK ~", (150, 70), 50, "White")
    canvas.draw_text("DEALER", (36, 185), 30, "#fcada7")
    canvas.draw_text("PLAYER", (36, 385), 30, "#fcada7")
    canvas.draw_text(outcome, (235, 385), 30, "#fcada7")
    canvas.draw_text(result_of_match, (235, 185), 30, "#fcada7")
    canvas.draw_text("Score:  " + str(score), (450, 115), 30, "white")
    dealerinput.draw(canvas, [-65, 200])
    playerinput.draw(canvas, [-65, 400])
    if inPlay is True:
        dealerinput.cards[0].draw_back(canvas, [36, 199])


def main():
    # initialization frame
    frame = simplegui.create_frame("Blackjack game", 650, 600)
    frame.set_canvas_background("Brown")
    # create buttons and canvas callback
    frame.add_button("Deal", deal, 200)
    frame.add_button("Hit",  hit, 200)
    frame.add_button("Stand", stand, 200)
    frame.set_draw_handler(draw)
    deal()
    frame.start()

if __name__ == '__main__':
    main()
