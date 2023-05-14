import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

perc_csv = {'Ху Тао': '\hu_tao_akasha.csv'}


def min_max_norm(x):
    """
    Функция возвращает нормализованный массив
    """
    x_min_max = (x-np.min(x, axis=0))/(np.max(x, axis=0) - np.min(x, axis=0))
    return x_min_max

# 'Max HP', 'ATK', 'DEF', 'EM', 'ER%', CR, CD
def find_optimal_stat(perc_name, xp):

    df = pd.read_csv('base_opti_stat'+perc_csv[perc_name],
                     on_bad_lines='skip', delimiter=r"\t",
                     engine='python')
    df = df.loc[:, ['Crit RatioCrit ValueCrit RateCrit DMG', 'Max HP', 'ATK',
                    'DEF', 'EM', 'ER%', 'Unnamed: 10']]
    df['CR'] = df['Crit RatioCrit ValueCrit RateCrit DMG'].str.split(
        expand=True)[0]
    df['CD'] = df['Crit RatioCrit ValueCrit RateCrit DMG'].str.split(
        expand=True)[2]
    df.drop('Crit RatioCrit ValueCrit RateCrit DMG', axis=1, inplace=True)
    df['ER%'] = df['ER%'].str.replace('%', '')
    df = df.astype(float)
    df.dropna(inplace=True)
    y = df['Unnamed: 10'].values
    y = min_max_norm(y).reshape(-1, 1)
    df.drop('Unnamed: 10', axis=1, inplace=True)
    x = df.values

    ln = LinearRegression()
    ln.fit(x, y)
    xp = xp.reshape(1,-1)
    return round(ln.predict(xp)[0][0]*100, 1)


#opt = find_optimal_stat('Ху Тао', np.asarray([
#    30000.0,  1368.0,   876.0,  140.0,  110.4,  89.0,  160.1]))
#print(round(opt[0][0]*100,1))
