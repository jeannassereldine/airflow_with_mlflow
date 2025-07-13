
from datetime import datetime, timedelta
import os, sys, time
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from airflow import DAG
from airflow.decorators import task, dag

@task
def ingest_data():
    # Simulate training model B
    time.sleep(30)
    print('ingesting data')

@task
def train_modal_1():
    time.sleep(12)
    print(f"training modal 1")
    
@task
def train_modal_2():
    time.sleep(6)
    print(f"training modal 2")

@dag
def train_modal_dag():
    t1 = ingest_data()
    t2 = train_modal_1()
    t3 = train_modal_2()
    t1 >> [t2 , t3 ]
 
dag = train_modal_dag()
  
 
 