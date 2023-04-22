import pandas as pd

df = pd.read_csv('./data/movie-reviews.csv', encoding='utf-8')
movies_amount = len(df.index)
print('Total de filmes:', movies_amount)

users_rating_list_string = list(df['User rating'])
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
print('Filmes com avaliações' ,movies_with_rating_amount)
print('Filmes sem avaliações', movies_without_rating_amount)

# maior e menor nota
greatest_user_rating = max(users_rating_list_float, key=float)
smallest_user_rating = min(users_rating_list_float, key=float)

#==================================#
# Quantidade de avaliações por rating
amount_per_rating = [0]*11 #0,1,2,3,4,5,6,7,8,9,10

for rating in users_rating_list_float:
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

print('Quantidade por avaliação' ,amount_per_rating)

#====================================#
# QUAIS SAO AS CLASSIFICAÇÕES E A QUANTIDADE DE CADA
#====================================#
age_rating_list = list(df['Rating'])

green_band = ('| Not Rated', '| Approved', '| TV-G', '| Passed', '| G', '| Unrated', '| NR', '| Open')
yellow_band = (
'| PG-13', '| R', '| TV-PG', '| GP', '| M', '| M/PG', '| PG', '| TV-MA',
'| TV-14','| PG--13', '| PG-13`', '| TV-Y7', '| TV-Y7-FV')
red_band = ('| X', '| NC-17', '| AO')

# Quantidade de filmes por banda ======== #
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

print('Quantidade de filmes por banda (green, yellow, red)',gyr_band_amount[0], gyr_band_amount[1], gyr_band_amount[2])


# ================ BAND X RATING ===================== #
def get_index_by_rating(rating):
    if rating >= 0 and rating < 1.0:
        return 0
    elif rating >= 1.0 and rating < 2.0:
        return 1
    elif rating >= 2.0 and rating < 3.0:
        return 2
    elif rating >= 3.0 and rating < 4.0:
        return 3
    elif rating >= 4.0 and rating < 5.0:
        return 4
    elif rating >= 5.0 and rating < 6.0:
        return 5
    elif rating >= 6.0 and rating < 7.0:
        return 6
    elif rating >= 7.0 and rating < 8.0:
        return 7
    elif rating >= 8.0 and rating < 9.0:
        return 8
    elif rating >= 9.0 and rating < 10.0:
        return 9
    elif rating >= 10:
        return 10
    else:
        return 11

#================================#
green_band_rating_amount = [0]*12
yellow_band_rating_amount = [0]*12
red_band_rating_amount = [0]*12

df_b = df
for movie in df_b.itertuples():
    if movie[4] == 'tbd':
        df_b = df_b.drop(movie[0])

for movie in df_b.itertuples():
    if movie[3] in green_band:
        green_band_rating_amount[get_index_by_rating(float(movie[4]))] += 1
    elif movie[3] in yellow_band:
        yellow_band_rating_amount[get_index_by_rating(float(movie[4]))] += 1
    elif movie[3] in red_band:
        red_band_rating_amount[get_index_by_rating(float(movie[4]))] += 1
    else:
        green_band_rating_amount[get_index_by_rating(float(movie[4]))] += 1

print('Avaliações na banda verde',green_band_rating_amount)
print('Avaliações na banda amarela', yellow_band_rating_amount)
print('Avaliações na banda vermelha', red_band_rating_amount)
