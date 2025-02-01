import random

class Deck:
    def __init__(self):
        self.card_values = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "j":10, "q":10, "k":10, "a":11}
        self.cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "j", "q", "k", "a"]
        self.faces = ["H", "S", "C", "D"]
        self.used_cards = []

    def random_card(self):
        """Returns a random card that has not been used yet."""
        while True:
            card = random.choice(self.cards)
            face = random.choice(self.faces)
            card_name = f"{card}{face}"
            if card_name not in self.used_cards:
                self.used_cards.append(card_name)
                return card_name

    def deal(self, game):
        """Deals two cards to player and dealer, updating scores correctly."""
        player_cards = []
        dealer_cards = []

        for _ in range(2):
            card = self.random_card()
            player_cards.append(card)
            game.add_card_value(card, player=True)

        for _ in range(2):
            card = self.random_card()
            dealer_cards.append(card)
            game.add_card_value(card, player=False)

        return player_cards, dealer_cards


class Game:
    def __init__(self):
        self.card_values = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "j":10, "q":10, "k":10, "a":11}
        self.playerscore = 0
        self.compscore = 0
        self.player_cards = []
        self.dealer_cards = []
        self.player_aces = 0
        self.dealer_aces = 0

    def add_card_value(self, card, player=True):
        """Adds card value to the respective player, handling Aces properly."""
        card_value = card[:-1]  # Extract numeric part of the card
        if card_value == "a":
            ace_value = 11
            if player:
                self.player_aces += 1
            else:
                self.dealer_aces += 1
        else:
            ace_value = self.card_values.get(card_value, 0)

        if player:
            self.playerscore += ace_value
            self.player_cards.append(card)
            self.adjust_aces(player=True)
        else:
            self.compscore += ace_value
            self.dealer_cards.append(card)
            self.adjust_aces(player=False)

    def adjust_aces(self, player=True):
        """Adjusts Aces from 11 to 1 if a player busts."""
        if player:
            while self.playerscore > 21 and self.player_aces:
                self.playerscore -= 10
                self.player_aces -= 1
        else:
            while self.compscore > 21 and self.dealer_aces:
                self.compscore -= 10
                self.dealer_aces -= 1

    def check_scores(self):
        """Checks the scores and determines if the game should continue."""
        if self.playerscore == 21 and self.compscore != 21:
            print("Player wins!")
            return False
        elif self.compscore == 21 and self.playerscore != 21:
            print("Dealer wins!")
            return False
        elif self.playerscore > 21:
            print("Player bust! Dealer wins.")
            return False
        elif self.compscore > 21:
            print("Dealer bust! Player wins.")
            return False
        return True

    def final_scores(self):
        """Compares final scores and declares the winner."""
        if self.playerscore > 21:
            print("Player bust! Dealer wins.")
        elif self.compscore > 21:
            print("Dealer bust! Player wins.")
        elif self.playerscore > self.compscore:
            print("Player wins!")
        elif self.compscore > self.playerscore:
            print("Dealer wins!")
        else:
            print("It's a tie!")

    def play(self):
        """Main game loop for playing Blackjack."""
        self.deck = Deck()
        player_cards, dealer_cards = self.deck.deal(self)

        print(f"Player Cards: {player_cards} (Score: {self.playerscore})")
        print(f"Dealer Card: {dealer_cards[0]}")  # Show only one dealer card

        in_play = self.check_scores()
        while in_play:
            x = input("Hit or Stand? ").lower()
            if x == "hit":
                card = self.deck.random_card()
                self.add_card_value(card, player=True)
                print(f"Player drew {card} (Score: {self.playerscore})")
                in_play = self.check_scores()
            else:
                print("\nRevealing Dealer Cards...")
                print(f"Dealer Cards: {self.dealer_cards} (Score: {self.compscore})")

                # Dealer must hit until score is at least 17
                while self.compscore < 17:
                    card = self.deck.random_card()
                    self.add_card_value(card, player=False)
                    print(f"Dealer drew {card} (Score: {self.compscore})")

                self.final_scores()
                break


# Run the game
game = Game()
game.play()