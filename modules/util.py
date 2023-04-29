def get_index_by_rating(rating):
    try:
        rating = float(rating)
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
    except:
        return 11
    
def get_index_by_year(year):
    if year > 25 and year <= 30:
        return 0
    if year > 30 and year <= 40:
        return 1
    if year > 40 and year <= 50:
        return 2
    if year > 50 and year <= 60:
        return 3
    if year > 60 and year <= 70:
        return 4
    if year > 70 and year <= 80:
        return 5
    if year > 80 and year <= 90:
        return 6
    if year > 90 and year <= 99 or year == 0:
        return 7
    if year > 0 and year <= 10:
        return 8
    if year > 10 and year <= 20:
        return 9
    if year > 20 and year <= 23:
        return 10
