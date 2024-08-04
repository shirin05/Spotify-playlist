import pandas as pd
import random
import numpy as np 
from pprint import pprint

def random_num_generator(k):
     """Random number generator.
     Args:
          k (int): Number of clusters.
     Returns:
          (list of lists): List of random number lists.
     """

     print("Generating random numbers...")
     # array called output which will hold all the random point lists 
     # is a 2D array
     output = []

     # will generate k amount of random points
     for i in range(k):
          danceability = random.random()
          energy = random.random()
          key = random.randint(0,11)
          loudness = random.uniform(-60, 0)
          mode = random.randint(0, 1)
          speechiness = random.random()
          acousticness = random.random()
          instrumentalness = random.random()
          liveness = random.random()
          valence = random.random() 
          time_signature = random.randint(3, 7)
          
          # list to hold all random points for each feature
          random_points = [danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, time_signature]
          
          # each new list of random points is added to the output array
          output.append(random_points)
     
     return output      

def euclidian_dist(a, b):
     """Euclidian distance function.
     Args:
          a (list): List of features.
          b (list): List of features.
     Returns:
          (float): Euclidian distance.
     """
     try:
          # finding the difference between two feature points and then squaring it
          danceability_diff = (a[0] - b[0])**2
          energy_diff = (a[1] - b[1])**2
          key_diff = (a[2] - b[2])**2
          loudness_diff = (a[3] - b[3])**2
          mode_diff = (a[4] - b[4])**2
          speechiness_diff = (a[5] - b[5])**2
          acousticness_diff = (a[6] - b[6])**2
          instrumentalness_diff = (a[7] - b[7])**2
          liveness_diff = (a[8] - b[8])**2
          valence_diff = (a[9] - b[9])**2
          time_signature_diff = (a[10] - b[10])**2

     except IndexError:
          print("=====================================")
          print("IndexError: list index out of range")
          pprint(a)
          print()
          pprint(b)
          print("IndexError: ", len(a), len(b))
          print("IndexError: ", type(a), type(b))
          return 0

     # finding the sum of all the above
     sum = danceability_diff + energy_diff + key_diff + loudness_diff + mode_diff + speechiness_diff + acousticness_diff + instrumentalness_diff + liveness_diff + valence_diff + time_signature_diff
     
     # finding the square root of the sum
     root = np.sqrt(sum)
     return root


def cluster_average(k):
     """Cluster average function.
     Args:
          k is an array of arrays.
     Returns:
          the mean of each feature in an array.
     """
     # converts k into a data frame    
     cluster_frame = pd.DataFrame(k)
     # finds mean of each feature and stores mean in a list
     cluster_mean = cluster_frame.mean().to_list()
     return cluster_mean



def clustering(k, music_csv, iterations):
     """Clustering function.
     Args:
          k (int): Number of clusters.
          music_csv (pandas dataframe): Dataframe of music features.
          iterations (int): Number of iterations for k-means.
     Returns:
          (list): List of clusters.
     """
     # generate random points 
     random_points = random_num_generator(k)

     # create a dict to hold all the clusters
     clusters = {}

     # assign each of the random points as cluster keys 
     for point in random_points:
          # use tuple instead of list as python does not allow list as a key
          clusters[tuple(point)] = []


     # iterate through the number of iterations
     
     length = len(music_csv)

     for i in range(iterations):
          counter = 0
          print("Iteration: ", i)
          for index, row in music_csv.iterrows():
               # progress bar
               counter += 1
               print("Progress: ", counter, "/", length)
               comparer = []
               for key in clusters:
                    comparer.append(euclidian_dist(row.to_list()[1:], key))
               min_euclidian = min(comparer)
               index_min = comparer.index(min_euclidian)

               # debugging print statements
               print("Min euclidian: ", min_euclidian)
               print("Index min: ", index_min)
               print("Key: ", list(clusters.keys())[index_min])
               pprint(list(clusters.keys()))

               closest_key = list(clusters.keys())[index_min]
               # add the row to the closest cluster
               clusters[closest_key].append(row.to_list())

          new_clusters = {}
          for key in clusters:
               print("Computing cluster average...")
               # update the key to be the average of all its values 
               clusters_new_mean = cluster_average(clusters[key])
               new_clusters[tuple(clusters_new_mean)] = clusters[key]
          clusters = new_clusters

          new_clusters = {}
          # discard any blank keys
          for key in clusters:
               if key != ():
                    new_clusters[key] = clusters[key]
          clusters = new_clusters
               
          pprint(list(clusters.keys()))

     return clusters

def best_cluster(clusters, means):
     """Best cluster function."""
     distances_best = []
     for key in clusters:
          distances_best.append(euclidian_dist(key, means))
     distance_min = min(distances_best)
     index_min_dist = distances_best.index(distance_min)
     best_cluster = list(clusters.keys())[index_min_dist]
     return best_cluster





