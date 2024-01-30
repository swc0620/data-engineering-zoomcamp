# download docker-compose file of airflow
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.8.1/docker-compose.yaml'

# create directories for airflow and add airflow user id to .env file
mkdir -p ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)" > .env

# build custom airflow docker image that includes Google Cloud SDK
docker build .
docker-compose up airflow-init
docker-compose up