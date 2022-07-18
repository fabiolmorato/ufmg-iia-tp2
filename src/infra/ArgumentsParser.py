class ArgumentsParser:
  def __init__(self, args_list):
    self.args_list = args_list
    self.args = {
      "__free_args__": []
    }
    self.__parse()
  
  def get_arg(self, arg):
    if not arg in self.args:
      return None
    return self.args[arg]
  
  def get_free_args(self):
    return self.args["__free_args__"]
  
  def is_arg_set(self, arg):
    return arg in self.args

  def __parse(self):
    last_arg = None
    for arg in self.args_list:
      if arg.startswith("-"):
        last_arg = arg
        self.args[last_arg] = True
      elif last_arg != None:
        self.args[last_arg] = arg
        last_arg = None
      else:
        self.args["__free_args__"].append(arg)
