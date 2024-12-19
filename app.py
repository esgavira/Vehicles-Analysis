# %%
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')
fig = px.histogram(car_data, x="odometer") # crear un histograma
fig.show() # crear gráfico de dispersión



