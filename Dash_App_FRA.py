# Import required libraries
import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px
import numpy as np
#import geopandas as gpd
import sys

print(sys.executable)
car = 'Ι.Χ.Ε.'


# Read the airline spacex_df into pandas dataframe
FRA = pd.read_csv('Data/FRA_df.csv', encoding='utf-8')
FRA['Date'] = pd.to_datetime(FRA['Date'])
FRA['year'] = (FRA.Date.dt.year).astype(int)
#FRA['year'] = FRA['year'].astype(str)
print(FRA.head())
#print(FRA.dtypes)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H4("Fatal Road Accidents (FRA) in Athens (2011-2015)"),

    html.Div([
        "Select vehicle: ",
        dcc.RadioItems(id='vehicle-radio',
        options=[
        {'label': 'car', 'value': car},
        {'label': 'motorcycle', 'value': 'motorcycle'},
        {'label': 'Other', 'value': 'Other'},
        {'label': 'All', 'value': 'All'}
            ],
        value='All',
        labelStyle={'display': 'block'}
        ) 
        ]),

        html.Div([
        "Select year: ",
        dcc.Dropdown(id='year-dropdown',
        options=[
        {'label': '2011', 'value': 2011},
        {'label': '2012', 'value': 2012},
        {'label': '2013', 'value': 2013},
        {'label': '2014', 'value': 2014},
        {'label':'All', 'value':'All'}
            ],
        value='All',
        ) 
        ]),

    html.Br(),

    html.Div(dcc.Graph(id='Bar-charts-Age_group')),
    html.Br(),

    #html.Div(dcc.Graph(id='Map-FRA')),
    #html.Br(),

    #html.Div(dcc.Graph(id='pie-chart-Time')),
    #html.Br(),
])

# 2 inputs - 3 outputs
#@app.callback(
#    Output(component_id='my-output', component_property='children'),
#    Input(component_id='my-input', component_property='value')
#)

@app.callback(
    Output(component_id='Bar-charts-Age_group', component_property='figure'),
    [Input(component_id='vehicle-radio', component_property='value'),
    Input(component_id="year-dropdown", component_property="value")])

#def update_output_div(input_value):
#    return 'Output: {}'.format(input_value)
#print(type(value_vehicle))

def update_output_barplot(value_vehicle, value_year):
    # value year
    if value_year=='All':
        #sel_years = [np.arange(2011,2015)]
        df_clip_1 = FRA.copy()
    else:
        sel_years = [value_year]
        #mask_1 = FRA.year.isin(sel_years)
        df_clip_1 = FRA[FRA.year == value_year].copy()
        # print(type(value_year))
    
    # value vehicle
    if value_vehicle=='All':
        #sel_vehicle = ['car', 'motorcycle', 'Other']
        df_clip_2 = df_clip_1.copy()
    else:
        #sel_vehicle = [value_vehicle]
        df_clip_2 = df_clip_1[df_clip_1.Vehicle == value_vehicle].copy()
        #mask_2 = df_clip_1.Vehicle.isin(sel_vehicle)
        #df_clip_2 = df_clip_1.loc[mask_2]
    
    time_series_Age = df_clip_2.Age.value_counts()
    time_series_Age = time_series_Age.to_frame()
    #return time_series_Age
    fig = px.bar(time_series_Age, x='Age', y=time_series_Age.index, title="Age groups",orientation='h')
    fig.update_layout(
        title="Age Groups",
        xaxis_title="Count",
        yaxis_title="Age Group")
    return fig
    #fig.show()


if __name__ == '__main__':
    app.run_server(debug=True)