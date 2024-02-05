FROM apache/airflow:2.8.1-python3.9

COPY webserver_config.py /opt/airflow/webserver_config.py
