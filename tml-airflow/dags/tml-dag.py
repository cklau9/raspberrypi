from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

from datetime import datetime

#Define default arguments
default_args = {
 'owner': 'Sebastian Maurice',
 'start_date': datetime (2024, 6, 29),
 'retries': 1,
}

# Instantiate your DAG
dag = DAG (dag_id="tml_iot_solution_dag_main", default_args=default_args, tags=["tml"], schedule=None)

# Define tasks
def task1():
 print ("Executing Task 11119")

def task2():
 print ("Executing Task 2")

tml_init_task_start = BashOperator(
    task_id='start',
    bash_command='date'
)

tml_produce_data = PythonOperator(
 task_id='tml_produce_data',
 python_callable=task1,
 dag=dag,
)
task_2 = PythonOperator(
 task_id='task_2',
 python_callable=task2,
 dag=dag,
)

#task_start >> [task_get_users, task_get_posts, task_get_comments, task_get_todos]

# Set task dependencies
tml_init_task_start >> [tml_produce_data, task_2]
