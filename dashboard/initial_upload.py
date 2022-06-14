import nepali_datetime as ndt
import streamlit as st
import numpy as np
import pandas as pd

from models import get_inputs_initial_list
from models import DataModification, read_data

now = str(ndt.datetime.now())
date_today = (now.split(' ')[0])

def app():
    st.markdown("## Upload NEW ARRIVALS	")
    data = get_inputs_initial_list(date_today)
    try:
        df = read_data(f"./data/buy_report/{date_today[0:7]}.csv")
    except FileNotFoundError:
        df = pd.DataFrame()
    df_object = DataModification(df)
    
    if st.button("Upload",help="Click after complete the fill up the above form"):
        st.write(data)
        df_object.insert_into_dataframe(data)
        df_object.save_dataframe(f"./data/buy_report/{date_today[0:7]}.csv")
        print(data)
    st.write("\n")

