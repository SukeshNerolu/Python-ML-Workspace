# Hierarchical Clustering:

## Definition:
Hierarchical clustering is a type of clustering algorithm that builds a hierarchy of clusters. It starts by treating each data point as a singleton cluster and iteratively merges or divides clusters until a desired clustering structure is obtained. The result is a tree-based representation of the data, known as a dendrogram.

## Why it is required:

Exploratory Analysis: Hierarchical clustering is useful for exploring the inherent structure within a dataset, grouping similar data points together.
Taxonomy Construction: In biology or taxonomy, hierarchical clustering is used to create hierarchical classifications of species based on shared characteristics.
Data Compression: It can be used for summarizing and compressing data by representing groups of similar data points with a single cluster.
## Where it is applicable:

Biology: In genomics to group genes with similar expression patterns.
Marketing: For customer segmentation based on purchasing behavior.
Image Analysis: In computer vision to group similar images.
Document Clustering: To group similar documents together.

## Important Libraries:

scikit-learn: Provides a AgglomerativeClustering class for hierarchical clustering.
SciPy: Offers a linkage function to perform hierarchical clustering and a dendrogram function for visualizing the results.
seaborn, matplotlib: Used for visualization.

## Explain
wardlink = linkage(data, method = 'ward')
dend = dendrogram(wardlink)

The linkage function is part of the SciPy library and is commonly used for hierarchical clustering. It computes the linkage matrix based on the specified method. In this case, the method is set to 'ward', which uses the Ward variance minimization algorithm. The data variable likely contains the input data for clustering.
The dendrogram function is used to visualize the hierarchical clustering result. It takes the linkage matrix (wardlink in this case) as input and generates a dendrogram, which is a tree diagram representing the arrangement of the clusters.

## clusters1 = fcluster(wardlink, 3, criterion='maxclust')
The fcluster function in the SciPy library is used for flat clustering, which means it directly assigns data points to clusters based on a specified criterion.
wardlink: This variable likely contains the linkage matrix computed using hierarchical clustering, particularly the Ward method.
3: This parameter specifies the number of clusters. In this case, it is set to 3, meaning you want to create three clusters.
criterion='maxclust': The criterion parameter specifies how to determine the number of clusters. Here, it is set to 'maxclust', indicating that the number provided (in this case, 3) is the maximum number of clusters.

## clusters2 = fcluster(wardlink, 23, criterion='distance')
wardlink: This variable likely contains the linkage matrix computed using hierarchical clustering, particularly the Ward method.
23: This parameter specifies a threshold distance. The fcluster function will assign data points to clusters based on this distance criterion. Data points that are within this distance will be grouped into the same cluster.
criterion='distance': The criterion parameter is set to 'distance', indicating that the provided threshold is a distance value, and data points will be assigned to clusters based on their distances with respect to this threshold.

## Interview Questions:

<!-- How does hierarchical clustering work?
Explain the concept of linkage in hierarchical clustering.
What is the difference between agglomerative and divisive hierarchical clustering?
Can you mention some distance metrics used in hierarchical clustering?
When would you choose hierarchical clustering over k-means clustering?
How do you determine the number of clusters in hierarchical clustering?
Discuss some applications of hierarchical clustering in real-world scenarios. -->

### How does hierarchical clustering work?

Hierarchical clustering starts by considering each data point as a separate cluster. It then iteratively merges the closest clusters based on a chosen linkage criterion (e.g., complete, average, or ward linkage). This process continues until all data points belong to a single cluster, forming a tree-like structure known as a dendrogram.

### Explain the concept of linkage in hierarchical clustering.

Linkage is the criterion used to measure the distance between two clusters when deciding which clusters to merge. Different linkage methods include:

Single Linkage: Distance between the closest elements of the two clusters.
Complete Linkage: Distance between the farthest elements of the two clusters.
Average Linkage: Average distance between all pairs of elements from the two clusters.
Ward's Linkage: Minimizes the variance within each cluster.

### What is the difference between agglomerative and divisive hierarchical clustering?

Agglomerative: Starts with individual data points as clusters and merges them iteratively.
Divisive: Starts with all data points in a single cluster and divides it into smaller clusters at each step.

### Can you mention some distance metrics used in hierarchical clustering?

Common distance metrics include:

Euclidean Distance: Straight-line distance between two points.
Manhattan Distance: Sum of absolute differences between the coordinates.
Cosine Similarity: Measures the cosine of the angle between two vectors.
Correlation Distance: Measures the Pearson correlation coefficient between two variables.

### When would you choose hierarchical clustering over k-means clustering?

Hierarchical Clustering: Preferred when the data has a hierarchical structure, and you are interested in understanding the relationships at different levels. Also suitable when the number of clusters is not known in advance.
K-means Clustering: Suitable for well-defined, spherical clusters when the number of clusters is known.

### How do you determine the number of clusters in hierarchical clustering?

The number of clusters is determined from the dendrogram by observing the vertical lines (branches) where the heights (distances) are significant. The number of clusters is often chosen by cutting the dendrogram at a certain height or by using other criteria, such as the elbow method.

### Discuss some applications of hierarchical clustering in real-world scenarios.

Biology: Grouping genes with similar expression patterns.
Marketing: Customer segmentation based on purchasing behavior.
Image Analysis: Grouping similar images.
Document Clustering: Grouping similar documents together.