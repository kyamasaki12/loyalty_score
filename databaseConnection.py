import pandas as pd
import sqlalchemy as db
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import inspect

file = 'historical_transactions.csv'
file2 = 'merchants.csv'
file3 = 'new_merchant_transactions.csv'
file4 = 'train.csv'
# print(pd.read_csv(file, nrows=5))

csv_database = create_engine('sqlite:///csv_database.db')
# print(csv_database.table_names())
# metadata = MetaData(csv_database) # metadata for engine csv_database
# inspector = inspect(csv_database)
# print(inspector.get_columns('table'))
chunksize = 100000
i = 0
j = 1
# for df in pd.read_csv(file, chunksize=chunksize, iterator=True):
#       df = df.rename(columns={c: c.replace(' ', '') for c in df.columns}) 
#       df.index += j
#       i+=1
#       df.to_sql('table', csv_database, if_exists='append')
#       j = df.index[-1] + 1
#       print(df)

# for df in pd.read_csv(file2, chunksize=chunksize, iterator=True):
#       df = df.rename(columns={c: c.replace(' ', '') for c in df.columns}) 
#       df.index += j
#       i+=1
#       df.to_sql('merchants', csv_database, if_exists='append')
#       j = df.index[-1] + 1
#       print(df)

# for df in pd.read_csv(file3, chunksize=chunksize, iterator=True):
#       df = df.rename(columns={c: c.replace(' ', '') for c in df.columns}) 
#       df.index += j
#       i+=1
#       df.to_sql('newmerchants', csv_database, if_exists='append')
#       j = df.index[-1] + 1
#       print(df)

# metadata = MetaData(csv_database) # metadata for engine csv_database
df = pd.read_sql_query('select AVG(installments) AS installments from "table" where "city_id"=307', csv_database)
print(df.ix[0,'installments'])
df = pd.read_sql_query('select COUNT(merchant_group_id) AS merchant_group_id from "merchants" where "city_id"=307', csv_database)
# print(df)
print(df.ix[0,'merchant_group_id'])
df = pd.read_sql_query('select MAX(authorized_flag) AS authorized_flag from "newmerchants" where "city_id"=307', csv_database)
# print(df)
print(df.ix[0,'authorized_flag'])