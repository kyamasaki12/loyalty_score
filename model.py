# model.py
import numpy as np
import pandas
import tensorflow as tf
import tensorflow.keras as keras
import tensorflow.keras.layers as layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.wrappers.scikit_learn import KerasRegressor

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

tf.enable_eager_execution()
# tensorflow hello world
# hello = tf.constant('Hello, TensorFlow!')
# sess = tf.Session()
# print(sess.run(hello).decode())
from sklearn.model_selection import train_test_split
import pickle

data = pickle.load( open( "train.p", "rb" ) )

yset = pickle.load( open( "yset.p", "rb" ) )

data_values = []
y_vals = []
keylist = list(data.keys())
keylist.sort()
for key in keylist:
	#data_keys.append(key)
	data_values.append(data[key])
	# print ("%s: %s" , (key, data[key]))

keylist = list(yset.keys())
keylist.sort()
for key in keylist:
	#data_keys.append(key)
	y_vals.append(float(yset[key]))
	
data_values=np.array(data_values)
y_vals=np.array(y_vals)
print(data_values.shape)
# train test split
X_train, X_test, y_train, y_test = train_test_split(data_values, y_vals, test_size=0.33, random_state=1)
print(X_train.shape)
def model():
	model = tf.keras.Sequential()
# add layer 64 units
	model.add(layers.Dense(64, activation='relu', input_dim=8))
	model.add(layers.Dense(64, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.01)))
# add layer 64 units
	model.add(layers.Dense(64, activation='relu'))
	model.add(layers.Dense(1, kernel_initializer='normal'))
	model.compile(loss='mean_squared_error', optimizer='adam')
	return model

# fit the model
# fix random seed for reproducibility

seed = 7
np.random.seed(seed)
estimator = KerasRegressor(build_fn=model(), epochs=100, batch_size=5, verbose=1)

kfold = KFold(n_splits=10, random_state=seed)
results = cross_val_score(estimator, X_train, y_train, cv=kfold)
print("Results: %.2f (%.2f) MSE" % (results.mean(), results.std()))
