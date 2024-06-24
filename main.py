import pandas as pd
from plotly.offline import plot
import numpy as np

import matplotlib.pyplot as plt

import plotly.graph_objs as go

import plotly.io as pio

import plotly.express as px

pio.templates.default = "plotly_white"

from statsmodels.tsa.arima.model import ARIMA

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

data = pd.read_csv('Netflix-Subscriptions.csv')

print(data.head())

fig = go.Figure()
fig.add_trace(go.Scatter(x=data['Time Period'], y=data['Subscribers'],mode='lines', name='Subscribers'))

fig.update_layout(title='Netflix Quarterly Subscriptions Growth', xaxis_title='Date', yaxis_title='Netflix Subscriptions')

plot(fig)

