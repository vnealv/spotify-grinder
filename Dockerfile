# pull official python alpine image
FROM python:3.6

# Set Environment Variable
ENV PYTHONUNBUFFERED 1

# Making source and static directory
RUN mkdir /src
RUN mkdir /static
RUN mkdir /config

# Creating Work Directory
WORKDIR /src

# Installing requirements.pip from project
COPY ./src/requirements.pip /scripts/
RUN pip install --no-cache-dir -r /scripts/requirements.pip

# Update pip
RUN pip install --upgrade pip

# CMD will run when this dockerfile is running
CMD ["sh", "-c", "python manage.py collectstatic --no-input; python manage.py migrate; gunicorn my_django.wsgi -b 0.0.0.0:8000 "]
