import sys
sys.path.append("/home/olyaza/projects/earthquakes/code/")
import catalogs


def main():
	pf = "../data/usgs_mmin3_19960101-20160907_lat24.6-50_lon-125--65_us.csv"
	output_format = "numpy"
	print(pf)
	usgs = catalogs.catalog_USGS(pf, output_format)
	print(usgs.path_file)
	data = usgs.read_catalog_pd()
	v1, v2, v3, v4, v5 = usgs.read_catalog_np()
	

if __name__ == "__main__":
    main()



