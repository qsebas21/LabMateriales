import matplotlib.pyplot as plt
import pandas as pd
import dataframe_image as dfi

df_vidrio = pd.read_csv('r_vidrio.csv', names=[1,2,3,4,5,6,7,8,9,10])
df_cuarzo = pd.read_csv('r_cuarzo.csv', names=[1,2,3])

s1 = df_vidrio.style.background_gradient(axis=None, cmap='YlOrRd')

s2 = df_cuarzo.style.background_gradient(vmax=700, axis=None, cmap='YlOrRd')

dfi.export(s1, 'r_vidrio.png')
dfi.export(s2, 'r_cuarzo.png')
