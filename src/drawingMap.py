import numpy as np
import matplotlib.pyplot as plt
import openpyxl
import scipy.cluster.hierarchy as sch
import pandas as pd

col_list=["X","Y"]
df = pd.read_excel('../communes/communes.xlsx', usecols=col_list)
plt.scatter(df["X"],df["Y"],s=5, c='k', marker='o')
plt.show()