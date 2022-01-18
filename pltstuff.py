# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 18:19:26 2021

@author: jackm
"""
import os
#%%
import pandas as pd
from sklearn.preprocessing import MinMaxScaler 
profiles = pd.read_csv('C:/Users/jackm/Documents/funstuff/fbref/newprof.csv')

profiles = profiles.rename(columns = {'Non.Penalty.Goals':'Non-Penalty Goals',
                                      'Progressive.Carries':'Progressive Carries',
                                      'Clustername':'Cluster Name',
                                      'Aerials.won':'Aerials Won'})

df = profiles[['Non-Penalty Goals', 'Progressive Carries','Cluster Name', 'Aerials Won',
               'Assists', 'Tackles', 'Interceptions']]

grouped = df.groupby('Cluster Name')
meaned = grouped.mean()
scaled = pd.DataFrame(MinMaxScaler().fit_transform(meaned))

scaled = scaled.rename(index = {0:'Attacking Midfielders',
                                  1:'Deep-Lying Midfielders',
                                  2:'Defenders',
                                  3:'Target Men',
                                  4:'Transcendent Stars',
                                  5:'Tricky Attackers'})

scaled = scaled.rename(columns = {0:'Non-Penalty Goals',
                                  1:'Progressive Carries',
                                  2:'Aerials Won',
                                  3:'Assists',
                                  4:'Tackles',
                                  5:'Interceptions'})


t = scaled.transpose()
t.reset_index(level=0, inplace = True)
scaled.reset_index(level=0, inplace = True)

#%%
import plotly.graph_objects as go
import chart_studio
import chart_studio.plotly as py

username ='jcmeulle'
api_key = '7l1lpe3DBSACxiDbDSuY'
chart_studio.tools.set_credentials_file(username=username, api_key=api_key)

categories = t["index"].tolist()

fig = go.Figure(data=go.Scatterpolar(
  r=t["Attacking Midfielders"].tolist(),
  theta=categories,
  fill='toself'
))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True
    ),
  ),
  showlegend=False,
  title = 'Attacking Midfielders'
)

py.plot(fig, filename = 'Attacking Midfielders', auto_open = True)

#%%
import plotly.graph_objects as go
import chart_studio
import chart_studio.plotly as py

username ='jcmeulle'
api_key = '7l1lpe3DBSACxiDbDSuY'
chart_studio.tools.set_credentials_file(username=username, api_key=api_key)

categories = t["index"].tolist()

fig = go.Figure(data=go.Scatterpolar(
  r=t["Deep-Lying Midfielders"].tolist(),
  theta=categories,
  fill='toself'
))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True
    ),
  ),
  showlegend=False,
  title = 'Deep-Lying Midfielders'
)

py.plot(fig, filename = 'Deep-Lying Midfielders', auto_open = True)

#%%
import plotly.graph_objects as go
import chart_studio
import chart_studio.plotly as py

username ='jcmeulle'
api_key = '7l1lpe3DBSACxiDbDSuY'
chart_studio.tools.set_credentials_file(username=username, api_key=api_key)

categories = t["index"].tolist()

fig = go.Figure(data=go.Scatterpolar(
  r=t["Defenders"].tolist(),
  theta=categories,
  fill='toself'
))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True
    ),
  ),
  showlegend=False,
  title = 'Defenders'
)

py.plot(fig, filename = 'Defenders', auto_open = True)

#%%
import plotly.graph_objects as go
import chart_studio
import chart_studio.plotly as py

username ='jcmeulle'
api_key = '7l1lpe3DBSACxiDbDSuY'
chart_studio.tools.set_credentials_file(username=username, api_key=api_key)

categories = t["index"].tolist()

fig = go.Figure(data=go.Scatterpolar(
  r=t["Target Men"].tolist(),
  theta=categories,
  fill='toself'
))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True
    ),
  ),
  showlegend=False,
  title = 'Target Men'
)

py.plot(fig, filename = 'Target Men', auto_open = True)

#%%
import plotly.graph_objects as go
import chart_studio
import chart_studio.plotly as py

username ='jcmeulle'
api_key = '7l1lpe3DBSACxiDbDSuY'
chart_studio.tools.set_credentials_file(username=username, api_key=api_key)

categories = t["index"].tolist()

fig = go.Figure(data=go.Scatterpolar(
  r=t["Transcendent Stars"].tolist(),
  theta=categories,
  fill='toself'
))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True
    ),
  ),
  showlegend=False,
  title = 'Transcendent Stars'
)

py.plot(fig, filename = 'Transcendent Stars', auto_open = True)

#%%
import plotly.graph_objects as go
import chart_studio
import chart_studio.plotly as py

username ='jcmeulle'
api_key = '7l1lpe3DBSACxiDbDSuY'
chart_studio.tools.set_credentials_file(username=username, api_key=api_key)

categories = t["index"].tolist()

fig = go.Figure(data=go.Scatterpolar(
  r=t["Tricky Attackers"].tolist(),
  theta=categories,
  fill='toself'
))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True
    ),
  ),
  showlegend=False,
  title = 'Tricky Attackers'
)

py.plot(fig, filename = 'Tricky Attackers', auto_open = True)