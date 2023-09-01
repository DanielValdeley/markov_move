import numpy as np 

def markov_move(A, s):
    n, u, accum = 0, np.random.uniform(0,1), A[s][0]
    while u > accum:
        n = n + 1
        accum = accum + A[s][n]
    return n


A = np.array([ [0.3, 0.5, 0.2], [0.3, 0.4, 0.3], [0.2, 0.5, 0.3] ])

s = 0
markov_move = []
for i in range(1000):
    s = markov_move(A,s)
    vet_cont[s] += 1 // TODO ajustar logica
    print(s)
