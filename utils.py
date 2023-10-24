import numpy as np
import pandas as pd
import graphviz as gr

def simulate(**kwargs):
  values = {}
  g = gr.Digraph()
  for k,v in kwargs.items():
    parents = v.__code__.co_varnames
    inputs = {arg: values[arg] for arg in v.__code__.co_varnames}
    values[k] = v(**inputs)
    for p in parents:
      g.edge(p, k)
  return pd.DataFrame(values), g
