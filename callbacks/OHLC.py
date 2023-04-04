# -*- coding: utf-8 -*-
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def render1(tab, df):
    if tab == '1d':
        fig = make_subplots(
            rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.03,
            subplot_titles=('OHLC', 'Volume'), row_width=[0.2, 0.7]
        )
        
        fig.add_trace(
            go.Candlestick(
                x=df.index,
                open=df['开盘'], high=df['最高'], low=df['最低'], close=df['收盘'],
                name='OHLC'
            ),
            row=1, col=1
        )

        fig.add_trace(
            go.Bar(x=df.index, y=df['成交量'], showlegend=False), row=2, col=1)

        fig.update(layout_xaxis_rangeslider_visible=False)
        return fig
    return go.Figure()

def render5(tab, df):
    if tab == '5d':
        rolling = df['收盘'].rolling(5).mean()
        fig = go.Figure(
            go.Scatter(
                x=rolling.index,
                y=rolling.values,
                mode='lines',
            ),
        )
        return fig
    return go.Figure()

def render10(tab, df):
    if tab == '10d':
        rolling = df['收盘'].rolling(10).mean()
        fig = go.Figure(
            go.Scatter(
                x=rolling.index,
                y=rolling.values,
                mode='lines',
            ),
        )
        return fig
    return go.Figure()


# def render1(tab, df):
#     if tab == '1d':
#         fig = make_subplots(
#             rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.03,
#             subplot_titles=('OHLC', 'Volume'), row_width=[0.2, 0.7]
#         )
        
#         fig.add_trace(
#             go.Candlestick(
#                 x=df.index,
#                 open=df['开盘'], high=df['最高'], low=df['最低'], close=df['收盘'],
#                 name='OHLC'
#             ),
#             row=1, col=1
#         )

#         fig.add_trace(
#             go.Bar(x=df.index, y=df['成交量'], showlegend=False), row=2, col=1)

#         fig.update(layout_xaxis_rangeslider_visible=False)
#         return fig
#     return go.Figure()