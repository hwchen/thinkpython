#thinkpython 18.6 poker hands

#compared to actual probability, it looks like my straight function
#might have a bug.

"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

from Card import *


class PokerHand(Hand):

	def suit_hist(self):
		"""Builds a histogram of the suits that appear in the hand.

		Stores the result in attribute suits.
		"""
		self.suits = {}
		for card in self.cards:
			self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

	def has_flush(self):
		"""Returns True if the hand has a flush, False otherwise.
      
		Note that this works correctly for hands with more than 5 cards.
		"""
		self.suit_hist()
		for val in self.suits.values():
			if val >= 5:
				return True
		return False


	def rank_hist(self):
		"""Builds a histogram of the ranks that appear in the hand.
		stores result in attribute ranks"""

		self.ranks = {}
		for card in self.cards:
			self.ranks[card.rank] = self.ranks.get(card.rank,0) + 1


	def has_pair(self):
		"returns true if hand has one  pair, false otherwise"""

		self.rank_hist()
		for value in self.ranks.values():
			if value >= 2:
				return True
		return False

	def has_two_pair(self):
		"returns true if hand has two pair, false otherwise"""

		self.rank_hist()
		total = 0
		for value in self.ranks.values():
			if value >= 2:
				total += 1
	
		if total >= 2:
			return True
		return False

	def has_three(self):
		"returns true if hand has three of a kind"

		self.rank_hist()
		for value in self.ranks.values():
			if value >= 3:
				return True
		return False

	def has_straight(self):
		"returns true if 5 ranks are consecutive, with Ace high or low"""

		#WHere's the bug?

		#bubble sort ranks, remove duplicate numbers

		t = []
		for card in self.cards:
			t.append(card.rank)		

		t.sort()

		m=0
		while m < (len(t)-1):
			if t[m] == t[m+1]:
				t.pop(m)
			else:
				m += 1

		#append ace high if necessary

		if t[0] == 1:
			t.append(14)

		#look for straight
		total = 0
		for i in range(len(t)-1):
			if t[i] == t[i+1] - 1:
				total +=1
				if total == 4:
					return True
			else:
				total = 0
		return False	


	def full_house(self):
		"""returns True if hand has 3 of a kind and 2 of a kind"""

		#should I reverse the dictionary?
		self.rank_hist()

		d = {}
		for key, value in self.ranks.items():
			d.setdefault(value,[]).append(key)

		if (2 in d) and (3 in d):
			return True 

		if (3 in d) and (len(d[3]) >= 2):
			return True

		return False

	def has_four(self):
		"""returns True if there is 4 of a kind"""
		self.rank_hist()
		if 4 in self.ranks.values():
			return True

		else:
			return False


	def straight_flush(self):
		""" returns true if 5 cards are both flush and straight.
			separate out the flush first, and then try for straight"""

		flush = 0
		flushhand = PokerHand() #This is to copy the hand.
		
		if self.has_flush():
			for suit, value  in self.suits.items():
				if value >=5:
					flush = suit

			for card in self.cards:
				if card.suit == flush:
					flushhand.add_card(card)
		
			return flushhand.has_straight()
		return False
				
	def best_hand(self):
		"""labels a hand with the best hand"""
		if self.straight_flush():
			self.label = 'straight flush'
		elif self.has_four():
			self.label = 'four of a kind'
		elif self.full_house():
			self.label =  'full house'
		elif self.has_flush():
			self.label = 'flush'
		elif self.has_straight():
			self.label = 'straight'
		elif self.has_three():
			self.label = 'three of a kind'
		elif self.has_two_pair():
			self.label = 'two pair'
		elif self.has_pair():
			self.label = 'pair'
		else:
			self.label = 'nothing'

def poker_hist(num_cards, n):
	""" runs hands for n number of times. stores results in 
	a histogram of possible hands, as well as the total hands
	num_cards is number of cards in a hand
	I'm doing one hand per deck first."""
	d = {}
	total = 0
	for i in range(n):
		deck = Deck()
		deck.shuffle()
		hand = PokerHand()
		deck.move_cards(hand, num_cards)
		hand.best_hand()
		d[hand.label] = d.get(hand.label,0) + 1
		total += 1
	
	#sort histogram

	t = []
	for key, value in d.items():
		t.append((value, key))
	t.sort()

	#print histogram

	print 'Number of runs: ' + str(total)
	for prob,label in t:
		print label.rjust(15), str(prob/float(total)).rjust(5)
	
	
if __name__ == '__main__':
	# make a deck
	#deck = Deck()
	#deck.shuffle()
	#hand = PokerHand()
	#deck.move_cards(hand,7)
	#print hand.has_straight()

	# deal the cards(7 per hand) and classify the hands
	#for i in range(7):
	#	hand = PokerHand()
	#	deck.move_cards(hand, 7)
	#	hand.sort()
	#	print hand
	#	hand.best_hand()
	#	print 'the best hand is: ' + str(hand.label)
	#	print ''

	hist = poker_hist(7,1000000)

	
