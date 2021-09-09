import sqlite3
import warnings
import itertools
import numpy as np
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
plt.style.use('fivethirtyeight')
import pandas as pd

import matplotlib
matplotlib.rcParams['axes.labelsize'] = 14
matplotlib.rcParams['xtick.labelsize'] = 12
matplotlib.rcParams['ytick.labelsize'] = 12
matplotlib.rcParams['text.color'] = 'k'
con = sqlite3.connect(database=r'ShakeWake.db')
cur = con.cursor()
cur.execute("Select category,product,date,amt,time from report ")
row = cur.fetchall()
df = pd.DataFrame(row, columns =['category','product','date','amt','time'])
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['time'] = pd.to_datetime(df['time'], errors='coerce')
df = df.set_index('date')

#---------------------------------------------------------------
y = df['date'].resample('MS').mean()
y.plot(figsize=(15,6))
plt.show()
