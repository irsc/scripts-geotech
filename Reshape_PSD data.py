#import relevant packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# set file path for data source
folder_path="C:/Users/ignacio.rivero/python_WIP/"
file_path = folder_path + "PSD_central.csv"
#Load file into lab_shc
PSD_csv= pd.read_csv(file_path)
#transform to a pandas Data Frame
df = pd.DataFrame(PSD_csv)

print(df.head())

df2 = pd.melt(df, id_vars =['Sample Ref','Location', 'TP No.','Depth'], value_vars =['100','63','50','20','10','0.063','0.001'])
df2.variable = pd.to_numeric(df2.variable)

df2 = df2.sort_values(['Sample Ref','variable'])

print(df2.head(50))

df2.to_csv(r'C:/Users/ignacio.rivero/python_WIP/PSD_reshape.csv',index = None, header=True)
