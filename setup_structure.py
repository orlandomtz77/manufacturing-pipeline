import os
carpetas = ['data','ingestion','transformation','warehouse','reporting','data/raw','data/processed']
for carpeta in carpetas:
    os.makedirs(carpeta,exist_ok=True)
    print(f"Carpeta: '{carpeta}' creada o ya existente")