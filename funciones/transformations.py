import pandas as pd


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


def hour_mapper(hour):
    if hour > 0:
        hour = 'madrugada'
    elif 6 < hour <= 12:
        hour = 'mañana'
    elif 13 <= hour <= 18:
        hour = 'tarde'
    else:
        hour = 'noche'
    return hour


def week_name(week):
    aux = 'wd_' + str(week)
    return aux


def month_name(month):
    aux = 'm_' + str(month)
    return aux


def categorize(data, columns: list):
    for column in columns:
        data[column] = pd.Categorical(data[column])
    return data


def pivot_several_functions(data, index: str, columns: str, values: str, function: list):
    table = data.pivot_table(index=index, columns=columns, values=values, aggfunc=function, fill_value=0)
    table_index = table.index.tolist()
    table_columns = [str(i) + '_' + str(j) for i, j in zip(table.columns.get_levels_value(None).tolist(),
                                                           table.columns.get_levels_value(columns).tolist())]
    table = pd.DataFrame(table.values, index=table_index, columns=table_columns)
    return table


def pivot_table(data, index: str, columns: str, values: str, function: str):
    aux = data.pivot_table(index=index, columns=columns, values=values, aggfunc=function, fill_value=0)
    aux_index = aux.index.tolist()
    aux_columns = aux.columns.tolist()
    aux = pd.DataFrame(aux.values, index=aux_index, columns=aux_columns)
    return aux




