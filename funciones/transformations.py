def day_mapper(day):
    if day > 5:
        day = 'fin de semana'
    else:
        day = 'semana'
    return day


def month_mapper(month):
    if month >= 6:
        month = 'segundo semestre'
    else:
        month = 'primer semestre'
    return month



