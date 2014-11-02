from helpers import *

num_trials = 100
eta = .01

for i in range(num_trials):
	# build data set
	N = 100
	data, slope, intercept = buildDataSet(N=N)
	X, y = extract(data)
	X = addIntercept(X)

	# use this to exit
	change_in_w = 10
	while change_in_w >= .01:
		# initialize weights to zeros
		w = np.zeros(X.shape[1])
		all_w = []
		epoch = 0
		for i in range(N):
			# stochastic gradient descent
			grad = -(y[i] * X[i, :])/ (1 + np.exp(y[i] * np.dot(w, X[i, :])))
			# update weights
			w = w - eta * grad
		epoch += 1
		all_w = all_w + [w]
		change_in_w = np.linalg.norm(all_w[epoch - 1] - all_w[epoch])

