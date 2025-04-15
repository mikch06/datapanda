import pandas as pd
import pygwalker as pyg

df = pd.read_csv('./output.csv')
walker = pyg.walk(df)