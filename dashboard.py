import duckdb
import streamlit as st

st.set_page_config(page_title="Air Quality Dashboard", layout="wide")
st.title("🌤️ Real-time Air Quality & Weather Dashboard")

con = duckdb.connect("warehouse/weather_dw.duckdb")
df = con.execute("SELECT * FROM fct_daily_air_quality").pl()

st.dataframe(df, use_container_width=True)

# Metric Summary
col1, col2, col3 = st.columns(3)
if len(df) > 0:
  col1.metric("KOTA DIPANTAU", len(df["city_name"].unique()))
  col2.metric("RATA-RATA SUHU", f"{df['avg_temperature_c'].mean():.1f} °C")
  col3.metric("RATA-RATA AQI", f"{df['avg_us_aqi'].mean():.0f}")