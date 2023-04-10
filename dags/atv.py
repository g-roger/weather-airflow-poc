from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator



with DAG(
    'atv',
    start_date=days_ago(1),
    schedule_interval='@DAILY'
) as dag:

    def get_hello():
        print('opa, hello')


    say_hello = PythonOperator(
        task_id='get_hello',
        python_callable=get_hello
    )
