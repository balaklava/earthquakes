import sys
sys.path.append("/home/olyaza/projects/earthquakes/code/")
import catalogs


def main():
	pf = "../data/usgs_mmin3_19960101-20160907_lat24.6-50_lon-125--65_us.csv"
	#output_format = "numpy"
	output_format = "pd"
	print(pf)
	usgs = catalogs.catalog_USGS(pf, output_format)
	print(usgs.path_file)
	data_pd = usgs.read_catalog_pd()
	#print(data_pd)
	data_np = usgs.read_catalog_np()
	print(data_np)
	print(type(data_pd), type(data_np))

	

if __name__ == "__main__":
    main()



