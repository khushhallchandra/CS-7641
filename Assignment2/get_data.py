import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split, KFold, cross_val_score, learning_curve, GridSearchCV, validation_curve

data_white = pd.read_csv('data/winequality-white.csv', delimiter=';')
data_red = pd.read_csv('data/winequality-red.csv', delimiter=';')
data_white["type"] = 0
data_red["type"] = 1

data = data_white.append(data_red, ignore_index=True)
data = data.dropna()

X, y = data.drop('quality', axis=1), data.quality
y = (y<6).astype(int)
y = y = np.expand_dims(y.values, axis=1) 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


train_data = np.concatenate((X_train, y_train),axis=1)
test_data = np.concatenate((X_test, y_test),axis=1)

np.savetxt("data/train.csv", train_data, delimiter=",")
np.savetxt("data/test.csv", train_data, delimiter=",")