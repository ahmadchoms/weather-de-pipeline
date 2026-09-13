import subprocess
from ingest_weather import fetch_weather_and_air_quality
from prefect import flow, task

@task(name='Ingest API Data', retries=3, retry_delay_seconds=10)
def task_ingest():
    fetch_weather_and_air_quality()
    
@task(name='Run dbt Models')
def task_dbt_run():
    result = subprocess.run(
        ['dbt', 'run'], cwd='dbt_project', capture_output=True, text=True
    )
    if result.returncode != 0:
        raise Exception(f"dbt run gagal:\n{result.stderr}")
    print(result.stdout)
    
@task(name='Run dbt Tests')
def task_dbt_test():
    result = subprocess.run(
        ['dbt', 'test'], cwd='dbt_project', capture_output=True, text=True
    )
    if result.returncode != 0:
        raise Exception(f"dbt test gagal:\n{result.stderr}")
    print('semua data quality test lolos')
    
@flow(name='Automated Real-Time Weather Pipeline')
def weather_pipeline_flow():
    task_ingest()
    task_dbt_run()
    task_dbt_test()
    
if __name__ == "__main__":
    weather_pipeline_flow.serve(
        name='hourly-weather-pipeline', interval=3600
    )