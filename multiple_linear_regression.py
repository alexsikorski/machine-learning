import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn import model_selection
from sklearn import linear_model
from sklearn import metrics

# settings
pd.set_option('display.max_columns', None)

# loading data
data = pd.read_csv('top-youtube-videos.csv')
data = data[['channelId', 'comments', 'duration', 'definition', 'licensedContent', 'likes', 'dislikes', 'views']]

# processing data
le = preprocessing.LabelEncoder()
data['definition'] = le.fit_transform(data['definition'])  # 0 is HD 1 is SD
data['licensedContent'] = le.fit_transform(data['licensedContent'])  # 1 is TRUE 0 is FALSE

X = data.iloc[:, :-1]  # without views
y = data.iloc[:, 7]  # views isolated

# converting unique channels to categorical columns
channel_ids = pd.get_dummies(X['channelId'], drop_first=True)  # dummy variable trap dealt with

# dropping chanelId column as dummies are calculated
X = X.drop('channelId', axis=1)

# concat dummy variables
X = pd.concat([X, channel_ids], axis=1)

# convert everything to a float
X = X.astype(float)
y = y.astype(float)

# check for NaN and inf
# print("NaN X:", np.any(np.isnan(X)),"NaN y:", np.any(np.isnan(y)), "|", "Inf X:", np.all(np.isfinite(X)),  "Inf y:", np.all(np.isfinite(y)))
X = X.fillna(0)

# training and testing
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2, random_state=0)

# fitting multiple linear regression to training set
reg = linear_model.LinearRegression()

reg.fit(X_train, y_train)

# predict the test set results
y_pred = reg.predict(X_test)



