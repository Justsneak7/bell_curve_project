import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

df=pd.read_csv("graph/data.csv")
fig=ff.create_distplot([df["Avg Rating"].to_list()], ["Rating"], show_hist=False)
fig.show()