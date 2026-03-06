import sqlite3
import pandas as pd
import os
base_dir = os.path.dirname(os.path.abspath(__file__))
processed_path = os.path.join(os.path.join(base_dir,'..','data/processed'))
df = pd.read_csv(f'{processed_path}/production_clean.csv')
conn = sqlite3.connect(f'{base_dir}/manufacturing.db')
df.to_sql('production_facts',conn,if_exists='replace',index=False)