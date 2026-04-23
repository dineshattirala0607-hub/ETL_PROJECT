import pyodbc
import pandas as pd

# 🔹 Connection
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"   # change if needed
    "DATABASE=AdventureWorks2016;"  # change this
    "Trusted_Connection=yes;"
)

# 🔹 Step 1: Extract
df = pd.read_sql("SELECT * FROM HumanResources.Source1", conn)
print("Source Data:")
print(df)

# 🔹 Step 2: Transform
df['Name_Upper'] = df['Name'].str.upper()

# 🔹 Step 3: Load
cursor = conn.cursor()

for index, row in df.iterrows():
    cursor.execute("""
        INSERT INTO HumanResources.Target1 (CustomerID, Name, City, Name_Upper)
        VALUES (?, ?, ?, ?)
    """, row.customerID, row.Name, row.city, row.Name_Upper)

conn.commit()
conn.close()

print("ETL Completed Successfully to Dinesh Test")