import duckdb

# Hubungkan ke DuckDB
con = duckdb.connect('warehouse/weather_dw.duckdb')

print("=== 1. DATA STAGING (stg_weather) ===")
stg_df = con.execute("SELECT * FROM stg_weather LIMIT 5").df()
print(stg_df)

print("\n=== 2. DATA MARTS / HASIL TRANSFORMATION (fct_daily_air_quality) ===")
marts_df = con.execute("SELECT * FROM fct_daily_air_quality").df()
print(marts_df)