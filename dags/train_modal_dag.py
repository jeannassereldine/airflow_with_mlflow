
from datetime import datetime, timedelta
import os, sys, time
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from airflow import DAG
from airflow.decorators import task, dag
import mlflow

mlflow_uri = os.getenv("MLFLOW_TRACKING_URI", "http://mlflow:5000")
mlflow.set_tracking_uri("http://mlflow:5000")

@task
def ingest_data():
    # Simulate training model B
    time.sleep(30)
    print('ingesting data')

@task
def train_modal_1():
    time.sleep(12)
    time.sleep(6)
    print(f"training modal 2")
    with mlflow.start_run():
    # Log parameters
        mlflow.log_param("model_name", "LogisticRegression")
        mlflow.log_param("penalty", "l2")
        mlflow.log_param("C", 1.0)
        mlflow.log_param("solver", "liblinear")
        mlflow.log_param("max_iter", 200)
    
        # Log metrics
        mlflow.log_metric("cv_mean_accuracy", 0.95)
        mlflow.log_metric("cv_std_accuracy", 0.03)
        mlflow.log_metric("test_accuracy", 0.933)
        mlflow.log_metric("cv_min_score", 0.9)
        mlflow.log_metric("cv_max_score", 1.0)
    
@task
def train_modal_2():
    time.sleep(6)
    print(f"training modal 2")
    with mlflow.start_run():
    # Log parameters
        mlflow.log_param("model_name", "RandomForestClassifier")
        mlflow.log_param("n_estimators", 100)
        mlflow.log_param("max_depth", 4)
        mlflow.log_param("random_state", 42)
    
        # Log metrics
        mlflow.log_metric("cv_mean_accuracy", 0.95)
        mlflow.log_metric("cv_std_accuracy", 0.03)
        mlflow.log_metric("test_accuracy", 0.933)
        mlflow.log_metric("cv_min_score", 0.9)
        mlflow.log_metric("cv_max_score", 1.0)

@dag
def train_modal_dag():
    t1 = ingest_data()
    t2 = train_modal_1()
    t3 = train_modal_2()
    t1 >> [t2 , t3 ]
 
dag = train_modal_dag()
  
 
 