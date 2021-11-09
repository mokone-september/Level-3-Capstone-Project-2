import matplotlib.pyplot as plt
import numpy as np
import csv
from sklearn.metrics import pairwise_distances_argmin
from collections import Counter, defaultdict

# Code section for K-Means clustering implementation


    '''The k-means clustering algorithm pseudocode 

input: Data points, axis_x and axis_y, Number of cluster, cluster_number
Step 1: Initialize cluster_number centroids randomly
Step 2: Associate each data point in axis_x and axis_y with the nearest centroid. Ths will divide the data points into cluster_numbers
Step 3: Recalculate the positions of the centroids 
Reapeat steps 2 and 3 until there are no more changes in the membership of the data points 
Output: Data points with cluster membership

Reference: Dilpreet Singh and Chandan K. Reddy, “A Survey on Platforms for Big Data 
Analytics”, Journal of Big Data, 1:1, 8, 2014.  
 

Further reading reference and related links used for research purposes to the following source code: https://stanford.edu/~cpiech/cs221/handouts/kmeans.html'''



# User input for the number of clusters 
cluster_number = int(input("Provide a cluster number: "))


# Code section function that reads data in from the csv file
def csv_read_function():
    axis_x = []
    axis_y = []
    countries = []
    axis_x_label = ""
    axis_y_label = ""
    with open('dataBoth.csv') as file_csv:
        reader = csv.reader(file_csv, delimiter=',')
        lines = 0
        for row in reader:
            if lines >= 1:
                print(', '.join(row))
                axis_x.append(float(row[1]))
                axis_y.append(float(row[2]))
                countries.append(row[0])
                lines += 1
            else:
                axis_x_label = row[1]
                axis_y_label = row[2]
                print(', '.join(row))
                lines += 1
    return axis_x, axis_y, axis_x_label, axis_y_label, countries


# Code section declaring variables for the data
axis_x, axis_y, axis_x_label, axis_y_label, countries = csv_read_function()

# Code section creating a two dimension array from axis_x and axis_y
two_dimension_array = np.vstack((axis_x, axis_y)).T


# Code section function that finds the closest centroid to each point out of all the centroids
# The Numpy RandomState is used allowing us to find the index of the smallest value in an array.
def closest_centroid_function(two_dimension_array, number_of_clusters, rseed=2):
    index_smallest_value = np.random.RandomState(rseed)
    i = index_smallest_value.permutation(two_dimension_array.shape[0])[:number_of_clusters]
    center_points_distance = two_dimension_array[i]

    # Code section implementation for the k-means algorithm, using appropriate looping for the number of iterations.
    print("\nClosest Centroids:")
    

    
    while True:
       
        # Code section using the pairwise_distances_argmin method to
        # determine the distances between points to centres
        distance_labels = pairwise_distances_argmin(two_dimension_array, center_points_distance)

        # Code section to calculate the new mean of all points in that cluster
        new_mean_of_all_points = np.array([two_dimension_array[distance_labels == i].mean(0)
                               for i in range(number_of_clusters)])

        # Code section to for new_mean_of_all_points
        if np.all(center_points_distance == new_mean_of_all_points):
            break
        center_points_distance = new_mean_of_all_points

        # Code section to print center_points_distance
        print(center_points_distance)
        print()

    return center_points_distance, distance_labels


# Code section to visualise and draw scatter plot
center_points_distance, distance_labels = closest_centroid_function(two_dimension_array, cluster_number)
plt.scatter(two_dimension_array[:, 0], two_dimension_array[:, 1], c=distance_labels, s=50, cmap='plasma')
plt.title('The Life Expectancy and Birth Rate using K-Means clustering')
plt.xlabel(axis_x_label)
plt.ylabel(axis_y_label)

# Code section to print out the results for questions
print("\nThe number of countries belonging to each cluster:")
print(Counter(distance_labels))

# Code section to get cluster indices
indices = defaultdict(list)
for i, j in enumerate(distance_labels):
    indices[j].append(i)

# Code section to print countries in each cluster and means
axis_x = 0
while axis_x < cluster_number:
    
    print("\nThe list of countries belonging to cluster " + str(axis_x + 1))

    for i in indices[axis_x]:
        print(countries[i])
    
    print("\nThe Birth Rate Mean:")
    print(center_points_distance[axis_x][0])
    
    print("\nThe Life Expectancy Mean:")
    print(center_points_distance[axis_x][1])
    axis_x += 1

# Show plot
plt.show()
