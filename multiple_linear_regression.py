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
data = pd.read_csv('top-youtube-videos.csv', sep=',')
data = data[['channelId', 'comments', 'duration', 'definition', 'licensedContent', 'likes', 'dislikes', 'views']]

# processing data
le = preprocessing.LabelEncoder()
data['definition'] = le.fit_transform(data['definition'])  # 0 is HD 1 is SD
data['licensedContent'] = le.fit_transform(data['licensedContent'])  # 1 is TRUE 0 is FALSE

x = data.iloc[:, :-1]  # without views
y = data.iloc[:, 7]  # views isolated

# converting unique channels to categorical columns
channel_ids = pd.get_dummies(x['channelId'], drop_first=True)  # dummy variable trap dealt with

# dropping chanelId column as dummies are calculated
x = x.drop('channelId', axis=1)

# concat dummy variables
x = pd.concat([x, channel_ids], axis=1)

# training and testing
x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.2, random_state=0)

# fitting multiple linear regression to training set
reg = linear_model.LinearRegression()
reg.fit(x_train, y_train)


