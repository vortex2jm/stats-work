import modules.df_data as df
import plotly.graph_objects as go
from plotly.subplots import make_subplots

colors_scheme = {
    'background': '#232323',
    'text': '#FFFFFF',
    'band_colors': ['#317A24', '#FFF000', '#B10505']
}

# =============================
amount_per_rating_label = ['0 - 0.9', '1.0 - 1.9', '2.0 - 2.9', '3.0 - 3.9', '4.0 - 4.9','5.0 - 5.9', '6.0 - 6.9', '7.0 - 7.9', '8.0 - 8.9', '9.0 - 9.9', '10', 'Sem avaliações']
amount_per_rating_graph = go.Figure(data=[go.Bar(
    x=amount_per_rating_label,
    y=df.amount_per_rating, 
    text=df.amount_per_rating, 
    textposition='auto', 
    marker_color='#AA14FF'
)])
amount_per_rating_graph.update_layout(
    # title_text='Quantidade de filmes por nota de avaliação',
    plot_bgcolor=colors_scheme['background'],
    paper_bgcolor=colors_scheme['background'],
    font_color=colors_scheme['text']
)

# =============================
amount_per_band_label = ['Verde', 'Amarela', 'Vermelha']
amount_per_band_values = [df.gyr_band_amount[0], df.gyr_band_amount[1], df.gyr_band_amount[2]]
amount_per_band_graph = go.Figure(data=[go.Pie(values=amount_per_band_values, labels=amount_per_band_label, pull=[0.2, 0.2, 0.2])])
amount_per_band_graph.update_layout(
    # title_text='Quantidade de filmes por classificação etária',
    plot_bgcolor=colors_scheme['background'],
    paper_bgcolor=colors_scheme['background'],
    font_color=colors_scheme['text']
)
amount_per_band_graph.update_traces(marker=dict(colors=colors_scheme['band_colors']))

# =============================
band_rating_label = amount_per_rating_label
specs = [[{}, {}, {}]]

gbr_graph = make_subplots(rows=1, cols=3, specs=specs)
gbr_graph.add_trace(go.Bar(
    name='Verde',
    x=band_rating_label, 
    y=df.green_band_rating_percentage, 
    marker=dict(color=colors_scheme['band_colors'][0]),
    text=df.green_band_rating_percentage,
    textposition='outside'    
),1, 1)
gbr_graph.add_trace(go.Bar(
    name='Amarela',
    x=band_rating_label, 
    y=df.yellow_band_rating_percentage, 
    marker=dict(color=colors_scheme['band_colors'][1]),
    text= df.yellow_band_rating_percentage,
    textposition='outside'   
), 1, 2)
gbr_graph.add_trace(go.Bar(
    name='Vermelha',
    x=band_rating_label, 
    y=df.red_band_rating_percentage, 
    marker=dict(color=colors_scheme['band_colors'][2]),
    text= df.red_band_rating_percentage,
    textposition='outside'
), 1, 3)

# gbr_graph.update_traces(hole=.4)
gbr_graph.update_layout(
    # title_text='Avaliações em uma determinada faixa por classificação etária',
    annotations=[dict(text='', x=0.12, y=0.5, font_size=20, showarrow=False),
                 dict(text='', x=0.5, y=0.5, font_size=20, showarrow=False),
                 dict(text='', x=0.9, y=0.5, font_size=20, showarrow=False)],
    plot_bgcolor=colors_scheme['background'],
    paper_bgcolor=colors_scheme['background'],
    font_color=colors_scheme['text']
)

# =============================
date_range = ['1926 - 1930', '1931 - 1940', '1941 - 1950', '1951 - 1960', '1961 - 1970', \
'1971 - 1980', '1981 - 1990', '1991 - 2000', '2001 - 2010', '2011 - 2020', '2021 - 2023']

specs = [[{}, {}, {}]]

gb_date_graph = make_subplots(rows=1, cols=3, specs=specs)
gb_date_graph.add_trace(go.Bar(
    name='Verde',
    x=date_range, 
    y=df.gree_band_years, 
    marker=dict(color=colors_scheme['band_colors'][0]),
    text=df.gree_band_years,
    textposition='outside'    
), 1, 1)
gb_date_graph.add_trace(go.Bar(
    name='Amarela',
    x=date_range, 
    y=df.yellow_band_years, 
    marker=dict(color=colors_scheme['band_colors'][1]),
    text=df.yellow_band_years,
    textposition='outside'
), 1, 2)
gb_date_graph.add_trace(go.Bar(
    name='Vermelha',
    x=date_range, 
    y=df.red_band_years, 
    marker=dict(color=colors_scheme['band_colors'][2]),
    text=df.red_band_years,
    textposition='outside'
), 1, 3)
# gb_date_graph.update_traces(hole=.4)
gb_date_graph.update_layout(
    # title_text='Quantidade de filmes em cada classificação etária por data de lançamento',
    annotations=[dict(text='', x=0.12, y=0.5, font_size=20, showarrow=False),
                 dict(text='', x=0.5, y=0.5, font_size=20, showarrow=False),
                 dict(text='', x=0.9, y=0.5, font_size=20, showarrow=False)],
    plot_bgcolor=colors_scheme['background'],
    paper_bgcolor=colors_scheme['background'],
    font_color=colors_scheme['text']
)

# =============================
rating_avarage_by_year_graph = go.Figure(data=[go.Bar(
    x=date_range, 
    y=df.avarage_rating_by_year, 
    text=df.avarage_rating_by_year,
    textposition='auto',
    marker_color='#AA14FF'
)])
rating_avarage_by_year_graph.update_layout(
    # title_text='Média das avaliações por data de lançamento',
    plot_bgcolor=colors_scheme['background'],
    paper_bgcolor=colors_scheme['background'],
    font_color=colors_scheme['text']
)

# =============================
rating_avarage_by_band_graph = go.Figure(data=[
    go.Bar(
    x=amount_per_band_label, 
    y=[df.gb_avarage_rating, df.yb_avarage_rating, df.rb_avarage_rating],
    text=[df.gb_avarage_rating, df.yb_avarage_rating, df.rb_avarage_rating],
    textposition='auto'    
)])
rating_avarage_by_band_graph.update_traces(marker=dict(color=colors_scheme['band_colors']))
rating_avarage_by_band_graph.update_layout(
    # title_text='Média das avaliações por classificação etária',
    plot_bgcolor=colors_scheme['background'],
    paper_bgcolor=colors_scheme['background'],
    font_color=colors_scheme['text']
)
