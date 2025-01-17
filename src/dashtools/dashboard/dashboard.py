'''
 # @ Create Time: 2022-10-04 15:30:29.442976
'''
import logging
import os
import sys
import webbrowser
from contextlib import contextmanager
from pathlib import Path

import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import Dash, dcc, html
from dash_iconify import DashIconify
from dashtools import version

try:
    import callbacks
except ModuleNotFoundError:
    from . import callbacks

app = Dash(
    title="DashTools - Application Management Dashboard",
    update_title=None,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
    prevent_initial_callbacks=True,
    assets_folder=Path(__file__).parent.absolute().joinpath('assets'),
    name=__name__
)

# Declare server for Heroku deployment. Needed for Procfile.
server = app.server


sidebar = html.Div(
    [
        html.Div(id='hidden-div'),
        dmc.Center([
            DashIconify(icon='heroicons:command-line-20-solid',
                        height=60, style={'margin-bottom': '8px', 'margin-right': '5px'}),
            html.H2("DashTools", className='dashtools-logo'),
        ]),
        dmc.Space(h=1, style={'margin-top': '-20px'}),
        html.H6(
            "Application Management Dashboard",
            style={'font-weight': 'inherit', 'font-size': '14px'}
        ),


        dbc.Nav(
            [
                # dbc.NavLink( # TODO
                #     [
                #         DashIconify(icon='akar-icons:plus',
                #                     style={'margin-right': '5px'}),
                #         "Create"
                #     ], href="/create", active="exact"),
                dbc.NavLink(
                    [
                        DashIconify(icon='akar-icons:cloud',
                                    style={'margin-right': '5px'}),
                        "Deploy"
                    ], href="/deploy", active="exact"),
                # dbc.NavLink(  # TODO
                #     [
                #         DashIconify(icon='akar-icons:info',
                #                     style={'margin-right': '5px'}),
                #         "Info"
                #     ], href="/info", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),

        dmc.Space(style={'height': '460px'}),
        html.Hr(),
        html.Div([
            html.H6(
                [
                    html.A(
                        [
                            DashIconify(
                                icon='logos:pypi',
                                width=20,
                                style={'margin-right': '10px'}),
                            f'PyPi v{version.__version__}',
                        ],
                        href="https://pypi.org/project/dash-tools/", target='_blank', style={'text-decoration': 'none', 'color': 'black', 'font-weight': 'lighter'}),
                ]),
            html.H6(
                [
                    html.A(
                        [
                            DashIconify(
                                icon='file-icons:readthedocs',
                                width=15,
                                style={'margin-right': '10px', 'margin-left': '5px'}),
                            f'Read the Docs',
                        ],
                        href="https://dash-tools.readthedocs.io/en/latest/index.html", target='_blank', style={'text-decoration': 'none', 'color': 'black', 'font-weight': 'lighter'}),
                ]),
            html.H6(
                [
                    html.A(
                        [
                            DashIconify(
                                icon='ant-design:github-filled',
                                width=20,
                                style={'margin-right': '8px', 'margin-left': '2px'}),
                            f'GitHub',
                        ],
                        href="https://github.com/andrew-hossack/dash-tools", target='_blank', style={'text-decoration': 'none', 'color': 'black', 'font-weight': 'lighter'}),
                ]),
        ]),
    ],
    style={
        "position": "fixed",
        "top": 0,
        "left": 0,
        "bottom": 0,
        "width": "20rem",
        "padding": "2rem 1rem",
        "background-color": "#f8f9fa",
    },

)

content = html.Div(
    id="page-content", style={
        "margin-left": "22rem",
        "margin-right": "2rem",
        "padding": "2rem 1rem",
    })

app.layout = dmc.NotificationsProvider(
    html.Div(
        [
            html.Div(id="notifications-container-file-explorer"),
            html.Div(id="notifications-container-file-generator"),
            dcc.Location(id="url"),
            sidebar,
            content
        ]))

callbacks.generate_callbacks(app)


def start_dashboard(**args):
    """
    Execute plotly server with only ERROR level logging
    """

    @contextmanager
    def silence_stdout():
        old_target = sys.stdout
        try:
            with open(os.devnull, "w") as new_target:
                sys.stdout = new_target
                yield new_target
        finally:
            sys.stdout = old_target

    logging.getLogger('werkzeug').setLevel(logging.ERROR)
    logging.getLogger(__name__).setLevel(logging.ERROR)

    with silence_stdout():
        webbrowser.open('http://127.0.0.1:8050/')
        app.run_server(**args)
