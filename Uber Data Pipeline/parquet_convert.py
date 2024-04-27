import pandas as pd

df = pd.read_parquet('data/fhv_tripdata_2016-01.parquet')
df.to_csv('fhv_tripdata_2016-01.csv')