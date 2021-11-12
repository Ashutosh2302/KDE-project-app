import dash
from dash import dcc
from dash import html
# import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
# import dash_html_components as html
import plotly.express as px
import pandas as pd
import requests

# selectAllCountiesQuery = '''PREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0A
# PREFIX%20ours%3A%20%3Chttp%3A%2F%2Fwww.semanticweb.org%2Fashutoshbansal%2Fontologies%2F2021%2F10%2Fproject-ontology%3E%0A
# select DISTINCT ?county where {
# 	?county rdf:type ours:county .
# }'''
# urlForSelectAllCounties = f'http://LAPTOP-45QEIGK2:7200/repositories/KDE-project?query={selectAllCountiesQuery}'  # Needs to be updated for every separate local machine
#
# res = requests.request('GET', urlForSelectAllCounties)
# print(res.text)
# counties = [res.text]  # Need to convert this string into an array of individual values


query_1 = {'poi': '', 'location-type': '', 'location': ''}
query_2 = {'poi': '', 'location-type': '', 'location': ''}
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

points_of_interest = ['Pilgrim Path', 'Museum', 'Walled Towns', 'Landmarks']
location = ['Town', 'County']


counties = [
                 {'label': 'Antrim', 'value': 'ANT'},
                 {'label': 'Armagh', 'value': 'ARM'},
                 {'label': 'Carlow', 'value': 'CAR'},
                 {'label': 'Cavan', 'value': 'CAV'},
                 {'label': 'Clare', 'value': 'CLA'},
                 {'label': 'Cork', 'value': 'COR'},
                 {'label': 'Derry', 'value': 'DER'},
                 {'label': 'Donegal', 'value': 'DON'},
                 {'label': 'Down', 'value': 'DOW'},
                 {'label': 'Dublin', 'value': 'DUB'},
                 {'label': 'Fermanagh', 'value': 'FER'},
                 {'label': 'Galway', 'value': 'GAL'},
                 {'label': 'Kerry', 'value': 'KER'},
                 {'label': 'Kildare', 'value': 'KIL'},
                 {'label': 'Kilkenny', 'value': 'KILK'},
                 {'label': 'Laois', 'value': 'LAO'},
                 {'label': 'Leitrim', 'value': 'LEI'},
                 {'label': 'Limerick', 'value': 'LIM'},
                 {'label': 'Longford', 'value': 'LON'},
                 {'label': 'Louth', 'value': 'LOU'},
                 {'label': 'Mayo', 'value': 'MAY'},
                 {'label': 'Meath', 'value': 'MEA'},
                 {'label': 'Monaghan', 'value': 'MON'},
                 {'label': 'Offaly', 'value': 'OFF'},
                 {'label': 'Roscommon', 'value': 'ROS'},
                 {'label': 'Sligo', 'value': 'SLI'},
                 {'label': 'Tipperary', 'value': 'TIP'},
                 {'label': 'Tyrone', 'value': 'TYR'},
                 {'label': 'Waterford', 'value': 'WAT'},
                 {'label': 'Westmeath', 'value': 'WES'},
                 {'label': 'Wexford', 'value': 'WEX'},
                 {'label': 'Wicklow', 'value': 'WIC'}
             ]
towns = [
                    {'label': 'Ardmore', 'value': 'ARD'},
                    {'label': 'Ballintubber', 'value': 'BAL'},
                    {'label': 'Ballycumber', 'value': 'BALC'},
                    {'label': 'Ballymacavany', 'value': 'BALM'},
                    {'label': 'Bunglass', 'value': 'BUN'},
                    {'label': 'Caherciveen', 'value': 'CAHE'},
                    {'label': 'Corofin', 'value': 'COR'},
                    {'label': 'Drimoleague', 'value': 'DRI'},
                    {'label': 'Glencolumbkille', 'value': 'Glen'},
                    {'label': 'Hollywood', 'value': 'HOL'},
                    {'label': 'Kilcommon', 'value': 'KILK'},
                    {'label': 'Kildare Town', 'value': 'KIL'},
                    {'label': 'Ventry', 'value': 'VEN'}
                    ]
app.layout = html.Div([

    html.Div(

            style={'backgroundColor': '#1d6b01', 'position': 'center', 'height': '20vh'},
            children=[
            html.H1(children='Query Historic Knowledge Graph', style={'textAlign': 'center', 'verticalAlign': 'middle', 'line-height': '20vh', 'color': 'white'})
            ]
            ),
    html.H1(children="Question 1", style={'textAlign': 'center', 'verticalAlign': 'middle', 'line-height': '20vh'}),
    html.Div(
        style={'backgroundColor': '#FFFF00'},
        children=[
            html.H3(children="Select a point of interest"),

            dcc.Dropdown(
                id='poi-dropdown',
                style={'width': '60%'},
                options=[{'label': poi, 'value': poi} for poi in points_of_interest],
                value='',
                multi=True,
                placeholder="Select a point of interest",
            ),
            html.H3(children="Select location type"),
            dcc.Dropdown(
                id='location-dropdown',
                style={'width': '40%'},
                options=[{'label': l, 'value': l} for l in location],
                value='',
                placeholder="Select location type",
            ),
            html.H3(children=f"Select town/county"),
            dcc.Dropdown(
                id='location-town-county-dropdown',
                style={'width': '40%'},
            ),
            html.Button('Submit', id='submit_1', n_clicks=0),
            html.Div(id='poi-output'),
            html.Div(id='location-output'),
            html.Div(id='location-town-county-output'),
        ]
    ),

    html.H1(children="Question 2", style={'textAlign': 'center', 'verticalAlign': 'middle', 'line-height': '20vh'}),
        html.Div(
            style={'backgroundColor': '#FFFF00'},
            children=[
                html.H3(children="Select a point of interest"),

                dcc.Dropdown(
                    id='poi1-dropdown',
                    style={'width': '60%'},
                    options=[{'label': poi, 'value': poi} for poi in points_of_interest],
                    value='',
                    multi=True,
                    placeholder="Select a point of interest",
                ),
                html.H3(children="Select location type"),
                dcc.Dropdown(
                    id='location1-dropdown',
                    style={'width': '40%'},
                    options=[{'label': l, 'value': l} for l in location],
                    value='',
                    placeholder="Select location type",
                ),
                html.Button('Submit', id='submit_2', n_clicks=0),
                html.Div(id='poi1-output'),
                html.Div(id='location1-output'),


            ]
        )

])


#call back to fetch value for poi
@app.callback(
    Output('poi-output', 'children'),
    Input('submit_1', 'n_clicks'),
    State('poi-dropdown', 'value')
)
def update_output(n_clicks, value):
    print(value)
    query_1['poi'] = value
    return 'The selected point of interest "{}"'.format(
        value
    )


#call back to fetch value for location type (town/county)
@app.callback(
    Output('location-output', 'children'),
    Input('submit_1', 'n_clicks'),
    State('location-dropdown', 'value')
)
def update_output(n_clicks, value):
    query_1['location-type'] = value
    print(value)
    return 'The selected location. "{}"'.format(
        value
    )


#call back to fetch location eg. dublin/cork
@app.callback(
    Output('location-town-county-output', 'children'),
    Input('submit_1', 'n_clicks'),
    State('location-town-county-dropdown', 'value')
)
def update_output(n_clicks, value):
    query_1['location'] = value
    print(value)
    print(query_1)
    return 'The selected location. "{}"'.format(
        value
    )


#callback to chain the dropdowns
@app.callback(
    dash.dependencies.Output('location-town-county-dropdown', 'options'),
    [dash.dependencies.Input('location-dropdown', 'value')])
def set_cities_options(value):
    return counties if value == 'County' else towns







# @app.callback(
# #     Output('poi1-output', 'children'),
# #     Input('submit_2', 'n_clicks'),
# #     State('poi1-dropdown', 'value')
# # )
# # def update_output(n_clicks, value):
# #     query_1['poi'] = value
# #     return 'The selected point of interest "{}"'.format(
# #
# #         value
# #     )
# #
# # @app.callback(
# #     Output('location1-output', 'children'),
# #     Input('submit_2', 'n_clicks'),
# #     State('location1-dropdown', 'value')
# # )
# # def update_output(n_clicks, value):
# #     query_1['location'] = value
# #     return 'The selected location. "{}"'.format(
# #         value
# #     )
if __name__ == '__main__':
    app.run_server(debug=True)
