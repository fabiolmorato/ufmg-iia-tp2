import abc
from typing import List, Dict

class IDataLoader(abc.ABC):
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def load(self, file_path: str) -> List[Dict]:
    return
