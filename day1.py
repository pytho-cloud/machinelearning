import numpy as np
import scipy as sp
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]


print("The mean using numpy is :", np.mean(speed))

print("the mean using numpy is :", np.median(speed))

print("the mode using scipy is : " , sp.stats.mode(speed))

print("the standrad deviation using numpy is:", np.std(speed))


