'''
 # @ Create Time: 2022-04-04 15:34:01.269310
'''
from dash import Dash, html, dcc, Input, Output
from containers.home import home_page
from dotenv import load_dotenv


# Load in environment variables
load_dotenv(override=True, verbose=True)


# global app definition
app = Dash(
    __name__,
    title="App Heroku Dash App",
    update_title=None,
    prevent_initial_callbacks=True,
    suppress_callback_exceptions=True,
)

# Heroku server hook
server = app.server


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname: str):
    """Generate the page content based on the pathname"""
    return html.Div(
        [home_page(app)],
        style={"backgroundColor": "#fff"})


app.layout = html.Div([
    # represents the URL bar, doesn't render anything
    dcc.Location(id='url', refresh=False),

    # content will be rendered in this element
    html.Div(id='page-content',
             style={"backgroundColor": "#202124"}
             ),

], style={"position": "relative", "minHeight": "100vh", 'backgroundColor': '#202124'})


if __name__ == '__main__':
    app.run_server(debug=True, threaded=True)
