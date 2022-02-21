import numpy as np
import matplotlib.pyplot as plt
import openpyxl
import scipy.cluster.hierarchy as sch
import plotly.express as px
import pandas as pd


def scatterCities(file="../../communes/communes.xlsx", scale=777):
    col_list = ["X", "Y", "nom_commune_majuscule"]
    df = pd.read_excel(file, usecols=col_list, nrows=scale)
    fig = px.scatter(df, x=col_list[0], y=col_list[1], hover_name=col_list[2])
    fig.show()


def drawPath(file='../../communes/communes.xlsx', scale=10, solution=[]):
    """
    draws the path between two cities according to a given list
    :param solution:
    :param file:
    :param scale:
    :return:
    """
