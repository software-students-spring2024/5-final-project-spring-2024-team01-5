FROM python:3.11
# Set the working directory in the image
WORKDIR /app

COPY . .
# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt
# Run app.py when the container launches
CMD [ "python3", "app.py" ]