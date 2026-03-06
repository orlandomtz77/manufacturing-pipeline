import sqlite3
import pandas as pd
import os
base_dir = os.path.dirname(os.path.abspath(__file__))
conn = sqlite3.connect(f'{base_dir}/manufacturing.db')
query = """SELECT 
    machine_id,
    AVG(oee) as avg_oee,
    AVG(availability) as avg_availability,
    AVG(quality) as avg_quality
FROM production_facts
GROUP BY machine_id
ORDER BY avg_oee DESC"""
query2 = """SELECT 
    machine_id,
    oee,
    RANK() OVER (ORDER BY oee DESC) as oee_rank,
    AVG(oee) OVER () as global_avg_oee
FROM production_facts"""
query3 = '''WITH machine_avg AS (
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
df2 = pd.read_sql_query(query2,conn)
df3 = pd.read_sql_query(query3,conn)

print(df)
print(df2)
print(df3)