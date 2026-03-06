import sqlite3
import pandas as pd
import os
base_dir = os.path.dirname(os.path.abspath(__file__))
ware_path = os.path.join(os.path.join(base_dir,'..','warehouse'))
processed_path = os.path.join(os.path.join(base_dir,'..','data/processed'))
conn = sqlite3.connect(f'{ware_path}/manufacturing.db')
query = '''WITH machine_avg AS (
    SELECT 
        machine_id,
        AVG(oee) as avg_oee
    FROM production_facts
    GROUP BY machine_id
)
SELECT 
    machine_id,
    avg_oee,
    CASE 
        WHEN avg_oee >= 0.70 THEN 'Bueno'
        WHEN avg_oee >= 0.40 THEN 'Regular'
        ELSE 'Crítico'
    END as estado
FROM machine_avg
ORDER BY avg_oee DESC'''

df = pd.read_sql_query(query,conn)
df['avg_oee'] = df['avg_oee'].round(2)
df.to_csv(f'{processed_path}/machine_summary.csv',index=False)