# Copyright 2021-2024 Avaiga Private Limited
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

"""
A page of the application.
Page content is imported from the Analysis.md file.

Please refer to https://docs.taipy.io/en/latest/manuals/gui/pages for more details.
"""
import plotly.graph_objects
from taipy.gui import Markdown
import pandas as pd
import plotly.express as px
import plotly
import taipy.gui.builder as tgb

# Assuming data is loaded from 'data/modified_supermarkt_sales_plus.csv'
data = pd.read_csv('data/modified_supermarkt_sales_plus.csv')
data['Date'] = pd.to_datetime(data['Date'])
data['Month_Year'] = data['Date'].dt.to_period('M').dt.to_timestamp()
    

def create_perc_fig(df: pd.DataFrame, group_column: str) -> plotly.graph_objects.Figure:
    """This function creates a plotly Figure representing a bar plot, expressed in percentage.
    Each bar represent, for a given time month and year (column Month_Year), the stacked percentage (of sales)
    represented by each category of the `group_column` variable, represented with different colors.

    Parameters
    ----------
    df : pd.DataFrame
        the dataframe containing three important variables for this function: `group_column`, `Month_Year`
        and `Total` (monthly sales)
    group_column : str
        the name of the grouping column

    Returns
    -------
    plotly.graph_objects.Figure
        the output figure, generated with plotly.express (px)
    """
    # Group, sum, and convert to percentage
    # Create and return the plot
    pass

fig_product_line = create_perc_fig(data, 'Product_line')
fig_city = create_perc_fig(data, 'City')
fig_gender = create_perc_fig(data, 'Gender')
fig_customer_type = create_perc_fig(data, 'Customer_type')

# TODO: complete the `on_change` function
def on_change(state, var_name, var_value):
    """
    This function implicitly triggers whenever a state variable from the page is modified (through user actions).
    We want to update the figures depending on which categories the user has selected (adding or removing).
    To do this, we will follow these steps:

    If `var_name` is any of 'city', 'customer_type' or 'gender' (e.g. one of those variables has changed), then
    create a variable `data` representing the filtered data (access it through `state.data`), filtered on several conditions:
    1. "City" column must be within the values of `state.city`
    2. "Customer_type" column must be within the values of `state.customer_type`
    3. "Gender" column must be within the values of `state.gender`
    Finally, update all figures (state.product_line, state.city, state.gender, state.customer_type) to reflect that change.
    """
    pass


customer_type = ["Normal", "Member"]
gender = ["Male", "Female"]
city = ["Bangkok", "Chiang Mai", "Vientiane", "Luang Prabang"]

Analysis = None
# TODO: Create a taipy page called Analysis using the builder (tgb)
    # TODO: Create a three-column layout with equal size
        # TODO: In each column, create a selector for each variable (customer_type, gender, city)
        # Make it such that the variable is dynamically modified when the user uses the selector.
        # This will ensure that the `on_change` function is triggered.
    # TODO: Create a two-columns layout with equal size
        # TODO: add the four charts (customer_type, city, gender, product_line) to this layout.
        # Use a dynamic version of the variables to link it to the dynamic value of selectors and make sure figs are updated.
        