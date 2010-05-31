select substring(trim(ST_Geohash(wkb_geometry)) from 0 for 5) as pdx_hash, 
		count(*) as address_point_count 
	from address_data group by pdx_hash order by address_point_count;
