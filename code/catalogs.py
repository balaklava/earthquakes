import pandas as pd

class catalog_USGS:
	
	def __init__(self, path_file):
        self.df = pd.read_csv(path_file)
        df_selected = self.df[["time","latitude","longitude","mag","depth"]]
        print(df_selected.head())
	
	def test_function(self):
		print("hello world")
		
	#def read_catalog(self):
	#	df  =  pd.read_csv("../data/usgs_mmin3_19960101-20160907_lat24.6-50_lon-125--65_us.csv")
	#	df_selected = df[["time","latitude","longitude","mag","depth"]]
	#	print(df_selected.head())
'''		

    def __init__(self, lat, lon, depth, mag, time):
        self.lat = lat
        self.lon = lon
        self.depth = depth

    def event_time(self, df[["time"]]):
        pd.datetime.strptime(df[["time"]], '%Y-%m-%dT%H:%M:%S')
        for index, row in df[["time"]].iterrows():
            print(row["time"],index)

            
    
           

    def comp_mag_max_curv(self, mag):
        pass
        
'''
