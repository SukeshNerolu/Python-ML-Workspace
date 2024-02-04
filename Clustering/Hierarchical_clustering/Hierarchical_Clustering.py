'''Hierarchical_clustering of nutrient composition'''

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import logging
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster.hierarchy import fcluster

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

df = pd.read_csv(r'C:\Users\sukesh.nerolu\Desktop\Python-workspace\Python-ML-Workspace\Clustering\Nutrient_Composition_Dataset.csv')

print(df.head())
print(df.iloc[:,1:5].describe())
'''# # Function to log DataFrame head using logger
# def log_dataframe_head(dataframe, logger, rows=5, level=logging.INFO):
#     dataframe_head_str = dataframe.head(rows).to_string(index=False)
#     logger.log(level, "\n" + dataframe_head_str)

# # Log the head of the DataFrame
# log_dataframe_head(df, logger)'''
data = df.iloc[:,1:5]
print(data.head())

#Clustering
wardlink = linkage(data, method = 'ward')
dend = dendrogram(wardlink)
# Show the dendrogram
# plt.show()

dend = dendrogram(wardlink,
                 truncate_mode='lastp',
                 p = 10,
                 )
# plt.show()

#Method 1
clusters1 = fcluster(wardlink, 3, criterion='maxclust')
print("Method-1:clusters",clusters1)

# Method 2

clusters2 = fcluster(wardlink, 23, criterion='distance')
print("Method-2:clusters",clusters2)

df['clusters'] = clusters2
print("Cluster dataframe")
print(df.head())

# df.to_csv('hc.csv')