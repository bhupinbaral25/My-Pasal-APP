import pandas as pd

def read_data(file_path):
	df = pd.read_csv(file_path)
	return df

class DataModification:
	def __init__(self, dataframe):
		self.dataframe = dataframe

	def insert_into_dataframe(self, data_dict: dict):
		"""
		Inserts a new row into the dataframe
		---------
		Parameters: data_dict: dict
		new dictionary to add to the dataframe
		"""
		data_df = pd.DataFrame(data_dict, index=[0])
		self.dataframe = self.dataframe.append(data_df, ignore_index=True)

	def update_dataframe(self, data_dict: dict):
		"""
		Updates the dataframe with the new data
		"""
		self.dataframe.update(data_dict)

	def delete_from_dataframe(self, index: int):
		"""
		Deletes a row from the dataframe
		"""
		self.dataframe.drop(index, inplace=True)

	def get_dataframe(self):
		"""
		Returns the dataframe
		"""
		return self.dataframe	

	def save_dataframe(self, file_path: str):
		"""
		Saves the dataframe to a csv file
		-----------
		Parameters: file_path: str
		"""
		self.dataframe.to_csv(file_path, index=False)

	def save_to_excel(self, file_path: str):
		"""
		Saves the dataframe to an excel file
		-----------
		Parameters: file_path: str
		"""
		self.dataframe.to_excel(file_path, index=False)

