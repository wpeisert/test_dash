# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
external_stylesheets = [dbc.themes.BOOTSTRAP]

print(external_stylesheets)

app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ]
)

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

df = pd.read_csv("app/flights.csv").head(5000)


# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# SIDEBAR
sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.P(
            "A simple sidebar layout with navigation links", className="lead"
        ),
    ],
    style=SIDEBAR_STYLE,
)

# MAIN PANEL
content = html.Div(
    [
        html.H3("MAIN PANEL"),
        html.H1(children='Hello Dash'),

        html.Div(children='''
            Dash: A web application framework for Python.
        '''),

        dcc.Graph(
            id='example-graph',
            figure=fig
        )
    ]
    ,style=CONTENT_STYLE)

#app.layout = html.Div([sidebar, content])

# APP LAYOUT
app.layout = html.Div(
    [
        dbc.Row(dbc.Col(html.H2("Dash title"))),

        # SECTION 1
        html.Hr(),
        dbc.Row([
            dbc.Col(
                html.Div("This is section number 1"), width="sm"
            ),
            dbc.Col(
                html.Div("This is section number 2"), width="sm"
            ),
            dbc.Col(
                html.Div("This is section number 3"), width="sm"
            ),
            dbc.Col(
                html.Div("This is section number 4"), width="sm"
            )
        ]),

        html.Hr(),
        html.Br(),

    ])

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=False)
