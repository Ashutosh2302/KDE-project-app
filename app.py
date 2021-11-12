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

query = '''SELECT    ?s ?p ?o
WHERE    {    
?s    ?p    ?o    .
}'''
url = f'http://DESKTOP-CLRQH7Q:7200/repositories/KDE-project?query={query}'

counties = []

selectAllCountiesQuery = '''PREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0A
PREFIX%20ours%3A%20%3Chttp%3A%2F%2Fwww.semanticweb.org%2Fashutoshbansal%2Fontologies%2F2021%2F10%2Fproject-ontology%3E%0A
select DISTINCT ?county where { 
    ?county rdf:type ours:county .
}'''
urlForSelectAllCounties = f'http://DESKTOP-CLRQH7Q:7200/repositories/KDE-project?query={selectAllCountiesQuery}'    #Needs to be updated for every separate local machine

#res = requests.request('GET', urlForSelectAllCounties)
#print(res.text)
#counties = [res.text]   #Need to convert this string into an array of individual values
app = dash.Dash(__name__)


selectedCounty = '';
selectedSiteType = '';

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(style={'backgroundColor' : '#EEEEEE'}, 
                      children=[
                          
    html.Div(
        style={'backgroundColor' : '#1d6b01', 'position' : 'center', 'height' : '20vh' },
        children=[
            html.H1(children='Query Historic Knowledge Graph', style = {'textAlign': 'center', 'verticalAlign': 'middle', 'line-height': '20vh', 'color':'white'})]),
    
            html.H3(children = 'Select a historical site of interest: ', style={'padding-top': '2.5vh', 'padding-left': '2.5vh'}),
            
            dcc.Dropdown(
                id = 'site-dropdown',
                options = [
                    {'label': 'Pilgrim Paths', 'value': 'PP'},
                    {'label': 'Walled Towns', 'value': 'WT'},
                    {'label': 'Landmarks', 'value': 'LM'},
                    {'label': 'Museums', 'value': 'MS'},
                    {'label': 'All of the above', 'value': 'ALL'}],
                style={'width' : '40vh', 'padding-left': '2.5vh'},
                value=''
                ),
            html.Div(id='dd-type-container', style = {'display': 'none'}),

        
            html.H3(children = 'Select a county of interest: ', style={'padding-top': '2.5vh', 'padding-left': '2.5vh'}),
            
    
        dcc.Dropdown(
        id='county-dropdown',
          options=[
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
             ],
           style={'width' : '40vh', 'padding-left': '2.5vh'},
         value='',
         ),
        html.Div(id='dd-county-container'),
       
        html.H3(children = 'Select a town of interest: ', style={'padding-top': '2.5vh', 'padding-left': '2.5vh'}),
            
            dcc.Dropdown(
                id = 'town-dropdown',
                options = [
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
                    ],
                style={'width' : '40vh', 'padding-left': '2.5vh'}),
            
            #html.P(selectedSiteType),

        ])


@app.callback(
    Output('dd-county-container', 'children'),
    Input('county-dropdown', 'value')
    )
def update_output(value):
    return 'Selected county: "{}" '.format(value)

@app.callback(
    Output('dd-type-container', 'children'),
    Input('site-dropdown', 'value'))

def update_output(value) :
    selectedSiteType = value;
    return 'Selected type: "{}" '.format(value);



if __name__ == '__main__':
    app.run_server(debug=True)






