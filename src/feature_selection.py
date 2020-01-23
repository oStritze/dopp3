import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import ExtraTreesRegressor
import matplotlib.pyplot as plt

import random
random.seed(1337)


#https://towardsdatascience.com/feature-selection-techniques-in-machine-learning-with-python-f24e7da3f36e

data = pd.read_csv("../data/clean/full_set.csv")


target_variable = "RelMigrations"
target = data.pop(target_variable)

# TODO: Delete the second multiples of country, code and year from full_set.csv
# drop unnecessary columns
columns_to_drop = ["Country","LocID","Time","MidPeriod","country","Code","year","Unnamed: 0","CNMR","NetMigrations"]
data = data.drop(columns_to_drop,axis=1)

data = data.fillna(0)

X = data
y = target

model = ExtraTreesRegressor()
model.fit(X,y)

feat_importances = pd.Series(model.feature_importances_, index=X.columns)
feat_importances.nlargest(50).plot(kind='barh')
plt.show()






# from sklearn.ensemble import ExtraTreesClassifier
# import matplotlib.pyplot as plt
# model = ExtraTreesClassifier()
# model.fit(X,y)
# print(model.feature_importances_) #use inbuilt class feature_importances of tree based classifiers
# #plot graph of feature importances for better visualization
# feat_importances = pd.Series(model.feature_importances_, index=X.columns)
# feat_importances.nlargest(20).plot(kind='barh')
# plt.show()

