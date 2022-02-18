# syntax=docker/dockerfile:1

# Install dependencies
#   Using the official python image as base
FROM python:3.9
#   Install pipenv
RUN pip install pipenv

# Move into the /app directory
WORKDIR /app

# Pip virtual environment
#   First, copy the pip files ...
COPY Pipfile Pipfile.lock ./
#   and then install them
RUN pipenv install --system --deploy

# Copy all djangp project files from django_root into /app
#   This works like rsync and does not create django_root
COPY django_root/ ./

# Specify the command that runs when the image is executed
#   The entrypoint is fixed ...
ENTRYPOINT ["python", "manage.py"]
#   while the cmd is the default that can be overwritten.
CMD ["runserver", "0.0.0.0"]
