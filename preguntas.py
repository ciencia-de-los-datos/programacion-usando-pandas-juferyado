"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():
    rows = len(tbl0.axes[0])
    return rows


def pregunta_02():
    cols = len(tbl0.axes[1])
    return cols


def pregunta_03():
    df = tbl0.groupby(['_c1'])['_c1'].count()
    return df


def pregunta_04():
    df = pd.read_csv("tbl0.tsv", sep="\t")[['_c1', '_c2']]
    df= df.groupby('_c1').mean()['_c2']
    return df


def pregunta_05():
    df = pd.read_csv("tbl0.tsv", sep="\t")[['_c1', '_c2']]
    return df


def pregunta_06():
    df = pd.read_csv("tbl1.tsv", sep="\t")
    l = [ x.upper() for x in df['_c4'].unique()]
    l=sorted(l)
    return l


def pregunta_07():
    """
    Calcule la suma de la _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.

    Rta/
    _c1
    A    37
    B    36
    C    27
    D    23
    E    67
    Name: _c2, dtype: int64
    """
    return


def pregunta_08():
    df = pd.read_csv("tbl0.tsv", sep="\t")
    df['suma'] = df['_c0'] + df['_c2']
    return df


def pregunta_09():
    df = pd.read_csv("tbl0.tsv", sep="\t")
    df['ano'] = df['_c3'].str[:4]
    return df


def pregunta_10():
    a = df.groupby('_c1')['_c2'].apply(list)
    a = a.reset_index()
    a.columns = ['_c0', 'lista']
    s = ':'
    for index, row in a.iterrows():
        row['lista'] = sorted(row['lista'])
        row['lista'] = [str(x) for x in row['lista']]
        row['lista'] = s.join(row['lista'])
    return a


def pregunta_11():
    df = pd.read_csv("tbl1.tsv", sep="\t")
    a = df.groupby('_c0')['_c4'].apply(list)
    a = a.reset_index()
    a.columns = ['_c0', 'lista']
    s = ','
    for index, row in a.iterrows():
        row['lista'] = [str(x) for x in sorted(row['lista'])]
        row['lista'] = s.join(row['lista'])
        a.loc[index, 'lista'] = row['lista']
    return a


def pregunta_12():
    df = pd.read_csv("tbl2.tsv", sep="\t")
    a = df.groupby('_c0')[['_c5a', '_c5b']].apply(lambda g: list(map(tuple, g.values.tolist())))
    a = a.reset_index()
    a.columns = ['_c0', 'lista']
    s = ','
    for index, row in a.iterrows():
        row['lista'] = [x[0]+':'+str(x[1]) for x in sorted(row['lista'])]
        row['lista'] = s.join(row['lista'])
        a.loc[index, 'lista'] = row['lista']
    return a


def pregunta_13():
    df = pd.read_csv("tbl2.tsv", sep="\t")
    a = df.groupby('_c0')[['_c5a', '_c5b']].apply(lambda g: list(map(tuple, g.values.tolist())))
    a = a.reset_index()
    a.columns = ['_c0', 'lista']
    s = ','
    for index, row in a.iterrows():
        row['lista'] = [x[0]+':'+str(x[1]) for x in sorted(row['lista'])]
        row['lista'] = s.join(row['lista'])
        a.loc[index, 'lista'] = row['lista']
    print(a)
    #Respuesta 13

    df1 = pd.read_csv("tbl0.tsv", sep="\t")[['_c0', '_c1']]
    df2 = pd.read_csv("tbl2.tsv", sep="\t")[['_c0', '_c5b']]
    d = pd.merge(df1, df2, on='_c0')
    a=(d.groupby('_c1').sum()['_c5b'])
    return a
