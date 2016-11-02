# -*- coding: utf-8 -*-
"""
This one is designed to work with numpy arrays only 
"""
from scipy.stats import binom, itemfreq
import numpy as np

def riffle(deck,n_times=1):
    
    n_cards = deck.size
    
    for j in range(n_times):
        # Split the deck into two piles (left and right) according to the binomial distribution at position "pos"
        pos = binom(n_cards,.5).rvs(1)[0]
        left, right = deck[:pos].copy(), deck[pos:].copy()
        
        # Initialize the deck.  Cards will be placed back here.
        deck[:] = -1

        # The probability of grabbing the card from left or right
        # is proportional to the size of that pile
        for i in range(n_cards):
            p = np.random.rand()
            thresh = left.size / (left.size + right.size)
            if p < thresh:
                deck[i] = left[0]
                left = np.delete(left,0)
            else:
                deck[i] = right[0]
                right = np.delete(right,0)

#http://stackoverflow.com/questions/18683988/count-numbers-of-consecutive-1s-and-0s-in-a-vector

def count_rises(deck):
    rising_sequences = (np.diff(deck)==1).astype(int) 
    w = np.hstack((0,rising_sequences,0))
    return itemfreq(np.where(np.diff(w)==-1)[0] - np.where(np.diff(w)==1)[0])
    
    
