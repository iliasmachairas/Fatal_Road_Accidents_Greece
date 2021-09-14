import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H4("Fatal Road Accidents (FRA) in Athens (2011-2015"),

    html.Div([
        "Select vehicle: ",
        dcc.RadioItems(id='vehicle-dropdown',
        options=[
        {'label': 'Car', 'value': 'Ι.Χ.Ε.'},
        {'label': 'Motrorcycle', 'value': 'Δίκυκλο'},
        {'label': 'Other', 'value': 'Άλλο'},
        {'label': 'All', 'value': 'All'}
            ],
        value='MTL',
        labelStyle={'display': 'block'}
        ) 
        ]),
    
        html.Div([
        "Select year: ",
        dcc.Dropdown(id='year-dropdown',
        options=[
        {'label': '2011', 'value': '2011'},
        {'label': '2012', 'value': '2012'},
        {'label': '2013', 'value': '2013'},
        {'label': '2014', 'value': '2014'},
        {'label':'All', 'value':'All'}
            ],
        value='All',
        ) 
        ]),

    html.Br(),
    html.Div([
        "Input: ",
        dcc.Input(id='my-input', value='initial value', type='text')
    ]),
    html.Br(),
    html.Div(id='my-output'),
    html.Br(),

    html.Div(dcc.Graph(id='pie-chart-Time')),
    html.Br(),

    html.Div(dcc.Graph(id='Map-FRA')),
    html.Br(),

    html.Div(dcc.Graph(id='Bar-charts-Age_group')),
    html.Br(),
])

# 2 inputs - 3 outputs
@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
    return 'Output: {}'.format(input_value)


if __name__ == '__main__':
    app.run_server(debug=True)