import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output
# import dash_html_components as html
import plotly.express as px
import pandas as pd
import requests

query = '''SELECT	?s ?p ?o
WHERE	{	
?s	?p	?o	.
}'''
url = f'http://DESKTOP-CLRQH7Q:7200/repositories/KDE-project?query={query}'

counties = []

selectAllCountiesQuery = '''PREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0A
PREFIX%20ours%3A%20%3Chttp%3A%2F%2Fwww.semanticweb.org%2Fashutoshbansal%2Fontologies%2F2021%2F10%2Fproject-ontology%3E%0A
select DISTINCT ?county where { 
	?county rdf:type ours:county .
}'''
urlForSelectAllCounties = f'http://DESKTOP-CLRQH7Q:7200/repositories/KDE-project?query={selectAllCountiesQuery}'    #Needs to be updated for every separate local machine

res = requests.request('GET', urlForSelectAllCounties)
print(res.text)
counties = [res.text]   #Need to convert this string into an array of individual values
app = dash.Dash(__name__)


selectedCounty = '';

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(style={'backgroundColor' : '#EEEEEE'}, 
                      children=[
    
    dcc.Dropdown(
    id='county-dropdown',
      options=[
             {'label': 'Dublin', 'value': 'DUB'},
             {'label': 'Wexford', 'value': 'WEX'},
             {'label': 'Galway', 'value': 'GAL'}
         ],
     #options = counties,
     value=''
     ),
    html.Div(id='dd-output-container'),
   
    ])

@app.callback(
    Output('dd-output-container', 'children'),
    Input('county-dropdown', 'value')
    )


def update_output(value):
    return 'Selected county: "{}" '.format(value)



if __name__ == '__main__':
    app.run_server(debug=True)






