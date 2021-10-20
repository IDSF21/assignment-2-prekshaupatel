#!/usr/bin/env python
# coding: utf-8

import geopandas as gp
import shapely
import shapefile
import plotly
import streamlit as st
from us_state_abbr import abbrev_to_us_state, us_state_to_abbrev

import numpy as np
import pandas as pd
import plotly.express as px
from plotly.figure_factory._county_choropleth import create_choropleth
from streamlit_plotly_events import plotly_events
from month_labels import month_labels, labels_to_months


data_file = "us_counties_covid19_daily.csv"
df = pd.read_csv(data_file)
df['month'] = df.date.str.extract(r'^([0-9]+-[0-9]+)-')

st.sidebar.title("Exploring 2020 COVID-19 Trends Across the U.S.")

category = st.sidebar.selectbox('Select Category', ('Cases', 'Deaths'))
category = category.lower()

title = ""
desc = ""
if category == 'cases':
    title = "COVID-19 Cases"
    desc = "Average Number of COVID-19 Cases per Month"
elif category == 'deaths':
    title = "COVID-19 related Deaths"
    desc = "Average Number of COVID-19 Related Deaths per Month"
st.title(title + " Across the U.S.")

all_plot_state_data = df[['state', 'month', category]].dropna().groupby(['state', 'month']).mean().reset_index().sort_values('month')
all_plot_state_data["Month "] = [' ' + labels_to_months[i] for i in all_plot_state_data.month]
all_states = [us_state_to_abbrev[i] for i in all_plot_state_data.state]

fig = px.choropleth(all_plot_state_data,
                    locations = all_states,
                    locationmode="USA-states",
                    color=all_plot_state_data[category],
                    animation_frame="Month ",
                    scope="usa")

fig.layout.template = None
selected_points = plotly_events(fig) 
st.caption(desc + "\n across the United States in 2020. Select a State on the Map to Analyze the Trends in that State.")

num = 0
if len(selected_points) > 0:
    num = selected_points[0]["pointNumber"]
state = list(all_plot_state_data['state'])[num]
    
st.title(title + " Across " + state)

method = st.radio("Plot Style", ("Absolute", "Relative"))
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

state_df = all_plot_state_data[all_plot_state_data['state'] == state]

if method == "Absolute":
    state_trend_fig = px.line(x=state_df['Month '], y=state_df[category], labels=dict(y="Average Number of " + title, x="Months (in 2020)"))
    st.plotly_chart(state_trend_fig)
    st.caption(desc + "\n Across " + state + " in 2020.")

if method == "Relative":
    months = list(state_df['Month '])[1:]
    vals = list(state_df[category])
    percent_change = [int((vals[i] - vals[i-1])*200/(vals[i-1] + vals[i] + 0.0000001)) for i in range(1, len(vals))]
    state_trend_fig = px.line(x=months, y=percent_change, labels=dict(y="Percentage Increase in " + title + " (%)", x="Months (in 2020)"))
    st.plotly_chart(state_trend_fig)
    st.caption("Percentage Change in " + desc + "\n Across " + state + " in 2020.")





