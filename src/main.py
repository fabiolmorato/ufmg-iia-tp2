import sys

from domain.DataLoader import DataLoader
from infra.SolverLoader import SolverLoader
from infra.ArgumentsParser import ArgumentsParser

class TP2:
  def __init__(self, argv):
    self.get_arguments(argv)
    
    solver_loader = SolverLoader()
    solver_loader.load_from_directory("./src/solvers")
    self.solver = solver_loader.get_solver(self.algorithm)(self.k)
    self.data_loader = DataLoader()
    self.prediction_results = {}
    self.labels = []
  
  def run(self):
    train_data = self.data_loader.load(self.train_dataset)
    test_data = self.data_loader.load(self.test_dataset)
    self.solver.train(train_data)
    self.get_labels(train_data)
    
    self.predict_dataset(test_data)

    if self.print_confusion_matrix:
      self.get_confusion_matrix()
      for label in self.labels:
        confusion_matrix = self.confusion_matrix[label]
        print(f"Confusion matrix for {label}:")
        print(confusion_matrix)

        self.print_accuracy(confusion_matrix)
        self.print_precision(confusion_matrix)
        self.print_recall(confusion_matrix)
        self.print_f1(confusion_matrix)
        
        print("")
  
  def predict_dataset(self, dataset):
    for row in dataset:
      predicted = self.solver.predict(row)
      if self.print_predictions:
        print(f"Real: {row['label']}, Predicted: {predicted}")
      if predicted == row["label"]:
        self.add_prediction_result(predicted, "true_positive")
        for label in self.labels:
          if label == predicted:
            continue
          self.add_prediction_result(label, "true_negative")
      else:
        self.add_prediction_result(predicted, "false_positive")
        self.add_prediction_result(row["label"], "false_negative")
        for label in self.labels:
          if label == predicted or label == row["label"]:
            continue
          self.add_prediction_result(label, "true_negative")
  
  def add_prediction_result(self, label, result):
    key = f'{label}_{result}'
    if not key in self.prediction_results:
      self.prediction_results[key] = 0
    self.prediction_results[key] += 1
  
  def get_labels(self, dataset):
    for data in dataset:
      if not data["label"] in self.labels:
        self.labels.append(data["label"])
    
    for label in self.labels:
      for result in ["true_positive", "false_positive", "false_negative", "true_negative"]:
        self.prediction_results[f"{label}_{result}"] = 0
  
  def get_confusion_matrix(self):
    self.confusion_matrix = {}
    for label in self.labels:
      self.confusion_matrix[label] = [
        [self.prediction_results[f"{label}_true_positive"], self.prediction_results[f"{label}_false_positive"]],
        [self.prediction_results[f"{label}_false_negative"], self.prediction_results[f"{label}_true_negative"]]
      ]
  
  def print_accuracy(self, confusion_matrix):
    if self.accuracy:
      accuracy = (confusion_matrix[0][0] + confusion_matrix[1][1]) / (confusion_matrix[0][0] + confusion_matrix[0][1] + confusion_matrix[1][0] + confusion_matrix[1][1])
      print(f"Accuracy: {accuracy}")
  
  def print_precision(self, confusion_matrix):
    if self.precision:
      divider = (confusion_matrix[0][0] + confusion_matrix[0][1])
      if divider == 0:
        precision = 1
      else:
        precision = confusion_matrix[0][0] / divider
      print(f"Precision: {precision}")

  def print_recall(self, confusion_matrix):
    if self.recall:
      divider = (confusion_matrix[0][0] + confusion_matrix[1][0])
      if divider == 0:
        recall = 1
      else:
        recall = confusion_matrix[0][0] / divider
      print(f"Recall: {recall}")
  
  def print_f1(self, confusion_matrix):
    if self.f1:
      precision_divider = (confusion_matrix[0][0] + confusion_matrix[0][1])
      if precision_divider == 0:
        precision = 1
      else:
        precision = confusion_matrix[0][0] / precision_divider
      
      recall_divider = (confusion_matrix[0][0] + confusion_matrix[1][0])
      if recall_divider == 0:
        recall = 1
      else:
        recall = confusion_matrix[0][0] / recall_divider
      
      f1_divider = (precision + recall)
      if f1_divider == 0:
        f1 = 1
      else:
        f1 = 2 * (precision * recall) / (precision + recall)

      print(f"F1 Score: {f1}")

  def get_arguments(self, argv):
    args_parser = ArgumentsParser(argv)
    self.algorithm = args_parser.get_arg("--algo").upper()
    self.k = int(args_parser.get_arg("-k"))
    self.train_dataset = "./data/iris treino.csv"
    self.test_dataset = "./data/iris teste.csv"
    self.accuracy = args_parser.get_arg("--accuracy") or False
    self.precision = args_parser.get_arg("--precision") or False
    self.recall = args_parser.get_arg("--recall") or False
    self.f1 = args_parser.get_arg("--f1") or False
    self.print_confusion_matrix = self.accuracy or self.precision or self.recall or self.f1
    self.print_predictions = args_parser.get_arg("--print-predictions")

    if args_parser.is_arg_set("--train-dataset"):
      self.train_dataset = args_parser.get_arg("--train-dataset")

    if args_parser.is_arg_set("--test-dataset"):
      self.test_dataset = args_parser.get_arg("--test-dataset")

if __name__ == "__main__":
  TP2(sys.argv).run()
