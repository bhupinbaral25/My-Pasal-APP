import streamlit as st
import pandas as pd
import numpy as np
import datetime
import time

from models import get_inputs_initial_list, get_selling_list

a_date = datetime.datetime.now()
days = datetime.timedelta(12)
a_date = str(a_date).split(' ')[0]

if st.button('INITIAL SETUP'):
	while(True):
		
		data = get_inputs_initial_list(a_date)
		if st.button('Submit'):
			print(data)
			break

