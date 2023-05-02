import modules.graphs as gp
from dash import Dash, dcc, html

app = Dash(__name__)
app.title = 'Stats'

text_style = {
    'textAlign': 'center',
    'color': gp.colors_scheme['text']
}

app.layout = html.Div(style={'backgroundColor': gp.colors_scheme['background']},
    children=[
        html.H1(children="Quantidade de filmes por nota de avaliação", style=text_style),
        dcc.Graph(id='2', figure=gp.amount_per_rating_graph),
        html.H1(children="Quantidade de filmes por classificação etária", style=text_style),
        dcc.Graph(id='3', figure=gp.amount_per_band_graph),
        html.H1(children="Avaliações em uma determinada faixa para diferentes classificações etárias (percentual)", style=text_style),
        dcc.Graph(id='4', figure=gp.gbr_graph),
        html.H1(children="Quantidade de filmes por data de lançamento para diferentes classificações etárias ", style=text_style),
        dcc.Graph(id='8', figure=gp.gb_date_graph),
        html.H1(children="Média das avaliações por data de lançamento", style=text_style),
        dcc.Graph(id='9', figure=gp.rating_avarage_by_year_graph),
        html.H1(children="Média das avaliações por classificação etária", style=text_style),
        dcc.Graph(id='10', figure=gp.rating_avarage_by_band_graph),
        html.H1(children="Distribuição das avaliações ao longo dos anos", style=text_style),
        html.H2(children="Faixa verde", style=text_style),
        dcc.Graph(id='11', figure=gp.green_rating_avarage_by_year_graph),
        html.H2(children="Faixa amarela", style=text_style),
        dcc.Graph(id='12', figure=gp.yellow_rating_avarage_by_year_graph),
        html.H2(children="Faixa vermelha", style=text_style),
        dcc.Graph(id='13', figure=gp.red_rating_avarage_by_year_graph)
    ]
)

if __name__ == '__main__':
    app.run_server()
