import imp
import os

from interfaces.ISolver import ISolver

class SolverLoader:
  def __init__(self):
    self.solvers = {}
  
  def load_from_directory(self, directory: str):
    for file in os.listdir(directory):
      if file.endswith(".py"):
        module_name = file[:-3]
        module = imp.load_source(module_name, os.path.join(directory, file))
        solver = module.export
        self.solvers[solver.identifier] = solver
  
  def get_solver(self, identifier: str) -> ISolver:
    return self.solvers[identifier]
