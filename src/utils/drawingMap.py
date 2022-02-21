import plotly.graph_objects as go
import pandas as pd
import os
import plotly.io as pio


# def scatterCities(file="../../communes/communes.xlsx", scale=777):
#     col_list = ["X", "Y", "nom_commune_majuscule"]
#     df = pd.read_excel(file, usecols=col_list, nrows=scale)
#     fig = px.scatter(df, x=col_list[0], y=col_list[1], hover_name=col_list[2], width=800, height=800)
#     fig.show()


def drawPath(file='../../communes/communes.xlsx', scale=50, paths=None) -> None:
    """
    draws the path between two cities according to a given list
    :param paths: a complete path to draw
    :param file: file leading to the xl
    :param scale: amount of cities to display
    """
    if paths is None:
        paths = [i for i in range(0, scale)]
    df_cities = pd.read_excel(file, nrows=scale)
    df_cities.head()

    df_paths = pd.read_excel(file, nrows=scale)
    df_paths.head()

    fig = go.Figure()

    for i in range(len(paths) - 1):
        fig.add_trace(
            go.Scattergeo(
                lon=[df_paths['longitude'][paths[i]], df_paths['longitude'][paths[i + 1]]],
                lat=[df_paths['latitude'][paths[i]], df_paths['latitude'][paths[i + 1]]],
                mode='lines',
                line=dict(width=1, color='red'),
                # opacity=float(df_paths['cnt'][i]) / float(df_paths['cnt'].max()),
            )
        )

    fig.add_trace(go.Scattergeo(
        lon=df_cities['longitude'],
        lat=df_cities['latitude'],
        hoverinfo='text',
        text=df_cities['nom_commune_majuscule'],
        mode='markers',
        line=dict(
            width=3,
            color='rgba(68, 68, 68, 0)'
        ),
        marker=dict(
            size=2,
            color='rgb(0, 0, 0)',

        )))
    lat_foc = df_paths['latitude'][48]
    lon_foc = df_paths['longitude'][48]
    fig.update_geos(
        visible=False, resolution=50,
        showcountries=True, countrycolor="RebeccaPurple",
        scope='europe',
        landcolor='rgb(243, 243, 243)',
        projection_scale=5,  # this is kind of like zoom
        center=dict(lat=lat_foc, lon=lon_foc),  # this will center on the point
    )
    fig.update_layout(
        title_text='The true beauty of things',
        showlegend=False,
        margin={'l': 0, 't': 50, 'b': 0, 'r': 0},

    )
    fig.show()


drawPath()
