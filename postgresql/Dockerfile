# Pull the base image
FROM python:3.10.4-slim-bullseye

# Set environemnt variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working dir
WORKDIR /code

# Copy the requirements
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy the project
COPY . . 