import sqlite3
import pandas as pd

#Reading DataBase
with sqlite3.connect('chinook.db') as con:
    customers = pd.read_sql("SELECT * FROM customers", con)
    invoices = pd.read_sql("SELECT * FROM invoices", con)
    
#Merging DataBase via CustomerID
    
merged=pd.merge(customers,invoices,on='CustomerId',how='inner') #returns series and assigns to merged

#groupby name and find all invoices
total_invoices=merged.groupby(['CustomerId','FirstName','LastName'])['InvoiceId'].count().reset_index()
total_invoices.rename(columns={'InvoiceId': 'TotalInvoices'}, inplace=True)
print(total_invoices.sort_values(by='TotalInvoices', ascending=False))