from math import sqrt
from typing import List

from interfaces.ISolver import ISolver

class KNN(ISolver):
  identifier = "KNN"

  def __init__(self, k):
    self.data = []
    self.trained = False
    self.k = k
  
  def train(self, data: List[List]):
    self.trained = True
    self.data = data
  
  def predict(self, point: List):
    if not self.trained:
      raise Exception("KNN not trained")
    distances = self.__calculate_distances(point)
    most_frequent = self.__get_most_frequent_label(distances[:self.k])
    return most_frequent
  
  def __calculate_distances(self, point: List):
    distances = []
    for row in self.data:
      acc = 0
      for i in range(4):
        acc += (point["data"][i] - row["data"][i]) ** 2
      distance = sqrt(acc)
      distances.append({
        "label": row["label"],
        "distance": distance
      })
    distances.sort(key=lambda d: d["distance"])
    return distances
  
  def __get_most_frequent_label(self, close_points: List):
    count_distances = {}
    for point in close_points:
      label = point["label"]
      if not label in count_distances:
        count_distances[label] = 0
      count_distances[label] += 1
    all_labels = [key for key in count_distances.keys()]
    most_frequent = all_labels[0]
    for label in all_labels:
      if count_distances[label] > count_distances[most_frequent]:
        most_frequent = label
    return label

export = KNN
