CDF      
      time       lon       lat             CDI       @Climate Data Interface version 2.0.3 (https://mpimet.mpg.de/cdi)   Conventions       CF-1.6     institution       -National Centers for Environmental Prediction      history      �Thu Mar 17 10:25:50 2022: ncatted -a units,TEMP2m,o,c,K tmed_serie_Temp_Kelvin.nc
Thu Mar 17 10:21:24 2022: cdo addc,273.15 tmed_serie.nc tmed_serie_Temp_Kelvin.nc
Tue Mar 30 11:19:18 2021: ncatted -a units,TEMP2m,o,c,C tmed_serie.nc out1.nc
Tue Mar 30 11:12:05 2021: cdo -selmon,1 -fldmean -subc,273.15 tmed_serie_temporal_365dias.nc out.nc
Tue Feb 23 01:32:29 2021: cdo -fldmean -ifthen mask.nc tmp02.nc brasil.nc
Tue Feb 23 01:31:16 2021: cdo remapbil,tmp02.nc /mnt/vol_queimadas_1/produtos/meteorologia/shapefile/brasil.5km.nc mask.nc
Fri Feb 23 16:46:07 2018: cdo remapbil,/dados/produtos/BOL_INFOQUEIMA/NUM_FOCOS/diario/NF.19990615.nc brasil.nc out.nc
Fri Feb 23 16:44:40 2018: cdo sellonlatbox,-75,-33,-34,7 shape.BR.nc brasil.nc
Fri Dec 01 12:33:26 2017: cdo remapbil,/dados/produtos/input/mapa_veg/lc_aml_2012.Land_Cover_Type_1_AL.nc /dados/produtos/input/so.Brasil.1km.nc shape.BR.int.AMER.LAT.nc
Wed Nov 29 11:08:18 2017: cdo sellonlatbox,-75,-32,-35,6 so.Brasil.1km.nc tmp.nc
Wed Nov 29 11:05:50 2017: cdo remapbil,REF_1km.AS.nc so.Brasil.20km.nc so.Brasil.1km.nc
Fri May 12 11:14:53 2017: cdo setmissval,0 so.Brasil.20km.nc x.nc
Fri May 12 11:07:11 2017: cdo chname,Brasil_ONLY,br so.Brasil.20km.nc x.nc       NCO       `netCDF Operators version 5.0.6 (Homepage = http://nco.sf.net, Code = http://github.com/nco/nco)    nco_openmp_thread_number            CDO       @Climate Data Operators version 2.0.3 (https://mpimet.mpg.de/cdo)         time                standard_name         time   units         hours since 2020-1-1 18:00:00      calendar      proleptic_gregorian    axis      T           	�   lon                standard_name         	longitude      	long_name         	longitude      units         degrees_east   axis      X           	�   lat                standard_name         latitude   	long_name         latitude   units         degrees_north      axis      Y           	�   TEMP2m                        standard_name         air_temperature    	long_name         2 metre temperature    units         K      param         0.0.0      
_FillValue        �y�    missing_value         �y�    cell_methods      height: mean        	�                        C��@8      C��9@H      C���@R      C��U@X      C��@^      C�U�@b      C�r@e      C�B
@h      C�ld@k      C���@n      C��:@p�     C�Z�@r      C�^T@s�     C��+@u      C�#@v�     C�K@x      C���@y�     C���@{      C��q@|�     C��:@~      C�R@�     C���@��     C�q\@�@     C���@�      C�xr@��     C��1@��     C�x @�@     C��w@�      C�4@��     C�V�@��     C�|�