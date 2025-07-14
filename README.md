````markdown
# 🚀 MLflow + Airflow: Parallel Workflow Orchestration with Docker

This project demonstrates how to build a **parallel machine learning pipeline** using:

- **Apache Airflow 3.0.2** with **CeleryExecutor**
- **MLflow 3.1.1** for experiment tracking
- **Docker Compose** for container orchestration
- **Redis + PostgreSQL** as the message broker and Airflow backend
- **Flower** to monitor Celery workers

> You can run multiple workers in parallel and track all parameters, metrics, and model training results using MLflow.

---

## 📦 Stack Overview

| Component      | Description                            |
|----------------|----------------------------------------|
| Airflow        | Orchestrates DAG workflows             |
| CeleryExecutor | Runs tasks on parallel workers         |
| MLflow         | Tracks experiments, metrics, models    |
| Redis          | Acts as Celery's message broker        |
| PostgreSQL     | Stores Airflow metadata                |
| Flower         | UI to monitor Celery workers           |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/jeannassereldine/airflow_with_mlflow.git
cd mlflow-airflow-parallel
````

### 2. Start the System

To launch all services including **2 Airflow workers**:

```bash
docker-compose up --build --scale airflow-worker=2
```

---

## 🌐 Web Interfaces

| Service          | URL                                            |
| ---------------- | ---------------------------------------------- |
| Airflow UI       | [http://localhost:8080](http://localhost:8080) |
| MLflow Tracking  | [http://localhost:5000](http://localhost:5000) |
| Flower Dashboard | [http://localhost:5555](http://localhost:5555) |

---

## 📁 Project Structure

```
.
├── dags/
│   └── train_modal_dag.py   # DAG with MLflow integration
├── Dockerfile               # Custom Airflow image
├── docker-compose.yml       # Services definition
├── pyproject.toml           # Python dependencies
├── .dockerignore
└── README.md
```

---

## 🧪 Example DAG (MLflow Integration)

Inside `dags/train_modal_dag.py`, we define a DAG that:

1. Simulates data ingestion
2. Trains two ML models in parallel
3. Logs parameters and metrics to MLflow

```python
@dag(...)
def train_modal_dag():
    t1 = ingest_data()
    t2 = train_modal_1()
    t3 = train_modal_2()
    t1 >> [t2, t3]
```

Each training task logs model info like:

```python
mlflow.log_param("model_name", "RandomForestClassifier")
mlflow.log_metric("test_accuracy", 0.91)
```

---

## 🐳 Dockerfile Highlights

* Based on `apache/airflow:slim-latest-python3.11`
* Installs [`uv`](https://astral.sh/blog/uv-announcement/) for faster dependency resolution
* Uses environment variables to configure Airflow, Redis, PostgreSQL, and MLflow

```Dockerfile
ENV MLFLOW_TRACKING_URI=http://mlflow:5000
ENV AIRFLOW__CORE__EXECUTOR=CeleryExecutor
ENV AIRFLOW__CELERY__BROKER_URL=redis://redis:6379/0
```

---

## 📦 Dependencies (`pyproject.toml`)

```toml
dependencies = [
    "psycopg2-binary==2.9.10",
    "apache-airflow==3.0.2",
    "apache-airflow[celery]",
    "asyncpg==0.30.0",
    "apache-airflow-providers-celery>=3.12.0",
    "flower==1.0.0",
    "redis==4.6.0",
    "mlflow==3.1.1"
]
```

---

## ✅ Features

* ✅ Run Airflow DAGs in parallel using multiple Celery workers
* ✅ Track model training metadata in MLflow
* ✅ Use Docker for easy deployment and reproducibility
* ✅ Monitor Celery workers in real-time with Flower

---

## 🛠️ Useful Commands

```bash
docker-compose up --scale airflow-worker=3
```

---

## 📸 Screenshots

> *(Add your screenshots of Airflow UI and MLflow UI here)*

---

## 📚 Resources

* [Apache Airflow Documentation](https://airflow.apache.org/docs/)
* [MLflow Documentation](https://mlflow.org/docs/latest/index.html)
* [CeleryExecutor in Airflow](https://airflow.apache.org/docs/apache-airflow/stable/executor/celery.html)
* [Flower Dashboard](https://flower.readthedocs.io/en/latest/)

---

## 🧠 Author

**Jean Nasser El Dine**
🔗 [LinkedIn](https://www.linkedin.com/in/your-link)
📫 Contact: [jean.nassereldine@gmail.com](mailto:jean.nassereldine@gmail.com)

---

## 📜 License

This project is licensed under the MIT License.


