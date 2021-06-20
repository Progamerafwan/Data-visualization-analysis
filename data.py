#data of 12 students of grade 3 participating in 4 levels of lesson 1
import pandas as pd 
import csv 
import plotly.graph_objects  as go 

df = pd.read_csv("data.csv")
print(df.groupby("level")["attempt"].mean())

fig = go.Figure(go.Bar(
    x = df.groupby("level")["attempt"].mean(),
    y = ['Level 1','Level 2','Level 3','Leve 4'],  
    orientation = 'h'
))
fig.show()

