import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

df=pd.read_csv("data.csv")
fig=ff.create_distplot([df["Mobile Brand"].to_list()], ["Brand Of Mobile"], show_hist=False)
fig.show()