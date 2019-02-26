import pandas as pd
import sqlalchemy as db
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import inspect
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

le = LabelEncoder()
# ohe = OneHotEncoder(handle_unknown='ignore')

file = 'historical_transactions.csv'
file2 = 'merchants.csv'
file3 = 'new_merchant_transactions.csv'
csv_database = create_engine('sqlite:///csv_database.db')
# where "city_id"=307'

# df = pd.read_sql_query('select distinct category_2 from "table" order by month_lag asc', csv_database)
# print(df)

# df = pd.read_sql_query('select max(purchase_date) from "table"', csv_database)
# print(df)

# creates dataframe with columns city_id and city_encoded, with the transition encoding transition for the given cities
# df = pd.read_sql_query('select card_id, city_id from "table" order by city_id asc', csv_database)
# df['city_encoded']=le.fit_transform(df.city_id)
# print(df)

# df = pd.read_sql_query('select distinct city_id from "table" order by city_id asc', csv_database)
# df['city_encoded']=le.fit_transform(df.city_id)
# print(df)

# get all numerical values from historical transactions given a card_id = cid
# this is how you iterate through the database based on card_id
cid = 'C_ID_4e6213e9bc'

# df = pd.read_sql_query('''select avg(installments) as installments,
#     max(installments) as maxInstallments,
#     min(installments) as minInstallments,
#     min(month_lag) as minMonthLag,
#     max(month_lag) as maxMonthLag,
#     avg(month_lag) as monthLag,
#     avg(purchase_amount) as purchaseAmount,
#     count(purchase_amount) as purchases

#     from "table" where "card_id" like ?'''
#     , csv_database, params=(cid,))
# print(df)

df = pd.read_sql_query('''select max(city_id) as city_id,
    max(category_1) as category_1,
    max(category_3) as category_3,
    max(merchant_category_id) as max_merchant_category,
    max(category_2) as category_2,
    max(state_id) as home_state,
    max(subsector_id) as home_sector,
    min(purchase_date) as start_date,
    max(purchase_date) as end_date
    from "table" where "card_id" like ?'''#group by card_id
    , csv_database, params=(cid,))
df = df.values
df=df[0]
print(df)
