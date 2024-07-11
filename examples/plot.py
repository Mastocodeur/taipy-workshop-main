import plotly.express as px
import taipy.gui.builder as tgb
from taipy.gui import Gui

data = {"x": [1, 2, 3, 4, 5], "y": [1, 2, 3, 6, 5]}

def create_line_chart(data):
    fig = px.line(data, x="x", y="y")
    return fig

fig = create_line_chart(data)

with tgb.Page() as page:
    tgb.text("# Not in Layout", mode="markdown")
    with tgb.layout(columns="1 2"):
        tgb.text("## In Layout", mode="markdown")
        tgb.chart(figure="{fig}")


Gui(pages={"Plot": page}).run()
    