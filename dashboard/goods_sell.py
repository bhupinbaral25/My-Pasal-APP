import nepali_datetime as ndt
import streamlit as st
import numpy as np
import pandas as pd

from models import get_selling_list
now = str(ndt.datetime.now())
date_today = (now.split(' ')[0])

def app():
    st.markdown("## Sell Details	")

    data = get_selling_list(date_today)

    if st.button("Complete",help="Click after complete the fill up the above form"):
        st.write(data)
        print(data)

    st.write("\n")
