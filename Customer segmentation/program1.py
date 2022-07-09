!pip install xlrd
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from google.colab import files
uploaded = files.upload()

df = pd.read_excel('online_retail_II.xlsx')
df = df[df['Customer ID'].notna()]
df_fix = df.sample(10000, random_state = 42)

from datetime import datetime
df_fix['InvoiceDate'] = pd.to_datetime(df.InvoiceDate, format='%d-%m-%y %H:%M:%S')
df_fix["TotalSum"] = df_fix["Quantity"] * df_fix["Price"]
import datetime
snapshot_date = max(df_fix.InvoiceDate) + datetime.timedelta(days=1)
customers = df_fix.groupby(['Customer ID']).agg({
    'InvoiceDate': lambda x: (snapshot_date - x.max()).days,
    'Invoice': 'count',
    'TotalSum': 'sum'})
customers.rename(columns = {'InvoiceDate': 'Recency',
                            'Invoice': 'Frequency',
                            'TotalSum': 'MonetaryValue'}, inplace=True)

customers

from scipy import stats
customers_fix = pd.DataFrame()
customers_fix["Recency"] = stats.boxcox(customers['Recency'])[0]
customers_fix["Frequency"] = stats.boxcox(customers['Frequency'])[0]
customers_fix["MonetaryValue"] = pd.Series(np.cbrt(customers['MonetaryValue'])).values
customers_fix.tail()

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(customers_fix)
customers_normalized = scaler.transform(customers_fix)
print(customers_normalized.mean(axis = 0).round(2)) 
print(customers_normalized.std(axis = 0).round(2)) 

df1 = pd.DataFrame(customers_normalized)
df1

#Modelling

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
sse = {}
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(customers_normalized)
    sse[k] = kmeans.inertia_ 
plt.title('The Elbow Method')
plt.xlabel('k')
plt.ylabel('SSE')
sns.pointplot(x=list(sse.keys()), y=list(sse.values()))
plt.show()

model = KMeans(n_clusters=3, random_state=42)
model.fit(customers_normalized)
model.labels_.shape

customers["Cluster"] = model.labels_
customers.groupby('Cluster').agg({
    'Recency':'mean',
    'Frequency':'mean',
    'MonetaryValue':['mean', 'count']}).round(2)

df_normalized = pd.DataFrame(customers_normalized, columns=['Recency', 'Frequency', 'MonetaryValue'])
df_normalized['ID'] = customers.index
df_normalized['Cluster'] = model.labels_
df_nor_melt = pd.melt(df_normalized.reset_index(),
                      id_vars=['ID', 'Cluster'],
                      value_vars=['Recency','Frequency','MonetaryValue'],
                      var_name='Attribute',
                      value_name='Value')
df_nor_melt.head()
sns.lineplot('Attribute', 'Value', hue='Cluster', data=df_nor_melt)

