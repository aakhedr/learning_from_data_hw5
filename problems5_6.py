import numpy as np 

w = np.array([1, 1])
eta = .1
error  = (w[0] * np.exp(w[1]) - 2 * w[1] * np.exp(-w[0]))**(2)
bound = 10**(-14)

iterations = 0		# keep track of the number of iterations
while error >= bound:
	# calculate the derivatives
    u = 2 * (np.exp(w[1]) + 2 * w[1] * np.exp(-w[0])) * (w[0] * 
    	np.exp(w[1]) - 2 * w[1] * np.exp(-w[0]))

    v = 2 * (w[0] * np.exp(w[1]) - 2 * w[1] * np.exp(-w[0])) * (w[0] 
    	* np.exp(w[1]) - 2 * np.exp(-w[0]))

    grad = np.array([u,v])

    # gradient descent update
    w = w - eta * grad
    # recalculate error
    error  = (w[0] * np.exp(w[1]) - 2 * w[1] * np.exp(-w[0]))**(2)

    iterations += 1

# problem 5
print iterations
# problem 6
print w