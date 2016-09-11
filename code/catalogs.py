import pandas as pd
import numpy as np

class catalog_USGS:
	def __init__(self, path_and_file):
		self.path_file = path_and_file
		
	def read_catalog_pd(self):
		df  =  pd.read_csv("../data/usgs_mmin3_19960101-20160907_lat24.6-50_lon-125--65_us.csv")
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
		
		# TODO: return like an attribute
		#return mag, lat, lon, depth, time_since_main
		
     	
'''
    def event_time(self, df[["time"]]):
        pd.datetime.strptime(df[["time"]], '%Y-%m-%dT%H:%M:%S')
        for index, row in df[["time"]].iterrows():
            print(row["time"],index)

            
    def comp_mag_max_curv(self, mag):
        pass
        
'''
