FROM python:3.12.5-slim-bullseye

# set the working directory inside the container
WORKDIR /app

# copy the requirements file
COPY requirements.txt .

# install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy the application code
COPY . .

# expose the port that gunicorn will listen on
EXPOSE 8080

# run gunicorn as the entrypoint for the container
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "main:app"]
