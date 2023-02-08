# Pull base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
ENV DockerHOME=/code
WORKDIR ${DockerHOME}

# Install dependencies
RUN pip install --upgrade pip
RUN pip install django
RUN pip install django-environ
RUN pip install psycopg2-binary
RUN pip install django-crispy-forms crispy-tailwind

# Copy project
COPY . .

#EXPOSE 8000



