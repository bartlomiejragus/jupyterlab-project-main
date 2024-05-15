# jupyterlab
Python with Spark env for real time data analysis. Dockerfiles are from: https://github.com/sebkaz/jupyterlab-project. Files from the model notes.ipynb notebook allow you to display the perceptron model in two variants using the REST API.

```bash
cd jupyterlab-project
docker compose up
```

## stop

```bash
ctrl + c 
docker compose down
```

### Contain: 
- Zookeeper
- Apache Kafka Broker
- MongoDB
- JupyterLab env with Apache Spark
