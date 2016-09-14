import pandas as pd
import numpy as np

class catalog_USGS:
	"""
	Class for reading and prepairing data from USGS and CMT catalogs.
	"""
	
	def __init__(self, path_and_file, output_format):
		"""
		Reading a catalog information:
		1. Path to the file and a file name;
		2. Catalog type: "USGS" or "CMT";
		3. Output data format: "numpy" for numpy array or "pandas" for Pandas DataFrame.
		"""
		self.path_file = path_and_file
		self.output_format = output_format
		
	# how to make it not seen as an attribute	
	def read_catalog_pd(self):
		df  =  pd.read_csv(self.path_file)
		df_selected = df[["time","latitude","longitude","mag","depth"]]
		return df_selected
	
	def read_catalog_np(self):
		df_select = self.read_catalog_pd()
		
		# numpy array
		mag 	=  np.array(df_select[["mag"]])
		lat 	=  np.array(df_select[["latitude"]])
		lon 	=  np.array(df_select[["longitude"]])
		depth 	=  np.array(df_select[["depth"]])
		time_since_main	=  np.array(df_select[["mag"]])
		
		# ??? is it possible to return data like attributes ??? 
		return mag, lat, lon, depth, time_since_main
	
		
	def read_catalog(self):
		print("Output format:", self.output_format)
		if self.output_format == "numpy":
			self.read_catolog_np()
		if self.output_format == "pandas":
			self.read_catalog_pd()
		else:
			raise ValueError("Output format should be 'numpy' or 'pandas'.")
		
		
		
     	
'''
    def event_time(self, df[["time"]]):
        pd.datetime.strptime(df[["time"]], '%Y-%m-%dT%H:%M:%S')
        for index, row in df[["time"]].iterrows():
            print(row["time"],index)

            
    def comp_mag_max_curv(self, mag):
        pass
        
'''
