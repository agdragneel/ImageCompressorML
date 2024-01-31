# ImageCompressorML
A Python Program that takes an image file as input and compresses it by changing it's quality using the K-Means Unsupervised Clustering Algorithm.

The image file converts the Image into an array of pixels, where each pixel is converted into an RGB Value.
Then, the K-Means clustering algorithm is used to find 16 clusters with 16 centroids.
Then, we replace each pixel with the value of the centroid of the cluster it belongs in.

This effectively reduces the number of unique colors in the image, thereby achieving compression but sacrificing quality.
The number of clusters is fixed to 16, but on changing the number of clusters, we can achieve different compression percentage, and different qualities.

A graph of NumberOfClusters(X-axis) and Compression Percentage(Y-axis) has been added for reference.

