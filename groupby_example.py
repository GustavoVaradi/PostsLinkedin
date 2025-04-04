import pandas as pd

df = pd.read_csv('data/synthetic_online_retail_data.csv')
df['gender'] = df['gender'].fillna('NDG')
df['review_score'] = df['review_score'].fillna('N/A')