import streamlit as st
import pandas as pd
import numpy as np
import datetime
import time

from dashboard import MultiPage
from dashboard import initial_upload, goods_sell

a_date = datetime.datetime.now()
days = datetime.timedelta(12)
a_date = str(a_date).split(' ')[0]

app = MultiPage()

st.title("My Pasal Application")

# Add all your applications (pages) here
app.add_page("Upload Initial Items", initial_upload.app)
app.add_page("Sell", goods_sell.app)


# The main app
app.run()