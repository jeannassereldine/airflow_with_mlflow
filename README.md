Here's a complete `README.md` file for your Airflow setup using `CeleryExecutor` with distributed workers, Redis, PostgreSQL, and `uv` for dependency management:

---

````markdown
# 🚀 Airflow with CeleryExecutor, Redis, and PostgreSQL (Python 3.11)

This project sets up **Apache Airflow** for distributed, parallel task execution using **CeleryExecutor**, with:

- **PostgreSQL** as the metadata database
- **Redis** as the message broker
- **Celery** workers for distributed processing
- **uv** for fast Python dependency resolution

---

## 📦 Stack Components

| Component        | Purpose                                       |
|------------------|-----------------------------------------------|
| Airflow Webserver| UI for managing DAGs and monitoring tasks     |
| Airflow Scheduler| Schedules DAG runs                            |
| Celery Workers   | Execute tasks in parallel                     |
| Redis            | Message broker for task distribution          |
| PostgreSQL       | Metadata database and result backend          |

---

## 🐳 Docker Setup

Make sure you have **Docker** and **Docker Compose** installed.

### 1. Clone the Repository

```bash
git clone https://github.com/your-org/your-repo.git
cd your-repo
````

### 2. Start the Stack

```bash
docker-compose up
```

> This builds the Airflow image with `uv`, installs dependencies from `pyproject.toml`, and starts all services.

---

## 🧠 Airflow Configuration Highlights

The following environment variables are configured in the Dockerfile:

### 🔁 `AIRFLOW__CELERY__BROKER_URL=redis://redis:6379/0`

Defines **Redis** as the **Celery broker**. Airflow pushes tasks into Redis queues, and Celery workers pull from them.

### ⚙️ `AIRFLOW__CORE__EXECUTOR=CeleryExecutor`

Enables **distributed parallel execution** of tasks using Celery. Multiple workers can run in parallel across machines or containers.

### 💾 `AIRFLOW__CELERY__RESULT_BACKEND=db+postgresql://...`

Celery stores task results and metadata in **PostgreSQL**, so the web UI and scheduler can track task states.

### 🌐 `AIRFLOW__API__BASE_URL=http://airflow-webserver:8080`

Sets the base URL for Airflow’s REST API. Used internally and for webhooks/callbacks.

### 📂 `AIRFLOW__CORE__DAGS_FOLDER=/opt/airflow/project/dags`

Specifies where DAGs are located in the container. Place your DAG `.py` files here.

### 🗄 `AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=postgresql+psycopg2://...`

Connects Airflow to the **PostgreSQL metadata DB**. This is essential for scheduling, task state tracking, etc.

---

## 📁 Folder Structure

```
.
├── dags/                   # Your DAG definitions go here
├── pyproject.toml          # Dependencies managed with uv
├── Dockerfile              # Builds custom Airflow image
├── docker-compose.yml      # Starts all services
└── README.md               # You are here
```

---

## 📌 How to Add New Dependencies

```bash
uv add some-package
```

This updates the `pyproject.toml` automatically.

---

## 🧪 Access the Airflow UI

* URL: [http://localhost:8080](http://localhost:8080)
* Default login:

  * **Username**: `admin`
  * **Password**: `you can find the password inside /airflow_home/simple_auth_manager_passwords.json.generated after doing docker-compose up`

---

## 🛠 Tips for Scaling

To add more Celery workers, simply scale the service:

```bash
docker compose up --scale airflow-worker=3
```
where 3 is the number of worker 

---

## 📜 License

MIT — feel free to use and modify.

---

## ✨ Credits

Built with 💡 by jean nassereldine (jean.nassereldine@gmail.com)
Based on the official [Apache Airflow Docker Stack](https://airflow.apache.org/docs/docker-stack/).

```

---
