FROM python:3.11
# Set the working directory in the image
WORKDIR /app
COPY . /app
COPY app/requirements.txt ./

RUN pip3 install -r requirements.txt
# the ADD command is how you add files from your local machine into a Docker image
ADD . .
# Run app.py when the container launches
CMD [ "python3", "app.py" ]