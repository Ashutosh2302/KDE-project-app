import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import requests

selectAllCountiesQuery = '''PREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0A
PREFIX%20ours%3A%20%3Chttp%3A%2F%2Fwww.semanticweb.org%2Fashutoshbansal%2Fontologies%2F2021%2F10%2Fproject-ontology%3E%0A
select DISTINCT ?county where {
	?county rdf:type ours:county .
}'''

urlForSelectAllCounties = f'http://LAPTOP-45QEIGK2:7200/repositories/KDE-project?query={selectAllCountiesQuery}'  # Needs to be updated for every separate local machine
#
# @lru_cache(maxsize=10)
def query():
    res = requests.request('GET', urlForSelectAllCounties)
    print(res.text)
    counties = [res.text]  # Need to convert this string into an array of individual values
    print(counties)


query_1 = {'poi': '', 'location-type': '', 'location': ''}
query_2 = {'poi': '', 'location-type': '', 'location': ''}
query_3 = {'poi': '', 'location-type': ''}
query_4 = {'poi': '', 'location-type': '', 'another_poi': '', 'name_of_another_poi': ''}
query_5 = {'poi': '', 'associated-with': '', 'pattern': ''}
query_6 = {'period': '', 'poi': ''}

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = 'Irish History'
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
            html.H2(children='Query Historic Knowledge Graph',
                    style={'textAlign': 'center', 'verticalAlign': 'middle', 'line-height': '20vh', 'color': 'white'})
        ]
    ),
    html.H2(children="Question 1", style={'textAlign': 'center', 'verticalAlign': 'middle', 'line-height': '20vh'}),
    html.Div(
        style={'backgroundColor': '#FFFF00'},
        children=[
            html.H4(children="Select point of interest"),

            dcc.Dropdown(
                id='poi-dropdown',
                style={'width': '60%'},
                options=[{'label': poi, 'value': poi} for poi in points_of_interest],
                value='',
                multi=True,
                placeholder="Select a point of interest",
            ),
            html.H4(children="Select location type"),
            dcc.Dropdown(
                id='location-dropdown',
                style={'width': '40%'},
                options=[{'label': l, 'value': l} for l in location],
                value='',
                placeholder="Select location type",
            ),
            html.H4(children=f"Select {query_1['location-type']}"),
            dcc.Dropdown(
                id='location-town-county-dropdown',
                style={'width': '40%'},
            ),
            html.Button('Submit', id='submit_1', n_clicks=0),
            html.Div(id='query1-output'),

        ]
    ),

    html.H2(children="Question 2", style={'textAlign': 'center', 'verticalAlign': 'middle', 'line-height': '20vh'}),
    html.Div(
        style={'backgroundColor': '#FFFF00'},
        children=[
            html.H4(children="Select point of interest"),

            dcc.Dropdown(
                id='poi-dropdown-2',
                style={'width': '60%'},
                options=[{'label': poi, 'value': poi} for poi in points_of_interest],
                value='',
                multi=True,
                placeholder="Select a point of interest",
            ),
            html.H4(children="Select location type"),
            dcc.Dropdown(
                id='location-dropdown-2',
                style={'width': '40%'},
                options=[{'label': l, 'value': l} for l in location],
                value='',
                placeholder="Select location type",
            ),
            html.H4(children=f"Select town/county"),
            dcc.Dropdown(
                id='location-town-county-dropdown-2',
                style={'width': '40%'},
            ),

            html.Button('Submit', id='submit_2', n_clicks=0),
            html.Div(id='query2-output'),

        ]
    ),

    html.H2(children="Get max and min POI", style={'textAlign': 'center', 'verticalAlign': 'middle', 'line-height': '20vh'}),
    html.Div(
        style={'backgroundColor': '#FFFF00'},
        children=[
            html.H4(children="Select point of interest"),

            dcc.Dropdown(
                id='poi-dropdown-3',
                style={'width': '60%'},
                options=[{'label': poi, 'value': poi} for poi in points_of_interest],
                value='',
                multi=True,
                placeholder="Select a point of interest",
            ),
            html.H4(children="Select location type"),
            dcc.Dropdown(
                id='location-dropdown-3',
                style={'width': '40%'},
                options=[{'label': l, 'value': l} for l in location],
                value='',
                placeholder="Select location type",
            ),

            html.Button('Submit', id='submit_3', n_clicks=0),
            html.Div(id='query3-output'),

        ]
    ),

    html.H2(children="List names of Poi in town/county where any other poi exists",
            style={'textAlign': 'center', 'verticalAlign': 'middle', 'line-height': '20vh'}),
    html.Div(
        style={'backgroundColor': '#FFFF00'},
        children=[
            html.H4(children="Select point of interest you want to know about"),

            dcc.Dropdown(
                id='poi-dropdown-4',
                style={'width': '60%'},
                options=[{'label': poi, 'value': poi} for poi in points_of_interest],
                value='',
                multi=True,
                placeholder="Select point(s) of interest",
            ),
            html.H4(children="Select location type"),
            dcc.Dropdown(
                id='location-dropdown-4',
                style={'width': '40%'},
                options=[{'label': l, 'value': l} for l in location],
                value='',
                placeholder="Select location type",
            ),

            html.H4(children="Select a Poi"),

            dcc.Dropdown(
                id='another-poi-dropdown-4',
                style={'width': '60%'},
                options=[{'label': poi, 'value': poi} for poi in points_of_interest],
                value='',
                placeholder="Select point of interest",
            ),
            #another dropdown for names of another poi
            html.H4(children="Select a name"),

            dcc.Dropdown(
                id='poi-choice',
                style={'width': '60%'},

                value='',

            ),
            html.Button('Submit', id='submit_4', n_clicks=0),
            html.Div(id='query4-output'),

        ]
    ),

    html.H2(children="List names of POI(s) associated with any given year/historicCentury/historicalPeriod",
            style={'textAlign': 'center', 'verticalAlign': 'middle', 'line-height': '20vh'}),
    html.Div(
        style={'backgroundColor': '#FFFF00'},
        children=[
            html.H4(children="Select point of interest you want to know about"),

            dcc.Dropdown(
                id='poi-dropdown-5',
                style={'width': '60%'},
                options=[{'label': poi, 'value': poi} for poi in points_of_interest],
                value='',
                multi=True,
                placeholder="Select point(s) of interest",
            ),
            html.H4(children="Select location type"),
            dcc.Dropdown(
                id='period-dropdown',
                style={'width': '40%'},
                options=[
                    {'label': 'year', 'value': 'year'},
                    {'label': 'historicCentury', 'value': 'historicCentury'},
                    {'label': 'historicalPeriod', 'value': 'historicalPeriod'},
                ],
                value='',
                placeholder="Select period",
            ),
            html.H4(children="Pattern"),
            dcc.Dropdown(
                id='pattern-dropdown',
                style={'width': '40%'},
                value='',
                placeholder="Select pattern",
            ),

            html.Button('Submit', id='submit_5', n_clicks=0),
            html.Div(id='query5-output'),

        ]
    ),

    html.H2(children="Get year/historicCentury/historicalPeriod with min and max POI(s) associated with it",
            style={'textAlign': 'center', 'verticalAlign': 'middle', 'line-height': '20vh'}),
    html.Div(
        style={'backgroundColor': '#FFFF00'},
        children=[
            html.H4(children="Select period type"),
            dcc.Dropdown(
                id='period-dropdown-6',
                style={'width': '40%'},
                options=[
                    {'label': 'year', 'value': 'year'},
                    {'label': 'historicCentury', 'value': 'historicCentury'},
                    {'label': 'historicalPeriod', 'value': 'historicalPeriod'},
                ],
                value='',
                placeholder="Select period",
            ),
            html.H4(children="Select point of interest you want to know about"),
            dcc.Dropdown(
                id='poi-dropdown-6',
                style={'width': '60%'},
                options=[{'label': poi, 'value': poi} for poi in points_of_interest],
                value='',
                multi=True,
                placeholder="Select point(s) of interest",
            ),

            html.Button('Submit', id='submit_6', n_clicks=0),
            html.Div(id='query6-output'),

        ]
    )

])


@app.callback(
    Output('query1-output', 'children'),
    Input('submit_1', 'n_clicks'),
    State('poi-dropdown', 'value'),
    State('location-dropdown', 'value'),
    State('location-town-county-dropdown', 'value'),
    prevent_initial_call=True
)
def update_output(n_clicks, poi, location_type, location):

    query_1['poi'] = poi
    query_1['location-type'] = location_type
    query_1['location'] = location
    print(f"query 1: {query_1}")
    return f'POI: {poi}, location type: {location_type}, location: {location}'


# callback to chain the dropdowns
@app.callback(
    dash.dependencies.Output('location-town-county-dropdown', 'options'),
    [dash.dependencies.Input('location-dropdown', 'value')],
    prevent_initial_call=True)
def set_cities_options(value):
    return counties if value == 'County' else towns



@app.callback(
    Output('query2-output', 'children'),
    Input('submit_2', 'n_clicks'),
    State('poi-dropdown-2', 'value'),
    State('location-dropdown-2', 'value'),
    State('location-town-county-dropdown-2', 'value'),
    prevent_initial_call=True
)
def update_output(n_clicks, poi, location_type, location):

    query_2['poi'] = poi
    query_2['location-type'] = location_type
    query_2['location'] = location
    print(f"query 2: {query_2}")
    return f'POI: {poi}, location type: {location_type}, location: {location}'


# callback to chain the dropdowns
@app.callback(
    dash.dependencies.Output('location-town-county-dropdown-2', 'options'),
    [dash.dependencies.Input('location-dropdown-2', 'value')],
    prevent_initial_call=True)
def set_cities_options(value):
    return counties if value == 'County' else towns


@app.callback(
    Output('query3-output', 'children'),
    Input('submit_3', 'n_clicks'),
    State('poi-dropdown-3', 'value'),
    State('location-dropdown-3', 'value'),
    prevent_initial_call=True
)
def update_output(n_clicks, poi, location_type):

    query_3['poi'] = poi
    query_3['location-type'] = location_type
    print(f"query 3: {query_3}")
    return f'POI: {poi}, location type: {location_type}'


@app.callback(
    Output('query4-output', 'children'),
    Input('submit_4', 'n_clicks'),
    State('poi-dropdown-4', 'value'),
    State('location-dropdown-4', 'value'),
    State('another-poi-dropdown-4', 'value'),
    prevent_initial_call=True
)
def update_output(n_clicks, poi, location_type, another_poi):

    query_4['poi'] = poi
    query_4['location-type'] = location_type
    query_4['another_poi'] = another_poi

    #TODO: name of another poi using sparql query

    print(f"query 4: {query_4}")
    return f'POI: {poi}, location type: {location_type}, another poi: {another_poi}'


@app.callback(
    Output('query5-output', 'children'),
    Input('submit_5', 'n_clicks'),
    State('poi-dropdown-5', 'value'),
    State('period-dropdown', 'value'),
    State('pattern-dropdown', 'value'),
    prevent_initial_call=True
)
def update_output(n_clicks, poi, period, pattern):

    query_5['poi'] = poi
    query_5['associated-with'] = period
    query_5['pattern'] = ''
    print(f"query 5: {query_5}")
    return f'POI: {poi}, associated_with: {period}, pattern: ""'


@app.callback(
    Output('query6-output', 'children'),
    Input('submit_6', 'n_clicks'),
    State('period-dropdown-6', 'value'),
    State('poi-dropdown-6', 'value'),
    prevent_initial_call=True
)
def update_output(n_clicks, period, poi):

    query_6['period'] = period
    query_6['poi'] = poi
    #TODO: max and min poi(s)
    print(f"query 6: {query_6}")
    return f'period: {period}, poi(s): {poi}"'


if __name__ == '__main__':

    app.run_server(debug=True)
