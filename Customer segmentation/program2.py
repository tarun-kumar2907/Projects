import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings('ignore')

from google.colab import files
uploaded = files.upload()

dframe = pd.read_excel("Dataset.xlsx")
dframe.head()

dframe.describe()

sns.distplot(dframe['Monthly_Income_Rs']);

dframe.columns

columns = ['Age', 'Monthly_Income_Rs','Spending_Score']
for i in columns:
    plt.figure()
    sns.distplot(dframe[i])

sns.kdeplot(dframe['Monthly_Income_Rs'],shade=True,hue=dframe['Gender']);

columns = ['Age', 'Monthly_Income_Rs','Spending_Score']
for i in columns:
    plt.figure()
    sns.kdeplot(dframe[i],shade=True,hue=dframe['Gender'])

columns = ['Age', 'Monthly_Income_Rs','Spending_Score']
for i in columns:
    plt.figure()
    sns.boxplot(data=dframe,x='Gender',y=dframe[i])

dframe['Gender'].value_counts(normalize=True)

sns.scatterplot(data=dframe, x='Monthly_Income_Rs',y='Spending_Score' )

sns.pairplot(dframe,hue='Gender')
dframe.groupby(['Gender'])['Age', 'Monthly_Income_Rs',
       'Spending_Score'].mean()

dframe.corr()

sns.heatmap(dframe.corr(),annot=True,cmap='coolwarm')

sns.scatterplot(data=dframe, x='Monthly_Income_Rs',y='Spending_Score' )

sns.pairplot(dframe,hue='Gender')

dframe.groupby(['Gender'])['Age', 'Monthly_Income_Rs',
       'Spending_Score'].mean()

dframe.corr()

sns.heatmap(dframe.corr(),annot=True,cmap='coolwarm')

clustering1 = KMeans(n_clusters=3)

clustering1.fit(dframe[['Monthly_Income_Rs']])

clustering1.labels_

dframe['Income Cluster'] = clustering1.labels_
dframe.head()

dframe['Income Cluster'].value_counts()

clustering1.inertia_

intertia_scores=[]
for i in range(1,11):
    kmeans=KMeans(n_clusters=i)
    kmeans.fit(dframe[['Monthly_Income_Rs']])
    intertia_scores.append(kmeans.inertia_)

intertia_scores

plt.plot(range(1,11),intertia_scores)

dframe.columns

dframe.groupby('Income Cluster')['Age', 'Monthly_Income_Rs',
       'Spending_Score'].mean()

clustering2 = KMeans(n_clusters=5)
clustering2.fit(dframe[['Monthly_Income_Rs','Spending_Score']])
dframe['Spending and Income Cluster'] =clustering2.labels_
dframe.head()

intertia_scores2=[]
for i in range(1,11):
    kmeans2=KMeans(n_clusters=i)
    kmeans2.fit(dframe[['Monthly_Income_Rs','Spending_Score']])
    intertia_scores2.append(kmeans2.inertia_)
plt.plot(range(1,11),intertia_scores2)

centers =pd.DataFrame(clustering2.cluster_centers_)
centers.columns = ['x','y']

plt.figure(figsize=(10,8))
plt.scatter(x=centers['x'],y=centers['y'],s=100,c='black',marker='*')
sns.scatterplot(data=dframe, x ='Monthly_Income_Rs',y='Spending_Score',hue='Spending and Income Cluster',palette='tab10')
plt.savefig('clustering_bivaraiate.png')

pd.crosstab(dframe['Spending and Income Cluster'],dframe['Gender'],normalize='index')

dframe.groupby('Spending and Income Cluster')['Age', 'Monthly_Income_Rs',
       'Spending_Score'].mean()

from sklearn.preprocessing import StandardScaler

scale = StandardScaler()

dframe.head()

dff = pd.get_dummies(dframe,drop_first=True)
dff.head()

dff.columns
dff = dff[['Age', 'Monthly_Income_Rs', 'Spending_Score','Gender_Male']]
dff.head()
dff = scale.fit_transform(dff)
dff = pd.DataFrame(scale.fit_transform(dff))
dff.head()
intertia_scores3=[]
for i in range(1,11):
    kmeans3=KMeans(n_clusters=i)
    kmeans3.fit(dff)
    intertia_scores3.append(kmeans3.inertia_)
plt.plot(range(1,11),intertia_scores3)

dframe

dframe.to_csv('Clustering.csv')
