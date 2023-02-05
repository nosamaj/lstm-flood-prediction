import pandas as pd

import pandas as pd
import plotly.express as px
import plotly.io as pio
#pio.renderers.default = 'firefox'

df = pd.read_csv('/home/nosamaj/Big Disk/Linuxstuff/Repos/lstm-flood-prediction/results.csv')

df['datetime'] = pd.date_range(df.datetime[0] , periods =len(df), freq = '120s')


fig = px.line(data_frame = df, x='datetime', y = ['obs' , 'pred'])

fig.show()
                           