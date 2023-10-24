import numpy as np
import pandas as pd

def simulate(**kwargs):
  values = {}
  for k,v in kwargs.items():
    inputs = {arg: values[arg] for arg in v.__code__.co_varnames}
    values[k] = v(**inputs)
  return pd.DataFrame(values)
