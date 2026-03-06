import pandas as pd
import random
import os
from faker import Faker

fake = Faker()
unidades_producidas = [random.randint(0,565) for _ in range(1000)]
datos = {
    'operator_id': [fake.unique.random_int(min=1000, max = 9999) for _ in range(1000)],
    'machine_id': [fake.bothify('MACH-##') for _ in range(1000)],
    'product_id': [fake.bothify('SKU-###') for _ in range(1000)],
    'units_produced':unidades_producidas,
    'defects':[random.randint(0,unidades_producidas[i]) for i in range(1000)],
    'downtime_minutes': [random.randint(0,480) for _ in range(1000)],
    'timestamp':[fake.date_this_year() for _ in range(1000)]
}
df = pd.DataFrame(datos)
current_dir = os.path.dirname(os.path.abspath(__file__))
config_dir = os.path.join(current_dir,'..','data/raw')
normalized_path = os.path.normpath(config_dir)
df.to_csv(f'{normalized_path}/production_data.csv',index=False)