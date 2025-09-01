# Fetching official base image for python
FROM python:3.11-slim

# Setting up the work directory
WORKDIR /app

# Copying requirement file
COPY requirements.txt .

# Installing dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copying all the files in our project
COPY . .

# Exposing the port
EXPOSE 8000

# Starting the server
CMD ["gunicorn","masterproduct.wsgi:application","--bind","0.0.0.0:8000"]