#blackjack in python
import random

#deck of cards
deck = [2,3,4,5,6,7,8,9,10,"J","Q","K","A",2,3,4,5,6,7,8,9,10,"J","Q","K","A",2,3,4,5,6,7,8,9,10,"J","Q","K","A",2,3,4,5,6,7,8,9,10,"J","Q","K","A"]

player_hand = []
dealer_hand = []

player_stand = False
dealer_stand = False

#deal card
def deal_card(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

#calculate total of hand
def total(turn):
    total = 0
    face = ["J","Q","K"]
    for card in turn:
        if card in range(1,11):
            total += card
        elif card in face:
            total += 10
        else:
            if total > 11:
                total += 1
            else:
                total += 11
    return total 

#check for winner
def reveal_dealer_hand():
    if len(dealer_hand) == 2:
        return dealer_hand[0]
    elif len(dealer_hand) > 2:
        return dealer_hand[0], dealer_hand[1]

#game loop
for _ in range(2):
    deal_card(dealer_hand)
    deal_card(player_hand)

print(dealer_hand)
print(player_hand)

while player_stand == False or dealer_stand == False:
    print(f"Dealer had {reveal_dealer_hand()} and X")
    print(f"You have {player_hand} with a total of {total(player_hand)}")
    