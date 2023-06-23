# Use an official Airflow image from the Apache Airflow's DockerHub as a parent image
FROM apache/airflow:2.1.2

# Install Chrome browser
RUN apt-get update \
    && apt-get install -y wget gnupg2 unzip \
    && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install

# Install Selenium
RUN pip install selenium