import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures

fields = ['World']  # only obtaining world column
df = pd.read_csv('total_cases.csv', skipinitialspace=True, usecols=fields)

X = np.array(df.index)
y = np.array(df['World'])

plt.plot(y, '-b')  # actual data is blue
plt.show()

poly_features = PolynomialFeatures(degree=2)
X = poly_features.fit_transform(X)

