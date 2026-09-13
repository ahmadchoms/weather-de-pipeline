import os
from datetime import datetime 
import polars as pl
import requests

CITIES = {
    'Jakarta': {'lat': -6.2088, 'lon': 106.8456},
    'Semarang': {'lat': -6.9667, 'lon': 110.4167},
    'Surabaya': {'lat': -7.2575, 'lon': 112.7521},
}

def fetch_weather_and_air_quality():
    records = []
    now = datetime.now()
    
    for city, coords in CITIES.items():
        # Fetch API
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={coords['lat']}&longitude={coords['lon']}&current_weather=true"
        w_res = requests.get(weather_url).json()
        curr_w = w_res.get('current_weather', {})
        
        aqi_url = f"https://air-quality-api.open-meteo.com/v1/air-quality?latitude={coords['lat']}&longitude={coords['lon']}&current=pm10,pm2_5,us_aqi"
        a_res = requests.get(aqi_url).json()
        curr_a = a_res.get('current', {})
        
        records.append({
            'timestamp': now.strftime('%Y-%m-%d %H:%M:%S'),
            'city': city,
            'temperature_celcius': curr_w.get('temperature'),
            'windspeed_kmh': curr_w.get('windspeed'),
            'weather_code': curr_w.get('weathercode'),
            'pm10': curr_a.get('pm10'),
            'pm2_5': curr_a.get('pm2_5'),
            'us_aqi': curr_a.get('us_aqi'),
        })
        
    df = pl.DataFrame(records)
    
    partition_path = (
      f"data_lake/raw_weather/year={now.year}/month={now.month:02d}"
    )
    os.makedirs(partition_path, exist_ok=True)
    
    file_name = f"weather_{now.strftime('%Y%m%d_%H%M%S')}.parquet"
    file_path = os.path.join(partition_path, file_name)
    
    df.write_parquet(file_path)
    print(f'[{now}] Sukses menyimpan {len(records)} data kota ke {file_path}')
    
if __name__ == "__main__":
    fetch_weather_and_air_quality()