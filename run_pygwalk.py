import pandas as pd
import pygwalker as pyg

df = pd.read_csv('./pygwalk.csv')
walker = pyg.walk(df)