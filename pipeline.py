import pandas as pd
import sqlite3

# Load CSV
df = pd.read_csv('data/sample.csv')

# Basic cleaning
df.dropna(inplace=True)

# Connect to database
conn = sqlite3.connect('database.db')

# Load into SQL
df.to_sql('data_table', conn, if_exists='replace', index=False)

print("Data loaded into SQL database!")

conn.close()