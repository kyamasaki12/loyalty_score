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

# df = pd.read_sql_query('''select card_id,
#             max(city_id) as city_id, 
#             max(category_1) as category_1, 
#             max(category_3) as category_3,
#             max(merchant_category_id) as most_common_merchant_cat,
#             date(max(purchase_date)) as last_date,
#             date(min(purchase_date)) as first_date,
#             max(category_2) as category_2,
#             max(state_id) as state_id,
#             max(subsector_id) as subsector_id
             
#             from "table" group by "card_id"
#             having 
#             order by "card_id" asc '''
#             , csv_database)
df_train = pd.read_sql_query('''
    select merchant_id, merchant_group_id, merchant_category_id,
    subsector_id, numerical_1, numerical_2, category_1,
    most_recent_sales_range, most_recent_purchases_range,
    avg_sales_lag3,avg_purchases_lag3,active_months_lag3,avg_sales_lag6,
    avg_purchases_lag6,active_months_lag6,avg_sales_lag12,avg_purchases_lag12,
    active_months_lag12,category_4,city_id,state_id,category_2
    from merchants
    order by "merchant_id"
''')

df = pd.read_sql_query('''
    select card_id, city_id
    from "table"
    where "card_id"= "C_ID_5037ff576e" group by "card_id"

''',
csv_database)
print(df)

# select card_id, max(city_id), city_id,
#             max(category_1), category_1,
#             max(category_3), category_3,
#             max(merchant_category_id), merchant_category_id,
#             date(max(purchase_date)) as last_date,
#             date(min(purchase_date)) as first_date,
#             max(category_2), category_2,
#             max(state_id), state_id,
#             max(subsector_id), subsector_id

