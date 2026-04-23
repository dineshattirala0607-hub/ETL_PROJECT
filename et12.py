import pyodbc
import pandas as pd

# ==============================
# 1. READ CSV FILE
# ==============================
df = pd.read_csv("Book1.csv")

print("CSV Data:")
print(df) 

# ==============================
# 2. CONNECT TO SQL SERVER
# ==============================
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=AdventureWorks2016;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

# ==============================
# 3. INSERT DATA (FAST)
# ==============================
data = df.values.tolist()

cursor.executemany("""
    INSERT INTO HumanResources.Pappendra (Empid,Name,State,Company,Role)
    VALUES (?, ?, ?, ?, ?)
""", data)

conn.commit()
cursor.close()
conn.close()

print("✅ Data Ingested Successfully to Dinesh Test2")