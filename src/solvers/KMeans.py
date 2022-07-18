from math import inf, floor, sqrt
from random import random

from interfaces.ISolver import ISolver

class KMeans(ISolver):
  identifier = "KMEANS"

  def __init__(self, k):
    self.k = k
    self.data = []
    self.trained = False
    self.centroids = []
  
  def train(self, data):
    self.trained = True
    dimensions = len(data[0]["data"])
    min_values, max_values = self.__get_min_max_values(dimensions, data)
    centroids = [self.__generate_random_centroid(min_values, max_values) for _ in range(self.k)]
    old_centroids = centroids

    while True:
      centroids = self.__converge_centroids(centroids, data)
      differences = 0
      for index, centroid in enumerate(centroids):
        distance = get_distance(centroid, old_centroids[index])
        if distance > 0:
          differences += 1
      if differences == 0:
        break
      old_centroids = centroids

    for centroid in centroids:
      self.centroids.append({
        "point": centroid,
        "label": len(self.centroids) + 1
      })
      print(f"Centroid #{len(self.centroids)}: {centroid}")
  
  def __get_min_max_values(self, dimensions, data):
    max_values = [-inf for _ in range(dimensions)]
    min_values = [inf for _ in range(dimensions)]
    for row in data:
      values = row["data"]
      for i in range(4):
        if values[i] > max_values[i]:
          max_values[i] = values[i]
        if values[i] < min_values[i]:
          min_values[i] = values[i]
    return min_values, max_values
  
  def __generate_random_centroid(self, min_values, max_values):
    centroid = []
    for i in range(len(min_values)):
      centroid.append(rand(min_values[i], max_values[i]))
    return centroid

  def __converge_centroids(self, centroids, data):
    centroid_points = [[] for _ in centroids]
    for row in data:
      point = row["data"]
      closest_centroid = self.__find_closest_centroid(point, centroids)
      centroid_points[closest_centroid].append(point)
  
    new_centroids = []
    for centroid in centroid_points:
      if len(centroid) == 0:
        continue
      acc = [0 for _ in range(len(point))]
      for point in centroid:
        for i in range(len(point)):
          acc[i] += point[i]
      for i in range(len(acc)):
        acc[i] /= len(centroid)
      new_centroids.append(acc)
    
    return new_centroids
  
  def __find_closest_centroid(self, point, centroids):
    closest_centroid = 0
    closest_centroid_distance = inf
    for index, centroid in enumerate(centroids):
      distance = get_distance(point, centroid)
      if distance < closest_centroid_distance:
        closest_centroid_distance = distance
        closest_centroid = index
    return closest_centroid
  
  def predict(self, point):
    if not self.trained:
      raise Exception("KMeans not trained")
    closest_centroid = None
    closest_centroid_distance = inf
    for centroid in self.centroids:
      distance = get_distance(point["data"], centroid["point"])
      if distance < closest_centroid_distance:
        closest_centroid_distance = distance
        closest_centroid = centroid
    return closest_centroid["label"]
    

def rand(min, max):
  return random() * (max - min) + min

def get_distance(point1, point2):
  acc_distance = 0
  for i in range(len(point1)):
    acc_distance += (point1[i] - point2[i]) ** 2
  distance = sqrt(acc_distance)
  return distance

export = KMeans
