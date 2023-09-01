import numpy as np 

def markov_move(A, s):
    n, u, accum = 0, np.random.uniform(0,1), A[s][0]
    while u > accum:
        n = n + 1
        accum = accum + A[s][n]
    return n


A = np.array([ [0.3, 0.5, 0.2], [0.3, 0.4, 0.3], [0.2, 0.5, 0.3] ])




runs = 1000000
s = 0
vet_cont = {}
tam = A[0].size
vet_cont = np.zeros(tam)
for i in range(runs):
    s = markov_move(A,s)
    vet_cont[s] += 1 

for i in range(tam):
    print(vet_cont[i]/runs)


