import math
import pandas as pd
from modules.util import get_index_by_rating, get_index_by_year

df = pd.read_csv('./data/movie-reviews.csv', encoding='utf-8')
movies_amount = len(df.index)

# TOTAL DE FILMES DO DATAFRAME
# print('Total de filmes:', movies_amount)

# COLUNA DE AVALIAÇÕES
users_rating_list_string = list(df['User rating'])

# AVALIAÇÕES VÁLIDAS
users_rating_list_float = []

for i,rating in enumerate(users_rating_list_string):
    try:
        x = float(rating)
        users_rating_list_float.append(x)
    except:
        continue

# quantidade de filmes com e sem avaliação
movies_with_rating_amount = len(users_rating_list_float)
movies_without_rating_amount = movies_amount - movies_with_rating_amount
# print('Filmes com avaliações' ,movies_with_rating_amount)
# print('Filmes sem avaliações', movies_without_rating_amount)

# maior e menor nota
greatest_user_rating = max(users_rating_list_float, key=float)
smallest_user_rating = min(users_rating_list_float, key=float)

#==================================#
# Quantidade de avaliações por nota
#0,1,2,3,4,5,6,7,8,9,10
amount_per_rating = [0]*12 

for rating in users_rating_list_string:
    
    try:
        rating = float(rating)
        if rating >= 0 and rating < 1.0:
            amount_per_rating[0] += 1
        elif rating >= 1.0 and rating < 2.0:
            amount_per_rating[1] += 1
        elif rating >= 2.0 and rating < 3.0:
            amount_per_rating[2] += 1
        elif rating >= 3.0 and rating < 4.0:
            amount_per_rating[3] += 1
        elif rating >= 4.0 and rating < 5.0:
            amount_per_rating[4] += 1
        elif rating >= 5.0 and rating < 6.0:
            amount_per_rating[5] += 1
        elif rating >= 6.0 and rating < 7.0:
            amount_per_rating[6] += 1
        elif rating >= 7.0 and rating < 8.0:
            amount_per_rating[7] += 1
        elif rating >= 8.0 and rating < 9.0:
            amount_per_rating[8] += 1
        elif rating >= 9.0 and rating < 10.0:
            amount_per_rating[9] += 1
        elif rating >= 10:
            amount_per_rating[10] += 1
    except:
        amount_per_rating[11] += 1

# print('Quantidade por avaliação' ,amount_per_rating)

#====================================#
# QUAIS SAO AS CLASSIFICAÇÕES E A QUANTIDADE DE CADA
#====================================#
age_rating_list = list(df['Rating'])

green_band = ('| Not Rated', '| Approved', '| TV-G', '| Passed', '| G', '| Unrated', '| NR', '| Open')
yellow_band = (
'| PG-13', '| R', '| TV-PG', '| GP', '| M', '| M/PG', '| PG', '| TV-MA',
'| TV-14','| PG--13', '| PG-13`', '| TV-Y7', '| TV-Y7-FV')
red_band = ('| X', '| NC-17', '| AO')

# Quantidade de filmes por classificação etária ======== #
# verde, amarela, vermelha
gyr_band_amount = [0]*3

for rating in age_rating_list:
    if rating in green_band:
        gyr_band_amount[0] += 1
    elif rating in yellow_band:
        gyr_band_amount[1] += 1
    elif rating in red_band:
        gyr_band_amount[2] += 1
    else:
        gyr_band_amount[0] += 1

# print('Quantidade de filmes por banda (green, yellow, red)',gyr_band_amount[0], gyr_band_amount[1], gyr_band_amount[2])


# ================ BAND X RATING ===================== #
#================================#
# o ultimo indice eh de filmes sem avaliação
# quantidade de avaliações por nota em cada classificação etária

green_band_rating_amount = [0]*12
yellow_band_rating_amount = [0]*12
red_band_rating_amount = [0]*12

# MÉDIA DE NOTAS DE AVALIAÇÕES EM CADA CLASSIFICAÇÃO ETÁRIA
gb_avarage_rating = 0
gb_avarage_amount = 0

yb_avarage_rating = 0
yb_avarage_amount = 0

rb_avarage_rating = 0
rb_avarage_amount = 0


for movie in df.itertuples():
    if movie[3] in green_band:
        green_band_rating_amount[get_index_by_rating((movie[4]))] += 1
        try:
            gb_avarage_rating += float(movie[4])
            gb_avarage_amount += 1
        except:
            continue

    elif movie[3] in yellow_band:
        yellow_band_rating_amount[get_index_by_rating((movie[4]))] += 1
        try:
            yb_avarage_rating += float(movie[4])
            yb_avarage_amount += 1
        except:
            continue

    elif movie[3] in red_band:
        red_band_rating_amount[get_index_by_rating((movie[4]))] += 1
        try:
            rb_avarage_rating += float(movie[4])
            rb_avarage_amount += 1
        except:
            continue

    else:
        green_band_rating_amount[get_index_by_rating((movie[4]))] += 1
        try:
            gb_avarage_rating += float(movie[4])
            gb_avarage_amount += 1
        except:
            continue

gb_avarage_rating /= gb_avarage_amount
gb_avarage_rating = round(gb_avarage_rating, 2)

yb_avarage_rating /= yb_avarage_amount
yb_avarage_rating = round(yb_avarage_rating, 2)

rb_avarage_rating /= rb_avarage_amount
rb_avarage_rating = round(rb_avarage_rating, 2)

# print('Avaliações por nota na banda verde',green_band_rating_amount)
# print('Avaliações por nota na banda amarela', yellow_band_rating_amount)
# print('Avaliações por nota na banda vermelha', red_band_rating_amount)


# DATES PROCESSING ===============================================#
dates_list = list(df['Release Date'])

# FILMES COM E SEM DATA
years_list = []
no_dates_list = []

for i,date in enumerate(dates_list):
    date = str(date)
    date = date.split('-')
    if len(date) == 3:
        years_list.append(int(date[2]))
    else:
        no_dates_list.append(date)


movies_with_date = len(years_list)
movies_without_date = len(no_dates_list)
# print('filmes com data ', movies_with_date)
# print('Filmes sem data ', movies_without_date)

#=================
# 1926 - 1930
# 1931 - 1940
# 1941 - 1950
# 1951 - 1960
# 1961 - 1970
# 1971 - 1980
# 1981 - 1990
# 1991 - 2000
# 2001 - 2010
# 2011 - 2020
# 2021 - 2023
#=================

# QUANTIDADE DE FILMES POR DATA EM CADA CLASSIFICAÇÃO ETÁRIA
gree_band_years = [0]*11
yellow_band_years = [0]*11
red_band_years = [0]*11

for movie in df.itertuples():
    date = movie[2].split('-')
    if len(date) == 3:
        if movie[3] in green_band:
            gree_band_years[get_index_by_year(int(date[2]))] += 1
        if movie[3] in yellow_band:
            yellow_band_years[get_index_by_year(int(date[2]))] += 1
        if movie[3] in red_band:
            red_band_years[get_index_by_year(int(date[2]))] += 1

# print('Quantidade de filmes por data de produção na banda verde ',gree_band_years)
# print('Quantidade de filmes por data de produção na banda amarela ',yellow_band_years)
# print('Quantidade de filmes por data de produção na banda vermelha ',red_band_years)

# ========================================
# Filmes que têm data e foram avaliados
df_b = df
for movie in df_b.itertuples():
    if movie[4] == 'tbd':
        df_b = df_b.drop(movie[0])

# MÉDIA DE AVALIAÇÕES POR DATA DE LANÇAMENTO
avarage_rating_by_year = [0]*11
avarage_rating_amount_by_year = [0]*11


for movie in df_b.itertuples():
    date = movie[2].split('-')
    if len(date) == 3:
        avarage_rating_by_year[get_index_by_year(int(date[2]))] += float(movie[4])
        avarage_rating_amount_by_year[get_index_by_year(int(date[2]))] += 1


for x in range(len(avarage_rating_by_year)):
    avarage_rating_by_year[x] /= avarage_rating_amount_by_year[x]
    avarage_rating_by_year[x] = round(avarage_rating_by_year[x],2)

# print(avarage_rating_by_year)

#================================
df_green = df
df_green = df_green[df_green['Rating'].apply(lambda x: green_band.__contains__(x))]
    #Muda o tipo da coluna data
df_green['Release Date'] = pd.to_datetime(df_green['Release Date'], errors="coerce", format="mixed")
    #Cria coluna so com os anos
df_green['Release Year'] = df_green['Release Date'].dt.year
    #Ajusta anos maiores que 2023
df_green['Release Year'] = df_green['Release Year'].apply(lambda x: x if x <= 2023 else x-100 if x>2023 and x<2100 else x - 1000)

df_green['User rating'] = pd.to_numeric(df_green['User rating'], errors='coerce')

green_label_amount = len(df_green.index)

df_yellow = df
df_yellow = df_yellow[df_yellow['Rating'].apply(lambda x: yellow_band.__contains__(x))]
df_yellow['Release Date'] = pd.to_datetime(df_yellow['Release Date'], errors="coerce")
df_yellow['Release Year'] = df_yellow['Release Date'].dt.year
df_yellow['Release Year'] = df_yellow['Release Year'].apply(lambda x: x if x <= 2023 else x-100 if x>2023 and x<2100 else x - 1000)
df_yellow['User rating'] = pd.to_numeric(df_yellow['User rating'], errors='coerce')

yellow_label_amount = len(df_yellow.index)

df_red = df
df_red = df_red[df_red['Rating'].apply(lambda x: red_band.__contains__(x))]
df_red['Release Date'] = pd.to_datetime(df_red['Release Date'], errors="coerce")
df_red['Release Year'] = df_red['Release Date'].dt.year
df_red['Release Year'] = df_red['Release Year'].apply(lambda x: x if x <= 2023 else x-100 if x>2023 and x<2100 else x - 1000)
df_red['User rating'] = pd.to_numeric(df_red['User rating'], errors='coerce')

red_label_amount = len(df_red.index)

#================================

green_band_rating_percentage = [0]*12
yellow_band_rating_percentage = [0]*12
red_band_rating_percentage = [0]*12

for i, x in enumerate(green_band_rating_amount):
    green_band_rating_percentage[i] = round(100*(x/green_label_amount),2)

for i, x in enumerate(yellow_band_rating_amount):
    yellow_band_rating_percentage[i] = round(100*(x/yellow_label_amount),2)

for i, x in enumerate(red_band_rating_amount):
    red_band_rating_percentage[i] = round(100*(x/red_label_amount),2)

#===============================

#Quantidade de reviews em cada decada
green_rating_per_decade = [0]*11
green_total_rating_per_decade = [0]*11

for i, row in df_green.iterrows():
    try: 
        arg = int(row['Release Year'])%100
        score = float(row['User rating'])
        if math.isnan(score):
            continue
    except:
        continue
    index = get_index_by_year(arg)

    green_rating_per_decade[index] += 1
    green_total_rating_per_decade[index] += float(row['User rating'])

green_average_rating_per_decade = [0]*11
for i, rating_total in enumerate(green_total_rating_per_decade):
    green_average_rating_per_decade[i] = round(rating_total/green_rating_per_decade[i], 1)

#vvvABANDONADOvvv#

# #Soma de todas as notas em cada ano
# green_total_rating_per_year = pd.Series(data=[0]*len(green_years), index=green_years)
# for year in green_years:
#     relevant_rows = df_green[df_green['Release Year'].apply(lambda x: x == year)]
#     green_total_rating_per_year[year] = relevant_rows['User rating'].sum()

# # Media das notas para cada ano
# green_average_rating_per_year = pd.Series(data=round(green_total_rating_per_year/green_rating_per_year, 2), index=green_years)

#===============================

#Quantidade de reviews em cada decada
yellow_rating_per_decade = [0]*11
yellow_total_rating_per_decade = [0]*11

for i, row in df_yellow.iterrows():
    try: 
        arg = int(row['Release Year'])%100
        score = float(row['User rating'])
        if math.isnan(score):
            continue
    except:
        continue
    index = get_index_by_year(arg)

    yellow_rating_per_decade[index] += 1
    yellow_total_rating_per_decade[index] += float(row['User rating'])

yellow_average_rating_per_decade = [0]*11
for i, rating_total in enumerate(yellow_total_rating_per_decade):
    if yellow_rating_per_decade[i] != 0:
        yellow_average_rating_per_decade[i] = round(rating_total/yellow_rating_per_decade[i], 1)

#vvvABANDONADOvvv#
# yellow_rating_per_year = df_yellow['Release Year'].groupby(df_yellow['Release Year']).count()

# yellow_years = yellow_rating_per_year.index

# yellow_total_rating_per_year = pd.Series(data=[0]*len(yellow_years), index=yellow_years)
# for year in yellow_years:
#     relevant_rows = df_yellow[df_yellow['Release Year'].apply(lambda x: x == year)]
#     yellow_total_rating_per_year[year] = relevant_rows['User rating'].sum()

# yellow_average_rating_per_year = pd.Series(data=round(yellow_total_rating_per_year/yellow_rating_per_year, 2), index=yellow_years)

#===============================

#Quantidade de reviews em cada decada
red_rating_per_decade = [0]*11
red_total_rating_per_decade = [0]*11

for i, row in df_red.iterrows():
    try: 
        arg = int(row['Release Year'])%100
        score = float(row['User rating'])
        if math.isnan(score):
            continue
    except:
        continue
    index = get_index_by_year(arg)

    red_rating_per_decade[index] += 1
    red_total_rating_per_decade[index] += float(row['User rating'])


red_average_rating_per_decade = [0]*11
for i, rating_total in enumerate(red_total_rating_per_decade):
    if red_rating_per_decade[i] != 0:
        red_average_rating_per_decade[i] = round(rating_total/red_rating_per_decade[i], 1)

# red_rating_per_year = df_red['Release Year'].groupby(df_red['Release Year']).count()

# red_years = red_rating_per_year.index

# red_total_rating_per_year = pd.Series(data=[0]*len(red_years), index=red_years)
# for year in red_years:
#     relevant_rows = df_red[df_red['Release Year'].apply(lambda x: x == year)]
#     red_total_rating_per_year[year] = relevant_rows['User rating'].sum()

# red_average_rating_per_year = pd.Series(data=round(red_total_rating_per_year/red_rating_per_year, 2), index=red_years)
