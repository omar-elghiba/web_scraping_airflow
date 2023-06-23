# Web scraping using Airflow and Selenium
![alt text](https://iili.io/HPMLBcl.png)


## Part 1: Description

In this project, I extract data from Twitter and other websites using a combination of different technologies to create a robust, high-performance, and easily maintainable system.

Firstly, I utilize Selenium, a powerful web scraping tool, to retrieve data from Twitter and other websites. The Selenium script is encapsulated in a Docker container, making it portable and easy to deploy on any Docker-enabled machine.

Next, the extracted data is stored in a MongoDB database, also contained within a Docker container. MongoDB is an excellent choice for storing the tweets and other unstructured data I retrieve. MongoDB Express, a web interface for MongoDB, is used to visualize the data and track metric trends.

To automate the data extraction process, I employ Airflow, a platform used for scheduling and monitoring workflows. Airflow is configured to run the Selenium script at regular intervals, enabling the tracking of Twitter and other website metrics over time.

Furthermore, I have created an API using FastAPI, a modern and high-performance web framework for building APIs with Python. This API exposes the extracted data, allowing other applications or services to interact with it.

All these technologies are orchestrated using Docker Compose, which facilitates consistent management of starting, stopping, and managing all the services. Docker Compose also simplifies the deployment of the system to any Docker-supported machine.

Finally, the entire system is hosted on an Ubuntu server, a robust and widely-used operating system that offers numerous security and management features. For networking and handling incoming requests, I employ Nginx, a high-performance web server.

By combining these technologies, I can effectively extract data from Twitter and other websites, store it in a structured manner, and make it available through an API. The entire process is automated and easily manageable thanks to the use of Docker containers and Airflow.





## Part 2: Deployment
The project is designed to be deployed using Docker, Docker Compose, and an Ubuntu Linux server.

It includes the following files for deployment:

#### Dockerfile: 

This file defines the Docker image for the project, specifying the environment in which the app runs.

#### docker-compose.yml: 

This file orchestrates the services that the application requires. It defines how Docker containers are built and how they interact with each other.

#### requirements.txt: 

This file lists all the Python libraries that your app depends on. When setting up the environment, Docker will use Pip to install these libraries.

## Running the Project

- docker compose up -d
