FROM  apache/airflow:slim-latest-python3.11

USER root
RUN apt-get update && apt-get install -y curl && apt-get clean

RUN curl -Ls https://astral.sh/uv/install.sh | bash

WORKDIR /opt/airflow/project
ENV AIRFLOW__LOGGING__BASE_LOG_FOLDER=/opt/airflow/project/airflow_home/logs
ENV AIRFLOW__LOGGING__DAG_PROCESSOR_CHILD_PROCESS_LOG_DIRECTORY=/opt/airflow/project/airflow_home/logs/dag_processor
ENV AIRFLOW__CORE__DAGS_FOLDER=/opt/airflow/project/dags
ENV AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=postgresql+psycopg2://airflow_user:airflow_pass@postgres_airflow:5432/airflow
ENV AIRFLOW_HOME=/opt/airflow/project/airflow_home
ENV MLFLOW_TRACKING_URI=http://mlflow:5000
ENV AIRFLOW__CELERY__BROKER_URL=redis://redis:6379/0
ENV AIRFLOW__CORE__EXECUTOR=CeleryExecutor
ENV AIRFLOW__CELERY__RESULT_BACKEND=db+postgresql://airflow_user:airflow_pass@postgres_airflow:5432/airflow
ENV AIRFLOW__API__BASE_URL=http://airflow-webserver:8080


COPY . /opt/airflow/project

RUN chown -R 777 /opt/airflow/project/
RUN uv pip install -r pyproject.toml

# CMD ["airflow", "standalone"]