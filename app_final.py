import datetime
import functools

import numpy as np
import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.graph_objects as go

from data_index import DataIndex
from assets.dash_layout.dash_layout import Layout


today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)

data = DataIndex()
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
app.layout = Layout(app).get_layout()


@app.callback(
    [
        # Output('graph_example', 'figure'),
        Output('country_left_table', 'data'),
        Output('country_right_table', 'data'),
        Output('left_pop_inf_gauge_graph', 'figure'),
        Output('left_inf_death_gauge_graph', 'figure'),
        # Output('table2', 'data'),
        Output('right_pop_inf_gauge_graph', 'figure'),
        Output('right_inf_death_gauge_graph', 'figure'),
        # Output("P_position1", "children"),
        # Output("P_value1", 'children'),
        # Output("P_skill1", 'children'),
        # Output("P_foot1", 'children'),
        # Output("P_position2", "children"),
        # Output("P_value2", 'children'),
        # Output("P_skill2", 'children'),
        # Output("P_foot2", 'children')
    ],
    [
        Input('country_left_ddown', 'value'),
        Input('country_right_ddown', 'value')
    ]
)
def tab_1_function(country_left_ddown, country_right_ddown):
    gauge_domain = {'x': [0, 1], 'y': [0, 1]}
    gauge_mode = "gauge+number+delta"
    gauge_range = [None, 100]
    gauge_layout_dict = {
        "height": 100,
        "margin": dict(l=10, r=10, t=40, b=10),
        "showlegend": False,
        "template": "plotly_dark",
        "plot_bgcolor": 'rgba(0, 0, 0, 0)',
        "paper_bgcolor": 'rgba(0, 0, 0, 0)',
        "font_color": "black",
        "font_size": 15
    }

    def conjunction(*conditions):
        return functools.reduce(np.logical_and, conditions)

    yesterday_rows = data.covid_dataset.date == str(yesterday)
    country_left_rows = data.covid_dataset.key_gadm == country_left_ddown
    country_right_rows = data.covid_dataset.key_gadm == country_right_ddown

    left_yesterday = data.covid_dataset[conjunction(yesterday_rows, country_left_rows)]
    right_yesterday = data.covid_dataset[conjunction(yesterday_rows, country_right_rows)]
    if any([len(left_yesterday) < 1, len(right_yesterday) < 1]):
        db_yesterday = today - datetime.timedelta(days=2)
        db_yesterday_rows = data.covid_dataset.date == str(db_yesterday)
        left_yesterday = data.covid_dataset[conjunction(db_yesterday_rows, country_left_rows)]
        right_yesterday = data.covid_dataset[conjunction(db_yesterday_rows, country_right_rows)]

    table_updated_left = left_yesterday.to_dict('records')
    table_updated_right = right_yesterday.to_dict('records')

    left_pop_inf_gauge = go.Figure(go.Indicator(
        domain=gauge_domain,
        mode=gauge_mode,
        value=round(((int(left_yesterday.confirmed) / int(left_yesterday.population)) * 100), 1),
        gauge={'axis': {'range': gauge_range}, 'bar': {'color': "#5000bf"}},
    ))

    right_pop_inf_gauge = go.Figure(go.Indicator(
        domain=gauge_domain,
        mode=gauge_mode,
        value=round(((int(right_yesterday.confirmed) / int(right_yesterday.population)) * 100), 1),
        gauge={'axis': {'range': gauge_range}, 'bar': {'color': "rgb(255,171,0)"}},
    ))

    left_inf_death_gauge = go.Figure(go.Indicator(
        domain=gauge_domain,
        mode=gauge_mode,
        value=round(((int(left_yesterday.deaths) / int(left_yesterday.confirmed)) * 100), 1),
        gauge={'axis': {'range': gauge_range}, 'bar': {'color': "#5000bf"}},
    ))

    right_inf_death_gauge = go.Figure(go.Indicator(
        domain=gauge_domain,
        mode=gauge_mode,
        value=round(((int(right_yesterday.deaths) / int(right_yesterday.confirmed)) * 100), 1),
        gauge={'axis': {'range': gauge_range}, 'bar': {'color': "rgb(255,171,0)"}},
    ))

    left_pop_inf_gauge.data[0].delta.reference = right_pop_inf_gauge.data[0].value
    right_pop_inf_gauge.data[0].delta.reference = left_pop_inf_gauge.data[0].value
    left_inf_death_gauge.data[0].delta.reference = right_inf_death_gauge.data[0].value
    right_inf_death_gauge.data[0].delta.reference = left_inf_death_gauge.data[0].value

    left_pop_inf_gauge.update_layout(**gauge_layout_dict)
    right_pop_inf_gauge.update_layout(**gauge_layout_dict)
    left_inf_death_gauge.update_layout(**gauge_layout_dict)
    right_inf_death_gauge.update_layout(**gauge_layout_dict)

    return table_updated_left, table_updated_right, left_pop_inf_gauge, left_inf_death_gauge, right_pop_inf_gauge, right_inf_death_gauge
     # fig
           # gauge1, barplot1, table_updated2, gauge2, barplot2, p_pos_1, p_value_1, p_skill_1, p_foot_1, p_pos_2, p_value_2, p_skill_2, p_foot_2
