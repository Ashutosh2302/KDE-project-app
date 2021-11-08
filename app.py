import dash
from dash import dcc
from dash import html
# import dash_core_components as dcc
# import dash_html_components as html
import plotly.express as px
import pandas as pd
import requests

query = '''SELECT	(COUNT(*)	as	?Triples)
WHERE	{	
?s	?p	?o	.
}'''

url = f'http://LAPTOP-45QEIGK2:7200/repositories/demorepo?query={query}'
res = requests.request('GET', url)
print(res.text)
app = dash.Dash(__name__)


app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children=f'{res.text}'),

])

if __name__ == '__main__':
    app.run_server(debug=True)






