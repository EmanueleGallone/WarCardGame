from random import shuffle

SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck():

    def __init__(self):
        print("Creating new ordered deck")
        self.allCards = [(s,r) for s in SUITE for r in RANKS]

    def __str__(self):
        return "cards: {}".format(str(self.allCards))

    def __len__(self):
        return self.allCards.__len__

    def shuffle(self):
        print("shuffling deck")
        shuffle(self.allCards)

    def split_in_half(self):
        return (self.allCards[:26], self.allCards[26:])



class Hand():
    
    def __init__(self, cards):
        self.cards = cards
    
    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def __len__(self):
        return len(self.cards)

    def add(self, added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()

class Player():
    
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed: {}".format(self.name, drawn_card))
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand) < 3:
            return self.hand.cards
        else:
            for _ in range(3):
                war_cards.append(self.hand.remove_card())
            return war_cards

    def still_has_cards(self):
        """
        Return True if player still has cards left
        """
        return len(self.hand.cards) != 0

    def cards_count(self):
        return len(self.hand)

############
##GAMEPLAY##
############

print("Welcome to War, let's being..")

#create decj and split it in half:
d = Deck()
d.shuffle()
half1,half2 = d.split_in_half()

#Creating both players
comp = Player("Computer", Hand(half1))

name = input("What is your name? ")
user = Player(name, Hand(half2))

total_rounds = 0
war_count = 0

#playing the game
while(user.still_has_cards() and comp.still_has_cards()):
    total_rounds += 1
    print("Time for a new round!")
    print("here are the current standings")
    print(user.name + " has the count : " + str(user.hand.__len__()))
    print(comp.name + " has the count : " + str(comp.hand.__len__()))

    table_cards = []
    c_card = comp.play_card()
    p_card = user.play_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    #remember that card is a tuple (s,r). I want the rank not the Suite
    if c_card[1] == p_card[1]:
        war_count += 1
        print("war!")

        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        # RANKS is ordered. checking the index is telling me which card has the highest value
        if RANKS.index(c_card[1]) > RANKS.index(p_card[1]):
            comp.hand.add(table_cards) # Here the card played by the computer has the higher value so wins the cards on the table
        else:
            user.hand.add(table_cards)
    else:
        if RANKS.index(c_card[1]) > RANKS.index(p_card[1]):
            comp.hand.add(table_cards)
        else:
            user.hand.add(table_cards)

print("total rounds: {}".format(str(total_rounds)))
print("a war happened: {} times".format(str(war_count)))
if comp.cards_count() > user.cards_count():
    print("Computer wins!")
else:
    print("{} wins!".format(user.name))

