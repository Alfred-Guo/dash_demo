# -*- coding: utf-8 -*-

from dash import Dash

app = Dash(
    __name__,
    suppress_callback_exceptions=True
)

app.title = 'dash_demo'

server = app.server