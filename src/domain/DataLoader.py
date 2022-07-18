from interfaces.IDataLoader import IDataLoader

class DataLoader(IDataLoader):
  def load(self, file_path: str):
    file = open(file_path, "r")
    data = [line.split("\n")[0].split(";") for line in file]
    parsed_data = []
    for row in data:
      parsed_row = {
        "data": [],
        "label": ""
      }
      for number in row[:4]:
        parsed_row["data"].append(float(number))
      parsed_row["label"] = row[4]
      parsed_data.append(parsed_row)
    return parsed_data
