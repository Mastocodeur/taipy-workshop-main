import plotly.express as px
import taipy.gui.builder as tgb
from taipy.gui import Gui

data = {"x": [1,2,3,4,5], "linear": [1, 2, 3, 6, 5], "quadratic": [1, 4, 9, 16, 25]}

def create_line_chart(data, y):
    fig = px.line(data, x="x", y=y)
    return fig

def on_change(state, var_name, var_value):
    if var_name == "selected_y":
        state.fig = create_line_chart(data, var_value)

selected_y = "linear"
y_lov = ["linear", "quadratic"]
fig = create_line_chart(data, selected_y)

with tgb.Page() as page:   
    tgb.selector(value="{selected_y}", lov=y_lov, multiple=True, dropdown=True, class_name="fullwidth", label="y-axis")
    tgb.chart(figure="{fig}")

Gui(pages={"Selector": page}).run()        