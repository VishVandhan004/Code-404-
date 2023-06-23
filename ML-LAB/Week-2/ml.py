import numpy as np
# A


def expectedvalue(values, weights):
    values = np.asarray(values)
    weights = np.asarray(weights)
    return (values*weights).sum()


values = [0, 1, 2, 3, 4]
probs = [.18, .34, .35, .11, .02]
print(expectedvalue(values, probs))

# B
# mean
x = np.array([1, 2, 3, 4, 5, 6, 7, 2, 6, 2, 1, 4, 2, 2, 6])
print(np.mean(x))
# median
y = np.sort(x)
print(np.median(y))


# mode
# from scipy import stats
# print(stats.mode(x))

# C
# SD
z = np.array([2, 4, 4, 4, 5, 5, 7, 9])
print(np.std(z))

# D
# VARIANCE
print(np.var(z))

# F
# COVARIANCE MATRIX
a = np.array([1, 3, -1])
b = np.array([1, 0, -1])
print("Original array:")
print(a)
print("Original array:")
print(b)
print("COV MATRIX:\n", np.cov(a, b))

# E
# COVARIANCE
x = np.array([10, 12, 14, 8])
y = np.array([40, 48, 56, 32])
X = np.mean(x)
Y = np.mean(y)
q = 0
for i in range(4):
    q = q+((x[i]-X)*(y[i]-Y))
print(q/4)
