import sys
sys.path.append("/home/olyaza/projects/earthquakes/code/")
import catalogs


def main():
	pf = "../data/usgs_mmin3_19960101-20160907_lat24.6-50_lon-125--65_us.csv"
	print(pf)
	usgs = catalogs.catalog_USGS(pf)
	print(usgs.path_file)
	data = usgs.read_catalog_pd()
	usgs.read_catalog_np()
	print(data.head())
    #usgs = catalogs.catalog_USGS(path_file)
    #usgs.test_function(path_file)




if __name__ == "__main__":
    main()



