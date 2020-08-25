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

plt.plot(y, '-b')  # actual data is blue
plt.xlabel('days')
plt.ylabel('coronavirus cases')

poly_features = PolynomialFeatures(degree=2)
X = poly_features.fit_transform(X)

print('--- training ---')
model = linear_model.LinearRegression()
model.fit(X, y)
acc = model.score(X, y)
print(f'Accuracy: {round(acc*100, 3)}%')

y0 = model.predict(X)
plt.plot(y0, '--r')  # predicted data is dashed red
plt.show()
