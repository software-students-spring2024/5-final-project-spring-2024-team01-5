FROM mongo:latest

# TODO: use docker secrets to get actual credentials, env variables
ENV MONGO_INITDB_ROOT_USERNAME=admin
ENV MONGO_INITDB_ROOT_PASSWORD=password
ENV MONGO_INITDB_DATABASE=mydatabase

EXPOSE 27017

CMD ["mongod"]

# Example usage
'''
docker build -t my-mongo-image .
docker run -d --name my-mongo-container -p 27017:27017 my-mongo-image
'''