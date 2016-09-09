import sys
sys.path.append("/home/olyaza/projects/earthquakes/code/")
import catalogs


def main():
	path_file = "../data/usgs_mmin3_19960101-20160907_lat24.6-50_lon-125--65_us.csv"
    usgs = catalogs.catalog_USGS()
    usgs.test_function()
    usgs.read_catalog()


if __name__ == "__main__":
    main()


