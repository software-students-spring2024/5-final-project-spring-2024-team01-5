FROM python:3.11
# Set the working directory in the image
WORKDIR /app
# install dependencies into the image
COPY requirements.txt
RUN pip3 install -r requirements.txt
ADD . .

# Run app.py when the container launches
CMD [ "python3", "app.py" ]