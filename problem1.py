import numpy as np 

sigma = .1
d = 8
bound = .008

N = np.array([10., 25., 100., 500., 1000.])
Ein = sigma**2 * (1 - ((d + 1)/ N))

for i in range(len(N)):
	if Ein[i] >= bound:
		print N[i]

