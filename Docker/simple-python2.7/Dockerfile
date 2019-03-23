# A docker base image based python 2.7
FROM python:2.7

# Set app working directory
WORKDIR /usr/src/app

# Install tornado library
RUN pip install tornado

# Copy the webserver python app to the working directory
COPY simple-web-server.py /simple-web-server.py

# Set the default execution command for this container
CMD ["python", "/simple-web-server.py"]