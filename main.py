from PIL import Image
import numpy as np
from sklearn.cluster import KMeans


image_path="testimg.png"
image=Image.open(image_path)

'''
Opening an image 
with the Pillow module.
'''

image_array=np.array(image)

'''Converts the image to a 3D Array, where a 2D array is used to store the pixel, and element of each 2D array
is a 4 element array having the RGBA vales
'''
flattened_pixels = image_array.reshape(-1,3) 

'''flattens the 3D array into a 2D array, after ignoring the last A value'''

#print(flattened_pixels)

'''Implementing K-Means Clustering Algorithm using SKLearn Library'''

num_clusters=18

'''Using 18 colors for compression'''

kmeans=KMeans(n_clusters=num_clusters,random_state=0)
kmeans.fit(flattened_pixels)

'''Getting the cluster assignments for each pixel'''

cluster_assignments=kmeans.predict(flattened_pixels)
centroids=kmeans.cluster_centers_


#print(cluster_assignments)
#print(centroids)

compressed_image_array=centroids[cluster_assignments].reshape(image_array.shape)
'''Replaces all instances of the pixels with their cluster centroids'''


compressed_image=Image.fromarray(np.uint8(compressed_image_array))
'''Constructs image from array'''

compressed_image.save("compressed_image.png")
compressed_image.show()

