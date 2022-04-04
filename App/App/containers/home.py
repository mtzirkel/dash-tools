# Created on 2022-04-04 15:34:01.270312

import dash_bootstrap_components as dbc
from dash import html, Dash, dcc
import platform
import datetime


def home_page(app: Dash):
    """
    Main landing page for App
    """

    return html.Div([

        html.Div([
            html.Div([
                # Text and Titles
                html.H3(
                    "App Heroku Dash App",
                    style={'padding-top': '10px'},
                ),
                html.H5([
                    "Application Details"
                ], style={'margin-bottom': '0px'}),
                html.Hr(style={'color': 'black',
                               'margin-top': '0px', 'margin-bottom': '30px'}),

                # Application Details
                html.Div(
                    [
                        html.Div([
                            html.H5("Platform"),
                            html.P(platform.platform())
                        ], className='col-md-6'),
                        html.Div([
                            html.H5("Python Version"),
                            html.P(platform.python_version())
                        ], className='col-md-6'),
                        html.Div([
                            html.H5("Dash Version"),
                            html.P(dcc.__version__)
                        ], className='col-md-6'),
                        html.Div([
                            html.H5("Dash Bootstrap Components Version"),
                            html.P(dbc.__version__)
                        ], className='col-md-6'),
                        html.Div([
                            html.H5("Date"),
                            html.P(datetime.datetime.now().strftime(
                                "%Y-%m-%d %H:%M:%S"))
                        ], className='col-md-6'),
                    ],
                    id='app-details',
                ),
            ],
                style={
                    'min-width': '400px',
                    'margin-bottom': '10px',
                    'color': '#444',
                    'padding-bottom': '100px'
            }),
        ],
            style={
                'width': '70%',
        },
            className='center'
        ),
    ],
        style={
            'padding-top': '10px',
            'margin-bottom': '60px',
            'min-height': '100vh',
    },
    )
