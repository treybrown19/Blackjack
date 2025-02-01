import random

class Deck:
	def __init__(self):
		self.card_values = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10, "j":10, "q":10,"k":10, "a":11}
		self.cards = ["2","3","4","5","6","7","8","9","10","j","q","k","a"]
		self.faces = ["H", "S", "C", "D"]
		self.used_cards = []
	def random_card(self):
		x = random.randint(0,len(self.cards)-1)
		y = random.randint(0,3)
		return "{card}{face}".format(card = self.cards[x], face = self.faces[y])
	def deal(self, game):
		x = self.card_values.keys()
		player_cards = []
		dealer_cards = []
		for i in range(2):
			rc = self.random_card()
			still_looking = True
			while still_looking:
				if rc not in self.used_cards:
					self.used_cards.append(rc)
					still_looking = False
				else:
					rc = self.random_card()
			game.playerscore += self.card_values.get(rc[0], 0)
			player_cards.append(rc)
		print("Player cards:", player_cards)
		for i in range(2):
			rc = self.random_card()
			still_looking = True
			while still_looking:
				if rc not in self.used_cards:
					self.used_cards.append(rc)
					still_looking = False
				else:
					rc = self.random_card()
			game.compscore += self.card_values[rc[0]]
			dealer_cards.append(rc)
		print("Dealer cards:", dealer_cards)
		first_deal = [player_cards, dealer_cards]
		return first_deal
	def hit(self, game):
		rc = self.random_card()
		still_looking = True
		while still_looking:
			if rc not in self.used_cards:
				self.used_cards.append(rc)
				still_looking = False
			else:
				rc = self.random_card()
		return rc 



class Game:
	def __init__(self):
		self.card_values = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10, "j":10, "q":10,"k":10, "a":11}
		self.playerscore = 0
		self.compscore = 0
		self.player_cards = []
		self.dealer_cards = []

	def check_scores(self):
		if self.playerscore == 21 and self.compscore != 21:
			print("Player wins!")
			return False
		elif self.compscore == 21 and self.playerscore != 21:
			print("Computer wins!")
			return False
		elif self.playerscore == 21 and self.compscore == 21:
			print("Tie")
			return False
		elif self.playerscore > 21:
			print("Player bust")
			return False
		elif self.compscore > 21:
			print("Computer bust")
			return False
		else:
			return True

	def final_scores(self):
		if self.playerscore == 21 and self.compscore != 21:
			print("Player wins!")
			return False
		elif self.compscore == 21 and self.playerscore != 21:
			print("Computer wins!")
			return False
		elif self.playerscore == 21 and self.compscore == 21:
			print("Tie")
			return False
		elif self.playerscore > 21:
			print("Player bust")
			return False
		elif self.compscore > 21:
			print("Computer bust")
			return False
		elif self.playerscore < 21 and self.playerscore > self.compscore:
			print("Player wins")
			return False 
		elif self.compscore < 21 and self.compscore > self.playerscore:
			print("Computer wins")
			return False 
		else:
			print("Some kind of issue happened here.")
			return False

	def play(self):
		self.deck = Deck()
		starting_deal = self.deck.deal(self)
		print("Player Cards: {player} \n Dealer Card: {dealer}".format(player = starting_deal[0], dealer = starting_deal[1][0]))
		self.playerscore += self.card_values.get(starting_deal[0][0], 0) + self.card_values.get(starting_deal[0][1], 0)
		self.compscore += self.card_values.get(starting_deal[1][0], 0)
		self.player_cards.append(starting_deal[0])
		self.dealer_cards.append(starting_deal[1])
		in_play = self.check_scores()
		while in_play:
			x = input("Hit or Stand? ")
			if x.lower() == "hit":
				hit = self.deck.hit(self)
				print(hit)
				self.playerscore += self.card_values.get(hit, 0)
				self.player_cards.append(hit)
				in_play = self.check_scores()

			else:
				print("Player Cards: {player} \n Dealer Cards: {dealer}".format(player = self.player_cards, dealer = self.dealer_cards))
				in_play = self.final_scores()



game = Game()
game.play()