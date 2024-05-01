![log](https://github.com/software-students-spring2024/5-final-project-spring-2024-team01-5/actions/workflows/event-logger.yml/badge.svg)
![CI/CD](https://github.com/software-students-spring2024/5-final-project-spring-2024-team01-5/actions/workflows/app.yml/badge.svg)

# Grade Manager App

## Description

This app is designed to allow users to keep track of their school grades. Users can upload data for their courses, denoting the name, grade, credits, semester, and instructor for each course. After uploading their course data, a user can view a dashboard displaying their courses and their current GPA for the semester. If a user is looking to reach some target grade in the class, our app allows someone to calculate the required final exam grade for it.

 ## These are the instructions to run on your local machine:

1. Pull the image from Docker Hub
   ```bash
    docker pull egnechng/swe-project-5:main
    ``` 
1. Run the container
    ```bash
    docker run --platform linux/amd64 -d -p 5001:5001 -e DB_USER=<username> -e DB_PASSWORD=<password> --name app egnechng/swe-project-5:main
    ```
- `--platform linux/amd64` Specifies the platform (CPU architecture) for which the container should run. 
- `-d` Runs the container in detached mode (in the background). 
- `-p 5001:5001` Maps the port 5001 on the host to the port 5001 in the container.
- `-e DB_USER=<username>`  Sets the environment variable DB_USER with provided username in the container.
- `-e DB_PASSWORD=<password>`  Sets the environment variable DB_PASSWORD with the provided password in the container.
- `--name app` Assigns the name "app" to the container for easy reference.
- `egnechng/swe-project-5:main` Specifies the Docker image to use when creating the container. 

## Link to Container Image on Docker Hub
[Link to Docker Hub](https://hub.docker.com/repository/docker/egnechng/swe-project-5)

## Team Members

- [Nathanuel Dixon](https://github.com/nathanuel0322)
- [Aarav Sawlani](https://github.com/aaravsawlani)
- [Joshua Forlenza](https://github.com/joshforlenza)
- [Eugene Chang](https://github.com/egnechng)
