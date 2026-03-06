import pandas as pd
import os
base_dir = os.path.dirname(os.path.abspath(__file__))
raw_path = os.path.join(os.path.join(base_dir,'..','data/raw'))
processed_path = os.path.join(os.path.join(base_dir,'..','data/processed'))

df = pd.read_csv(f'{raw_path}/production_data.csv')
df['good_units'] = df['units_produced'] - df['defects']
df['availability'] = ((480 -df['downtime_minutes'])/480).round(2)
df['quality'] = (df['good_units']/df['units_produced']).round(2)
df['oee'] = (df['availability']*df['quality']).round(2)
df['oee'] = df['oee'].fillna(0)
df['quality'] = df['quality'].fillna(0)
df.to_csv(f'{processed_path}/production_clean.csv',index=False)