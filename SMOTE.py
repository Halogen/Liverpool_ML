#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
This is an implementation of the SMOTE Algorithm. 
'''

import numpy as np
from random import randrange, choice
from sklearn.neighbors import NearestNeighbors

def SMOTE(T, N, k):
    """
    Returns (N/100) * n_minority_samples synthetic minority samples.

    Parameters
    ----------
    T : array-like, shape = [n_minority_samples, n_features]
        Holds the minority samples
    N : percetange of new synthetic samples: 
        n_synthetic_samples = N/100 * n_minority_samples. Can be < 100.
    k : int. Number of nearest neighbours. 

    Returns
    -------
    S : array, shape = [(N/100) * n_minority_samples, n_features]
    """    
    n_minority_samples, n_features = T.shape
    
    if N < 100:
        #create synthetic samples only for a subset of T.
        #TODO: select random minortiy samples
        N = 100
        pass

    if (N % 100) != 0:
        raise ValueError("N must be < 100 or multiple of 100")
    
    N = N/100
    n_synthetic_samples = N * n_minority_samples
    S = np.zeros(shape=(int(n_synthetic_samples), n_features))
    
    #Learn nearest neighbours
    neigh = NearestNeighbors(n_neighbors = k)
    neigh.fit(T)

    
    #Calculate synthetic samples
    neighbours = neigh.kneighbors(T, return_distance=False)
    for i in range(n_minority_samples):
        nn = neighbours[i]
        for n in range(int(N)):
            nn_index = choice(nn)
            #NOTE: nn includes T[i], we don't want to select it 
            while nn_index == i:
                nn_index = choice(nn)
            dif = T[nn_index] - T[i] 
            gap = np.random.random()
            S[int(n + i * N), :] = T[i,:] + gap * dif[:]
    return S

