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
df = pd.read_sql_query('''select card_id
            max(city_id) as city_id, 
            max(category_1) as category_1, 
            max(category_3) as category_3,
            max merchant_category_id as most_common_merchant_cat,
            date(max(purchase_date)) as last_date,
            date(min(purchase_date)) as first_date,
            max(category_2) as category_2,
            from "table" group by "card_id"
            order by "card_id" asc '''
            , csv_database)