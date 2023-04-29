import modules.graphs as gp
from dash import Dash, dcc, html

app = Dash(__name__)
app.title = 'Stats'

app.layout = html.Div(
    children=[
        dcc.Graph(id='2', figure=gp.amount_per_rating_graph),
        dcc.Graph(id='3', figure=gp.amount_per_band_graph),
        dcc.Graph(id='4', figure=gp.gbr_graph),
        dcc.Graph(id='8', figure=gp.gb_date_graph),
        dcc.Graph(id='9', figure=gp.rating_avarage_by_year_graph),
        dcc.Graph(id='10', figure=gp.rating_avarage_by_band_graph)
    ]
)

if __name__ == '__main__':
    app.run_server()
