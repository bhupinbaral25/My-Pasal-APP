import streamlit as st
import nepali_datetime as ndt

inputs_initial_list = [
	'Date',
	'Accessories-Name',
	'Accessories-Quantity',
	'Accessories-Category',
	'Accessories-Brand',
	'buying_price_per_unit'
]

selling_list = [
	'Sold-Date',
	'Accessories-Name',
	'Sold-Quantity',
	'Sold-Price',
	'Accessories-Category',
	]	

stored_list =[
	'Date',
	'Accessories-Name',
	'Stock-Quantity',
	'Accessories-Category',
	'Accessories-Brand',
	'profit_per_unit'
	]

def get_inputs_initial_list(today: str) -> dict:
	for i in range(10):
		init_dicts = {
			'Date': today,
			'Accessories-Name': st.text_input('Accessories-Name'),
			'Accessories-Quantity': st.number_input('Accessories-Quantity'),
			'Accessories-Category': st.text_input('Accessories-Category'),
			'Accessories-Brand': st.text_input('Accessories-Brand'),
			'buying_price_per_unit': st.number_input('Price_per_unit')
		}
	return init_dicts

def get_selling_list(today: str)->dict:
	selling_dicts = {
		'Sold-Date': today,
		'Accessories-Name': st.text_input('Accessories-Name'),
		'Sold-Quantity': st.number_input('Sold-Quantity'),
		'Sold-Price': st.number_input('Sold-Price'),
		'Accessories-Category': st.text_input('Accessories-Category'),
	}
	return selling_dicts
