# -*- coding: utf-8 -*-
"""
This one is designed to work with numpy arrays only 
"""
from random import random
from scipy.stats import binom, itemfreq
from numpy import array, diff, hstack, where

def riffle(deck,n_times=1):
    
    n_cards = len(deck)
    
    for j in range(n_times):
        # Split the deck into two piles according to the binomial distribution
        pos = binom(n_cards,.5).rvs(1)
        heap = [deck[:pos].copy(), deck[pos:].copy()]
        
        # Initialize the deck
        deck[:] = -1

        for i in range(n_cards):
            p = random()
            thresh = float(len(heap[0])) / (len(heap[0]) + len(heap[1]))
            if p < thresh:
                deck[i] = heap[0][0]
                heap[0] = heap[0][1:]
            else:
                deck[i] = heap[1][0]
                heap[1] = heap[1][1:]

#http://stackoverflow.com/questions/18683988/count-numbers-of-consecutive-1s-and-0s-in-a-vector

def count_rises(deck):
    rising_sequences = (diff(deck)==1).astype(int) 
    w = hstack((0,rising_sequences,0))
    return itemfreq(where(diff(w)==-1)[0] - where(diff(w)==1)[0])
    
    
