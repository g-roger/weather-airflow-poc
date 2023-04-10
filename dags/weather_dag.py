from airflow import DAG
import pendulum
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.macros import ds_add
from os.path import join
import pandas as pd
from datetime import datetime, timedelta


with DAG(
	'weather_dag',
	start_date=pendulum.datetime(2023, 3, 20, tz='UTC'),
	schedule_interval='0 0 * * 1'
	) as dag:

	task1 = BashOperator(
		task_id = 'create_folder',
		bash_command = 'mkdir -p "/Users/gabrielroger/Documents/projects/weather-data/week={{data_interval_end.strftime("%Y-%m-%d")}}"'
		)

	def extraction(data_interval_end):
		city = 'SaoPaulo'
		key = 'TQP5WZSYY6STLLS977A5564JY'


		URL = join('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/',
			f'{city}/{data_interval_end}/{ds_add(data_interval_end, 7)}?unitGroup=metric&include=days&key={key}&contentType=csv')

		data = pd.read_csv(URL)

		file_path = f'/Users/gabrielroger/Documents/projects/weather-data/week={data_interval_end}/'

		data.to_csv(file_path + 'data_large.csv')
		data[['datetime', 'tempmin', 'temp', 'tempmax', 'feelslikemax', 'feelslikemin', 'feelslike']].to_csv(file_path + 'temperature.csv')
		data[['datetime', 'description', 'icon', 'humidity']].to_csv(file_path + 'condition.csv')


	task2 = PythonOperator(
		task_id = 'extraction_weather_data',
		python_callable = extraction,
		op_kwargs = {'data_interval_end': '{{data_interval_end.strftime("%Y-%m-%d")}}'}
		)


	task1 >> task2