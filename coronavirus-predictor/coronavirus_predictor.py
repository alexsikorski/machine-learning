import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model

fields = ['World']  # only obtaining world column
df = pd.read_csv('total_cases.csv', skipinitialspace=True, usecols=fields)
df['id'] = df.index  # copy index to id column

X = np.array(df['id']).reshape(-1, 1)
y = np.array(df['World']).reshape(-1, 1)

poly_features = PolynomialFeatures(degree=4)
X = poly_features.fit_transform(X)

print('--- training ---')
model = linear_model.LinearRegression()
model.fit(X, y)
acc = model.score(X, y)
print(f'Accuracy: {round(acc*100, 3)}%')

# testing
y0 = model.predict(X)

print('--- prediction ---')
days = 30
print(f'prediction - cases after {days} days: ', end='')
print(round(int(model.predict(poly_features.fit_transform([[240 + days]]))) / 1000000, 2), 'million')
# the data has gathered 241 days worth of data (index starts at 0 so 240 is used)
# changing days variable will display appropriate prediction.

x1 = np.array(list(range(1, 240 + days))).reshape(-1, 1)
y1 = model.predict(poly_features.fit_transform(x1))

plt.xlabel('days')
plt.ylabel('coronavirus cases')

plt.plot(y, '-b')  # actual data is blue
plt.plot(y1, '--y')  # prediction of the future
plt.plot(y0, '--r')  # line of best fit
plt.show()