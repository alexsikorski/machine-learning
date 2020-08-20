import matplotlib.pyplot as plt
import numpy as np
import random
from sklearn import model_selection
from sklearn import linear_model

# populating data
x = list(range(0, 50))  # celcius
y = [1.8 * F + 32 + random.randint(-3, 3) for F in x]  # farenheit
# y = [1.8 * F + 32 for F in x]  # farenheit

print(f'x: {x}')
print(f'y: {y}')

plt.plot(x, y, '-*r')

# required format for machine learning library
x = np.array(x).reshape(-1, 1)
y = np.array(y).reshape(-1, 1)

x_training, x_testing, y_training, y_testing = model_selection.train_test_split(x, y, test_size=0.2)
# test_size 20%, training is therefore 80%

model = linear_model.LinearRegression()
model.fit(x_training, y_training)

print(f'Coefficients: {model.coef_}')  # this is m in y = mx + c, should be 1.8
print(f'Intercept: : {model.intercept_}')  # this is the c in y = mx + c, should be 32

accuracy = model.score(x_testing, y_testing)
print(f'Accuracy: {round(accuracy * 100, 2)}')

# displaying new values

x = x.reshape(1, -1)[0]
m = model.coef_[0][0]
c = model.intercept_[0]
y = [m * F + c for F in x]
plt.plot(x, y, '-*b')
plt.show()