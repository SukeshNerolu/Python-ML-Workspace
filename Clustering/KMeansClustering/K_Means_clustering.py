import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.cluster import KMeans 
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_samples, silhouette_score
# %matplotlib inline - specific to jupyter notebook

data_df = pd.read_csv(r'C:\Users\sukesh.nerolu\Desktop\Python-workspace\Python-ML-Workspace\Clustering\KMeansClustering\Cust_Spend_Data_New.csv')

print("Data head: 5 rows", data_df.head(5))
print("Shape of the data: ", data_df.shape)
print("data types: ", data_df.dtypes)
print("data information: ", data_df.info())
print("data description: ", data_df.describe())
print("duplicate data: ", data_df.duplicated().sum())

cust_df = data_df.drop(['Name','Cust_ID'], axis=1)

print(cust_df.head()) # after drop

X = StandardScaler()
scaled_df = X.fit_transform(cust_df)

print(scaled_df)

k_means2 = KMeans(n_clusters = 2)

print(k_means2.fit(scaled_df))

print(k_means2.labels_)

print(k_means2.inertia_)

k_means3 = KMeans(n_clusters = 3)
print(k_means3.fit(scaled_df))
print(k_means3.inertia_)

k_means4 = KMeans(n_clusters = 4)
print(k_means4.fit(scaled_df))
print(k_means4.inertia_)

k_means1 = KMeans(n_clusters = 1)
print(k_means1.fit(scaled_df))
print(k_means1.inertia_)

k_means5 = KMeans(n_clusters = 5)
print(k_means5.fit(scaled_df))
print(k_means5.inertia_)

k_means6 = KMeans(n_clusters = 6)
print(k_means6.fit(scaled_df))
print(k_means6.inertia_)


wss =[] 
for i in range(1,11):
    KM = KMeans(n_clusters=i)
    KM.fit(scaled_df)
    wss.append(KM.inertia_)

print(wss)

for i in range(1,11):
    KM = KMeans(n_clusters=i)
    KM.fit(scaled_df)
    wss.append(KM.inertia_)

print(wss)

plt.plot(range(1,11), wss)

k_means = KMeans(n_clusters = 3)
k_means.fit(scaled_df)
labels = k_means.labels_

data_df["Clus_kmeans"] = labels
print(data_df.head(5))

#silhout -sklearn library import
print(silhouette_score(scaled_df,labels))

sil_width = silhouette_samples(scaled_df,labels)

data_df["sil_width"] = sil_width
print(data_df.head(5))

print(silhouette_samples(scaled_df,labels).min())

# data_df.to_csv('km.csv')





