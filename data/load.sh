ogr2ogr -overwrite -t_srs "EPSG:4326" -a_srs "EPSG:4326" -f "PostgreSQL" PG:"host=localhost user=eknuth dbname=civicapps password=random" address.vrt -nln address_data
