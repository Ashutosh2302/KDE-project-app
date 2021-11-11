import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
# import dash_html_components as html
import plotly.express as px
import pandas as pd
import requests


selectAllCountiesQuery = '''PREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0A
PREFIX%20ours%3A%20%3Chttp%3A%2F%2Fwww.semanticweb.org%2Fashutoshbansal%2Fontologies%2F2021%2F10%2Fproject-ontology%3E%0A
select DISTINCT ?county where { 
	?county rdf:type ours:county .
}'''
urlForSelectAllCounties = f'http://LAPTOP-45QEIGK2:7200/repositories/KDE-project?query={selectAllCountiesQuery}'  # Needs to be updated for every separate local machine

res = requests.request('GET', urlForSelectAllCounties)
print(res.text)
counties = [res.text]  # Need to convert this string into an array of individual values

selectedCounty = ''

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(style={'backgroundColor': '#EEEEEE'},
                      children=[

                          dcc.Dropdown(
                              id='county-dropdown',
                              options=[
                                  {'label': 'Dublin', 'value': 'DUB'},
                                  {'label': 'Wexford', 'value': 'WEX'},
                                  {'label': 'Galway', 'value': 'GAL'}
                              ],
                              # options = counties,
                              value=''
                          ),
                          html.Button('Submit', id='submit-val', n_clicks=0),
                          html.Div(id='dd-output-container'),

                      ])


@app.callback(
    Output('dd-output-container', 'children'),
    Input('submit-val', 'n_clicks'),
    State('county-dropdown', 'value')
)
def update_output(n_clicks, value):
    return 'The input value was "{}"'.format(
        value
    )


# return 'Selected county: "{}" '.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)
