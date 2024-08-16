from airflow import DAG
from group.crawl_ohitv import crawl_tasks
from group.transform_data import processing_tasks
from group.load_to_postgres import load_tasks
from datetime import datetime

with DAG(
        dag_id='ohitv_pipeline',
        start_date=datetime(year=2024, month=8, day=1),
        schedule_interval='@daily',
        catchup=False) as dag:

    crawl = crawl_tasks()

    processing = processing_tasks()

    load = load_tasks()

    crawl >> processing >> load