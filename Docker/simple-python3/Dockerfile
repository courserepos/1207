# A docker base image based python 3
FROM python:3

# Set app working directory
WORKDIR /usr/src/app

# Install tornado library
RUN pip install tornado

# Copy the webserver python app to the working directory
COPY simple-web-server.py /simple-web-server.py

# Set the default execution command for this container
CMD ["python", "/simple-web-server.py"]