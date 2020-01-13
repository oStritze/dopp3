import pandas as pd
import numpy as np

with open("test.csv") as f:
    df = pd.read_csv(f,sep=";",error_bad_lines=False,engine="python")

print(df.index)