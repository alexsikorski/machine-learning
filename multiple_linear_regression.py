import pandas as pd
from sklearn import preprocessing

# settings
pd.set_option('display.max_columns', None)

# loading data
data = pd.read_csv('top-youtube-videos.csv', sep=',')
data = data[['comments', 'duration', 'definition', 'licensedContent', 'likes', 'dislikes', 'views']]

# processing data
le = preprocessing.LabelEncoder()
data['definition'] = le.fit_transform(data['definition'])  # 0 is HD 1 is SD
data['licensedContent'] = le.fit_transform(data['licensedContent'])  # 1 is TRUE 0 is FALSE

print(data.head())
