import pandas as pd

df = pd.read_csv('data/synthetic_online_retail_data.csv')
df['gender'] = df['gender'].fillna('N/A')
df['review_score'] = df['review_score'].fillna('N/A')

df_groupby = df.groupby(['category_name', 'product_name']).agg({
    'price': 'sum',
    'quantity': 'sum'
}).reset_index().rename(columns={'price': 'total price', 'customer_id':'qtd total'})

df_pivot_table = pd.pivot_table(df, 
               values=['price', 'quantity'],
               index=['product_name'],
               columns='gender',
               aggfunc={'price': 'sum', 'quantity': 'sum'},
               fill_value=0
               ).reset_index()