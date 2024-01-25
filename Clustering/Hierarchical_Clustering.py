'''Hierarchical_clustering of nutrient composition'''

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

df=pd.read_csv('Nutrient_Composition_Dataset.csv')

df.head()

# # Function to log DataFrame head
# def log_dataframe_head(dataframe, logger, rows=5, level=logging.INFO):
#     dataframe_head_str = dataframe.head(rows).to_string(index=False)
#     logger.log(level, "\n" + dataframe_head_str)

# # Log the head of the DataFrame
# log_dataframe_head(df, logger)

