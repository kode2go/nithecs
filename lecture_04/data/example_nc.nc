netcdf example_data {
dimensions:
    time = 365 ;
    lat = 180 ;
    lon = 360 ;
variables:
    float temperature(time, lat, lon) ;
        temperature:units = "degrees Celsius" ;
        temperature:long_name = "Surface temperature" ;
        temperature:_FillValue = -999.0f ;
    float precipitation(time, lat, lon) ;
        precipitation:units = "mm/day" ;
        precipitation:long_name = "Daily precipitation" ;
        precipitation:_FillValue = -999.0f ;
    float humidity(time, lat, lon) ;
        humidity:units = "percent" ;
        humidity:long_name = "Relative humidity" ;
        humidity:_FillValue = -999.0f ;
    double time(time) ;
        time:units = "days since 1970-01-01" ;
        time:calendar = "standard" ;
    float lat(lat) ;
        lat:units = "degrees_north" ;
        lat:long_name = "Latitude" ;
        lat:_FillValue = -999.0f ;
    float lon(lon) ;
        lon:units = "degrees_east" ;
        lon:long_name = "Longitude" ;
        lon:_FillValue = -999.0f ;
}
data:
    temperature =
        25.0, 25.1, 24.9, ..., 26.5, 26.4, 26.2,
        26.5, 26.4, 26.2, ..., 25.0, 25.1, 24.9 ;
    precipitation =
        0.0, 0.1, 0.0, ..., 0.3, 0.2, 0.1,
        0.3, 0.2, 0.1, ..., 0.0, 0.1, 0.0 ;
    humidity =
        50.0, 50.5, 49.9, ..., 51.2, 51.1, 50.9,
        51.2, 51.1, 50.9, ..., 50.0, 50.5, 49.9 ;
    time = 0, 1, 2, ..., 362, 363, 364 ;
    lat = -90.0, -89.0, -88.0, ..., 88.0, 89.0, 90.0 ;
    lon = -180.0, -179.0, -178.0, ..., 177.0, 178.0, 179.0 ;
}
