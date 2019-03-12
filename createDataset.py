import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.layers import Dense, BatchNormalization, Dropout, Input
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from tensorflow.keras.models import Sequential
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, Imputer
import os 
import matplotlib.pyplot as plt

merchants = pd.read_csv("merchants.csv")
historical = pd.read_csv("historical_transactions.csv")

train_df = pd.read_csv("train.csv")
new_merchants_df = pd.read_csv("new_merchant_transactions.csv")

gdf = historical.groupby("card_id")
gdf = gdf["purchase_amount"].agg(['sum', 'mean', 'std', 'min', 'max']).reset_index()
gdf.columns = ["card_id", "sum_hist_trans", "mean_hist_trans",
    "std_hist_trans", "min_hist_trans", "max_hist_trans"]
train_df = pd.merge(train_df, gdf, on="card_id", how="left")
print(train_df.head(5))

gdf = new_merchants_df.groupby("card_id")
gdf = gdf["purchase_amount"].size().reset_index()
gdf.columns = ["card_id", "num_merch_transactions"]
train_df = pd.merge(train_df, gdf, on="card_id", how="left")
print(train_df.head(5))

gdf = new_merchants_df.groupby("card_id")
gdf = gdf["purchase_amount"].agg(['sum', 'mean', 'std', 'min', 'max']).reset_index()
gdf.columns = ["card_id", "sum_merch_trans", "mean_merch_trans", "std_merch_trans", "min_merch_trans", "max_merch_trans"]
train_df = pd.merge(train_df, gdf, on="card_id", how="left")
print(train_df.head(5))

train_df["year"] = train_df["first_active_month"].dt.year
train_df["month"] = train_df["first_active_month"].dt.month

cols_to_use = ["feature_1", "feature_2", "feature_3", 
               "sum_hist_trans", "mean_hist_trans", "std_hist_trans", 
               "min_hist_trans", "max_hist_trans",
               "year", "month","num_merch_transactions", 
                "sum_merch_trans", "mean_merch_trans", "std_merch_trans",
                "min_merch_trans", "max_merch_trans",
              ]

data_df = train_df[cols_to_use]
data_y = train_df['target'].values
print(data_df.head(5))

sc = StandardScaler()
data_df = data_df.fillna(0)
data_df = sc.fit_transform(data_df)
data_df, x_test, data_y, y_test = train_test_split(data_df, data_y, test_size = .2, random_stat=2)
x_train, x_val, y_train, y_val = train_test_split(data_df, data_y, test_size = .1, random_stat=2)

import tensorflow.keras.backend as K 
def rmse(y_true, y_pred):
    return K.sqrt(K.mean(K.square(y_pred - y_true), axis=-1))

model = Sequential()
model.add(Dense(2048, input_dim = x_train.shape[1], activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(.5))
model.add(Dense(4096, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(.5))
model.add(Dense(2048, activation='relu'))
model.add(Dropout(.5))
model.add(Dense(1024, activation='elu'))
model.add(Dense(1,activation= 'linear'))

model.compile(optimizer='adam', loss=rmse)
early_stopping = EarlyStopping(monitor = 'val_loss', patience = 10)
checkpointer = ModelCheckpoint(filepath='weights.hdf5', verbose=1, save_best_only=True)

model.fit(x_train, y_train, validation_data = (x_val, y_val), epochs = 50, batch_size =1024, callback = [early_stopping, checkpointer])

plt.plot(model.history.history['val_loss'], label = "val_loss")
plt.plot(model.history.history['loss'], label = "loss")
plt.legend()
