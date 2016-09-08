
class catalog_USGS:

    def __init__(self, lat, lon, depth, mag, time):
        self.lat = lat
        self.lon = lon
        self.depth = depth

    def event_time(self, df[["time"]]):
        pd.datetime.strptime(df[["time"]], '%Y-%m-%dT%H:%M:%S')
        for index, row in df[["time"]].iterrows():
            print(row["time"],index)
            


    def read_catalog(self):
        # time:     2015-04-25T16:05:17.880Z,
        # lat:      38.7861667,
        # lon:      -122.72,
        # depth:    2.43,
        # mag:      3.28,
        # mag_type: ml,
        # nst:      102,
        # gap:      32,
        # XXX:      0.006638,
        # XXX:      0.07,
        # XXX:      nc,
        # XXX:      nc72435065,
        # XXX:      2015-07-03T00:23:40.040Z,
        # XXX:      "3km S of Cobb, California",
        # event_type: earthquake,
        # XXX:      0.1,
        # XXX:      0.16,
        # XXX:      0.201,
        # XXX:      55,
        # XXX:      reviewed,
        # XXX:      nc,
        # XXX:      nc

        df  =  pd.read_csv("usgs_mmin3_19960101-20160907_lat24.6-50_lon-125--65_us.csv")

        df_selected = df[["time","latitude","longitude","mag","depth"]]
        
        


    def comp_mag_max_curv(self, mag):
        pass
