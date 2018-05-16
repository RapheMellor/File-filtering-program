import pandas as pd
import geopandas as gpd
import os
import sys

Location = r'C:/Users/raphe.mellor/Documents/Test/sx2783.S10'
df = pd.read_csv(Location)
df.head(10)

df = pd.read_csv(Location, names=['chainage', 'speed', 'blank1', 'result', 'blank2', 'blank3', 'blank4'])
df.head(10)

df.to_csv("/Users/raphe.mellor/Documents/Test/sx2783S10.csv")

Location = r'C:/Users/raphe.mellor/Documents/Test/sx2783.zm3'
df1 = pd.read_csv(Location)
df1.head(10)

df1 = pd.read_csv(Location, names=['chainage', 'X', 'Y', 'Z', 'blank1', 'blank2'])
df1.head(10)

df1.to_csv("/Users/raphe.mellor/Documents/Test/2783ZM3.csv")

FileNames = []

os.chdir(r"C:\Users\raphe.mellor\Documents\Test\Test2")

for files in os.listdir("."):
    if files.endswith(".csv"):
        FileNames.append(files)
        
FileNames

import os
from functools import partial

project_directory = r'C:\Users\raphe.mellor\Documents\Test\Test2'
project_path = partial(os.path.join, project_directory)

def GetFile(fnombre):
    location = project_path(fnombre)
    if any([location.endswith(extension) for extension in [".xls", "xlsx"]]):
        df = pd.read_excel(location, 0)
    elif location.endswith(".csv"):
        df = pd.read_csv(location)
        
    df['File'] = fnombre
    return df.set_index(['File'])
	
	df_list = pd.concat([df, df1], axis =1)
df_list

df_list.to_csv("/Users/raphe.mellor/Documents/Test/Test2/TestResults.csv")

df_list = df_list[df_list['result'] > 30]
df_list = df_list[df_list['speed'] > 25]
df_list.to_csv("/Users/raphe.mellor/Documents/Test/Test2/TestResults2.csv")