import numpy as np
import matplotlib.pyplot as plt
import openpyxl
import scipy.cluster.hierarchy as sch
import pandas as pd


def scatterCities(file='../communes/communes.xlsx', scale=10):
    col_list=["X","Y"]
    df = pd.read_excel(file, usecols=col_list, nrows=scale)
    plt.scatter(df["X"],df["Y"],s=5, c='k', marker='o')
    plt.show()

def drawPath(file='../communes/communes.xlsx', scale=10, solution=[]):
    """
    draws the path between two cities according to a given list
    :param solution:
    :param file:
    :param scale:
    :return:
    """
