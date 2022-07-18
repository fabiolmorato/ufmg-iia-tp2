import abc
from typing import List

class ISolver(abc.ABC):
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def train(self, data: List):
    return
  
  @abc.abstractmethod
  def predict(self, point: List) -> str:
    return
