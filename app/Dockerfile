FROM python:3.11
WORKDIR /app
COPY requirements.txt ./

RUN pip3 install -r requirements.txt
# the ADD command is how you add files from your local machine into a Docker image
ADD . .
# Run app.py when the container launches
CMD ["python3", "app.py"]