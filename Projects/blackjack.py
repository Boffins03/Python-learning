import random

class Card():
    def __init__(self, suit, rank) -> None:
        self.suit = suit
        self.rank = rank

    def __str__(self) -> str:
        return f"{self.rank['rank']} of {self.suit}"    

class Deck:
    def __init__(self) -> None:
        self.cards = []
        suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
        ranks = [{'rank':'A','value':11},
                {'rank':'2','value':2},
                {'rank':'3','value':3},
                {'rank':'4','value':4},
                {'rank':'5','value':5},
                {'rank':'6','value':6},
                {'rank':'7','value':7},
                {'rank':'8','value':8},
                {'rank':'9','value':9},
                {'rank':'10','value':10},
                {'rank':'K','value':10},
                {'rank':'Q','value':10},
                {'rank':'J','value':10}]
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self, number):
        card_dealt = []
        for _ in range(number):
            if len(self.cards) > 0:
                card = self.cards.pop()
                card_dealt.append(card)
        return card_dealt 

class Hand:
    def __init__(self, dealer=False) -> None:
        self.cards = []
        self.value = 0
        self.dealer = dealer

    def add_card(self, card_list):
        self.cards.extend(card_list)

    def calculate_value(self):
        self.value = 0
        has_ace = False

        for card in self.cards:
            card_value = card.rank['value']          
            self.value += card_value
            if card.rank['rank'] == "A":
                has_ace = True

        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        self.calculate_value()
        return self.value

    def is_blackjack(self):
        return self.get_value() == 21
                                
    def display(self, show_all_dealer_card=False):
        print(f"{'Dealer' if self.dealer else 'Your'} hand:")
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer and not show_all_dealer_card and not self.is_blackjack():
                print("Hidden")
            else:    
                print(card)

        if not self.dealer:
            print(f"Value: {self.get_value()}")

class Game:
    def play(self):
        games_number = 0
        games_to_play = 0
        
        while games_to_play <= 0:
            try:
                games_to_play = int(input("How many games do you want to play? "))
                break
            except ValueError:
                pass    

        while games_number < games_to_play:
            games_number += 1        

            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

            for _ in range(2):
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))

            print()
            print("-" * 20)
            print(f"Game {games_number} out of {games_to_play} games")
            print("-" * 20)

            player_hand.display()
            print()
            dealer_hand.display()
            print()

            if self.check_winner(player_hand, dealer_hand):
                choice = ""
                while player_hand.get_value() < 21 and choice not in ['s', 'stand']:
                    choice = input("Please choose 'Hit' or 'Stand': ").lower()
                    print()
                    while choice not in ['h', 's', 'hit', 'stand']:
                        choice = input("Please choose 'Hit' or 'Stand' (or H/S): ").lower()
                        print()

                    if choice in ['hit', 'h']:
                        player_hand.add_card(deck.deal(1))
                        player_hand.display()
                        print()

            if self.check_winner(player_hand, dealer_hand):
                player_hand_value = player_hand.get_value()
                dealer_hand_value = dealer_hand.get_value()

                while dealer_hand_value < 17:
                    dealer_hand.add_card(deck.deal(1))
                    dealer_hand_value = dealer_hand.get_value()

                dealer_hand.display(show_all_dealer_card=True)    
                
            if self.check_winner(player_hand, dealer_hand):        
                print("Final Result")
                print("Your hand:", player_hand_value)
                print("Dealer's hand:", dealer_hand_value)

                self.check_winner(player_hand, dealer_hand, True)

        print("\nThanks for playing!")

    def check_winner(self, player_hand, dealer_hand, game_over=False):
        if not game_over:
            if player_hand.get_value() > 21:
                print("You busted, Dealer wins!")
            elif dealer_hand.get_value() > 21:
                print("Dealer busted, You win!")
            elif player_hand.is_blackjack() and dealer_hand.is_blackjack():
                print("Game is a tie!")
            elif player_hand.is_blackjack():
                print("You have blackjack. You win!")
            elif dealer_hand.is_blackjack():
                print("Dealer has blackjack. Dealer wins!")
            return True
        else:
            if  player_hand.get_value() > dealer_hand.get_value():
                print("You win")
            elif player_hand.get_value() == dealer_hand.get_value():
                print("Game is a tie")
            else:
                print("Dealer wins")        
            return True
        return False

g = Game()
g.play()
