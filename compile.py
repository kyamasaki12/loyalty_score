import csv
import pandas as pd
import sqlalchemy as db
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import inspect
import numpy as np
import pickle
from sklearn import preprocessing


file = 'historical_transactions.csv'
csv_database = create_engine('sqlite:///csv_database.db')
ySet={}
dataSet= {}
merchantDetails={}
rowTrain = 0
rowsHist = 0
rowsMerch = 0
rowsNewMerch = 0

pd.read_csv('train.csv', )
# df = array for transactions
df = pd.read_sql_query('''select card_id,
            avg(installments) as installments,
            max(installments) as maxInstallments,
            min(installments) as minInstallments,
            min(month_lag) as minMonthLag,
            max(month_lag) as maxMonthLag,
            avg(month_lag) as monthLag,
            avg(purchase_amount) as purchaseAmount,
            count(purchase_amount) as purchases
            from "table" group by "card_id"
            order by "card_id" asc '''
            , csv_database)#, params=(cid,))
# print(df)
df = df.values
print("done with sqlquery")
# print(df[0][0])
# print(df[0][1])
# create trainTemp
df_i = []
counter = 0
with open('train.csv') as trainFile:
    tempReader = csv.reader(trainFile)
    for row in tempReader:
        counter +=1
        print("row = ",counter)
        print(row)
        
        if rowTrain != 0:
            cid = row[1]
            df_i = [0]
            for i in df:
                # print("i is:")
                # print(i)
                if i[0]==cid:
                    df_i = i
                    df_i = df_i[1:]
                    break
            dataSet.update({cid:df_i})
            ySet.update({cid:row[5]})
        rowTrain += 1
        # if row[1] in dataSet.keys():
        #     print(dataSet[row[1]])
print(dataSet)
# print(ySet)

with open('train.p', 'wb') as handle:
    pickle.dump(dataSet, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('yset.p', 'wb') as handle:
    pickle.dump(ySet, handle, protocol=pickle.HIGHEST_PROTOCOL)

# with open('train.p', 'rb') as handle:
#     b = pickle.load(handle)

# print(dataSet)
# create merchants file
# with open('merchants.csv') as tempFile:
#     tempReader = csv.reader(tempFile)
#     for row in tempReader:
#         if rowsMerch != 0:
#             # do this
#             merchantDetails.update(row[0]:[row[1], row[2], row[3], row[4], row[5],
#             row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13],
#             row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21],])
#         rowsMerch += 1
    
# create histTrans
# with open('historical_transactions.csv') as tempFile:
#     tempReader = csv.reader(tempFile)
#     for row in tempReader:
#         if rowsHist != 0:
#             if row[0] == 'Y':
#                 row[0] = 1
#             else:
#                 row[0] = 0
            


#         rowsHist +=1    
# for row in histTrans:
#     rows += 1
#     # print(row)
# print(rows)
# print(histTrans)
# create newMerchTrans
# with open('new_merchant_transactions.csv') as tempFile:
#     tempReader = csv.reader(tempFile)
#     newMerchTrans = list(tempReader)


# 