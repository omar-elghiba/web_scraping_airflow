from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 6, 22),
    
}

def run_selenium_test_bank():
    driver = webdriver.Remote(
        command_executor='http://selenium:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME)

    driver.get("https://www.banquepopulaire.fr/bpaura/epargner/livret-transition-energetique/")
    print(driver.title)

    with open('data_bank.txt', 'w') as f:
        f.write(driver.title)

    driver.quit()

dag = DAG(
    'selenium_test_bank', default_args=default_args, schedule_interval=None)

run_test = PythonOperator(
    task_id='run_test_bank',
    python_callable=run_selenium_test_bank,
    dag=dag)