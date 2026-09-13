WITH stg AS (
    SELECT * FROM {{ ref('stg_weather') }}
)
SELECT
    CAST(observed_at AS DATE) AS observation_date,
    city_name,
    ROUND(AVG(temp_c), 2) AS avg_temperature_c,
    ROUND(AVG(pm2_5_concentration), 2) AS avg_pm2_5,
    ROUND(AVG(air_quality_index), 0) AS avg_us_aqi,
    CASE 
        WHEN AVG(air_quality_index) <= 50 THEN 'Baik (Good)'
        WHEN AVG(air_quality_index) <= 100 THEN 'Sedang (Moderate)'
        WHEN AVG(air_quality_index) <= 150 THEN 'Tidak Sehat (Kelompok Sensitif)'
        ELSE 'Sangat Tidak Sehat (Unhealthy)'
    END AS aqi_category,
    COUNT(*) AS total_readings
FROM stg
GROUP BY 1, 2
ORDER BY 1 DESC, 2 ASC