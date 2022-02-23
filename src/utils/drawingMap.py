import plotly.graph_objects as go
import pandas as pd
import os
import plotly.io as pio


# def scatterCities(file="../../communes/communes.xlsx", scale=777):
#     col_list = ["X", "Y", "nom_commune_majuscule"]
#     df = pd.read_excel(file, usecols=col_list, nrows=scale)
#     fig = px.scatter(df, x=col_list[0], y=col_list[1], hover_name=col_list[2], width=800, height=800)
#     fig.show()


def drawPath(file='../../communes/communes.xlsx', scale=10, paths=None) -> None:
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
                name="ordre= " + str(paths[i]),
                hovertext="Start point : " + str(paths[i]) + " End Point : " + str(paths[i+1]),
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
        marker=dict(
            size=4,
            color='rgb(0, 0, 0)',

        )))
    lat_foc = 47.0749572
    lon_foc = 2.404171376
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
        showlegend=True,
        margin={'l': 0, 't': 50, 'b': 0, 'r': 0},
        # updatemenus={
        #
        #     dict(
        #         direction="left",
        #         pad={"r": 10, "t": 87},
        #         showactive=False,
        #         type="buttons",
        #         buttons=list(
        #
        #             list(method="restyle",
        #
        #                  args=list("", "Rainbow"),
        #
        #                  label="Rainbow"),
        #
        #         )
        #     )
        # }

    )
    fig.show()