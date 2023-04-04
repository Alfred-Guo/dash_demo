# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 08:24:36 2023

@author: Alfred
"""
from dash import html, dcc
from dash.dependencies import Input, Output

from models.OHLC import OHLC
from callbacks.OHLC import render1, render5, render10

from server import app

# data
ohlc = OHLC()

# components
def color():
    if ohlc.diff() == 0:
        _color = 'White'
    elif ohlc.diff() > 0:
        _color = 'Green'
    else:
        _color = 'Red'
    return {'color': _color}

brief = html.Div(
    [
        html.H3('Shantui Construction Machinery Co Ltd'),
        html.H1(ohlc.close(), style=color()),
        html.H4(
            '+' if ohlc.diff() > 0 else '' + '{diff:.4f}\t({pa:.4%})'.format(
                diff=ohlc.diff(), pa=ohlc.pa()
            ),
            style=color(),
        ),
    ]
)

tabs = dcc.Tabs(
    id='tabs', value='1d',
    children = [
        dcc.Tab(
            label='%sd' % i, value='%sd' % i, 
            children=[dcc.Graph(id='g%s' % i)],
        )
        for i in [1, 5, 10]
    ]
)

table = html.Table(
    [
        html.Thead(
            html.Tr([html.Th(col) for col in ohlc.df.columns])
        ),
        html.Tbody(
            [
                html.Tr(
                    [
                        html.Td('%.2f' % ohlc.df.iloc[i][col])
                        for col in ohlc.df.columns
                    ]
                )
                for i in range(min(len(ohlc.df), 10))
            ]
        )
    ]
)

Tabs = dcc.Tabs(
    id='Tabs', value='Chart',
    children = [
        dcc.Tab(label='Chart', value='Chart', children=[tabs]),
        dcc.Tab(label='Historical Data', value='Historical Data', children=[table]),
    ]
)

# layout
app.layout = html.Div(
    [
         brief,
         Tabs,
    ]
)

# callback
@app.callback(
    Output('g1', 'figure'),
    Input('tabs', 'value')
)
def render_tab1(tab):
    return render1(tab, ohlc.df)

@app.callback(
    Output('g5', 'figure'),
    Input('tabs', 'value')
)
def render_tab5(tab):
    return render5(tab, ohlc.df)

@app.callback(
    Output('g10', 'figure'),
    Input('tabs', 'value')
)
def render_tab10(tab):
    return render10(tab, ohlc.df)


if __name__ == '__main__':
    app.run_server(debug=False)
    # app.run_server(debug=True)
    