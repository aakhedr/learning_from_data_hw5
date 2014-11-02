import numpy as np 

w = np.array([1, 1])
eta = .1
error  = (w[0] * np.exp(w[1]) - 2 * w[1] * np.exp(-w[0]))**(2)

for i in range(15):
    # move along u axis
    u = 2 * (np.exp(w[1]) + 2 * w[1] * np.exp(-w[0])) * (w[0]*np.exp(w[1]) - 2 
    	* w[1] * np.exp(-w[0]))
    w = w - eta * np.array([u,0])

    # move along v axis
    v = 2 * (w[0] * np.exp(w[1]) - 2 * w[1] * np.exp(-w[0])) * (w[0] * 
    	np.exp(w[1]) - 2 * np.exp(-w[0]))
    w = w - eta * np.array([0,v])

    # calcualte the error
    error  = (w[0]*np.exp(w[1]) - 2*w[1]*np.exp(-w[0]))**(2)

print error
