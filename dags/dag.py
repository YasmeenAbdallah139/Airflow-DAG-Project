from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import random

def welcome_message():
    print("Welcome! My name is Yasmeen")

def generate_random():
    number = random.randint(1, 100)
    with open("/tmp/random.txt", "w") as f:
        f.write(str(number))
    print(f"Random number {number} saved to /tmp/random.txt")
#we can save it to any folder like shared for example


with DAG(
    dag_id="Airflow_Depi",
    start_date=datetime(2025, 10, 3),
    schedule_interval=timedelta(minutes=1),
    catchup=False
) as dag:
    task1 = BashOperator(
        task_id="print_date",
        bash_command="date"
    )
    
    task2 = PythonOperator(
        task_id="print_welcome",
        python_callable=welcome_message
    )

    task3 = PythonOperator(
        task_id="generate_random",
        python_callable=generate_random
    )
task1 >> task2 >> task3