import numpy as np 
import random

def buildDataSet(N=100):
	'''
	Construct a 3 column data set with N rows of floats chosen at random
	from the interval [-1, 1] as follow:
	x1=column1 - x2=column2 - y=column3=values of either (-1) or (+1).
	Also constructs a line separating points(y=-1) from points(y=-1).
	Returns the data set, line slope, line y intercept.
	'''
	x1 = np.array([random.uniform(-1, 1) for i in range(N)])
	x2 = np.array([random.uniform(-1, 1) for i in range(N)])

	X = np.column_stack((x1, x2))

	pointsX = np.array([random.uniform(-1, 1) for i in range(2)])
	pointsY = np.array([random.uniform(-1, 1) for i in range(2)])

	# y = ax + b

	slope = (pointsY[1] - pointsY[0])/ (pointsX[1] - pointsX[0])
	yIntercept = pointsY[1] - (slope * pointsX[1])

	y = np.empty(shape=(N, 1), dtype=int)
	for i in range(X.shape[0]):
		yEst = slope * X[i, 0] + yIntercept
		if X[i, 1] > yEst:
			y[i] = 1
		elif X[i, 1] < yEst:
			y[i] = -1
		else:
			y[i] = 0

	assert(y[y==0].shape[0] == 0)		# make sure there are no points on the line!
	data = np.column_stack((X, y))

	return(data, slope, yIntercept)

