import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

data = pickle.load( open( "train.p", "rb" ) )

yset = pickle.load( open( "yset.p", "rb" ) )

# print(len(data))
# print(len(yset))
# do some stuff here, dictionaries to arrays
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
	# print ("%s: %s" , (key, yset[key]))
# for key, value in sorted(data.iteritems(), key=lambda (k,v): (v,k)):
# 	result.append(key);
# # SO again for yset

# print(result)
data_values=np.array(data_values)
y_vals=np.array(y_vals)
# print(data_values.shape)
# print(y_vals.shape)

# #'''select card_id,
#             avg(installments) as installments,
#             max(installments) as maxInstallments,
#             min(installments) as minInstallments,
#             min(month_lag) as minMonthLag,
#             max(month_lag) as maxMonthLag,
#             avg(month_lag) as monthLag,
#             avg(purchase_amount) as purchaseAmount,
#             count(purchase_amount) as purchases
#             from "table" group by "card_id"
#             order by "card_id" asc '''

avg_installments = [];


for row in data_values:
	avg_installments.add(row[0])



X_train, X_test, y_train, y_test = train_test_split(data_values[][1], y_vals, test_size=0.33, random_state=1)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)
reg = LinearRegression().fit(X_train,y_train)
print(reg.score(X_train,y_train))




