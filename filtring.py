
import pandas as pd
from sqlalchemy import create_engine, text
###
# Connexion à la base de données MySQL
engine = create_engine('mysql+pymysql://root:@localhost/ocpdb')

# 1. Fusionner les deux tables en une nouvelle table
# Supposons que les tables sont `table1` et `table2`, et qu'elles ont un champ commun `id`
merge_query = """
    CREATE TABLE IF NOT EXISTS merged_table AS
    SELECT t1.Nom, t2.niveau, t1.numero
    FROM agents t1
    JOIN demandes t2 ON t1.Nom = t2.Nom
"""
with engine.connect() as conn:
    conn.execute(text(merge_query))

# 2. Lire les données de la nouvelle table et les filtrer selon les types de vue
# Lire toutes les données de la table fusionnée
query = "SELECT * FROM merged_table"
df = pd.read_sql(query, con=engine)

# Filtrer et trier les données par type de vue et coefficient
# Supposons que `type_vue` est le champ du type de vue et `coefficient` est le champ à trier
types_vue = df['niveau'].unique()
sorted_dfs = {type_vue: df[df['niveau'] == type_vue].sort_values(by='numero', ascending=False) for type_vue in types_vue}

# 3. Exporter les données filtrées et triées dans un fichier Excel
output_file = r'C:\Users\PC\Desktop\MergedDataFiltered.xlsx'
with pd.ExcelWriter(output_file) as writer:
    for type_vue, sorted_df in sorted_dfs.items():
        sorted_df.to_excel(writer, sheet_name=type_vue, index=False)

print("Données exportées avec succès vers le fichier Excel.")

###
