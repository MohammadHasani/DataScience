import random

import pandas
from plotly import graph_objs


class GraphModel:

    def broken_bars(self, xstart, xfinish, ywidth, ystep, colors):
        shapes = []
        for k in range(len(xstart)):
            jj = len(xstart) - k - 1
            shapes.append(dict(type="rect",
                               x0=xstart[k],
                               x1=xfinish[k],
                               y0=jj * (ywidth + ystep),
                               y1=(jj + 1) * ywidth + jj * ystep,
                               fillcolor=colors[k],
                               line_color=colors[k]))
        return shapes

    def create_graph(self):
        df = pandas.read_excel("IPP EXAMPLE TO.xlsx", engine="openpyxl")

        colors2 = []

        for i in range(len(df['End Chainage'])):
            red = str(random.randrange(200))
            green = str(random.randrange(200))
            blue = str(random.randrange(200))
            new_color = 'rgb(' + red + ',' + green + ',' + blue + ')'
            colors2.append(new_color)

        colors3 = ['rgb(0,0,255)' for i in range(len(df['End Chainage']))]

        fig = graph_objs.Figure()

        ywidth = 10
        ystep1 = ywidth / 2

        tickvals1 = [(ywidth + ystep1) * (len(df['Feature\n']) - i - 1) + ystep1 for i in range(len(df['Feature\n']))]

        fig.update_layout(width=1000, height=600,
                          xaxis_range=[df['End Chainage'].min(), df['Start Chainage'].max()],
                          yaxis_range=[0, len(df['Feature\n']) * (ywidth + ystep1)],
                          shapes=self.broken_bars(df['End Chainage'], df['Start Chainage'], ywidth, ystep1,
                                                  colors=colors2))
        fig.update_yaxes(tickvals=tickvals1, ticktext=df['Feature\n'], tickmode='array')
        fig.write_html('Gantt.html', auto_open=False)
