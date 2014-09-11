#thinkpython 11 inheritance, playing cards

import random

class Card(object):
	"""represents one playing card. ranks and suits are stored as ints 0-3, 1-13. 
	and mapped to class attributes for printing."""
	
	#attributes
	suit_name= ['Clubs', 'Diamonds', 'Hearts', 'Spades']
	rank_name= [None, 'Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']

	def __init__(self, rank=2, suit=0):
		self.rank = rank
		self.suit = suit

	def __str__(self):
		return '%s of %s' % (Card.rank_name[self.rank], Card.suit_name[self.suit])

	def __cmp__(self, other):
		t1 = (self.suit, self.rank)
		t2 = (other.suit, other.rank)
		return cmp(t1,t2)

class Deck(object):
	"""Deck of cards. attribute cards holds current deck"""

	def __init__(self):
		"""initialize one full deck"""
		self.cards = []
		for suit in range(0,3):
			for rank in range(1,14):
				self.cards.append(Card(rank, suit))

	def __str__(self):
	 	res = []
		for card in self.cards:
			res.append(str(card))
		return '\n'.join(res)

	def pop(self):
		"""removes card from end of queue in cards. returns card."""
		return self.cards.pop()

	def add(self, card):
		"""Appends a card to the end of the list"""
		self.cards.append(card)
	
	def shuffle(self):
		"""shuffles deck. doesn't return copy"""
		random.shuffle(self.cards)

	def sort(self):
		"""sorts cards, first by suit, then by rank"""

		sorted = False
		while not sorted:
			sorted = True
			for x in range(len(self.cards)-1):
				if self.cards[x] > self.cards[x+1]:
					self.cards[x], self.cards[x+1] = self.cards[x+1], self.cards[x]
					sorted = False
			
	def move_cards(self, hand, num):
		""" moves int num of cards from deck to hand (or other deck, or hand to hand)"""

		for i in range(num):
			hand.cards.append(self.pop())

	def deal_hands(self, num_hands, num_cards):
		"""from the deck, deals out num_cards to num_hands. Returns list of Hands"""
		
		hands = []
		
		for i in range(num_hands):
			hands.append(Hand())
			self.move_cards(hands[i], num_cards)
	
		return hands


class Hand(Deck):
	"""represents a hand of cards, it inherits from deck"""

	def __init__(self, label=''):
		"""creates an empty hand"""

		self.cards = []
		self.label = label
			

if __name__ == '__main__':
	deck1 = Deck()

	game1 = deck1.deal_hands(5,5)
	for i in game1:
		print i
		print ''



#	print 'initialised..........................................'
#	print deck1
#	deck1.shuffle()
#	print 'shuffled.............................................'
#	print deck1
#	deck1.sort()
#	print 'sorted...............................................'
#	print deck1
