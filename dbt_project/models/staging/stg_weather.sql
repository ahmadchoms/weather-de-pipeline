WITH raw_data AS (
    SELECT * 
    FROM read_parquet('data_lake/raw_weather/*/*/*.parquet')
)
SELECT
    CAST(timestamp AS TIMESTAMP) AS observed_at,
    CAST(city AS VARCHAR) AS city_name,
    CAST(temperature_celcius AS FLOAT) AS temp_c,
    CAST(windspeed_kmh AS FLOAT) AS windspeed_kmh,
    CAST(pm2_5 AS FLOAT) AS pm2_5_concentration,
    CAST(pm10 AS FLOAT) AS pm10_concentration,
    CAST(us_aqi AS INTEGER) AS air_quality_index
FROM raw_data