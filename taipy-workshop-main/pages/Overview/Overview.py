import pandas as pd
import plotly.express as px
import taipy.gui.builder as tgb
from plotly.graph_objects import Figure
import os


# Load the dataset
data = pd.read_csv('data/modified_supermarkt_sales_plus.csv')


def create_pie_figure(data: pd.DataFrame, group_by: str) -> Figure:
    """This function creates a pie chart of the sales repartition by the `group_by` variable by:
    1. Computing the sum of sales per category of the `group_by` variable.
    2. Creating and returning the pie chart created with plotly express (px)

    Parameters
    ----------
    data : pd.DataFrame
        the dataframe
    group_by : str
        the variable name to group on

    Returns
    -------
    Figure
        the figure created with plotly.express (px)
    """
    pass

def create_bar_figure(data: pd.DataFrame, group_by: str) -> Figure:
    """This function creates a bar chart of the sales repartition by the `group_by` variable by:
    1. Computing the sum of sales per category of the `group_by` variable.
    2. Creating and returning the pie chart created with plotly express (px)

    Parameters
    ----------
    data : pd.DataFrame
        the dataframe
    group_by : str
        the variable name to group on

    Returns
    -------
    Figure
        the figure created with plotly.express (px)
    """
    sales_over_time = data.groupby(group_by)['Total'].sum().reset_index()
    fig = px.bar(sales_over_time, x=group_by, y='Total', title=f'Sales Trends Over {group_by}', color='Total')
    return fig

def create_sales_by_city_map(data: pd.DataFrame) -> Figure:
    """This function creates a mapbox plot of the sales per city by:
    1. grouping data by the `City` variable and aggregating the following function to other variables:
    - `Total`: sum of values
    - `Latitude`: mean
    - `Longitude`: mean
    2. Creating and returning a mapbox plot (px.scatter_mapbox) to represent the cities geographically per sales importance.

    Parameters
    ----------
    data : pd.DataFrame
        the data

    Returns
    -------
    Figure
        the mapbox plot representing cities by volume of sales.
    """
    pass


fig_product_line = create_pie_figure(data, 'Product_line')
fig_city = create_pie_figure(data, 'City')
fig_customer_type = create_pie_figure(data, 'Customer_type')

Overview = None
# TODO: Create a taipy page called "Overview" thanks to the builder (tgb)
    # TODO: In this page, create a chart containing the mapbox plot figure of the data, with height equal to 600px
    # You can use this syntax: "{my_variable}" to reference a variable or the output of a function.

    # TODO: Then, create a three-column layout with equal size for each column
        # TODO: In these three columns, add:
            # 1. a chart containing `fig_product_line`
            # 2. a chart containing `fig_city`
            # 3. a chart containing `fig_customer_type`
    # TODO: Finally, add two bar figures in the page:
        # 1. One bar figure representing sales over the `Time` variable
        # 2. Another bar figure representing sales over the `Date` variable