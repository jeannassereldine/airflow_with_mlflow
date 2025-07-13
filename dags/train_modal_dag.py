
from datetime import datetime, timedelta
import os, sys, time
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from airflow import DAG
from airflow.decorators import task, dag

@task
def task_parallel_1():
    # Simulate training model B
    time.sleep(25)
    print('task_parallel_1')

@task
def task_parallel_2():
    time.sleep(10)
    print(f"task_parallel_2")
    
@task
def task_parallel_3():
    time.sleep(3)
    print(f"task_parallel_3")

@dag
def train_modal_dag():
    t1 = task_parallel_1()
    t2 = task_parallel_2()
    t3 = task_parallel_3()
 
dag = train_modal_dag()
    
 
 