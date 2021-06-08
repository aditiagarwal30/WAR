#suit, Rank, value

# make a dictionary for values

import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace') 
values= {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

#***********  CLASS CARD  *****************

class Card:
    
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value= values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit

#***********  CLASS DECK  ****************

class Deck:
    
    def __init__(self):
        
        self.all_cards=[]
        
        for suit in suits:
            for rank in ranks:
                
                # Creating card object
                created_card= Card(suit,rank)
                
                self.all_cards.append(created_card)
                
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()

                                      
#*************  CLASS PLAYER  ******************


class Player:
    
    def __init__(self,name):
        self.name = name
        # A new player has no cards
        self.all_cards = [] 
        
    def remove_one(self):
        # Note we remove one card from the list of all_cards
        # We state 0 to remove from the "top" of the deck
        # We'll imagine index -1 as the bottom of the deck
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


#***************** GAME SETUP **********************


p1=input('Enter Player 1 name: ')
player1= Player(p1)

p2=input('Enter Player 2 name: ')
player2= Player(p2)

new_deck= Deck()
new_deck.shuffle()

for x in range(26):
    player1.add_cards(new_deck.deal_one())
    player2.add_cards(new_deck.deal_one()) 

import pdb 
game_on = True

round_num = 0
while game_on:
    
    round_num += 1
    print(f"Round {round_num}")
    
    # Check to see if a player is out of cards:

    if len(player1.all_cards) == 0:
        print(f'{p1} out of cards! Game Over')
        print('          ')
        print(f'{p2} Wins!')
        game_on = False
        break
        
    if len(player2.all_cards) == 0:
        print(f'{p2} out of cards! Game Over')
        print('          ')
        print(f'{p1} Wins!')
        game_on = False
        break
    
    # Otherwise, the game is still on!
    
    # Start a new round and reset current cards "on the table"

    player1_cards = []
    player1_cards.append(player1.remove_one())
    
    player2_cards = []
    player2_cards.append(player2.remove_one())
    
    at_war = True

    while at_war:


        if player1_cards[-1].value > player2_cards[-1].value:

            # Player One gets the cards
            player1.add_cards(player1_cards)
            player1.add_cards(player2_cards)
            
            
            # No Longer at "war" , time for next round
            at_war = False
        
        # Player Two Has higher Card
        elif player1_cards[-1].value < player2_cards[-1].value:

            # Player Two gets the cards
            player2.add_cards(player1_cards)
            player2.add_cards(player2_cards)
            
            # No Longer at "war" , time for next round
            at_war = False

        else:
            print('WAR!')
            # This occurs when the cards are equal.
            # We'll grab another card each and continue the current war.
            
            # First check to see if player has enough cards
            
            # Check to see if a player is out of cards:
            if len(player1.all_cards) < 5:
                print(f'{p1} unable to play war! Game Over at War')
                print('          ')
                print(f'{p2} Wins!')
                game_on = False
                break

            elif len(player2.all_cards) < 5:
                print(f'{p2} unable to play war! Game Over at War')
                print('          ')
                print(f'{p1} Wins!')
                game_on = False
                break
            # Otherwise, we're still at war, so we'll add the next cards
            else:
                for num in range(5):
                    player1_cards.append(player1.remove_one())
                    player2_cards.append(player2.remove_one())
